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
    'GetStaticIpsResult',
    'AwaitableGetStaticIpsResult',
    'get_static_ips',
    'get_static_ips_output',
]

@pulumi.output_type
class GetStaticIpsResult:
    """
    A collection of values returned by getStaticIps.
    """
    def __init__(__self__, id=None, location=None, project=None, static_ips=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if static_ips and not isinstance(static_ips, list):
            raise TypeError("Expected argument 'static_ips' to be a list")
        pulumi.set(__self__, "static_ips", static_ips)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="staticIps")
    def static_ips(self) -> Sequence[str]:
        """
        A list of static IP addresses that Datastream will connect from.
        """
        return pulumi.get(self, "static_ips")


class AwaitableGetStaticIpsResult(GetStaticIpsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStaticIpsResult(
            id=self.id,
            location=self.location,
            project=self.project,
            static_ips=self.static_ips)


def get_static_ips(location: Optional[str] = None,
                   project: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStaticIpsResult:
    """
    Returns the list of IP addresses that Datastream connects from. For more information see
    the [official documentation](https://cloud.google.com/datastream/docs/ip-allowlists-and-regions).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    datastream_ips = gcp.datastream.get_static_ips(location="us-west1",
        project="my-project")
    pulumi.export("ipList", datastream_ips.static_ips)
    ```


    :param str location: The location to list Datastream IPs for. For example: `us-east1`.
    :param str project: Project from which to list static IP addresses. Defaults to project declared in the provider.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:datastream/getStaticIps:getStaticIps', __args__, opts=opts, typ=GetStaticIpsResult).value

    return AwaitableGetStaticIpsResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        project=pulumi.get(__ret__, 'project'),
        static_ips=pulumi.get(__ret__, 'static_ips'))


@_utilities.lift_output_func(get_static_ips)
def get_static_ips_output(location: Optional[pulumi.Input[str]] = None,
                          project: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStaticIpsResult]:
    """
    Returns the list of IP addresses that Datastream connects from. For more information see
    the [official documentation](https://cloud.google.com/datastream/docs/ip-allowlists-and-regions).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    datastream_ips = gcp.datastream.get_static_ips(location="us-west1",
        project="my-project")
    pulumi.export("ipList", datastream_ips.static_ips)
    ```


    :param str location: The location to list Datastream IPs for. For example: `us-east1`.
    :param str project: Project from which to list static IP addresses. Defaults to project declared in the provider.
    """
    ...
