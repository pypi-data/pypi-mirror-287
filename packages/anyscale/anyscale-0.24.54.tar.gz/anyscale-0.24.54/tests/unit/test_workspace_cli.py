import os
from typing import Dict, Generator, Optional, Tuple
import uuid

import click
from click.testing import CliRunner
import pytest

from anyscale._private.sdk import _LAZY_SDK_SINGLETONS
from anyscale.commands.workspace_commands_v2 import create, start, terminate
from anyscale.workspace.commands import _WORKSPACE_SDK_SINGLETON_KEY
from anyscale.workspace.models import WorkspaceConfig


def _get_test_file_path(subpath: str) -> str:
    return os.path.join(os.path.dirname(__file__), "test_files/", subpath)


EMPTY_CONFIG_PATH = _get_test_file_path("workspace_config_files/empty.yaml")
MINIMAL_CONFIG_PATH = _get_test_file_path("workspace_config_files/minimal.yaml")
FULL_CONFIG_PATH = _get_test_file_path("workspace_config_files/full.yaml")
UNRECOGNIZED_OPTION_CONFIG_PATH = _get_test_file_path(
    "workspace_config_files/unrecognized_option.yaml"
)

FULL_CONFIG_SCHEDULE_NAME = "test-name-from-file"


class FakeWorkspaceSDK:
    def __init__(self):
        self._created_workspaces: Dict[str, WorkspaceConfig] = {}
        self._workspace_status: Dict[str, str] = {}

    def _resolve_to_workspace_model(
        self,
        *,
        id: Optional[str] = None,  # noqa: A002
        name: Optional[str] = None,
        cloud: Optional[str] = None,
        project: Optional[str] = None,
    ) -> Tuple[str, WorkspaceConfig]:
        workspace_config = None
        workspace_id = None
        if id is not None:
            workspace_config = self._created_workspaces.get(id)
            workspace_id = id
        elif name is not None:
            for key, config in self._created_workspaces.items():
                if (
                    config.name == name
                    and (cloud is None or config.cloud == cloud)
                    and (project is None or config.project == project)
                ):
                    workspace_config = config
                    workspace_id = key
                    break
        assert workspace_id is not None, "Workspace was not found."
        if workspace_config is None:
            raise RuntimeError("Workspace was not found.")
        return workspace_id, workspace_config

    def create(self, config: WorkspaceConfig) -> str:
        assert isinstance(config, WorkspaceConfig)
        id = str(uuid.uuid4())  # noqa: A001
        self._created_workspaces[id] = config
        return id

    def start(
        self,
        *,
        name: Optional[str] = None,
        id: Optional[str] = None,  # noqa: A002
        cloud: Optional[str] = None,
        project: Optional[str] = None,
    ) -> str:
        workspace_id, _ = self._resolve_to_workspace_model(
            name=name, id=id, cloud=cloud, project=project
        )
        self._workspace_status[workspace_id] = "Running"
        return workspace_id

    def terminate(
        self,
        *,
        name: Optional[str] = None,
        id: Optional[str] = None,  # noqa: A002
        cloud: Optional[str] = None,
        project: Optional[str] = None,
    ) -> str:
        workspace_id, _ = self._resolve_to_workspace_model(
            name=name, id=id, cloud=cloud, project=project
        )
        self._workspace_status[workspace_id] = "Terminated"
        return workspace_id


@pytest.fixture()
def fake_workspace_sdk() -> Generator[FakeWorkspaceSDK, None, None]:
    fake_workspace_sdk = FakeWorkspaceSDK()
    _LAZY_SDK_SINGLETONS[_WORKSPACE_SDK_SINGLETON_KEY] = fake_workspace_sdk
    try:
        yield fake_workspace_sdk
    finally:
        del _LAZY_SDK_SINGLETONS[_WORKSPACE_SDK_SINGLETON_KEY]


def _assert_error_message(result: click.testing.Result, *, message: str):
    assert result.exit_code != 0
    assert message in result.stdout


class TestCreate:
    def test_missing_arg(self, fake_workspace_sdk):
        runner = CliRunner()
        result = runner.invoke(create)
        _assert_error_message(result, message="Workspace name must be configured")

    def test_config_file_not_found(self, fake_workspace_sdk):
        runner = CliRunner()
        result = runner.invoke(create, ["-f", "missing_config.yaml"])
        _assert_error_message(
            result, message="Error: Config file 'missing_config.yaml' not found.",
        )

    @pytest.mark.parametrize(
        "config_file_arg", [MINIMAL_CONFIG_PATH, FULL_CONFIG_PATH],
    )
    def test_basic(self, fake_workspace_sdk, config_file_arg):
        runner = CliRunner()
        result = runner.invoke(create, ["-f", config_file_arg])
        assert result.exit_code == 0, result.stdout
        assert len(fake_workspace_sdk._created_workspaces) == 1

    def test_override_name(self, fake_workspace_sdk):
        runner = CliRunner()
        name = "test-different-name"
        result = runner.invoke(create, ["--name", name, "-f", FULL_CONFIG_PATH])
        assert result.exit_code == 0
        assert result.exit_code == 0, result.stdout
        assert len(fake_workspace_sdk._created_workspaces) == 1

        workspace_config = list(fake_workspace_sdk._created_workspaces.values())[0]
        assert workspace_config.name == name


class TestStart:
    def test_missing_arg(self, fake_workspace_sdk):
        runner = CliRunner()
        result = runner.invoke(create)
        _assert_error_message(result, message="Workspace name must be configured")

    def test_start_with_id(self, fake_workspace_sdk):
        runner = CliRunner()
        result = runner.invoke(create, ["-f", MINIMAL_CONFIG_PATH])
        assert result.exit_code == 0, result.stdout

        # Start the workspace
        workspace_id = list(fake_workspace_sdk._created_workspaces.keys())[0]

        result = runner.invoke(start, ["--id", workspace_id])
        assert result.exit_code == 0, result.stdout
        assert fake_workspace_sdk._workspace_status[workspace_id] == "Running"

    def test_start_with_name(self, fake_workspace_sdk):
        runner = CliRunner()
        result = runner.invoke(create, ["-f", MINIMAL_CONFIG_PATH])
        assert result.exit_code == 0, result.stdout

        # Start the workspace
        workspace_id = list(fake_workspace_sdk._created_workspaces.keys())[0]
        workspace_name = list(fake_workspace_sdk._created_workspaces.values())[0].name
        result = runner.invoke(start, ["--name", workspace_name])
        assert result.exit_code == 0, result.stdout
        assert fake_workspace_sdk._workspace_status[workspace_id] == "Running"

    def test_invalid_args(self, fake_workspace_sdk):
        runner = CliRunner()
        result = runner.invoke(create, ["-f", MINIMAL_CONFIG_PATH])
        assert result.exit_code == 0, result.stdout

        workspace_id = list(fake_workspace_sdk._created_workspaces.keys())[0]
        workspace_name = list(fake_workspace_sdk._created_workspaces.values())[0].name

        result = runner.invoke(start, ["--name", workspace_name, "--id", workspace_id])
        _assert_error_message(
            result, message="Only one of '--name' and '--id' can be provided."
        )


class TestTerminate:
    def test_missing_arg(self, fake_workspace_sdk):
        runner = CliRunner()
        result = runner.invoke(create)
        _assert_error_message(result, message="Workspace name must be configured")

    def test_terminate_with_id(self, fake_workspace_sdk):
        runner = CliRunner()
        result = runner.invoke(create, ["-f", MINIMAL_CONFIG_PATH])
        assert result.exit_code == 0, result.stdout

        # Terminate the workspace
        workspace_id = list(fake_workspace_sdk._created_workspaces.keys())[0]

        result = runner.invoke(terminate, ["--id", workspace_id])
        assert result.exit_code == 0, result.stdout
        assert fake_workspace_sdk._workspace_status[workspace_id] == "Terminated"

    def test_terminate_with_name(self, fake_workspace_sdk):
        runner = CliRunner()
        result = runner.invoke(create, ["-f", MINIMAL_CONFIG_PATH])
        assert result.exit_code == 0, result.stdout

        # Terminate the workspace
        workspace_id = list(fake_workspace_sdk._created_workspaces.keys())[0]
        workspace_name = list(fake_workspace_sdk._created_workspaces.values())[0].name
        result = runner.invoke(terminate, ["--name", workspace_name])
        assert result.exit_code == 0, result.stdout
        assert fake_workspace_sdk._workspace_status[workspace_id] == "Terminated"

    def test_invalid_args(self, fake_workspace_sdk):
        runner = CliRunner()
        result = runner.invoke(create, ["-f", MINIMAL_CONFIG_PATH])
        assert result.exit_code == 0, result.stdout

        workspace_id = list(fake_workspace_sdk._created_workspaces.keys())[0]
        workspace_name = list(fake_workspace_sdk._created_workspaces.values())[0].name

        result = runner.invoke(
            terminate, ["--name", workspace_name, "--id", workspace_id]
        )
        _assert_error_message(
            result, message="Only one of '--name' and '--id' can be provided."
        )
