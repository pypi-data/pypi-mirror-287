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
    'RepositoryIamBindingCondition',
    'RepositoryIamMemberCondition',
    'RepositoryPubsubConfig',
    'GetRepositoryPubsubConfigResult',
]

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
class RepositoryPubsubConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "messageFormat":
            suggest = "message_format"
        elif key == "serviceAccountEmail":
            suggest = "service_account_email"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RepositoryPubsubConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RepositoryPubsubConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RepositoryPubsubConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 message_format: str,
                 topic: str,
                 service_account_email: Optional[str] = None):
        """
        :param str message_format: The format of the Cloud Pub/Sub messages.
               - PROTOBUF: The message payload is a serialized protocol buffer of SourceRepoEvent.
               - JSON: The message payload is a JSON string of SourceRepoEvent.
               Possible values are: `PROTOBUF`, `JSON`.
        :param str topic: The identifier for this object. Format specified above.
        :param str service_account_email: Email address of the service account used for publishing Cloud Pub/Sub messages.
               This service account needs to be in the same project as the PubsubConfig. When added,
               the caller needs to have iam.serviceAccounts.actAs permission on this service account.
               If unspecified, it defaults to the compute engine default service account.
        """
        pulumi.set(__self__, "message_format", message_format)
        pulumi.set(__self__, "topic", topic)
        if service_account_email is not None:
            pulumi.set(__self__, "service_account_email", service_account_email)

    @property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> str:
        """
        The format of the Cloud Pub/Sub messages.
        - PROTOBUF: The message payload is a serialized protocol buffer of SourceRepoEvent.
        - JSON: The message payload is a JSON string of SourceRepoEvent.
        Possible values are: `PROTOBUF`, `JSON`.
        """
        return pulumi.get(self, "message_format")

    @property
    @pulumi.getter
    def topic(self) -> str:
        """
        The identifier for this object. Format specified above.
        """
        return pulumi.get(self, "topic")

    @property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[str]:
        """
        Email address of the service account used for publishing Cloud Pub/Sub messages.
        This service account needs to be in the same project as the PubsubConfig. When added,
        the caller needs to have iam.serviceAccounts.actAs permission on this service account.
        If unspecified, it defaults to the compute engine default service account.
        """
        return pulumi.get(self, "service_account_email")


@pulumi.output_type
class GetRepositoryPubsubConfigResult(dict):
    def __init__(__self__, *,
                 message_format: str,
                 service_account_email: str,
                 topic: str):
        """
        :param str message_format: The format of the Cloud Pub/Sub messages.
               - PROTOBUF: The message payload is a serialized protocol buffer of SourceRepoEvent.
               - JSON: The message payload is a JSON string of SourceRepoEvent. Possible values: ["PROTOBUF", "JSON"]
        :param str service_account_email: Email address of the service account used for publishing Cloud Pub/Sub messages.
               This service account needs to be in the same project as the PubsubConfig. When added,
               the caller needs to have iam.serviceAccounts.actAs permission on this service account.
               If unspecified, it defaults to the compute engine default service account.
        """
        pulumi.set(__self__, "message_format", message_format)
        pulumi.set(__self__, "service_account_email", service_account_email)
        pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> str:
        """
        The format of the Cloud Pub/Sub messages.
        - PROTOBUF: The message payload is a serialized protocol buffer of SourceRepoEvent.
        - JSON: The message payload is a JSON string of SourceRepoEvent. Possible values: ["PROTOBUF", "JSON"]
        """
        return pulumi.get(self, "message_format")

    @property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> str:
        """
        Email address of the service account used for publishing Cloud Pub/Sub messages.
        This service account needs to be in the same project as the PubsubConfig. When added,
        the caller needs to have iam.serviceAccounts.actAs permission on this service account.
        If unspecified, it defaults to the compute engine default service account.
        """
        return pulumi.get(self, "service_account_email")

    @property
    @pulumi.getter
    def topic(self) -> str:
        return pulumi.get(self, "topic")


