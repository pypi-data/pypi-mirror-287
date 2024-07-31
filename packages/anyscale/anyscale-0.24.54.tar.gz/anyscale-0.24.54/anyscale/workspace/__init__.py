from typing import Optional

from anyscale._private.anyscale_client import AnyscaleClientInterface
from anyscale._private.sdk import sdk_docs
from anyscale._private.sdk.base_sdk import Timer
from anyscale.cli_logger import BlockLogger
from anyscale.workspace._private.workspace_sdk import PrivateWorkspaceSDK
from anyscale.workspace.commands import (
    _CREATE_ARG_DOCSTRINGS,
    _CREATE_EXAMPLE,
    _START_ARG_DOCSTRINGS,
    _START_EXAMPLE,
    _TERMINATE_ARG_DOCSTRINGS,
    _TERMINATE_EXAMPLE,
    create,
    start,
    terminate,
)
from anyscale.workspace.models import WorkspaceConfig


class WorkspaceSDK:
    def __init__(
        self,
        *,
        client: Optional[AnyscaleClientInterface] = None,
        logger: Optional[BlockLogger] = None,
        timer: Optional[Timer] = None,
    ):
        self._private_sdk = PrivateWorkspaceSDK(
            client=client, logger=logger, timer=timer
        )

    @sdk_docs(
        doc_py_example=_CREATE_EXAMPLE, arg_docstrings=_CREATE_ARG_DOCSTRINGS,
    )
    def create(self, config: WorkspaceConfig) -> str:  # noqa: F811
        """Create a workspace.

        Returns the id of the workspace.
        """
        return self._private_sdk.create(config=config)

    @sdk_docs(
        doc_py_example=_START_EXAMPLE, arg_docstrings=_START_ARG_DOCSTRINGS,
    )
    def start(  # noqa: F811
        self,
        *,
        name: Optional[str] = None,
        id: Optional[str] = None,  # noqa: A002
        cloud: Optional[str] = None,
        project: Optional[str] = None,
    ) -> str:
        """Start a workspace.

        Returns the id of the started workspace.
        """
        return self._private_sdk.start(name=name, id=id, cloud=cloud, project=project)

    @sdk_docs(
        doc_py_example=_TERMINATE_EXAMPLE, arg_docstrings=_TERMINATE_ARG_DOCSTRINGS,
    )
    def terminate(  # noqa: F811
        self,
        *,
        name: Optional[str] = None,
        id: Optional[str] = None,  # noqa: A002
        cloud: Optional[str] = None,
        project: Optional[str] = None,
    ) -> str:
        """Terminate a workspace.

        Returns the id of the terminated workspace.
        """
        return self._private_sdk.terminate(
            name=name, id=id, cloud=cloud, project=project
        )
