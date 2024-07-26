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
    'GetAddressResult',
    'AwaitableGetAddressResult',
    'get_address',
    'get_address_output',
]

@pulumi.output_type
class GetAddressResult:
    """
    A collection of values returned by getAddress.
    """
    def __init__(__self__, address=None, address_type=None, id=None, name=None, network=None, network_tier=None, prefix_length=None, project=None, purpose=None, region=None, self_link=None, status=None, subnetwork=None, users=None):
        if address and not isinstance(address, str):
            raise TypeError("Expected argument 'address' to be a str")
        pulumi.set(__self__, "address", address)
        if address_type and not isinstance(address_type, str):
            raise TypeError("Expected argument 'address_type' to be a str")
        pulumi.set(__self__, "address_type", address_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        pulumi.set(__self__, "network", network)
        if network_tier and not isinstance(network_tier, str):
            raise TypeError("Expected argument 'network_tier' to be a str")
        pulumi.set(__self__, "network_tier", network_tier)
        if prefix_length and not isinstance(prefix_length, int):
            raise TypeError("Expected argument 'prefix_length' to be a int")
        pulumi.set(__self__, "prefix_length", prefix_length)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if purpose and not isinstance(purpose, str):
            raise TypeError("Expected argument 'purpose' to be a str")
        pulumi.set(__self__, "purpose", purpose)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if subnetwork and not isinstance(subnetwork, str):
            raise TypeError("Expected argument 'subnetwork' to be a str")
        pulumi.set(__self__, "subnetwork", subnetwork)
        if users and not isinstance(users, str):
            raise TypeError("Expected argument 'users' to be a str")
        pulumi.set(__self__, "users", users)

    @property
    @pulumi.getter
    def address(self) -> str:
        """
        The IP of the created resource.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter(name="addressType")
    def address_type(self) -> str:
        return pulumi.get(self, "address_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> str:
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> str:
        return pulumi.get(self, "network_tier")

    @property
    @pulumi.getter(name="prefixLength")
    def prefix_length(self) -> int:
        return pulumi.get(self, "prefix_length")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def purpose(self) -> str:
        return pulumi.get(self, "purpose")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Indicates if the address is used. Possible values are: RESERVED or IN_USE.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def subnetwork(self) -> str:
        return pulumi.get(self, "subnetwork")

    @property
    @pulumi.getter
    def users(self) -> str:
        return pulumi.get(self, "users")


class AwaitableGetAddressResult(GetAddressResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAddressResult(
            address=self.address,
            address_type=self.address_type,
            id=self.id,
            name=self.name,
            network=self.network,
            network_tier=self.network_tier,
            prefix_length=self.prefix_length,
            project=self.project,
            purpose=self.purpose,
            region=self.region,
            self_link=self.self_link,
            status=self.status,
            subnetwork=self.subnetwork,
            users=self.users)


def get_address(name: Optional[str] = None,
                project: Optional[str] = None,
                region: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAddressResult:
    """
    Get the IP address from a static address. For more information see
    the official [API](https://cloud.google.com/compute/docs/reference/latest/addresses/get) documentation.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    my_address = gcp.compute.get_address(name="foobar")
    prod = gcp.dns.ManagedZone("prod",
        name="prod-zone",
        dns_name="prod.mydomain.com.")
    frontend = gcp.dns.RecordSet("frontend",
        name=prod.dns_name.apply(lambda dns_name: f"frontend.{dns_name}"),
        type="A",
        ttl=300,
        managed_zone=prod.name,
        rrdatas=[my_address.address])
    ```


    :param str name: A unique name for the resource, required by GCE.
           
           - - -
    :param str project: The project in which the resource belongs. If it
           is not provided, the provider project is used.
    :param str region: The Region in which the created address reside.
           If it is not provided, the provider region is used.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    __args__['region'] = region
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:compute/getAddress:getAddress', __args__, opts=opts, typ=GetAddressResult).value

    return AwaitableGetAddressResult(
        address=pulumi.get(__ret__, 'address'),
        address_type=pulumi.get(__ret__, 'address_type'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        network=pulumi.get(__ret__, 'network'),
        network_tier=pulumi.get(__ret__, 'network_tier'),
        prefix_length=pulumi.get(__ret__, 'prefix_length'),
        project=pulumi.get(__ret__, 'project'),
        purpose=pulumi.get(__ret__, 'purpose'),
        region=pulumi.get(__ret__, 'region'),
        self_link=pulumi.get(__ret__, 'self_link'),
        status=pulumi.get(__ret__, 'status'),
        subnetwork=pulumi.get(__ret__, 'subnetwork'),
        users=pulumi.get(__ret__, 'users'))


@_utilities.lift_output_func(get_address)
def get_address_output(name: Optional[pulumi.Input[str]] = None,
                       project: Optional[pulumi.Input[Optional[str]]] = None,
                       region: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAddressResult]:
    """
    Get the IP address from a static address. For more information see
    the official [API](https://cloud.google.com/compute/docs/reference/latest/addresses/get) documentation.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    my_address = gcp.compute.get_address(name="foobar")
    prod = gcp.dns.ManagedZone("prod",
        name="prod-zone",
        dns_name="prod.mydomain.com.")
    frontend = gcp.dns.RecordSet("frontend",
        name=prod.dns_name.apply(lambda dns_name: f"frontend.{dns_name}"),
        type="A",
        ttl=300,
        managed_zone=prod.name,
        rrdatas=[my_address.address])
    ```


    :param str name: A unique name for the resource, required by GCE.
           
           - - -
    :param str project: The project in which the resource belongs. If it
           is not provided, the provider project is used.
    :param str region: The Region in which the created address reside.
           If it is not provided, the provider region is used.
    """
    ...
