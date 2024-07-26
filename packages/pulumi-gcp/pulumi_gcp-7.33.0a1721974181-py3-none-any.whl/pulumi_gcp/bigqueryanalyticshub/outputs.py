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
    'DataExchangeIamBindingCondition',
    'DataExchangeIamMemberCondition',
    'ListingBigqueryDataset',
    'ListingDataProvider',
    'ListingIamBindingCondition',
    'ListingIamMemberCondition',
    'ListingPublisher',
    'ListingRestrictedExportConfig',
]

@pulumi.output_type
class DataExchangeIamBindingCondition(dict):
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
class DataExchangeIamMemberCondition(dict):
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
class ListingBigqueryDataset(dict):
    def __init__(__self__, *,
                 dataset: str):
        """
        :param str dataset: Resource name of the dataset source for this listing. e.g. projects/myproject/datasets/123
               
               - - -
        """
        pulumi.set(__self__, "dataset", dataset)

    @property
    @pulumi.getter
    def dataset(self) -> str:
        """
        Resource name of the dataset source for this listing. e.g. projects/myproject/datasets/123

        - - -
        """
        return pulumi.get(self, "dataset")


@pulumi.output_type
class ListingDataProvider(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "primaryContact":
            suggest = "primary_contact"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ListingDataProvider. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ListingDataProvider.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ListingDataProvider.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 primary_contact: Optional[str] = None):
        """
        :param str name: Name of the data provider.
        :param str primary_contact: Email or URL of the data provider.
        """
        pulumi.set(__self__, "name", name)
        if primary_contact is not None:
            pulumi.set(__self__, "primary_contact", primary_contact)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the data provider.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> Optional[str]:
        """
        Email or URL of the data provider.
        """
        return pulumi.get(self, "primary_contact")


@pulumi.output_type
class ListingIamBindingCondition(dict):
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
class ListingIamMemberCondition(dict):
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
class ListingPublisher(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "primaryContact":
            suggest = "primary_contact"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ListingPublisher. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ListingPublisher.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ListingPublisher.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 primary_contact: Optional[str] = None):
        """
        :param str name: Name of the listing publisher.
        :param str primary_contact: Email or URL of the listing publisher.
        """
        pulumi.set(__self__, "name", name)
        if primary_contact is not None:
            pulumi.set(__self__, "primary_contact", primary_contact)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the listing publisher.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> Optional[str]:
        """
        Email or URL of the listing publisher.
        """
        return pulumi.get(self, "primary_contact")


@pulumi.output_type
class ListingRestrictedExportConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "restrictQueryResult":
            suggest = "restrict_query_result"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ListingRestrictedExportConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ListingRestrictedExportConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ListingRestrictedExportConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: Optional[bool] = None,
                 restrict_query_result: Optional[bool] = None):
        """
        :param bool enabled: If true, enable restricted export.
        :param bool restrict_query_result: If true, restrict export of query result derived from restricted linked dataset table.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if restrict_query_result is not None:
            pulumi.set(__self__, "restrict_query_result", restrict_query_result)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        If true, enable restricted export.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="restrictQueryResult")
    def restrict_query_result(self) -> Optional[bool]:
        """
        If true, restrict export of query result derived from restricted linked dataset table.
        """
        return pulumi.get(self, "restrict_query_result")


