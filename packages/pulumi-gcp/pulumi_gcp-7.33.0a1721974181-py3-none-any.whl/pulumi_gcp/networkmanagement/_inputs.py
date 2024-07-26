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
    'ConnectivityTestDestinationArgs',
    'ConnectivityTestDestinationArgsDict',
    'ConnectivityTestSourceArgs',
    'ConnectivityTestSourceArgsDict',
]

MYPY = False

if not MYPY:
    class ConnectivityTestDestinationArgsDict(TypedDict):
        instance: NotRequired[pulumi.Input[str]]
        """
        A Compute Engine instance URI.
        """
        ip_address: NotRequired[pulumi.Input[str]]
        """
        The IP address of the endpoint, which can be an external or
        internal IP. An IPv6 address is only allowed when the test's
        destination is a global load balancer VIP.
        """
        network: NotRequired[pulumi.Input[str]]
        """
        A Compute Engine network URI.
        """
        port: NotRequired[pulumi.Input[int]]
        """
        The IP protocol port of the endpoint. Only applicable when
        protocol is TCP or UDP.
        """
        project_id: NotRequired[pulumi.Input[str]]
        """
        Project ID where the endpoint is located. The Project ID can be
        derived from the URI if you provide a VM instance or network URI.
        The following are two cases where you must provide the project ID:
        1. Only the IP address is specified, and the IP address is within
        a GCP project. 2. When you are using Shared VPC and the IP address
        that you provide is from the service project. In this case, the
        network that the IP address resides in is defined in the host
        project.

        - - -
        """
elif False:
    ConnectivityTestDestinationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ConnectivityTestDestinationArgs:
    def __init__(__self__, *,
                 instance: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 project_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] instance: A Compute Engine instance URI.
        :param pulumi.Input[str] ip_address: The IP address of the endpoint, which can be an external or
               internal IP. An IPv6 address is only allowed when the test's
               destination is a global load balancer VIP.
        :param pulumi.Input[str] network: A Compute Engine network URI.
        :param pulumi.Input[int] port: The IP protocol port of the endpoint. Only applicable when
               protocol is TCP or UDP.
        :param pulumi.Input[str] project_id: Project ID where the endpoint is located. The Project ID can be
               derived from the URI if you provide a VM instance or network URI.
               The following are two cases where you must provide the project ID:
               1. Only the IP address is specified, and the IP address is within
               a GCP project. 2. When you are using Shared VPC and the IP address
               that you provide is from the service project. In this case, the
               network that the IP address resides in is defined in the host
               project.
               
               - - -
        """
        if instance is not None:
            pulumi.set(__self__, "instance", instance)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if network is not None:
            pulumi.set(__self__, "network", network)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[str]]:
        """
        A Compute Engine instance URI.
        """
        return pulumi.get(self, "instance")

    @instance.setter
    def instance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the endpoint, which can be an external or
        internal IP. An IPv6 address is only allowed when the test's
        destination is a global load balancer VIP.
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[str]]:
        """
        A Compute Engine network URI.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The IP protocol port of the endpoint. Only applicable when
        protocol is TCP or UDP.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Project ID where the endpoint is located. The Project ID can be
        derived from the URI if you provide a VM instance or network URI.
        The following are two cases where you must provide the project ID:
        1. Only the IP address is specified, and the IP address is within
        a GCP project. 2. When you are using Shared VPC and the IP address
        that you provide is from the service project. In this case, the
        network that the IP address resides in is defined in the host
        project.

        - - -
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)


if not MYPY:
    class ConnectivityTestSourceArgsDict(TypedDict):
        instance: NotRequired[pulumi.Input[str]]
        """
        A Compute Engine instance URI.
        """
        ip_address: NotRequired[pulumi.Input[str]]
        """
        The IP address of the endpoint, which can be an external or
        internal IP. An IPv6 address is only allowed when the test's
        destination is a global load balancer VIP.
        """
        network: NotRequired[pulumi.Input[str]]
        """
        A Compute Engine network URI.
        """
        network_type: NotRequired[pulumi.Input[str]]
        """
        Type of the network where the endpoint is located.
        Possible values are: `GCP_NETWORK`, `NON_GCP_NETWORK`.
        """
        port: NotRequired[pulumi.Input[int]]
        """
        The IP protocol port of the endpoint. Only applicable when
        protocol is TCP or UDP.
        """
        project_id: NotRequired[pulumi.Input[str]]
        """
        Project ID where the endpoint is located. The Project ID can be
        derived from the URI if you provide a VM instance or network URI.
        The following are two cases where you must provide the project ID:
        1. Only the IP address is specified, and the IP address is
        within a GCP project.
        2. When you are using Shared VPC and the IP address
        that you provide is from the service project. In this case,
        the network that the IP address resides in is defined in the
        host project.
        """
elif False:
    ConnectivityTestSourceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ConnectivityTestSourceArgs:
    def __init__(__self__, *,
                 instance: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 network_type: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 project_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] instance: A Compute Engine instance URI.
        :param pulumi.Input[str] ip_address: The IP address of the endpoint, which can be an external or
               internal IP. An IPv6 address is only allowed when the test's
               destination is a global load balancer VIP.
        :param pulumi.Input[str] network: A Compute Engine network URI.
        :param pulumi.Input[str] network_type: Type of the network where the endpoint is located.
               Possible values are: `GCP_NETWORK`, `NON_GCP_NETWORK`.
        :param pulumi.Input[int] port: The IP protocol port of the endpoint. Only applicable when
               protocol is TCP or UDP.
        :param pulumi.Input[str] project_id: Project ID where the endpoint is located. The Project ID can be
               derived from the URI if you provide a VM instance or network URI.
               The following are two cases where you must provide the project ID:
               1. Only the IP address is specified, and the IP address is
               within a GCP project.
               2. When you are using Shared VPC and the IP address
               that you provide is from the service project. In this case,
               the network that the IP address resides in is defined in the
               host project.
        """
        if instance is not None:
            pulumi.set(__self__, "instance", instance)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if network is not None:
            pulumi.set(__self__, "network", network)
        if network_type is not None:
            pulumi.set(__self__, "network_type", network_type)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[str]]:
        """
        A Compute Engine instance URI.
        """
        return pulumi.get(self, "instance")

    @instance.setter
    def instance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the endpoint, which can be an external or
        internal IP. An IPv6 address is only allowed when the test's
        destination is a global load balancer VIP.
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[str]]:
        """
        A Compute Engine network URI.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the network where the endpoint is located.
        Possible values are: `GCP_NETWORK`, `NON_GCP_NETWORK`.
        """
        return pulumi.get(self, "network_type")

    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_type", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The IP protocol port of the endpoint. Only applicable when
        protocol is TCP or UDP.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Project ID where the endpoint is located. The Project ID can be
        derived from the URI if you provide a VM instance or network URI.
        The following are two cases where you must provide the project ID:
        1. Only the IP address is specified, and the IP address is
        within a GCP project.
        2. When you are using Shared VPC and the IP address
        that you provide is from the service project. In this case,
        the network that the IP address resides in is defined in the
        host project.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)


