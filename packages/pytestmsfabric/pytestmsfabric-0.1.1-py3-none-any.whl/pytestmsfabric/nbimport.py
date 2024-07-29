"""Import Jupyter Notebooks as modules in Python."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from importlib.machinery import ModuleSpec

import importlib.abc
import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Sequence

from IPython.core.interactiveshell import InteractiveShell
from nbformat import NotebookNode, read

BuiltInImporter = importlib.abc.MetaPathFinder

class NotebookLoader(importlib.abc.Loader):
    """Module loader for Jupyter Notebooks."""

    def __init__(self) -> None:
        """Initialize the loader."""
        self.shell = InteractiveShell.instance()

    def create_module(self, spec: ModuleSpec) -> ModuleType:
        """Return a module to initialize and into which to load.

        This method should raise ImportError if anything prevents it
        from creating a new module.  It may return None to indicate
        that the spec should create the new module.
        """
        module = ModuleType(spec.name)
        module.__file__ = spec.origin
        module.__loader__ = spec.loader

        return module

    def exec_module(self, module: ModuleType) -> None:
        """Initialize the module by executing the notebook."""
        if module.__file__ is None:
            msg = f"Cannot find notebook {module.__name__}"
            raise ImportError(msg)

        # Read the notebook from disk and parse it.
        notebook_version = 4
        with Path(module.__file__).open(encoding="utf-8") as notebook_file:
            notebook_node: NotebookNode = read(notebook_file, notebook_version)

        # Ensure that magics that would affect the user_ns actually affect the notebook module's ns.
        save_user_ns = self.shell.user_ns
        self.shell.user_ns = module.__dict__

        try:
            for cell in notebook_node.cells:
                if cell.cell_type == "code":
                    # Transform the input to executable Python.
                    code = self.shell.input_transformer_manager.transform_cell(cell.source)
                    # Run the code in the module.

                    # Execute the code in the module.
                    exec(code, module.__dict__)  # noqa: S102
        finally:
            self.shell.user_ns = save_user_ns


class NotebookFinder(importlib.abc.MetaPathFinder):
    """Module finder that locates Jupyter Notebooks."""

    _module_spec_cache: dict[Path, ModuleSpec | None]

    def __init__(self) -> None:
        """Initialize the finder."""
        self._module_spec_cache = {}

    def find_spec(
            self,
            fullname: str,
            path: Sequence[str] | None,
            _target: ModuleType | None = None,
        ) -> ModuleSpec | None:
        """Create a ModuleSpec for the specified notebook if it exists."""
        file_name = fullname.rsplit(".", 1)[-1] + ".ipynb"

        search_dir = Path()
        if path:
            search_dir = search_dir.joinpath(*path)

        file_path = search_dir / file_name

        if file_path in self._module_spec_cache:
            return self._module_spec_cache[file_path]

        if not file_path.is_file():
            self._module_spec_cache[file_path] = None
            return None

        spec = importlib.util.spec_from_file_location(
            fullname,
            file_path,
            loader=NotebookLoader(),
        )

        if spec is None:
            return None

        self._module_spec_cache[file_path] = spec
        return spec

    def invalidate_caches(self) -> None:
        """Clear the finder's cache, if any.

        This method is used by importlib.invalidate_caches().
        """
        self._module_spec_cache = {}
