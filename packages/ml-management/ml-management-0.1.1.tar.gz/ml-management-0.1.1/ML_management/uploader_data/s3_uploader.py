"""Define S3Uploader class."""
import os
import posixpath
from http import HTTPStatus
from typing import List

from boto3 import client
from botocore.awsrequest import AWSRequest, AWSResponse
from tqdm.autonotebook import tqdm

from ML_management.mlmanagement import get_s3_gateway_url, variables
from ML_management.mlmanagement.session import AuthSession
from ML_management.mlmanagement.visibility_options import VisibilityOptions
from ML_management.uploader_data.utils import get_space_size, get_upload_paths


class S3Uploader:
    """S3 uploader files class."""

    def __init__(self):
        """Init creds."""
        self.default_url = get_s3_gateway_url()
        self.default_access_key_id, self.default_secret_access_key = variables._get_s3_credentials()
        self.session = AuthSession(gateway_url=self.default_url)

    def upload(
        self,
        local_path: str,
        bucket: str,
        new_bucket_visibility: VisibilityOptions = VisibilityOptions.PRIVATE,
        verbose: bool = True,
    ):
        """Upload."""
        local_path = os.path.normpath(local_path)
        if not os.path.exists(local_path):
            raise FileNotFoundError(f"Path: {local_path} does not exist")

        service_client = client(
            service_name="s3",
            use_ssl=True,
            verify=None,
            endpoint_url=posixpath.join(self.default_url, "s3/"),
            aws_access_key_id=self.default_access_key_id,
            aws_secret_access_key=self.default_secret_access_key,
        )
        event_system = service_client.meta.events
        event_system.register("before-sign.s3.*", self._add_auth_cookies)
        event_system.register("after-call.s3.*", self._update_auth_cookies)
        buckets = self._list_buckets()
        if bucket not in buckets:
            self._create_bucket(name=bucket, visibility=new_bucket_visibility)

        space_size = get_space_size(local_path)
        upload_paths = get_upload_paths(local_path)

        with tqdm(
            total=space_size,
            disable=not verbose,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for path in upload_paths:
                with open(path.local_path, "rb") as _file:
                    service_client.upload_fileobj(
                        Fileobj=_file,
                        Bucket=bucket,
                        Key=path.storage_path,
                        Callback=pbar.update,
                    )

    # arguments to callback are passed like kwargs, so kwargs must be present in signature
    def _add_auth_cookies(self, request: AWSRequest, **kwargs) -> None:  # noqa
        request.headers.add_header("Cookie", self.session._get_cookie_header())

    # arguments to callback are passed like kwargs, so kwargs must be present in signature
    def _update_auth_cookies(self, http_response: AWSResponse, **kwargs) -> None:  # noqa
        cookie_header = http_response.headers.get("set-cookie")
        if cookie_header is None:
            return
        cookies: list[str] = cookie_header.split("; ")
        for cookie in cookies:
            if "kc-access" not in cookie:
                continue
            _, new_access_token = cookie.split("=", maxsplit=1)
            self.session.cookies["kc-access"] = new_access_token
            break

    def _list_buckets(self) -> List[str]:
        with self.session.get(posixpath.join(self.default_url, "list-buckets")) as response:
            return response.json()["buckets"]

    def _create_bucket(self, name: str, visibility: VisibilityOptions) -> None:
        with self.session.post(
            posixpath.join(self.default_url, "create-bucket"), json={"name": name, "visibility": visibility.value}
        ) as response:
            if response.status_code != HTTPStatus.CREATED:
                raise RuntimeError(f"Failed to create bucket: {response.text}")
