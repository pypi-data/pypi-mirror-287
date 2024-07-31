from typing import Optional

from anyscale._private.workload.workload_sdk import WorkloadSDK
from anyscale.client.openapi_client.models import (
    CreateExperimentalWorkspace,
    ExperimentalWorkspace,
)
from anyscale.utils.runtime_env import parse_requirements_file
from anyscale.workspace.models import WorkspaceConfig


class PrivateWorkspaceSDK(WorkloadSDK):
    def _resolve_to_workspace_model(
        self,
        *,
        id: Optional[str] = None,  # noqa: A002
        name: Optional[str] = None,
        cloud: Optional[str] = None,
        project: Optional[str] = None,
    ) -> ExperimentalWorkspace:
        if name is None and id is None:
            raise ValueError("One of 'name' or 'id' must be provided.")

        if name is not None and id is not None:
            raise ValueError("Only one of 'name' or 'id' can be provided.")

        if id is not None and (cloud is not None or project is not None):
            raise ValueError("'cloud' and 'project' should only be used with 'name'.")

        model: Optional[ExperimentalWorkspace] = self.client.get_workspace(
            name=name, id=id, cloud=cloud, project=project
        )
        if model is None:
            if name is not None:
                raise ValueError(f"Workspace with name '{name}' was not found.")
            else:
                raise ValueError(f"Workspace with ID '{id}' was not found.")

        return model

    def create(self, config: WorkspaceConfig) -> str:
        if not config or config.name is None:
            raise ValueError("Workspace name must be configured")

        name = config.name

        compute_config_id, cloud_id = self.resolve_compute_config_and_cloud_id(
            compute_config=config.compute_config, cloud=config.cloud,
        )

        project_id = self.client.get_project_id(
            parent_cloud_id=cloud_id, name=config.project
        )

        build_id = None

        if config.containerfile is not None:
            build_id = self._image_sdk.build_image_from_containerfile(
                name=f"image-for-workspace-{name}",
                containerfile=self.get_containerfile_contents(config.containerfile),
                ray_version=config.ray_version,
            )
        elif config.image_uri is not None:
            build_id = self._image_sdk.registery_image(
                image_uri=config.image_uri,
                registry_login_secret=config.registry_login_secret,
                ray_version=config.ray_version,
            )

        dynamic_requirements = None
        if (
            config.requirements
            and self._image_sdk.enable_image_build_for_tracked_requirements
        ):
            requirements = (
                parse_requirements_file(config.requirements)
                if isinstance(config.requirements, str)
                else config.requirements
            )
            if requirements:
                build_id = self._image_sdk.build_image_from_requirements(
                    name=f"image-for-workspace-{name}",
                    base_build_id=self.client.get_default_build_id(),
                    requirements=requirements,
                )
        elif config.requirements:
            dynamic_requirements = (
                parse_requirements_file(config.requirements)
                if isinstance(config.requirements, str)
                else config.requirements
            )

        if build_id is None:
            build_id = self.client.get_default_build_id()

        workspace_id = self.client.create_workspace(
            model=CreateExperimentalWorkspace(
                name=name,
                project_id=project_id,
                compute_config_id=compute_config_id,
                cluster_environment_build_id=build_id,
                idle_timeout_minutes=config.idle_termination_minutes,
                cloud_id=cloud_id,
                skip_start=True,
            )
        )

        self._logger.info(f"Workspace created successfully id: {workspace_id}")

        if dynamic_requirements:
            self.client.update_workspace_dependencies_offline_only(
                workspace_id=workspace_id, requirements=dynamic_requirements
            )
            self._logger.info(f"Applied dynamic requirements to workspace id: {name}")
        if config.env_vars:
            self.client.update_workspace_env_vars_offline_only(
                workspace_id=workspace_id, env_vars=config.env_vars
            )
            self._logger.info(f"Applied environment variables to workspace id: {name}")

        return workspace_id

    def start(
        self,
        *,
        id: Optional[str] = None,  # noqa: A002
        name: Optional[str] = None,
        cloud: Optional[str] = None,
        project: Optional[str] = None,
    ) -> str:
        workspace_model = self._resolve_to_workspace_model(
            id=id, name=name, cloud=cloud, project=project
        )
        self.client.start_workspace(workspace_model.id)
        self.logger.info(f"Starting workspace '{workspace_model.name}'")
        return workspace_model.id

    def terminate(
        self,
        *,
        id: Optional[str] = None,  # noqa: A002
        name: Optional[str] = None,
        cloud: Optional[str] = None,
        project: Optional[str] = None,
    ) -> str:
        workspace_model = self._resolve_to_workspace_model(
            id=id, name=name, cloud=cloud, project=project
        )
        self.client.terminate_workspace(workspace_model.id)
        self.logger.info(f"Terminating workspace '{workspace_model.name}'")
        return workspace_model.id
