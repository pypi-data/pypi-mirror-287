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
    'GetWebBackendServiceIamPolicyResult',
    'AwaitableGetWebBackendServiceIamPolicyResult',
    'get_web_backend_service_iam_policy',
    'get_web_backend_service_iam_policy_output',
]

@pulumi.output_type
class GetWebBackendServiceIamPolicyResult:
    """
    A collection of values returned by getWebBackendServiceIamPolicy.
    """
    def __init__(__self__, etag=None, id=None, policy_data=None, project=None, web_backend_service=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policy_data and not isinstance(policy_data, str):
            raise TypeError("Expected argument 'policy_data' to be a str")
        pulumi.set(__self__, "policy_data", policy_data)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if web_backend_service and not isinstance(web_backend_service, str):
            raise TypeError("Expected argument 'web_backend_service' to be a str")
        pulumi.set(__self__, "web_backend_service", web_backend_service)

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
        (Required only by `iap.WebBackendServiceIamPolicy`) The policy data generated by
        a `organizations_get_iam_policy` data source.
        """
        return pulumi.get(self, "policy_data")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="webBackendService")
    def web_backend_service(self) -> str:
        return pulumi.get(self, "web_backend_service")


class AwaitableGetWebBackendServiceIamPolicyResult(GetWebBackendServiceIamPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebBackendServiceIamPolicyResult(
            etag=self.etag,
            id=self.id,
            policy_data=self.policy_data,
            project=self.project,
            web_backend_service=self.web_backend_service)


def get_web_backend_service_iam_policy(project: Optional[str] = None,
                                       web_backend_service: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebBackendServiceIamPolicyResult:
    """
    Retrieves the current IAM policy data for webbackendservice

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.iap.get_web_backend_service_iam_policy(project=default["project"],
        web_backend_service=default["name"])
    ```


    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    :param str web_backend_service: Used to find the parent resource to bind the IAM policy to
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['webBackendService'] = web_backend_service
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:iap/getWebBackendServiceIamPolicy:getWebBackendServiceIamPolicy', __args__, opts=opts, typ=GetWebBackendServiceIamPolicyResult).value

    return AwaitableGetWebBackendServiceIamPolicyResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        policy_data=pulumi.get(__ret__, 'policy_data'),
        project=pulumi.get(__ret__, 'project'),
        web_backend_service=pulumi.get(__ret__, 'web_backend_service'))


@_utilities.lift_output_func(get_web_backend_service_iam_policy)
def get_web_backend_service_iam_policy_output(project: Optional[pulumi.Input[Optional[str]]] = None,
                                              web_backend_service: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebBackendServiceIamPolicyResult]:
    """
    Retrieves the current IAM policy data for webbackendservice

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.iap.get_web_backend_service_iam_policy(project=default["project"],
        web_backend_service=default["name"])
    ```


    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    :param str web_backend_service: Used to find the parent resource to bind the IAM policy to
    """
    ...
