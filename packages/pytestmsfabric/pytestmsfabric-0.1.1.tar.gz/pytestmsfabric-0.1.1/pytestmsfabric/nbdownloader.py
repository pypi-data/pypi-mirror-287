import asyncio
import base64
from azure.core.credentials import AccessToken
from azure.identity import DefaultAzureCredential
from fabricclientaio.auth.fabrictokenprovider import FabricTokenProvider
from fabricclientaio.fabricclient import FabricClient
from fabricclientaio.fabriccoreclient import FabricCoreClient
from fabricclientaio.fabricworkspaceclient import FabricWorkspaceClient


class DefaultAzureCredentialProvider(FabricTokenProvider):
    def __init__(self):
        pass

    async def get_token(self) -> AccessToken:
        default_credentials = DefaultAzureCredential()
        return default_credentials.get_token("https://api.fabric.microsoft.com/.default")


def download_test_notebooks(workspace_id: str) -> None:
    """Download test notebooks from the workspace."""
    try:
        event_loop = asyncio.get_running_loop()
        event_loop.run_until_complete(_download_test_notebooks(workspace_id))
    except RuntimeError:
        asyncio.run(_download_test_notebooks(workspace_id))

async  def _download_test_notebooks(workspace_id: str) -> None:
    fabric_client = FabricClient(DefaultAzureCredentialProvider())

    workspace_client = FabricWorkspaceClient(fabric_client, workspace_id)
    to_download = [item async for item in workspace_client.get_items() if item.type == "Notebook"]

    for item in to_download:
        item_definition = await workspace_client.get_item_definition(item.id, "ipynb")
        prefix = "tests/" if item.display_name.startswith("test_") else ""
        with open(f"{prefix}{item.display_name}.ipynb", "w") as file:
            payload_base64 = item_definition["definition"]["parts"][0]["payload"]
            file.write(base64.b64decode(payload_base64).decode("utf-8"))
