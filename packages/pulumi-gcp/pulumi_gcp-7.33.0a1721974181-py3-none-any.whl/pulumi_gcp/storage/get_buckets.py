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
from . import outputs

__all__ = [
    'GetBucketsResult',
    'AwaitableGetBucketsResult',
    'get_buckets',
    'get_buckets_output',
]

@pulumi.output_type
class GetBucketsResult:
    """
    A collection of values returned by getBuckets.
    """
    def __init__(__self__, buckets=None, id=None, prefix=None, project=None):
        if buckets and not isinstance(buckets, list):
            raise TypeError("Expected argument 'buckets' to be a list")
        pulumi.set(__self__, "buckets", buckets)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if prefix and not isinstance(prefix, str):
            raise TypeError("Expected argument 'prefix' to be a str")
        pulumi.set(__self__, "prefix", prefix)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def buckets(self) -> Sequence['outputs.GetBucketsBucketResult']:
        """
        A list of all retrieved GCS buckets. Structure is defined below.
        """
        return pulumi.get(self, "buckets")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")


class AwaitableGetBucketsResult(GetBucketsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBucketsResult(
            buckets=self.buckets,
            id=self.id,
            prefix=self.prefix,
            project=self.project)


def get_buckets(prefix: Optional[str] = None,
                project: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBucketsResult:
    """
    Gets a list of existing GCS buckets.
    See [the official documentation](https://cloud.google.com/storage/docs/introduction)
    and [API](https://cloud.google.com/storage/docs/json_api/v1/buckets/list).

    ## Example Usage

    Example GCS buckets.

    ```python
    import pulumi
    import pulumi_gcp as gcp

    example = gcp.storage.get_buckets(project="example-project")
    ```


    :param str prefix: Filter results to buckets whose names begin with this prefix.
    :param str project: The ID of the project. If it is not provided, the provider project is used.
    """
    __args__ = dict()
    __args__['prefix'] = prefix
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:storage/getBuckets:getBuckets', __args__, opts=opts, typ=GetBucketsResult).value

    return AwaitableGetBucketsResult(
        buckets=pulumi.get(__ret__, 'buckets'),
        id=pulumi.get(__ret__, 'id'),
        prefix=pulumi.get(__ret__, 'prefix'),
        project=pulumi.get(__ret__, 'project'))


@_utilities.lift_output_func(get_buckets)
def get_buckets_output(prefix: Optional[pulumi.Input[Optional[str]]] = None,
                       project: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBucketsResult]:
    """
    Gets a list of existing GCS buckets.
    See [the official documentation](https://cloud.google.com/storage/docs/introduction)
    and [API](https://cloud.google.com/storage/docs/json_api/v1/buckets/list).

    ## Example Usage

    Example GCS buckets.

    ```python
    import pulumi
    import pulumi_gcp as gcp

    example = gcp.storage.get_buckets(project="example-project")
    ```


    :param str prefix: Filter results to buckets whose names begin with this prefix.
    :param str project: The ID of the project. If it is not provided, the provider project is used.
    """
    ...
