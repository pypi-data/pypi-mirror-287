"""Pytest plugin for Microsoft Fabric."""

from __future__ import annotations

import asyncio
import os
import sys
from typing import TYPE_CHECKING, Sequence

import pytest

from pytestmsfabric import upload
from pytestmsfabric.nbdownloader import download_test_notebooks
from pytestmsfabric.nbimport import NotebookFinder

if TYPE_CHECKING:
    from pathlib import Path

from pyspark.sql import SparkSession

sys.meta_path.append(NotebookFinder())

_downloaded_notebooks = False

def get_workspace_id() -> str:
    """Return the workspace ID."""
    msg = "You are not running in a Fabric workspace. Please add --workspace-id to the command line."
    spark = SparkSession.getActiveSession()
    if spark is None:
        raise AttributeError(msg)

    res = spark.conf.get("trident.workspace.id")
    if res is None:
        raise AttributeError(msg)

    return res


@pytest.hookimpl()
def pytest_addoption(parser: pytest.Parser) -> None:
    """Add options to the pytest command line."""
    parser.addoption(
        "--test-id",
        action="store",
        dest="fabric_test_id",
        default="latest",
        help="Test ID. Used to identify the test run.",
    )

    parser.addoption(
        "--storage-account",
        action="store",
        dest="fabric_storage_account",
        default=None,
        help="Storage account name.",
    )

    parser.addoption(
        "--container",
        action="store",
        dest="fabric_container",
        default="tests",
        help="Container name.",
    )

    parser.addoption(
        "--folder",
        action="store",
        dest="fabric_folder",
        default="/",
        help="Folder name.",
    )

    parser.addoption(
        "--workspace-id",
        action="store",
        dest="fabric_workspace_id",
        default=None,
        help="Workspace ID.",
    )


@pytest.hookimpl()
def pytest_collect_file(file_path: Path, path: str, parent: pytest.Collector) -> pytest.Collector | None:  # noqa: ARG001
    """Collect Jupyter Notebooks notebooks as test modules."""
    if file_path.name.endswith(".ipynb"):
        return pytest.Module.from_parent(parent, path=file_path)
    return None

@pytest.hookimpl()
def pytest_configure(config: pytest.Config) -> None:
    """Plugin configuration hook."""
    config.addinivalue_line("markers", "dq: data quality test.")

    my_arg = config.getoption("--storage-account")
    if my_arg is None:
        pytest.exit("The --storage-account option is required.", returncode=1)

    workspace_id = config.getoption("--workspace-id")
    if workspace_id is None:
        workspace_id = get_workspace_id()
        config.option.fabric_workspace_id = workspace_id

    global _downloaded_notebooks  # noqa: PLW0603
    if not _downloaded_notebooks:
        try:
            asyncio.get_running_loop()
            pytest.exit(
                "pytestmsfabric cannot be run from an existing event loop. Use pytestmsfabric.main.",
                returncode=1,
            )
        except RuntimeError:
            pass
        asyncio.run(download_test_notebooks(workspace_id))
        _downloaded_notebooks = True


@pytest.hookimpl()
def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    """Session finish hook."""
    try:
        xml_path: str = session.config.option.nunit_xmlpath
    except AttributeError as e:
        msg = "Please install pytest-azurepipelines."
        raise AttributeError(msg) from e

    upload.upload_file(
        xml_path,
        session.config.option.fabric_test_id,
        session.config.option.fabric_storage_account,
        session.config.option.fabric_container,
        session.config.option.fabric_folder,
    )


async def main(
    args: list[str] | os.PathLike[str] | None = None,
    plugins: Sequence[str | object] | None = None,
) -> int | pytest.ExitCode:
    """Perform an in-process test run.

    :param args:
        List of command line arguments. If `None` or not given, defaults to reading
        arguments directly from the process command line (:data:`sys.argv`).
    :param plugins: List of plugin objects to be auto-registered during initialization.

    :returns: An exit code.
    """
    config = pytest.Config.fromdictargs({"args": args, "plugins": plugins}, [])

    workspace_id = config.getoption("--workspace-id")
    if workspace_id is None:
        workspace_id = get_workspace_id()

    global _downloaded_notebooks  # noqa: PLW0603
    await download_test_notebooks(workspace_id)

    _downloaded_notebooks = True

    return pytest.main(args=args, plugins=plugins)
