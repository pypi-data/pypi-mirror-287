from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class UploadInfo:
    """
    UploadInfo represents the information required for uploading.
    """
    ak: str
    sk: str
    token: str  # upload token
    endpoint: str  # endpoint
    region: str  # region
    bucket: str  # bucket for uploading
    prefix_to_save: str  # file upload directory structure: dataset / user ID /

@dataclass(frozen=True)
class DatasetFile:
    """
    DatasetFile represents a file on S3.
    """
    _id: str
    key: str
    size: int

@dataclass(frozen=True)
class Dataset:
    """
    Dataset represents a dataset.
    """
    _id: str
    title: str
    short_description: str
    folder_name: str
    files: list[DatasetFile]
    created_at: datetime
    updated_at: datetime
