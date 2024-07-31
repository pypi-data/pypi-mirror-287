from typing import Optional

from anyscale._private.sdk import sdk_command
from anyscale.workspace._private.workspace_sdk import PrivateWorkspaceSDK
from anyscale.workspace.models import WorkspaceConfig


_WORKSPACE_SDK_SINGLETON_KEY = "workspace_sdk"

_CREATE_EXAMPLE = """
import anyscale
from anyscale.workspace.models import WorkspaceConfig

anyscale.workspace.create(
    WorkspaceConfig(
        name="my-workspace",
        idle_termination_minutes=120,
    ),
)
"""

_CREATE_ARG_DOCSTRINGS = {"config": "The config for defining the workspace."}


@sdk_command(
    _WORKSPACE_SDK_SINGLETON_KEY,
    PrivateWorkspaceSDK,
    doc_py_example=_CREATE_EXAMPLE,
    arg_docstrings=_CREATE_ARG_DOCSTRINGS,
)
def create(config: WorkspaceConfig, *, _sdk: PrivateWorkspaceSDK) -> str:
    """Create a workspace.

    Returns the id of the created workspace.
    """
    return _sdk.create(config)


_START_EXAMPLE = """
import anyscale

anyscale.workspace.start(
    name="my-workspace",
)
"""

_START_ARG_DOCSTRINGS = {
    "name": "Name of the workspace.",
    "id": "Unique ID of the workspace",
    "cloud": "The Anyscale Cloud to run this workload on. If not provided, the organization default will be used (or, if running in a workspace, the cloud of the workspace).",
    "project": "Named project to use for the workspace. If not provided, the default project for the cloud will be used (or, if running in a workspace, the project of the workspace).",
}


@sdk_command(
    _WORKSPACE_SDK_SINGLETON_KEY,
    PrivateWorkspaceSDK,
    doc_py_example=_START_EXAMPLE,
    arg_docstrings=_START_ARG_DOCSTRINGS,
)
def start(
    *,
    name: Optional[str] = None,
    id: Optional[str] = None,  # noqa: A002
    cloud: Optional[str] = None,
    project: Optional[str] = None,
    _sdk: PrivateWorkspaceSDK
) -> str:
    """Start a workspace.

    Returns the id of the started workspace.
    """
    return _sdk.start(name=name, id=id, cloud=cloud, project=project)


_TERMINATE_EXAMPLE = """
import anyscale

anyscale.workspace.terminate(
    name="my-workspace",
)
"""

_TERMINATE_ARG_DOCSTRINGS = {
    "name": "Name of the workspace.",
    "id": "Unique ID of the workspace",
    "cloud": "The Anyscale Cloud to run this workload on. If not provided, the organization default will be used (or, if running in a workspace, the cloud of the workspace).",
    "project": "Named project to use for the workspace. If not provided, the default project for the cloud will be used (or, if running in a workspace, the project of the workspace).",
}


@sdk_command(
    _WORKSPACE_SDK_SINGLETON_KEY,
    PrivateWorkspaceSDK,
    doc_py_example=_TERMINATE_EXAMPLE,
    arg_docstrings=_TERMINATE_ARG_DOCSTRINGS,
)
def terminate(
    *,
    name: Optional[str] = None,
    id: Optional[str] = None,  # noqa: A002
    cloud: Optional[str] = None,
    project: Optional[str] = None,
    _sdk: PrivateWorkspaceSDK
) -> str:
    """Terminate a workspace.

    Returns the id of the terminated workspace.
    """
    return _sdk.terminate(name=name, id=id, cloud=cloud, project=project)
