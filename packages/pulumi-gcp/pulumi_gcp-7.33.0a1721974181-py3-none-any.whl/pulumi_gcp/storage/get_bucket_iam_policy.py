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
    'GetBucketIamPolicyResult',
    'AwaitableGetBucketIamPolicyResult',
    'get_bucket_iam_policy',
    'get_bucket_iam_policy_output',
]

@pulumi.output_type
class GetBucketIamPolicyResult:
    """
    A collection of values returned by getBucketIamPolicy.
    """
    def __init__(__self__, bucket=None, etag=None, id=None, policy_data=None):
        if bucket and not isinstance(bucket, str):
            raise TypeError("Expected argument 'bucket' to be a str")
        pulumi.set(__self__, "bucket", bucket)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policy_data and not isinstance(policy_data, str):
            raise TypeError("Expected argument 'policy_data' to be a str")
        pulumi.set(__self__, "policy_data", policy_data)

    @property
    @pulumi.getter
    def bucket(self) -> str:
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        (Computed) The etag of the IAM policy.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> str:
        """
        (Required only by `storage.BucketIAMPolicy`) The policy data generated by
        a `organizations_get_iam_policy` data source.
        """
        return pulumi.get(self, "policy_data")


class AwaitableGetBucketIamPolicyResult(GetBucketIamPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBucketIamPolicyResult(
            bucket=self.bucket,
            etag=self.etag,
            id=self.id,
            policy_data=self.policy_data)


def get_bucket_iam_policy(bucket: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBucketIamPolicyResult:
    """
    Retrieves the current IAM policy data for bucket

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.storage.get_bucket_iam_policy(bucket=default["name"])
    ```


    :param str bucket: Used to find the parent resource to bind the IAM policy to
    """
    __args__ = dict()
    __args__['bucket'] = bucket
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:storage/getBucketIamPolicy:getBucketIamPolicy', __args__, opts=opts, typ=GetBucketIamPolicyResult).value

    return AwaitableGetBucketIamPolicyResult(
        bucket=pulumi.get(__ret__, 'bucket'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        policy_data=pulumi.get(__ret__, 'policy_data'))


@_utilities.lift_output_func(get_bucket_iam_policy)
def get_bucket_iam_policy_output(bucket: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBucketIamPolicyResult]:
    """
    Retrieves the current IAM policy data for bucket

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.storage.get_bucket_iam_policy(bucket=default["name"])
    ```


    :param str bucket: Used to find the parent resource to bind the IAM policy to
    """
    ...
