import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import List

from tqdm import tqdm

import instalabel.client
from instalabel.client.models.image_response import ImageResponse
from instalabel.client.models.project_response import ProjectResponse
from instalabel.client.models.project_update_request import ProjectUpdateRequest
from instalabel.client.models.task_enum import TaskEnum
from instalabel.client.rest import ApiException
from instalabel.config import API_URL

configuration = instalabel.client.Configuration(host=API_URL)


class Image:
    def __init__(self, image: ImageResponse):
        self.id = image.image_id
        self.project_id = image.project_id
        self.user_id = image.user_id
        self.filename = image.filename
        self.status = image.status
        self.annotations_count = image.annotations_count
        self.annotations = image.annotations
        self.created_at = image.created_at
        self.updated_at = image.updated_at
        self.presigned_url = image.presigned_url

    def get_image(self):
        # Enter a context with an instance of the API client
        with instalabel.client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = instalabel.client.ImagesApi(api_client)
            image_id = self.id
            project_id = self.project_id

            try:
                # Get Image
                api_response = api_instance.get_image_api_v1_images_image_id_get(
                    image_id, project_id
                )

                # Update the image object with the response
                self.user_id = api_response.user_id
                self.filename = api_response.filename
                self.status = api_response.status
                self.annotations_count = api_response.annotations_count
                self.annotations = api_response.annotations
                self.created_at = api_response.created_at
                self.updated_at = api_response.updated_at
                self.presigned_url = api_response.presigned_url

            except Exception as e:
                print(
                    "Exception when calling ImagesApi->get_image_api_v1_images_image_id_get: %s\n"
                    % e
                )

    def __str__(self):
        return f"Image: {self.filename} | Status: {self.status}"


class Project:
    def __init__(self, project: ProjectResponse):
        self.id = project.project_id
        self.name = project.project_name
        self.description = project.project_description
        self.task = project.task
        self.created_at = project.created_at
        self.updated_at = project.updated_at
        self.image_count = project.image_count
        self.ontology = project.ontology

    def upload_single_image(self, file_path: str):
        supported_extensions = (".jpg", ".jpeg", ".png")

        # Check if the file format is supported
        if not file_path.lower().endswith(supported_extensions):
            print(f"Unsupported file format for {file_path}. Skipping upload.")
            return

        with instalabel.client.ApiClient(configuration) as api_client:
            api_instance = instalabel.client.ImagesApi(api_client)
            project_id = self.id

            try:
                api_response = api_instance.upload_image_api_v1_images_post(
                    project_id=project_id, file=file_path
                )
                return Image(api_response)

            except Exception as e:
                print(
                    "Exception when calling ImagesApi->upload_image_api_v1_images_post: %s\n"
                    % e
                )

    def upload_images(self, image_paths: List[str]):
        def upload(image_path: str):
            self.upload_single_image(image_path)

        # Using ThreadPoolExecutor for multithreading
        with ThreadPoolExecutor() as executor:
            list(
                tqdm(
                    executor.map(upload, image_paths),
                    total=len(image_paths),
                    desc="Uploading images",
                )
            )

    def upload_directory(self, dataset_path: str):
        # Get all image files from the dataset directory
        supported_extensions = (".jpg", ".jpeg", ".png")
        image_paths = [
            str(file_path)
            for file_path in Path(dataset_path).rglob("*")
            if file_path.suffix.lower() in supported_extensions
        ]
        # Upload all images found in the dataset
        self.upload_images(image_paths)

    def get_project(self):
        # Enter a context with an instance of the API client
        with instalabel.client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = instalabel.client.ProjectsApi(api_client)
            project_id = self.id  # str |

            try:
                # Read Project
                api_response = api_instance.read_project_api_v1_projects_project_id_get(
                    project_id
                )

                # Update the project object with the response
                self.name = api_response.project_name
                self.description = api_response.project_description
                self.task = api_response.task
                self.created_at = api_response.created_at
                self.updated_at = api_response.updated_at
                self.image_count = api_response.image_count
                self.ontology = api_response.ontology

                return Project(api_response)

            except Exception as e:
                print(
                    "Exception when calling ProjectsApi->read_project_api_v1_projects_project_id_get: %s\n"
                    % e
                )

    def update_project(self, project_name: str = None, project_description: str = None):

        if project_name is None and project_description is None:
            print("Please provide either project_name or project_description")
            return

        with instalabel.client.ApiClient(configuration) as api_client:
            api_instance = instalabel.client.ProjectsApi(api_client)
            project_id = self.id
            project_update_request = ProjectUpdateRequest(
                project_name=project_name, project_description=project_description
            )

            try:
                api_response = (
                    api_instance.update_project_api_v1_projects_project_id_patch(
                        project_id, project_update_request
                    )
                )

                # Update the project object with the response
                self.name = api_response.project_name
                self.description = api_response.project_description
                self.task = api_response.task
                self.created_at = api_response.created_at
                self.updated_at = api_response.updated_at
                self.image_count = api_response.image_count
                self.ontology = api_response.ontology

            except Exception as e:
                print(
                    "Exception when calling ProjectsApi->update_project_api_v1_projects_project_id_patch: %s\n"
                    % e
                )

    def get_images(self):
        # Enter a context with an instance of the API client
        with instalabel.client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = instalabel.client.ImagesApi(api_client)
            project_id = self.id  # str |

            try:
                # Get Project Images
                api_response = api_instance.get_project_images_api_v1_images_get(
                    project_id
                )
                return [Image(image) for image in api_response]
            except Exception as e:
                print(
                    "Exception when calling ImagesApi->get_project_images_api_v1_images_get: %s\n"
                    % e
                )

    def __str__(self):
        return f"Project: {self.name} | Task: {self.task.value}"


class InstaLabel:
    def __init__(self):
        return

    def login(self, username: str, password: str):
        with instalabel.client.ApiClient(configuration) as api_client:
            api_instance = instalabel.client.AuthApi(api_client)
            try:
                api_response = (
                    api_instance.login_for_access_token_api_v1_auth_token_post(
                        username, password
                    )
                )
                configuration.access_token = api_response.access_token
                os.environ["ACCESS_TOKEN"] = api_response.access_token

                self.get_projects()

            except ApiException as e:
                print(
                    "Exception when calling AuthApi->login_for_access_token_api_v1_auth_token_post: %s\n"
                    % e
                )

    def get_projects(self):
        with instalabel.client.ApiClient(configuration) as api_client:
            api_instance = instalabel.client.ProjectsApi(api_client)
            try:
                api_response = api_instance.read_projects_api_v1_projects_get()

                projects = [Project(project) for project in api_response]

                return projects
            except Exception as e:
                print(
                    "Exception when calling ProjectsApi->read_projects_api_v1_projects_get: %s\n"
                    % e
                )

    def create_project(
        self, project_name: str, task: TaskEnum, project_description: str
    ):

        with instalabel.client.ApiClient(configuration) as api_client:
            api_instance = instalabel.client.ProjectsApi(api_client)

            # project_ = instalabel.client.Project
            project_create = instalabel.client.ProjectCreate(
                project_name=project_name,
                task=task,
                project_description=project_description,
            )

            try:
                # Create Project
                api_response = api_instance.create_project_api_v1_projects_post(
                    project_create
                )

                return Project(api_response)

            except Exception as e:
                print(
                    "Exception when calling ProjectsApi->create_project_api_v1_projects_post: %s\n"
                    % e
                )

    def __str__(self):
        return f"InstaLabel: {self.name}"
