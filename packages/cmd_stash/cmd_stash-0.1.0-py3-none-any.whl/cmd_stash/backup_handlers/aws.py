import logging
from typing import Optional

import boto3
from botocore.exceptions import ClientError

from cmd_stash.backup_handlers.exceptions import (
    AWSBucketCreationException,
    AWSBucketDeletionException,
)
from cmd_stash.backup_service import BackupService
from cmd_stash.config import AWSConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class AWSManager(BackupService):
    def __init__(self, config: AWSConfig, object_name: str):
        """Initialize the AWSManager service with AWSConfig and object name."""
        self.config = config
        self.object_name = object_name
        self.client = boto3.client("s3", region_name=self.config.region)

        logger.info(
            f"Initialized AWSManager for region: {self.config.region}, bucket: {self.config.bucket_name}"
        )

    def _delete_objects(self, bucket_name, objects):
        """Delete a batch of objects from the specified bucket."""
        if objects:
            try:
                response = self.client.delete_objects(
                    Bucket=bucket_name, Delete={"Objects": objects}
                )
                logger.info(f"Deleted objects from bucket {bucket_name}: {response}")
                return response
            except ClientError as e:
                logger.error(f"Error deleting objects from bucket {bucket_name}: {e}")
                raise

    def _empty_bucket(self, bucket_name):
        """Empty all objects from the specified S3 bucket."""
        try:
            logger.info(f"Starting to empty bucket: {bucket_name}")
            paginator = self.client.get_paginator("list_object_versions")
            delete_objects = []
            delete_markers = []

            for page in paginator.paginate(Bucket=bucket_name):
                versions = page.get("Versions", [])
                delete_markers_list = page.get("DeleteMarkers", [])

                for version in versions:
                    delete_objects.append(
                        {"Key": version["Key"], "VersionId": version["VersionId"]}
                    )

                for marker in delete_markers_list:
                    delete_markers.append(
                        {"Key": marker["Key"], "VersionId": marker["VersionId"]}
                    )

                if delete_objects:
                    self._delete_objects(bucket_name, delete_objects)
                    delete_objects = []

                if delete_markers:
                    self._delete_objects(bucket_name, delete_markers)
                    delete_markers = []

            response = self.client.list_objects_v2(Bucket=bucket_name)
            if (
                "Contents" in response
                or "Versions" in response
                or "DeleteMarkers" in response
            ):
                logger.warning("Bucket still contains objects after deletion attempts.")
            else:
                logger.info("Bucket is empty after deletion.")

        except ClientError as e:
            logger.error(f"Error emptying bucket {bucket_name}: {e}")
            raise

    def destroy_backup(self, resource_name: str) -> str:
        """Destroy a backup by deleting an S3 bucket after removing all its contents."""
        try:
            logger.info(f"Starting backup destruction for resource: {resource_name}")
            self._empty_bucket(resource_name)
            self.client.delete_bucket(Bucket=resource_name)
            logger.info(f"Bucket {resource_name} deleted successfully.")
            return "Backup destroyed successfully."
        except ClientError as e:
            logger.error(f"AWS client error during backup destruction: {e}")
            raise AWSBucketDeletionException(f"AWS client error occurred: {e}")
        except Exception as e:
            logger.error(f"Unexpected error during backup destruction: {e}")
            raise AWSBucketDeletionException(
                f"Unexpected error during backup destruction: {e}"
            )

    def create_backup(self, resource_name: str) -> str:
        """Create a backup by creating a bucket."""
        return self.create_bucket(resource_name)

    def backup_exists(self, resource_name: str) -> bool:
        """Check if the backup bucket exists."""
        return self.bucket_exists(resource_name)

    def backup(self, file_path: str, resource_name: str, key: str) -> str:
        """Upload a file to the specified bucket (backup)."""
        try:
            self.upload_file(file_path, resource_name, key)
            logger.info(f"File {file_path} uploaded to {resource_name}/{key}.")
            return f"File {file_path} uploaded to {resource_name}/{key}."
        except ClientError as e:
            logger.error(
                f"Error uploading file {file_path} to {resource_name}/{key}: {e}"
            )
            return f"Error uploading file: {e}"

    def restore(self, resource_name: str, key: str, local_path: str) -> str:
        """Download a file from the specified bucket (backup)."""
        try:
            self.download_file(resource_name, key, local_path)
            logger.info(f"File {key} downloaded from {resource_name} to {local_path}.")
            return f"File {key} downloaded from {resource_name} to {local_path}."
        except ClientError as e:
            logger.error(f"Error downloading file {key} from {resource_name}: {e}")
            return f"Error downloading file: {e}"

    def create_bucket(self, bucket_name: str, acl: Optional[str] = None) -> str:
        """Create an S3 bucket."""
        acl = acl or self.config.bucket_acl
        try:
            if self.bucket_exists(bucket_name):
                logger.info(f"Bucket {bucket_name} already exists.")
                return f"Bucket {bucket_name} already exists."

            create_bucket_config = {}
            if self.config.region != "us-east-1":
                create_bucket_config = {
                    "CreateBucketConfiguration": {
                        "LocationConstraint": self.config.region
                    }
                }

            self.client.create_bucket(
                Bucket=bucket_name, ACL=acl, **create_bucket_config
            )
            logger.info(f"Bucket {bucket_name} created successfully.")
            return f"Bucket {bucket_name} created."
        except ClientError as e:
            logger.error(f"Error creating bucket {bucket_name}: {e}")
            raise AWSBucketCreationException(f"Error creating bucket: {e}")
        except Exception as e:
            logger.error(f"Unexpected error creating bucket {bucket_name}: {e}")
            raise AWSBucketCreationException(f"Unexpected error creating bucket: {e}")

    def delete_bucket(self, bucket_name: str) -> str:
        """Delete an S3 bucket."""
        try:
            if not self.bucket_exists(bucket_name):
                logger.info(f"Bucket {bucket_name} does not exist.")
                return f"Bucket {bucket_name} does not exist."
            self.client.delete_bucket(Bucket=bucket_name)
            logger.info(f"Bucket {bucket_name} deleted successfully.")
            return f"Bucket {bucket_name} deleted."
        except ClientError as e:
            logger.error(f"Error deleting bucket {bucket_name}: {e}")
            raise AWSBucketDeletionException(f"Error deleting bucket: {e}")
        except Exception as e:
            logger.error(f"Unexpected error deleting bucket {bucket_name}: {e}")
            raise AWSBucketDeletionException(f"Unexpected error deleting bucket: {e}")

    def bucket_exists(self, bucket_name: str) -> bool:
        """Check if an S3 bucket exists."""
        try:
            self.client.head_bucket(Bucket=bucket_name)
            logger.info(f"Bucket {bucket_name} exists.")
            return True
        except ClientError:
            logger.info(f"Bucket {bucket_name} does not exist.")
            return False

    def upload_file(self, file_path: str, bucket_name: str, s3_key: str) -> str:
        """Upload a file to an S3 bucket."""
        try:
            self.client.upload_file(file_path, bucket_name, s3_key)
            logger.info(f"File {file_path} uploaded to {bucket_name}/{s3_key}.")
            return f"File {file_path} uploaded to {bucket_name}/{s3_key}."
        except ClientError as e:
            logger.error(
                f"Error uploading file {file_path} to {bucket_name}/{s3_key}: {e}"
            )
            return f"Error uploading file: {e}"

    def download_file(self, bucket_name: str, s3_key: str, local_path: str) -> str:
        """Download a file from an S3 bucket."""
        try:
            self.client.download_file(bucket_name, s3_key, local_path)
            logger.info(f"File {s3_key} downloaded from {bucket_name} to {local_path}.")
            return f"File {s3_key} downloaded from {bucket_name} to {local_path}."
        except ClientError as e:
            logger.error(f"Error downloading file {s3_key} from {bucket_name}: {e}")
            return f"Error downloading file: {e}"
