# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

__all__ = [
    'InstanceHostConfig',
    'InstanceIamBindingCondition',
    'InstanceIamMemberCondition',
    'InstancePrivateConfig',
    'RepositoryIamBindingCondition',
    'RepositoryIamMemberCondition',
    'RepositoryInitialConfig',
    'RepositoryUri',
]

@pulumi.output_type
class InstanceHostConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "gitHttp":
            suggest = "git_http"
        elif key == "gitSsh":
            suggest = "git_ssh"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InstanceHostConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InstanceHostConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InstanceHostConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 api: Optional[str] = None,
                 git_http: Optional[str] = None,
                 git_ssh: Optional[str] = None,
                 html: Optional[str] = None):
        """
        :param str api: (Output)
               API hostname.
        :param str git_http: (Output)
               Git HTTP hostname.
        :param str git_ssh: (Output)
               Git SSH hostname.
        :param str html: (Output)
               HTML hostname.
        """
        if api is not None:
            pulumi.set(__self__, "api", api)
        if git_http is not None:
            pulumi.set(__self__, "git_http", git_http)
        if git_ssh is not None:
            pulumi.set(__self__, "git_ssh", git_ssh)
        if html is not None:
            pulumi.set(__self__, "html", html)

    @property
    @pulumi.getter
    def api(self) -> Optional[str]:
        """
        (Output)
        API hostname.
        """
        return pulumi.get(self, "api")

    @property
    @pulumi.getter(name="gitHttp")
    def git_http(self) -> Optional[str]:
        """
        (Output)
        Git HTTP hostname.
        """
        return pulumi.get(self, "git_http")

    @property
    @pulumi.getter(name="gitSsh")
    def git_ssh(self) -> Optional[str]:
        """
        (Output)
        Git SSH hostname.
        """
        return pulumi.get(self, "git_ssh")

    @property
    @pulumi.getter
    def html(self) -> Optional[str]:
        """
        (Output)
        HTML hostname.
        """
        return pulumi.get(self, "html")


@pulumi.output_type
class InstanceIamBindingCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


@pulumi.output_type
class InstanceIamMemberCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


@pulumi.output_type
class InstancePrivateConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "caPool":
            suggest = "ca_pool"
        elif key == "isPrivate":
            suggest = "is_private"
        elif key == "httpServiceAttachment":
            suggest = "http_service_attachment"
        elif key == "sshServiceAttachment":
            suggest = "ssh_service_attachment"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InstancePrivateConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InstancePrivateConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InstancePrivateConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 ca_pool: str,
                 is_private: bool,
                 http_service_attachment: Optional[str] = None,
                 ssh_service_attachment: Optional[str] = None):
        """
        :param str ca_pool: CA pool resource, resource must in the format of `projects/{project}/locations/{location}/caPools/{ca_pool}`.
        :param bool is_private: 'Indicate if it's private instance.'
        :param str http_service_attachment: (Output)
               Service Attachment for HTTP, resource is in the format of `projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`.
        :param str ssh_service_attachment: (Output)
               Service Attachment for SSH, resource is in the format of `projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`.
        """
        pulumi.set(__self__, "ca_pool", ca_pool)
        pulumi.set(__self__, "is_private", is_private)
        if http_service_attachment is not None:
            pulumi.set(__self__, "http_service_attachment", http_service_attachment)
        if ssh_service_attachment is not None:
            pulumi.set(__self__, "ssh_service_attachment", ssh_service_attachment)

    @property
    @pulumi.getter(name="caPool")
    def ca_pool(self) -> str:
        """
        CA pool resource, resource must in the format of `projects/{project}/locations/{location}/caPools/{ca_pool}`.
        """
        return pulumi.get(self, "ca_pool")

    @property
    @pulumi.getter(name="isPrivate")
    def is_private(self) -> bool:
        """
        'Indicate if it's private instance.'
        """
        return pulumi.get(self, "is_private")

    @property
    @pulumi.getter(name="httpServiceAttachment")
    def http_service_attachment(self) -> Optional[str]:
        """
        (Output)
        Service Attachment for HTTP, resource is in the format of `projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`.
        """
        return pulumi.get(self, "http_service_attachment")

    @property
    @pulumi.getter(name="sshServiceAttachment")
    def ssh_service_attachment(self) -> Optional[str]:
        """
        (Output)
        Service Attachment for SSH, resource is in the format of `projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`.
        """
        return pulumi.get(self, "ssh_service_attachment")


@pulumi.output_type
class RepositoryIamBindingCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


@pulumi.output_type
class RepositoryIamMemberCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


@pulumi.output_type
class RepositoryInitialConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "defaultBranch":
            suggest = "default_branch"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RepositoryInitialConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RepositoryInitialConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RepositoryInitialConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 default_branch: Optional[str] = None,
                 gitignores: Optional[Sequence[str]] = None,
                 license: Optional[str] = None,
                 readme: Optional[str] = None):
        """
        :param str default_branch: Default branch name of the repository.
        :param Sequence[str] gitignores: List of gitignore template names user can choose from.
               Valid values can be viewed at https://cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.repositories#initialconfig.
        :param str license: License template name user can choose from.
               Valid values can be viewed at https://cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.repositories#initialconfig.
        :param str readme: README template name.
               Valid values can be viewed at https://cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.repositories#initialconfig.
        """
        if default_branch is not None:
            pulumi.set(__self__, "default_branch", default_branch)
        if gitignores is not None:
            pulumi.set(__self__, "gitignores", gitignores)
        if license is not None:
            pulumi.set(__self__, "license", license)
        if readme is not None:
            pulumi.set(__self__, "readme", readme)

    @property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[str]:
        """
        Default branch name of the repository.
        """
        return pulumi.get(self, "default_branch")

    @property
    @pulumi.getter
    def gitignores(self) -> Optional[Sequence[str]]:
        """
        List of gitignore template names user can choose from.
        Valid values can be viewed at https://cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.repositories#initialconfig.
        """
        return pulumi.get(self, "gitignores")

    @property
    @pulumi.getter
    def license(self) -> Optional[str]:
        """
        License template name user can choose from.
        Valid values can be viewed at https://cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.repositories#initialconfig.
        """
        return pulumi.get(self, "license")

    @property
    @pulumi.getter
    def readme(self) -> Optional[str]:
        """
        README template name.
        Valid values can be viewed at https://cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.repositories#initialconfig.
        """
        return pulumi.get(self, "readme")


@pulumi.output_type
class RepositoryUri(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "gitHttps":
            suggest = "git_https"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RepositoryUri. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RepositoryUri.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RepositoryUri.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 api: Optional[str] = None,
                 git_https: Optional[str] = None,
                 html: Optional[str] = None):
        """
        :param str api: (Output)
               API is the URI for API access.
        :param str git_https: (Output)
               git_https is the git HTTPS URI for git operations.
        :param str html: (Output)
               HTML is the URI for the user to view the repository in a browser.
        """
        if api is not None:
            pulumi.set(__self__, "api", api)
        if git_https is not None:
            pulumi.set(__self__, "git_https", git_https)
        if html is not None:
            pulumi.set(__self__, "html", html)

    @property
    @pulumi.getter
    def api(self) -> Optional[str]:
        """
        (Output)
        API is the URI for API access.
        """
        return pulumi.get(self, "api")

    @property
    @pulumi.getter(name="gitHttps")
    def git_https(self) -> Optional[str]:
        """
        (Output)
        git_https is the git HTTPS URI for git operations.
        """
        return pulumi.get(self, "git_https")

    @property
    @pulumi.getter
    def html(self) -> Optional[str]:
        """
        (Output)
        HTML is the URI for the user to view the repository in a browser.
        """
        return pulumi.get(self, "html")


