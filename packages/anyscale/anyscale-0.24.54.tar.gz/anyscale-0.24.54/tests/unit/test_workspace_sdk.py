from typing import Optional, Tuple

from common import TEST_CONTAINERFILE, TestLogger
import pytest

from anyscale import Anyscale
from anyscale._private.anyscale_client import FakeAnyscaleClient
from anyscale._private.sdk.timer import FakeTimer
from anyscale.compute_config.models import ComputeConfig, HeadNodeConfig
from anyscale.workspace import WorkspaceSDK
from anyscale.workspace.models import WorkspaceConfig


@pytest.fixture()
def workspace_sdk_with_fakes(
    sdk_with_fakes: Tuple[Anyscale, FakeAnyscaleClient, TestLogger, FakeTimer]
) -> Tuple[WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer]:
    sdk, client, logger, timer = sdk_with_fakes
    return sdk.workspace, client, logger, timer


class TestCreate:
    @pytest.mark.parametrize(
        "config", [WorkspaceConfig(name=None, project=None, cloud=None), None,],
    )
    def test_missing_arg(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
        config: Optional[WorkspaceConfig],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        with pytest.raises(ValueError, match="Workspace name must be configured"):
            sdk.create(config=config)

    def test_basic(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)
        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"

    def test_with_container_image(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(
                name="test_workspace", containerfile=TEST_CONTAINERFILE,
            )
        )
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)

        builds = fake_client.get_non_default_cluster_env_builds()
        assert len(builds) == 1
        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"
        assert created_workspace.environment_id == builds[0].id

    def test_with_image_uri(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(name="test_workspace", image_uri="test_image_uri",)
        )
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)
        builds = fake_client.get_non_default_cluster_env_builds()
        assert len(builds) == 1
        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"
        assert created_workspace.environment_id == builds[0].id

    def test_with_compute_config(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(
                name="test_workspace",
                compute_config=ComputeConfig(
                    cloud=fake_client.DEFAULT_CLOUD_NAME,
                    head_node=HeadNodeConfig(
                        instance_type="head-node-instance-type", flags={},
                    ),
                    flags={},
                ),
            )
        )
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)
        workspace_compute_config_id = created_workspace.compute_config_id
        compute_config = fake_client.get_compute_config(workspace_compute_config_id)
        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"
        assert compute_config.config.cloud_id == fake_client.DEFAULT_CLOUD_ID
        assert (
            compute_config.config.head_node_type.instance_type
            == "head-node-instance-type"
        )

    def test_with_idle_termination(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(name="test_workspace", idle_termination_minutes=180,)
        )
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)

        workspace_compute_config_id = created_workspace.compute_config_id
        compute_config = fake_client.get_compute_config(workspace_compute_config_id)
        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"
        assert compute_config.idle_timeout_minutes == 180

    def test_with_requirements(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(name="test_workspace", requirements=["emoji"],)
        )
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)

        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"
        assert fake_client._workspaces_dependencies[created_workspace.id] == ["emoji"]

    def test_with_env_vars(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(name="test_workspace", env_vars={"key": "value"},)
        )
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)

        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"
        assert fake_client._workspaces_env_vars[created_workspace.id] == {
            "key": "value"
        }

    def test_with_full_config(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(
                name="test_workspace",
                idle_termination_minutes=180,
                containerfile=TEST_CONTAINERFILE,
                compute_config=ComputeConfig(
                    cloud=fake_client.DEFAULT_CLOUD_NAME,
                    head_node=HeadNodeConfig(
                        instance_type="head-node-instance-type", flags={},
                    ),
                    flags={},
                ),
                env_vars={"key": "value"},
                requirements=["emoji"],
            )
        )
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)

        builds = fake_client.get_non_default_cluster_env_builds()
        workspace_compute_config_id = created_workspace.compute_config_id
        compute_config = fake_client.get_compute_config(workspace_compute_config_id)
        assert len(builds) == 1
        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"
        assert created_workspace.environment_id == builds[0].id
        assert created_workspace.cloud_id == fake_client.DEFAULT_CLOUD_ID
        assert created_workspace.creator_id == fake_client.DEFAULT_USER_ID
        assert created_workspace.creator_email == fake_client.DEFAULT_USER_EMAIL
        assert created_workspace.organization_id == fake_client.DEFAULT_ORGANIZATION_ID

        # verify compute config
        assert compute_config.idle_timeout_minutes == 180
        assert compute_config.config.cloud_id == fake_client.DEFAULT_CLOUD_ID
        assert (
            compute_config.config.head_node_type.instance_type
            == "head-node-instance-type"
        )

        # verify dependencies
        assert fake_client._workspaces_dependencies[created_workspace.id] == ["emoji"]
        assert fake_client._workspaces_env_vars[created_workspace.id] == {
            "key": "value"
        }


class TestStart:
    def test_missing_arg(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        with pytest.raises(ValueError, match="One of 'name' or 'id' must be provided."):
            sdk.start(name=None, id=None, cloud=None, project=None)

    def test_basic_with_id(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        sdk.start(id=workspace_id)
        created_workspace = fake_client.get_workspace(id=workspace_id)
        assert created_workspace is not None
        assert created_workspace.state == "Running"

    def test_basic_with_name(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        sdk.start(name="test_workspace")
        created_workspace = fake_client.get_workspace(id=workspace_id)
        assert created_workspace is not None
        assert created_workspace.state == "Running"


class TestTerminate:
    def test_missing_arg(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        with pytest.raises(ValueError, match="One of 'name' or 'id' must be provided."):
            sdk.terminate(name=None, id=None, cloud=None, project=None)

    def test_basic_with_id(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        sdk.terminate(id=workspace_id)
        created_workspace = fake_client.get_workspace(id=workspace_id)
        assert created_workspace is not None
        assert created_workspace.state == "Terminated"

    def test_basic_with_name(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        sdk.terminate(name="test_workspace")
        created_workspace = fake_client.get_workspace(id=workspace_id)
        assert created_workspace is not None
        assert created_workspace.state == "Terminated"
