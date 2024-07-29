"""Configuration file for AIMMOCORE"""

import os

AIMMOCORE_HOME = os.path.join(os.path.expanduser("~"), ".aimmocore")
AIMMOCORE_WORKDIR = f"{AIMMOCORE_HOME}/workdir"
CURATION_UPLOAD_ENDPOINT = "https://curation-dataset-upload.azurewebsites.net/api/curation/upload"
CURATION_STATUS_ENDPOINT = "https://curation-status.azurewebsites.net/api/curation/status"
CURATION_AUTH_ENDPOINT = "https://curation-status.azurewebsites.net/api/curation/auth"
THUMBNAIL_DIR = f"{AIMMOCORE_HOME}/thumbnails"
DEFAULT_CURATION_MODEL_ID = "va-torch-meta-emd:3"
REQUEST_TIMEOUT = 10
CURATION_MINIMUM_SIZE = 30
SUPPORT_IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".bmp"]
DEFAULT_LOCAL_DB_PORT = 27817


def init_directory(path):
    """Ensure that the directory exists."""
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def init_workspace():
    """Initialize workspace"""
    if not os.path.exists(AIMMOCORE_WORKDIR):
        os.makedirs(AIMMOCORE_WORKDIR, exist_ok=True)


def init_thumbnail_dir():
    """Initialize thumbnail directory"""
    if not os.path.exists(THUMBNAIL_DIR):
        os.makedirs(THUMBNAIL_DIR, exist_ok=True)


def get_database_port():
    """Get the default local database port."""
    return DEFAULT_LOCAL_DB_PORT


init_workspace()
init_thumbnail_dir()
