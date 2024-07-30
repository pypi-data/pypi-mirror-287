import base64

from azure.core.credentials import AccessToken
from azure.identity import DefaultAzureCredential
from fabricclientaio.auth.fabrictokenprovider import FabricTokenProvider
from fabricclientaio.fabricclient import FabricClient
from fabricclientaio.fabricworkspaceclient import FabricWorkspaceClient


class DefaultAzureCredentialProvider(FabricTokenProvider):
    """Use the default Azure credential to get a token."""

    def __init__(self):
        """Initialize the class."""

    async def get_token(self) -> AccessToken:
        """Get a token."""
        default_credentials = DefaultAzureCredential()
        return default_credentials.get_token("https://api.fabric.microsoft.com/.default")


async def download_test_notebooks(workspace_id: str) -> None:
    """Download test notebooks from the workspace."""
    fabric_client = FabricClient(DefaultAzureCredentialProvider())

    workspace_client = FabricWorkspaceClient(fabric_client, workspace_id)
    to_download = [item async for item in workspace_client.get_items() if item.type == "Notebook"]

    # TODO(): gather the notebooks in parallel
    for item in to_download:
        item_definition = await workspace_client.get_item_definition(item.id, "ipynb")
        prefix = "tests/" if item.display_name.startswith("test_") else ""
        # TODO(): Use async file io? Not currently supported by asyncio.
        with open(f"{prefix}{item.display_name}.ipynb", "w") as file:
            payload_base64 = item_definition["definition"]["parts"][0]["payload"]
            file.write(base64.b64decode(payload_base64).decode("utf-8"))
