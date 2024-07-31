import pathlib
from typing import Optional, Tuple

import click

from anyscale._private.models.image_uri import ImageURI
from anyscale.cli_logger import BlockLogger
from anyscale.commands.util import convert_kv_strings_to_dict
import anyscale.workspace
from anyscale.workspace.models import WorkspaceConfig


log = BlockLogger()  # CLI Logger


def _validate_workspace_name_and_id(
    name: Optional[str], id: Optional[str]  # noqa: A002
):
    if name is None and id is None:
        raise click.ClickException("One of '--name' and '--id' must be provided.")

    if name is not None and id is not None:
        raise click.ClickException("Only one of '--name' and '--id' can be provided.")


@click.group("workspace_v2", help="Anyscale workspace commands V2.")
def workspace_cli() -> None:
    pass


@workspace_cli.command(
    name="create", help="Create a workspace on Anyscale.",
)
@click.option(
    "-f",
    "--config-file",
    required=False,
    default=None,
    type=str,
    help="Path to a YAML config file to deploy. When deploying from a file, import path and arguments cannot be provided. Command-line flags will overwrite values read from the file.",
)
@click.option(
    "-n", "--name", required=False, help="Name of the workspace to create.",
)
@click.option(
    "--image-uri",
    required=False,
    default=None,
    type=str,
    help="Container image to use for the workspace. This is exclusive with --containerfile.",
)
@click.option(
    "--registry-login-secret",
    required=False,
    default=None,
    type=str,
    help="Name or identifier of the secret containing credentials to authenticate to the docker registry hosting the image. "
    "This can only be used when 'image_uri' is specified and the image is not hosted on Anyscale.",
)
@click.option(
    "--containerfile",
    required=False,
    default=None,
    type=str,
    help="Path to a containerfile to build the image to use for the workspace. This is exclusive with --image-uri.",
)
@click.option(
    "--ray-version",
    required=False,
    default=None,
    type=str,
    help="The Ray version (X.Y.Z) to the image specified by --image-uri. This is only used when --image-uri is provided. If not provided, the latest Ray version will be used.",
)
@click.option(
    "--compute-config",
    required=False,
    default=None,
    type=str,
    help="Named compute configuration to use for the workspace.",
)
@click.option(
    "--cloud",
    required=False,
    default=None,
    type=str,
    help="The Anyscale Cloud to run this workload on. If not provided, the organization default will be used (or, if running in a workspace, the cloud of the workspace).",
)
@click.option(
    "--project",
    required=False,
    default=None,
    type=str,
    help="Named project to use for the workspace. If not provided, the default project for the cloud will be used (or, if running in a workspace, the project of the workspace).",
)
@click.option(
    "-r",
    "--requirements",
    required=False,
    default=None,
    type=str,
    help="Path to a requirements.txt file containing dependencies for the workspace. These will be installed on top of the image.",
)
@click.option(
    "--env",
    required=False,
    multiple=True,
    type=str,
    help="Environment variables to set for the workspace. The format is 'key=value'. This argument can be specified multiple times. When the same key is also specified in the config file, the value from the command-line flag will overwrite the value from the config file.",
)
def create(  # noqa: PLR0913, PLR0912, C901
    config_file: Optional[str],
    name: Optional[str],
    image_uri: Optional[str],
    registry_login_secret: Optional[str],
    ray_version: Optional[str],
    containerfile: Optional[str],
    compute_config: Optional[str],
    cloud: Optional[str],
    project: Optional[str],
    requirements: Optional[str],
    env: Optional[Tuple[str]],
) -> None:
    """Creates a new workspace.

    A name must be provided, either in the file or in the arguments.

    `$ anyscale workspace_v2 create -n my-workspace`

    or add all the information in the config file and do:

    `$ anyscale workspace_v2 create -f config-file.yaml`

    Command-line flags override values in the config file.
    """
    if config_file is not None:
        if not pathlib.Path(config_file).is_file():
            raise click.ClickException(f"Config file '{config_file}' not found.")

        config = WorkspaceConfig.from_yaml(config_file)
    else:
        config = WorkspaceConfig()

    if containerfile and image_uri:
        raise click.ClickException(
            "Only one of '--containerfile' and '--image-uri' can be provided."
        )

    if ray_version and (not image_uri and not containerfile):
        raise click.ClickException(
            "Ray version can only be used with an image or containerfile.",
        )

    if registry_login_secret and (
        not image_uri or ImageURI.from_str(image_uri).is_cluster_env_image()
    ):
        raise click.ClickException(
            "Registry login secret can only be used with an image that is not hosted on Anyscale."
        )

    if name is not None:
        config = config.options(name=name)

    if not config.name:
        raise click.ClickException("Workspace name must be configured")

    if image_uri is not None:
        config = config.options(image_uri=image_uri)

    if registry_login_secret is not None:
        config = config.options(registry_login_secret=registry_login_secret)

    if ray_version is not None:
        config = config.options(ray_version=ray_version)

    if containerfile is not None:
        config = config.options(containerfile=containerfile)

    if compute_config is not None:
        config = config.options(compute_config=compute_config)

    if cloud is not None:
        config = config.options(cloud=cloud)
    if project is not None:
        config = config.options(project=project)

    if requirements is not None:
        if not pathlib.Path(requirements).is_file():
            raise click.ClickException(f"Requirements file '{requirements}' not found.")
        config = config.options(requirements=requirements)
    if env:
        env_dict = convert_kv_strings_to_dict(env)
        if env_dict:
            config = config.options(env_vars=env_dict)

    anyscale.workspace.create(config,)


@workspace_cli.command(name="start", short_help="Starts a workspace.")
@click.option(
    "--id", "--workspace-id", required=False, help="Unique ID of the workspace."
)
@click.option("--name", "-n", required=False, help="Name of the workspace.")
@click.option(
    "--cloud",
    required=False,
    default=None,
    type=str,
    help="The Anyscale Cloud to run this workload on. If not provided, the organization default will be used.",
)
@click.option(
    "--project",
    required=False,
    default=None,
    type=str,
    help="Named project to use for the workpsace. If not provided, the default project for the cloud will be used.",
)
def start(
    id: Optional[str],  # noqa: A002
    name: Optional[str],
    cloud: Optional[str],
    project: Optional[str],
) -> None:
    """Start a workspace.

    To specify the workspace by name, use the --name flag. To specify the workspace by id, use the --id flag. Either name or
id should be used, specifying both will result in an error.
    """
    _validate_workspace_name_and_id(name=name, id=id)
    anyscale.workspace.start(name=name, id=id, cloud=cloud, project=project)


@workspace_cli.command(name="terminate", short_help="Terminate a workspace.")
@click.option(
    "--id", "--workspace-id", required=False, help="Unique ID of the workspace."
)
@click.option("--name", "-n", required=False, help="Name of the workspace.")
@click.option(
    "--cloud",
    required=False,
    default=None,
    type=str,
    help="The Anyscale Cloud to run this workload on. If not provided, the organization default will be used.",
)
@click.option(
    "--project",
    required=False,
    default=None,
    type=str,
    help="Named project to use for the workpsace. If not provided, the default project for the cloud will be used.",
)
def terminate(
    id: Optional[str],  # noqa: A002
    name: Optional[str],
    cloud: Optional[str],
    project: Optional[str],
) -> None:
    """Terminate a workspace.

    To specify the workspace by name, use the --name flag. To specify the workspace by id, use the --id flag. Either name or
id should be used, specifying both will result in an error.
    """
    _validate_workspace_name_and_id(name=name, id=id)
    anyscale.workspace.terminate(name=name, id=id, cloud=cloud, project=project)
