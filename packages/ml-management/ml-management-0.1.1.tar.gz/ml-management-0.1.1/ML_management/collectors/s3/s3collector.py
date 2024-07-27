"""S3 Collector for downloading files and folders."""
import os
import posixpath
from typing import List, Optional, Union

from boto3 import client
from botocore.awsrequest import AWSRequest, AWSResponse
from botocore.exceptions import ClientError
from tqdm.autonotebook import tqdm

from ML_management.collectors.collector_pattern import CollectorPattern
from ML_management.mlmanagement import get_s3_gateway_url, variables
from ML_management.mlmanagement.session import AuthSession


class S3FolderNotFoundError(Exception):
    """Define Version Not Found Exception."""

    def __init__(self, path: str, bucket: str):
        self.path = path
        self.bucket = bucket
        self.message = f'Folder "{path}" is not found in "{bucket}" bucket'
        super().__init__(self.message)

    def __reduce__(self):
        """Define reduce method to make exception picklable."""
        return (S3FolderNotFoundError, (self.path, self.bucket))


class S3BucketNotFoundError(Exception):
    """Define Bucket Not Found Exception."""

    def __init__(self, bucket: str):
        self.bucket = bucket
        self.message = f'Bucket "{bucket}" does not exist'
        super().__init__(self.message)

    def __reduce__(self):
        """Define reduce method to make exception picklable."""
        return (S3FolderNotFoundError, (self.bucket))


class S3ObjectNotFoundError(Exception):
    """Define Version Not Found Exception."""

    def __init__(self, path: str, bucket: str):
        self.path = path
        self.bucket = bucket
        self.message = f'Object "{path}" is not found in "{bucket}" bucket'
        super().__init__(self.message)

    def __reduce__(self):
        """Define reduce method to make exception picklable."""
        return (S3ObjectNotFoundError, (self.path, self.bucket))


class S3Collector(CollectorPattern):
    """Collector for S3 paths using boto3 library."""

    def __init__(self) -> None:
        """Init creds."""
        self.default_url = get_s3_gateway_url()
        self.default_access_key_id, self.default_secret_access_key = variables._get_s3_credentials()
        self.session = AuthSession(gateway_url=self.default_url)

    @staticmethod
    def get_json_schema():
        """Return json schema."""
        return {
            "type": "object",
            "properties": {
                "bucket": {"type": "string"},
                "remote_paths": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["bucket"],
            "additionalProperties": False,
        }

    def set_data(
        self,
        *,
        local_path: str = "s3_data",
        bucket: str,  # TODO do we pass bucket or not? is it always possible to parse?
        remote_paths: Optional[List[str]] = None,
        service_name: str = "s3",
        region_name: Optional[str] = None,
        api_version: Optional[str] = None,
        use_ssl: bool = True,
        verify: Optional[Union[bool, str]] = None,
        endpoint_url: Optional[str] = None,
        aws_access_key_id: Optional[str] = None,
        aws_secret_access_key: Optional[str] = None,
        aws_session_token: Optional[str] = None,
        verbose: bool = True,
    ) -> str:
        """
        Set data.

        :type local_path: string
        :param local_path: Local path to save data to.  Defaults to /s3_data/.

        :type bucket: string
        :param bucket: Bucket containing requested files.

        :type remote_paths: list(string)
        :param remote_paths: List of paths relative to passed bucket.  Each path
            can represent either a single file, or a folder.  If a path represents
            a folder (should end with a slash), then all contents of a folder are recursively downloaded.

        :type service_name: string
        :param service_name: The name of a service, e.g. 's3' or 'ec2'
        available to boto3.  Defaults to 's3'.

        :type region_name: string
        :param region_name: The name of the region associated with the client.
            A client is associated with a single region.

        :type api_version: string
        :param api_version: The API version to use.  By default, botocore will
            use the latest API version when creating a client.  You only need
            to specify this parameter if you want to use a previous API version
            of the client.

        :type use_ssl: boolean
        :param use_ssl: Whether to use SSL.  By default, SSL is used.
            Note that not all services support non-ssl connections.

        :type verify: boolean/string
        :param verify: Whether to verify SSL certificates.  By default,
            SSL certificates are verified.  You can provide the following
            values:

            * False - do not validate SSL certificates.  SSL will still be
              used (unless use_ssl is False), but SSL certificates
              will not be verified.
            * path/to/cert/bundle.pem - A filename of the CA cert bundle to
              uses.  You can specify this argument if you want to use a
              different CA cert bundle than the one used by botocore.

        :type endpoint_url: string
        :param endpoint_url: The complete URL to use for the constructed
            client. Normally, botocore will automatically construct the
            appropriate URL to use when communicating with a service.  You
            can specify a complete URL (including the "http/https" scheme)
            to override this behavior.  If this value is provided,
            then ``use_ssl`` is ignored.

        :type aws_access_key_id: string
        :param aws_access_key_id: The access key to use when creating
            the client.  This is entirely optional, and if not provided,
            the credentials configured for the session will automatically
            be used.  You only need to provide this argument if you want
            to override the credentials used for this specific client.

        :type aws_secret_access_key: string
        :param aws_secret_access_key: The secret key to use when creating
            the client.  Same semantics as aws_access_key_id above.

        :type aws_session_token: string
        :param aws_session_token: The session token to use when creating
            the client.  Same semantics as aws_access_key_id above.

        :type verbose: bool
        :param verbose: Whether to disable the entire progressbar wrapper.
        """
        service_client = client(
            service_name=service_name,
            region_name=region_name,
            api_version=api_version,
            use_ssl=use_ssl,
            verify=verify,
            endpoint_url=endpoint_url if endpoint_url else posixpath.join(self.default_url, "s3/"),
            aws_access_key_id=aws_access_key_id if aws_access_key_id else self.default_access_key_id,
            aws_secret_access_key=aws_secret_access_key if aws_secret_access_key else self.default_secret_access_key,
            aws_session_token=aws_session_token,
        )
        event_system = service_client.meta.events
        event_system.register("before-sign.s3.*", self._add_auth_cookies)
        event_system.register("after-call.s3.*", self._update_auth_cookies)

        def compute_space(paginator, remote_path: str = ""):
            space_size = 0

            page_iterator = paginator.paginate(
                Bucket=bucket,
                Prefix=remote_path,
            )
            for page in page_iterator:
                if page["KeyCount"] == 0:
                    raise S3ObjectNotFoundError(path=remote_path, bucket=bucket)
                for obj in page.get("Contents", []):
                    space_size += obj["Size"]

            return space_size

        remote_paths = remote_paths if remote_paths else [""]
        data_size = 0

        try:
            paginator = service_client.get_paginator("list_objects_v2")
            for remote_path in remote_paths:
                data_size += compute_space(paginator, remote_path)
        except ClientError as err:
            if err.response["Error"]["Code"] == "NoSuchBucket":
                raise S3BucketNotFoundError(bucket=bucket) from None
            else:
                raise

        with tqdm(
            total=data_size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            disable=not verbose,
        ) as pbar:
            for remote_path in remote_paths:
                page_iterator = paginator.paginate(
                    Bucket=bucket,
                    Prefix=remote_path,
                )
                for page in page_iterator:
                    for obj in page.get("Contents", []):
                        file_path = obj.get("Key")

                        local_dir_path = os.path.join(local_path, posixpath.dirname(file_path))
                        local_file_path = os.path.join(local_path, file_path)
                        if not os.path.exists(local_dir_path):
                            os.makedirs(local_dir_path, exist_ok=True)

                        with open(local_file_path, "wb") as _file:
                            service_client.download_fileobj(
                                Bucket=bucket,
                                Key=file_path,
                                Fileobj=_file,
                                Callback=pbar.update,
                            )

        return local_path

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
