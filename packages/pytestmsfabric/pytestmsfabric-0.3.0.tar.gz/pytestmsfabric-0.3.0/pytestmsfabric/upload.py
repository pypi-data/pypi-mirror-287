"""Upload test results to Azure Blob Storage."""

from pathlib import Path

from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import (
    DataLakeServiceClient,
)


def upload_file(file: str, test_id: str, account: str, container: str, folder: str) -> None:
    """Upload a file to Azure Blob Storage."""
    credential = DefaultAzureCredential()
    account_url = f"https://{account}.dfs.core.windows.net"
    service_client = DataLakeServiceClient(account_url, credential=credential)
    file_system_client = service_client.get_file_system_client(container)
    directory_client = file_system_client.get_directory_client(folder)
    file_client = directory_client.get_file_client(test_id + ".xml")

    input_file = Path(file)

    with input_file.open(mode="rb") as data:
        file_client.upload_data(data, overwrite=True)
