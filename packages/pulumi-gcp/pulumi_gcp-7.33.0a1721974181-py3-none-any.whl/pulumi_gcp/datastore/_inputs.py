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
    'DataStoreIndexPropertyArgs',
    'DataStoreIndexPropertyArgsDict',
]

MYPY = False

if not MYPY:
    class DataStoreIndexPropertyArgsDict(TypedDict):
        direction: pulumi.Input[str]
        """
        The direction the index should optimize for sorting.
        Possible values are: `ASCENDING`, `DESCENDING`.
        """
        name: pulumi.Input[str]
        """
        The property name to index.
        """
elif False:
    DataStoreIndexPropertyArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DataStoreIndexPropertyArgs:
    def __init__(__self__, *,
                 direction: pulumi.Input[str],
                 name: pulumi.Input[str]):
        """
        :param pulumi.Input[str] direction: The direction the index should optimize for sorting.
               Possible values are: `ASCENDING`, `DESCENDING`.
        :param pulumi.Input[str] name: The property name to index.
        """
        pulumi.set(__self__, "direction", direction)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Input[str]:
        """
        The direction the index should optimize for sorting.
        Possible values are: `ASCENDING`, `DESCENDING`.
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: pulumi.Input[str]):
        pulumi.set(self, "direction", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The property name to index.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


