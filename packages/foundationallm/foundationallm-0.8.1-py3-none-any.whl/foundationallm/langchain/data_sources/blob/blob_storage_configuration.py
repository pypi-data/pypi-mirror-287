from typing import List, Optional, Literal
from foundationallm.langchain.data_sources import DataSourceConfiguration

class BlobStorageConfiguration(DataSourceConfiguration):
    """
    Connection information indicating the connection string to connect,
    the container to find the files, and the list of files to process.
    """
    configuration_type: Literal['blob_storage']
    connection_string_secret: str
    container: str
    files: Optional[List[str]] = None
