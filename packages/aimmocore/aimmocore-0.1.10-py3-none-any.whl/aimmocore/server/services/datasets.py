"""Datasets service module."""

import os
import json
import asyncio
from typing import List, Dict, Any
from loguru import logger
from aimmocore import config as conf
from aimmocore.core.database import db_connection
from aimmocore.core import services as acs
from aimmocore.core import utils
from aimmocore.core.utils import sanitize_filename
from aimmocore.server.schemas.datasets import ProcessStatus


META_TYPE = {
    "weather": ["clear", "cloudy", "rainy"],
    "road_feature": ["city", "highway"],
    "location": ["inside", "outside"],
    "time": ["night", "day", "sunrise/sunset"],
}


async def update_curation_status():
    """Update curation Status"""
    await update_status(ProcessStatus.ERROR.value)
    await update_status(ProcessStatus.PROCESSING.value)


async def update_status(status: str):
    """Updates the processing status of datasets currently marked as 'Processing'.

    Environment Variables:
        CURATION_API_KEY (str): The API key used for authentication; should be set in the environment.

    """
    dataset_list = get_dataset_list(status=status)
    if not dataset_list:
        return

    api_key = os.getenv("CURATION_API_KEY", "")
    if not api_key:
        logger.debug("API key is not set, skipping update processing status")
        return

    auth_headers = {"Authorization": f"Bearer {api_key}", "version": utils.get_version()}
    for dataset in dataset_list:
        await process_dataset(dataset, auth_headers)


async def process_dataset(dataset, auth_headers):
    """Processes an individual dataset to update its status.

    Args:
        dataset (dict): The dataset to be processed, containing at least the 'dataset_id'.
        auth_headers (dict): Authorization headers containing API key for authentication.

    Raises:
        Exception: If fetching the status from the API or updating the database fails, logs the specific error.
    """

    dataset_id = dataset["dataset_id"]
    logger.debug(f"Updating processing status for dataset {dataset_id}")
    try:
        json_results = await fetch_status(dataset_id, auth_headers)
        status = get_valid_status(json_results, dataset_id)
        if status:
            await update_status_based_on_result(dataset_id, status, json_results)
    except Exception as e:  # pylint: disable=broad-except
        logger.error(f"Failed to process dataset {dataset_id}: {e}")


async def fetch_status(dataset_id, headers) -> dict:
    """Fetches the current status of a specific dataset from an API.

    Args:
        dataset_id (str): The unique identifier of the dataset whose status is being queried.
        headers (dict): A dictionary of headers to be used in the API request, including authorization tokens.

    Returns:
        dict: A dictionary containing the JSON response from the API which includes the dataset's status.
    """
    url = f"{conf.CURATION_STATUS_ENDPOINT}?dataset_id={dataset_id}"
    return utils.make_get_request(url, headers)


def get_valid_status(json_results, dataset_id):
    """Validates the status retrieved from an API against predefined Enum values.

    This function checks if the 'status' key in the provided JSON results matches any valid enum value
    in the `ProcessStatus` class. It logs the process tracing information if the status is valid, or an error if not.

    Args:
        json_results (dict): A dictionary containing the JSON payload returned by the API.
        dataset_id (str): The identifier for the dataset whose status is being checked.

    Returns:
        ProcessStatus or None: Returns a `ProcessStatus` enum if the status is valid, otherwise None.
    """
    status_str = json_results.get("status")
    try:
        print(status_str)
        status = ProcessStatus(status_str)
        logger.info(f"Tracing curation task, dataset_id is {dataset_id}, status is {status_str}")
        return status
    except ValueError:
        logger.error(f"Invalid status '{status_str}' received for dataset {dataset_id}")
        return None


async def update_status_based_on_result(dataset_id, status, json_results):
    """Updates the dataset's status based on the results obtained from an API call.

    Depending on the status, this function updates either the curation results or the dataset's status in the database.
    If the dataset is marked as 'Completed', it updates the curation results. For statuses 'Failed' or 'Error',
    it updates the dataset's status in the database.

    Args:
        dataset_id (str): The identifier of the dataset being processed.
        status (ProcessStatus): The current status of the dataset, which must be an instance of the `ProcessStatus` enum.
        json_results (dict): A dictionary containing additional data from the API needed for updating the curation results.

    Side Effects:
        Updates database entries for the dataset based on the status or updates the curation results.
    """
    if status in [ProcessStatus.COMPLETED, ProcessStatus.FAILED, ProcessStatus.ERROR]:
        if status == ProcessStatus.COMPLETED:
            await update_curation_results_async(dataset_id, json_results)
        else:
            await update_dataset_info_status_async(dataset_id, status.value)


async def update_dataset_info_status_async(dataset_id: str, status: str):
    """Asynchronously updates the status of a specific dataset in the database.

    Opens a database connection and updates the dataset status using the provided dataset ID and status. This function
    ensures that the operation is performed asynchronously and the database connection is managed using context management
    to ensure it is properly closed after the operation.

    Args:
        dataset_id (str): The unique identifier of the dataset whose status needs to be updated.
        status (str): The new status to be set for the dataset.

    Side Effects:
        Updates the dataset's status in the database.

    Raises:
        DatabaseError: If any issue occurs during the database connection or update process.
    """
    async with db_connection() as db:
        await acs.update_dataset_info_status(db, dataset_id, status)


async def update_curation_results_async(dataset_id: str, results: dict):
    """
    Asynchronously update the curation results in the database.

    Args:
        dataset_id (str): The unique identifier for the dataset.
        results (dict): The results dictionary containing the curation outcomes,
                        specifically the 'emd_results' and the 'status' of the curation.
    """
    processed_count = len(results["emd_results"])
    async with db_connection() as db:
        meta_list = await acs.update_curation_results(db, dataset_id, results)
        await acs.update_dataset_info(db, dataset_id, results["status"], meta_list, processed_count)


def get_dataset_embeddings(dataset_id: str) -> List[Dict]:
    """Retrieve dataset embeddings by dataset_id.

    Args:
        dataset_id (str): dataset id

    Returns:
        List[Dict]: List of dataset embeddings
    """
    return asyncio.get_event_loop().run_until_complete(get_dataset_embeddings_async(dataset_id, {}))


def extract_field_from_embeddings(name):
    """Helper function to simplify embedding extraction."""
    return {
        "$arrayElemAt": [
            {
                "$filter": {
                    "input": "$embeddings",
                    "as": "item",
                    "cond": {"$eq": ["$$item.name", name]},
                }
            },
            0,
        ]
    }


async def get_dataset_embeddings_async(dataset_id: str, filter_value: dict):
    """
    Fetches and processes embedding data for a specific dataset from the database using an aggregation pipeline.

    Args:
        dataset_id (str): The unique identifier for the dataset.
        filter_value (dict): Filters to apply to the dataset query.

    Returns:
        list: A list of processed documents with embeddings and other related information.
    """
    match_query = await build_match_query_with_filter(dataset_id, filter_value)
    match_query["$match"]["updated_at"] = {"$exists": True}

    pipeline = [
        match_query,
        {
            "$lookup": {
                "from": "raw_files",
                "localField": "image_id",
                "foreignField": "id",
                "as": "raw_files_docs",
            }
        },
        {"$unwind": "$raw_files_docs"},
        {
            "$project": {
                "_id": 0,
                "file_id": "$raw_files_docs.id",
                "thumbnail_url": "$raw_files_docs.thumbnail_url",
                "image_url": "$raw_files_docs.image_url",
                "created_at": 1,
                "embedding": extract_field_from_embeddings("embedding"),
                "curated_mask": extract_field_from_embeddings("curated_mask"),
                "anomaly_score": extract_field_from_embeddings("anomaly_score"),
            }
        },
        {
            "$project": {
                "file_id": 1,
                "thumbnail_url": 1,
                "image_url": 1,
                "embeddings": "$embedding.value",
                "curated_mask": "$curated_mask.value",
                "anomaly_score": {"$toDouble": "$anomaly_score.value"},
            }
        },
    ]

    async with db_connection() as db:
        result = await db.datasets.aggregate(pipeline).to_list(None)
        return result


def validate_status(status: str) -> bool:
    """Validates the status against the ProcessStatus enum.

    Args:
        status (str): The status to validate.

    Returns:
        bool: True if the status is valid, False otherwise.
    """
    try:
        ProcessStatus(status)
        return True
    except ValueError:
        all_status_values = [status.value for status in ProcessStatus]
        logger.error(f"Invalid status '{status}'. Valid statuses are: {all_status_values}")
        return False


def get_dataset_list(name: str = "", status: str = "") -> List[Dict]:
    """from get_dataset_list_async

    Args:
        name (str, optional): _description_. Defaults to "".
        status (str, optional): _description_. Defaults to "".

    Returns:
        List[Dict]: _description_
    """
    return asyncio.get_event_loop().run_until_complete(get_dataset_list_async(name, status))


def get_dataset(dataset_id: str) -> Dict:
    """from get_dataset_async

    Args:
        dataset_id(str): ID of the dataset to retrieve.

    Returns:
        Dict: dataset information
    """
    return asyncio.get_event_loop().run_until_complete(get_dataset_async(dataset_id))


async def get_dataset_async(dataset_id: str) -> Dict:
    """Get a list of datasets filtered by dataset_name and sorted by created_at in descending order.

    Args:
        dataset_id(str): ID of the dataset to retrieve.

    Returns:
        Dict: dataset information
    """
    filter_condition = {"dataset_id": dataset_id}
    async with db_connection() as db:
        doc = await db.dataset_info.find_one(filter_condition, {"_id": 0, "model_types": 0})
        if doc is None:
            return {}
        if doc["curation_count"]:
            doc["file_count"] = doc["curation_count"]
        return doc


async def get_dataset_list_async(name: str = "", status: str = "") -> List[Dict]:
    """Get a list of datasets filtered by dataset_name and sorted by created_at in descending order.

    Args:
        name_filter (str, optional): Partial name to filter datasets by. Defaults to "".

    Returns:
        List[Dict]: List of datasets
    """
    query = {}
    if name:
        query["dataset_name"] = {"$regex": name, "$options": "i"}
    if status:
        if not validate_status(status):
            return []
        query["status"] = status
    projection = {"_id": 0, "model_types": 0}
    async with db_connection() as db:
        documents = await db.dataset_info.find(query, projection).sort("created_at", -1).to_list(None)

        # Adjust file_count to curation_count if curation_count exists
        for document in documents:
            if "curation_count" in document:
                document["file_count"] = document["curation_count"]

        return documents


async def delete_dataset(dataset_id: str) -> None:
    """Delete a dataset by dataset_id.

    Args:
        dataset_id (str): ID of the dataset to delete.
    """
    async with db_connection() as db:
        await db.dataset_info.delete_one({"dataset_id": dataset_id})
        await db.datasets.delete_many({"dataset_id": dataset_id})


async def build_match_query_with_filter(dataset_id: str, filter_value: Dict[str, Any]) -> Dict[str, Any]:
    """매치 쿼리를 구성하는 함수"""
    match_query = {"$match": {"dataset_id": dataset_id, "updated_at": {"$exists": True}}}
    if "metas" in filter_value and isinstance(filter_value["metas"], list):
        metas: Dict[str, list] = {}
        for meta in filter_value["metas"]:
            key = find_meta_key(meta)
            if key:
                metas.setdefault(key, []).append(meta)
        filter_value = metas
        logger.debug(f"Get meta aggregation for dataset {dataset_id} with filter {filter_value}")
        dataset_file_ids = await apply_meta_filters(dataset_id, filter_value)
        match_query["$match"]["image_id"] = {"$in": dataset_file_ids}
    return match_query


def build_lookup_stage() -> Dict[str, Any]:
    """lookup 스테이지를 구성하는 함수"""
    return {
        "$lookup": {
            "from": "raw_files",
            "localField": "image_id",
            "foreignField": "id",
            "as": "raw_files_docs",
        }
    }


def export_dataset_files(datsaet_id: str, filename: str):
    """sync function from export_dataset_files_async

    Args:
        datsaet_id (str): dataset_id

    Returns:
        _type_: _description_
    """
    return asyncio.get_event_loop().run_until_complete(export_dataset_files_async(datsaet_id, filename, {}))


async def get_dataset_info(dataset_id: str):
    async with db_connection() as db:
        dataset_info = await db.dataset_info.find_one({"dataset_id": dataset_id}, {"_id": 0, "dataset_name": 1})
        return dataset_info


async def export_dataset_files_async(dataset_id: str, file_name: str, filter_value: dict):
    """Export dataset files to a CSV file."""
    query = {"dataset_id": dataset_id, "per_page": 0}
    dataset_files, _ = await get_dataset_file_list_async(query, filter_value)

    # check plz
    if not dataset_files:
        return None, None

    if not file_name:
        dataset_info = await get_dataset_info(dataset_id)
        if dataset_info and "dataset_name" in dataset_info:
            file_name = dataset_info["dataset_name"]
        else:
            file_name = dataset_id
    file_name = sanitize_filename(file_name) + ".json"
    logger.debug(f"Exporting dataset files to {file_name}")
    file_path = f"{conf.AIMMOCORE_WORKDIR}/{file_name}"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(dataset_files, f, ensure_ascii=False, indent=4)
    return file_path, file_name


def get_curation_data_combination_step():
    """
    Constructs a dictionary that specifies the fields to be included in the output of a MongoDB aggregation query.

    This function sets up a projection step for use in a MongoDB aggregation pipeline.
    It configures the extraction and transformation of specific fields from documents within a collection.
    The function prepares mappings for file metadata, embeddings transformations,
    and other related data for each document in the dataset.

    Returns:
        dict: A dict containing MongoDB projection operators that specify how to transform each document in the collection.
        This includes direct mappings of dataset and file identifiers, transformations of metadata,
        extraction of specific embeddings like 'curated_mask' and 'anomaly_score',
        and retrieval of specific elements from arrays using conditions.

    """
    return {
        "_id": 0,
        "dataset_id": 1,
        "file_id": "$raw_files_docs.id",
        "file_name": "$raw_files_docs.file_name",
        "file_path": "$raw_files_docs.file_path",
        "file_size": "$raw_files_docs.file_size",
        "thumbnail_url": "$raw_files_docs.thumbnail_url",
        "image_url": "$raw_files_docs.image_url",
        "metas": {"$map": {"input": "$metas", "as": "meta", "in": "$$meta.value"}},
        "embedding": extract_field_from_embeddings("embedding"),
        "curated_mask": extract_field_from_embeddings("curated_mask"),
        "anomaly_score": extract_field_from_embeddings("anomaly_score"),
        "similar_ids": extract_field_from_embeddings("similar_ids"),
        "similar_distances": extract_field_from_embeddings("similar_distances"),
        "created_at": 1,
    }


def get_dataset_raw_files_lookup_step():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {
        "$lookup": {
            "from": "raw_files",
            "localField": "image_id",
            "foreignField": "id",
            "as": "raw_files_docs",
        }
    }


def get_curation_data_refine_step():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {
        "dataset_id": 1,
        "file_id": 1,
        "file_name": 1,
        "file_path": 1,
        "file_size": 1,
        "thumbnail_url": 1,
        "image_url": 1,
        "metas": 1,
        "embeddings": "$embedding.value",
        "curated_mask": "$curated_mask.value",
        "anomaly_score": {"$toDouble": "$anomaly_score.value"},
        "similar_ids": "$similar_ids.value",
        "similar_distances": "$similar_distances.value",
        "created_at": 1,
    }


def get_dataset_file(dataset_id: str, file_id: str):
    return asyncio.get_event_loop().run_until_complete(get_dataset_file_async(dataset_id, file_id))


async def get_dataset_file_async(dataset_id: str, file_id: str):

    match_query = {"$match": {"dataset_id": dataset_id, "image_id": file_id}}
    pipeline = [
        match_query,
        get_dataset_raw_files_lookup_step(),
        {"$unwind": "$raw_files_docs"},  # 조인 결과 배열 풀기
        {"$project": get_curation_data_combination_step()},
        {"$project": get_curation_data_refine_step()},
    ]
    async with db_connection() as db:
        return await db.datasets.aggregate(pipeline).to_list(None)


def get_dataset_file_list_by_id(dataset_id: str):
    """sync function from get_dataset_file_list_async"""
    query = {"dataset_id": dataset_id}
    return asyncio.get_event_loop().run_until_complete(get_dataset_file_list_async(query, {}))


def get_dataset_file_list(query: dict, filter_value: dict):
    """sync function from get_dataset_file_list_async"""
    return asyncio.get_event_loop().run_until_complete(get_dataset_file_list_async(query, filter_value))


async def get_dataset_file_list_async(query: dict, filter_value: dict):
    """Retrieve a paginated list of dataset files based on the provided query and filter criteria.

    Args:
        query (dict): A dictionary containing query parameters. Expected keys are:
            - dataset_id (str): The ID of the dataset to query.
            - page (int, optional): The page number for pagination. Defaults to 1.
            - per_page (int, optional): The number of items per page for pagination. Defaults to 20.
            - sort (list of dict, optional): A list of dictionaries specifying the sort criteria,
              where each dictionary has 'field' and 'order' keys.
        filter_value (dict): A dictionary containing filter criteria to apply to the dataset query.


    Returns:
        tuple: A tuple containing:
            - list: A list of paginated dataset file results.
            - int: The total count of dataset files that match the query and filter criteria.

    """
    dataset_id = query["dataset_id"]

    page = query.get("page", 1)
    per_page = query.get("per_page", 20)
    # sort_criteria = {item["field"]: item["order"] for item in query["sort"]}

    match_query = await build_match_query_with_filter(dataset_id, filter_value)

    pipeline = [
        match_query,
        get_dataset_raw_files_lookup_step(),
        {"$unwind": "$raw_files_docs"},  # 조인 결과 배열 풀기
        {
            "$facet": {
                "total_count": [{"$count": "count"}],
                "paged_results": [
                    {"$skip": (page - 1) * per_page if per_page > 0 else 0},
                    {"$limit": per_page if per_page > 0 else 999999999},
                    {"$project": get_curation_data_combination_step()},
                    {"$project": get_curation_data_refine_step()},
                    {"$sort": {"file_path": 1, "file_name": 1}},
                ],
            }
        },
    ]

    async with db_connection() as db:
        paged_results = []
        total_count = 0
        async for result in db.datasets.aggregate(pipeline):
            total_count = result["total_count"][0]["count"] if result["total_count"] else 0
            paged_results = result["paged_results"]
    return paged_results, total_count


def find_meta_key(value: str):
    """메타 value를 기반으로 key를 찾습니다."""
    for key, values in META_TYPE.items():
        if value in values:
            return key
    return None


async def get_dataset_file_ids(dataset_id: str):
    """
    Retrieves a list of image IDs for a given dataset from the database.

    Args:
        dataset_id (str): The unique identifier for the dataset.

    Returns:
        list: A list of image IDs associated with the dataset.
    """
    async with db_connection() as db:
        query = {"dataset_id": dataset_id}
        projection = {"image_id": 1}
        dataset_files = await db.datasets.find(query, projection).to_list(None)
        dataset_file_ids = [d["image_id"] for d in dataset_files]
        return dataset_file_ids


async def get_dataset_meta_aggregation(dataset_id: str, filter_value: dict):
    """Retrieves an aggregation of metadata counts for a specific dataset based on provided filters.

    Args:
        dataset_id (str): The unique identifier for the dataset.
        filter_value (dict): A dictionary containing metadata filters. Expected format:
                             {'metas': ['rainy', 'daytime']}, where 'metas' is a key and the
                             list contains the metadata values to filter by.

    Returns:
        list: An aggregated list of metadata counts corresponding to the filtered dataset files.
              Each item in the list is a dictionary with metadata keys and their counts.
    """
    dataset_file_ids = await get_dataset_file_ids(dataset_id)
    if not dataset_file_ids:
        return []
    if "metas" in filter_value and isinstance(filter_value["metas"], list):
        metas: Dict[str, list] = {}
        for meta in filter_value["metas"]:
            key = find_meta_key(meta)
            if key:
                metas.setdefault(key, []).append(meta)
        filter_value = metas.copy()
    logger.debug(f"Get meta aggregation for dataset {dataset_id} with filter {filter_value}")
    dataset_file_ids = await apply_meta_filters(dataset_id, filter_value)
    aggregation = await get_meta_count_aggregation(dataset_id, dataset_file_ids)
    return aggregation


async def apply_meta_filters(dataset_id: str, metas: dict):
    """메타 name/ value 기반의 image id를 필터링합니다."""
    async with db_connection() as db:
        meta_filter_aggregation_pipeline = create_meta_filter_aggregation_pipeline(dataset_id, metas)
        cursor = db.datasets.aggregate(meta_filter_aggregation_pipeline)
        result = await cursor.to_list(None)
        return [doc["image_id"] for doc in result]


def create_meta_filter_aggregation_pipeline(dataset_id: str, conditions: dict):
    """Create aggregation pipeline for meta filtering

    Create aggregation pipeline for filtering documents based on meta name and value.

    Args:
        dataset_id: 조회할 dataset id
        conditions: {
            'weather': ['rainy', 'clear'],
            'time': ['daytime'],
            ...
        }
    Returns:
        aggregation pipeline
    """
    add_fields_stage = {"$addFields": {}}
    match_conditions = []

    for name, values in conditions.items():
        condition_field_name = f"{name}_condition"
        # have to fix......
        if name == "time":
            values = ["sunset" if value == "sunrise/sunset" else value for value in values]

        add_fields_stage["$addFields"][condition_field_name] = {
            "$ifNull": [
                {
                    "$filter": {
                        "input": "$metas",
                        "as": "meta",
                        "cond": {"$and": [{"$eq": ["$$meta.name", name]}, {"$in": ["$$meta.value", values]}]},
                    }
                },
                [],
            ]
        }
        # 생성된 필터링 조건을 기반으로 문서를 매칭하는 조건을 추가합니다.
        match_conditions.append({"$gt": [{"$size": f"${condition_field_name}"}, 0]})

    pipeline = [
        {"$match": {"dataset_id": dataset_id}},
        add_fields_stage,
        {"$match": {"$expr": {"$and": match_conditions}}},
        {"$project": {"image_id": 1}},  # 필요한 경우 추가 필드를 포함시킬 수 있습니다.
    ]

    return pipeline


def create_meta_count_aggregation_pipeline(dataset_id: str, image_id_list: list):
    """_summary_

    Args:
        dataset_id (str): _description_
        image_id_list (list): _description_

    Returns:
        _type_: _description_
    """
    pipeline = [
        {"$match": {"dataset_id": dataset_id, "image_id": {"$in": image_id_list}}},
        {"$unwind": "$metas"},
        {"$group": {"_id": {"name": "$metas.name", "value": "$metas.value"}, "count": {"$sum": 1}}},  # 합계
        {"$sort": {"_id.name": 1, "_id.value": 1}},
    ]
    return pipeline


def initialize_aggregation():
    """Initialize the aggregation dictionary based on META_TYPE."""
    return {key: {item: 0 for item in value} for key, value in META_TYPE.items()}


async def get_meta_count_aggregation(dataset_id: str, image_id_list: list):
    """메타별로 통계를 내어 반환합니다."""
    async with db_connection() as db:
        pipeline = create_meta_count_aggregation_pipeline(dataset_id, image_id_list)
        results = await db.datasets.aggregate(pipeline).to_list(None)
        aggregation = initialize_aggregation()
        for result in results:
            name = result["_id"]["name"]
            value = result["_id"]["value"]
            # have to fix......
            value = "sunrise/sunset" if value == "sunset" else value
            count = result["count"]
            aggregation[name][value] = count
        return camelize_top_level_keys(aggregation)


def camelize_string(s):
    parts = s.split("_")
    # 첫 부분을 제외하고 각 부분의 첫 글자만 대문자로 만듭니다.
    return "".join(part.capitalize() if i > 0 else part for i, part in enumerate(parts))


def camelize_top_level_keys(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            new_key = camelize_string(key)  # 최상위 키만 변환
            new_dict[new_key] = value  # 값을 그대로 유지
        return new_dict
    # 최상위 수준이 딕셔너리가 아니면 변환 없이 반환
    return data
