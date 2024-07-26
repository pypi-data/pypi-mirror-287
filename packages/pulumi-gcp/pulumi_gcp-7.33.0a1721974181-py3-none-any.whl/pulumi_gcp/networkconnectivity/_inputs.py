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
    'HubRoutingVpcArgs',
    'HubRoutingVpcArgsDict',
    'PolicyBasedRouteFilterArgs',
    'PolicyBasedRouteFilterArgsDict',
    'PolicyBasedRouteInterconnectAttachmentArgs',
    'PolicyBasedRouteInterconnectAttachmentArgsDict',
    'PolicyBasedRouteVirtualMachineArgs',
    'PolicyBasedRouteVirtualMachineArgsDict',
    'PolicyBasedRouteWarningArgs',
    'PolicyBasedRouteWarningArgsDict',
    'ServiceConnectionPolicyPscConfigArgs',
    'ServiceConnectionPolicyPscConfigArgsDict',
    'ServiceConnectionPolicyPscConnectionArgs',
    'ServiceConnectionPolicyPscConnectionArgsDict',
    'ServiceConnectionPolicyPscConnectionErrorArgs',
    'ServiceConnectionPolicyPscConnectionErrorArgsDict',
    'ServiceConnectionPolicyPscConnectionErrorInfoArgs',
    'ServiceConnectionPolicyPscConnectionErrorInfoArgsDict',
    'SpokeLinkedInterconnectAttachmentsArgs',
    'SpokeLinkedInterconnectAttachmentsArgsDict',
    'SpokeLinkedRouterApplianceInstancesArgs',
    'SpokeLinkedRouterApplianceInstancesArgsDict',
    'SpokeLinkedRouterApplianceInstancesInstanceArgs',
    'SpokeLinkedRouterApplianceInstancesInstanceArgsDict',
    'SpokeLinkedVpcNetworkArgs',
    'SpokeLinkedVpcNetworkArgsDict',
    'SpokeLinkedVpnTunnelsArgs',
    'SpokeLinkedVpnTunnelsArgsDict',
]

MYPY = False

if not MYPY:
    class HubRoutingVpcArgsDict(TypedDict):
        uri: NotRequired[pulumi.Input[str]]
        """
        The URI of the VPC network.
        """
elif False:
    HubRoutingVpcArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class HubRoutingVpcArgs:
    def __init__(__self__, *,
                 uri: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] uri: The URI of the VPC network.
        """
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        """
        The URI of the VPC network.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)


if not MYPY:
    class PolicyBasedRouteFilterArgsDict(TypedDict):
        protocol_version: pulumi.Input[str]
        """
        Internet protocol versions this policy-based route applies to.
        Possible values are: `IPV4`.
        """
        dest_range: NotRequired[pulumi.Input[str]]
        """
        The destination IP range of outgoing packets that this policy-based route applies to. Default is "0.0.0.0/0" if protocol version is IPv4.

        - - -
        """
        ip_protocol: NotRequired[pulumi.Input[str]]
        """
        The IP protocol that this policy-based route applies to. Valid values are 'TCP', 'UDP', and 'ALL'. Default is 'ALL'.
        """
        src_range: NotRequired[pulumi.Input[str]]
        """
        The source IP range of outgoing packets that this policy-based route applies to. Default is "0.0.0.0/0" if protocol version is IPv4.
        """
elif False:
    PolicyBasedRouteFilterArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PolicyBasedRouteFilterArgs:
    def __init__(__self__, *,
                 protocol_version: pulumi.Input[str],
                 dest_range: Optional[pulumi.Input[str]] = None,
                 ip_protocol: Optional[pulumi.Input[str]] = None,
                 src_range: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] protocol_version: Internet protocol versions this policy-based route applies to.
               Possible values are: `IPV4`.
        :param pulumi.Input[str] dest_range: The destination IP range of outgoing packets that this policy-based route applies to. Default is "0.0.0.0/0" if protocol version is IPv4.
               
               - - -
        :param pulumi.Input[str] ip_protocol: The IP protocol that this policy-based route applies to. Valid values are 'TCP', 'UDP', and 'ALL'. Default is 'ALL'.
        :param pulumi.Input[str] src_range: The source IP range of outgoing packets that this policy-based route applies to. Default is "0.0.0.0/0" if protocol version is IPv4.
        """
        pulumi.set(__self__, "protocol_version", protocol_version)
        if dest_range is not None:
            pulumi.set(__self__, "dest_range", dest_range)
        if ip_protocol is not None:
            pulumi.set(__self__, "ip_protocol", ip_protocol)
        if src_range is not None:
            pulumi.set(__self__, "src_range", src_range)

    @property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> pulumi.Input[str]:
        """
        Internet protocol versions this policy-based route applies to.
        Possible values are: `IPV4`.
        """
        return pulumi.get(self, "protocol_version")

    @protocol_version.setter
    def protocol_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol_version", value)

    @property
    @pulumi.getter(name="destRange")
    def dest_range(self) -> Optional[pulumi.Input[str]]:
        """
        The destination IP range of outgoing packets that this policy-based route applies to. Default is "0.0.0.0/0" if protocol version is IPv4.

        - - -
        """
        return pulumi.get(self, "dest_range")

    @dest_range.setter
    def dest_range(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dest_range", value)

    @property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The IP protocol that this policy-based route applies to. Valid values are 'TCP', 'UDP', and 'ALL'. Default is 'ALL'.
        """
        return pulumi.get(self, "ip_protocol")

    @ip_protocol.setter
    def ip_protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_protocol", value)

    @property
    @pulumi.getter(name="srcRange")
    def src_range(self) -> Optional[pulumi.Input[str]]:
        """
        The source IP range of outgoing packets that this policy-based route applies to. Default is "0.0.0.0/0" if protocol version is IPv4.
        """
        return pulumi.get(self, "src_range")

    @src_range.setter
    def src_range(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "src_range", value)


if not MYPY:
    class PolicyBasedRouteInterconnectAttachmentArgsDict(TypedDict):
        region: pulumi.Input[str]
        """
        Cloud region to install this policy-based route on for Interconnect attachments. Use `all` to install it on all Interconnect attachments.
        """
elif False:
    PolicyBasedRouteInterconnectAttachmentArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PolicyBasedRouteInterconnectAttachmentArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str]):
        """
        :param pulumi.Input[str] region: Cloud region to install this policy-based route on for Interconnect attachments. Use `all` to install it on all Interconnect attachments.
        """
        pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        Cloud region to install this policy-based route on for Interconnect attachments. Use `all` to install it on all Interconnect attachments.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)


if not MYPY:
    class PolicyBasedRouteVirtualMachineArgsDict(TypedDict):
        tags: pulumi.Input[Sequence[pulumi.Input[str]]]
        """
        A list of VM instance tags that this policy-based route applies to. VM instances that have ANY of tags specified here will install this PBR.
        """
elif False:
    PolicyBasedRouteVirtualMachineArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PolicyBasedRouteVirtualMachineArgs:
    def __init__(__self__, *,
                 tags: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of VM instance tags that this policy-based route applies to. VM instances that have ANY of tags specified here will install this PBR.
        """
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of VM instance tags that this policy-based route applies to. VM instances that have ANY of tags specified here will install this PBR.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "tags", value)


if not MYPY:
    class PolicyBasedRouteWarningArgsDict(TypedDict):
        code: NotRequired[pulumi.Input[str]]
        """
        (Output)
        A warning code, if applicable.
        """
        data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[str]]]]
        """
        (Output)
        Metadata about this warning in key: value format. The key should provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be scope and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement.
        """
        warning_message: NotRequired[pulumi.Input[str]]
        """
        (Output)
        A human-readable description of the warning code.
        """
elif False:
    PolicyBasedRouteWarningArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PolicyBasedRouteWarningArgs:
    def __init__(__self__, *,
                 code: Optional[pulumi.Input[str]] = None,
                 data: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 warning_message: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] code: (Output)
               A warning code, if applicable.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] data: (Output)
               Metadata about this warning in key: value format. The key should provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be scope and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement.
        :param pulumi.Input[str] warning_message: (Output)
               A human-readable description of the warning code.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)
        if data is not None:
            pulumi.set(__self__, "data", data)
        if warning_message is not None:
            pulumi.set(__self__, "warning_message", warning_message)

    @property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[str]]:
        """
        (Output)
        A warning code, if applicable.
        """
        return pulumi.get(self, "code")

    @code.setter
    def code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "code", value)

    @property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        (Output)
        Metadata about this warning in key: value format. The key should provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be scope and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement.
        """
        return pulumi.get(self, "data")

    @data.setter
    def data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "data", value)

    @property
    @pulumi.getter(name="warningMessage")
    def warning_message(self) -> Optional[pulumi.Input[str]]:
        """
        (Output)
        A human-readable description of the warning code.
        """
        return pulumi.get(self, "warning_message")

    @warning_message.setter
    def warning_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "warning_message", value)


if not MYPY:
    class ServiceConnectionPolicyPscConfigArgsDict(TypedDict):
        subnetworks: pulumi.Input[Sequence[pulumi.Input[str]]]
        """
        IDs of the subnetworks or fully qualified identifiers for the subnetworks
        """
        limit: NotRequired[pulumi.Input[str]]
        """
        Max number of PSC connections for this policy.
        """
elif False:
    ServiceConnectionPolicyPscConfigArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServiceConnectionPolicyPscConfigArgs:
    def __init__(__self__, *,
                 subnetworks: pulumi.Input[Sequence[pulumi.Input[str]]],
                 limit: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnetworks: IDs of the subnetworks or fully qualified identifiers for the subnetworks
        :param pulumi.Input[str] limit: Max number of PSC connections for this policy.
        """
        pulumi.set(__self__, "subnetworks", subnetworks)
        if limit is not None:
            pulumi.set(__self__, "limit", limit)

    @property
    @pulumi.getter
    def subnetworks(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        IDs of the subnetworks or fully qualified identifiers for the subnetworks
        """
        return pulumi.get(self, "subnetworks")

    @subnetworks.setter
    def subnetworks(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnetworks", value)

    @property
    @pulumi.getter
    def limit(self) -> Optional[pulumi.Input[str]]:
        """
        Max number of PSC connections for this policy.
        """
        return pulumi.get(self, "limit")

    @limit.setter
    def limit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "limit", value)


if not MYPY:
    class ServiceConnectionPolicyPscConnectionArgsDict(TypedDict):
        consumer_address: NotRequired[pulumi.Input[str]]
        """
        The resource reference of the consumer address.
        """
        consumer_forwarding_rule: NotRequired[pulumi.Input[str]]
        """
        The resource reference of the PSC Forwarding Rule within the consumer VPC.
        """
        consumer_target_project: NotRequired[pulumi.Input[str]]
        """
        The project where the PSC connection is created.
        """
        error: NotRequired[pulumi.Input['ServiceConnectionPolicyPscConnectionErrorArgsDict']]
        """
        The most recent error during operating this connection.
        Structure is documented below.
        """
        error_info: NotRequired[pulumi.Input['ServiceConnectionPolicyPscConnectionErrorInfoArgsDict']]
        """
        The error info for the latest error during operating this connection.
        Structure is documented below.
        """
        error_type: NotRequired[pulumi.Input[str]]
        """
        The error type indicates whether the error is consumer facing, producer
        facing or system internal.
        Possible values are: `CONNECTION_ERROR_TYPE_UNSPECIFIED`, `ERROR_INTERNAL`, `ERROR_CONSUMER_SIDE`, `ERROR_PRODUCER_SIDE`.
        """
        gce_operation: NotRequired[pulumi.Input[str]]
        """
        The last Compute Engine operation to setup PSC connection.
        """
        psc_connection_id: NotRequired[pulumi.Input[str]]
        """
        The PSC connection id of the PSC forwarding rule.
        """
        state: NotRequired[pulumi.Input[str]]
        """
        The state of the PSC connection.
        Possible values are: `STATE_UNSPECIFIED`, `ACTIVE`, `CREATING`, `DELETING`, `FAILED`.
        """
elif False:
    ServiceConnectionPolicyPscConnectionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServiceConnectionPolicyPscConnectionArgs:
    def __init__(__self__, *,
                 consumer_address: Optional[pulumi.Input[str]] = None,
                 consumer_forwarding_rule: Optional[pulumi.Input[str]] = None,
                 consumer_target_project: Optional[pulumi.Input[str]] = None,
                 error: Optional[pulumi.Input['ServiceConnectionPolicyPscConnectionErrorArgs']] = None,
                 error_info: Optional[pulumi.Input['ServiceConnectionPolicyPscConnectionErrorInfoArgs']] = None,
                 error_type: Optional[pulumi.Input[str]] = None,
                 gce_operation: Optional[pulumi.Input[str]] = None,
                 psc_connection_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] consumer_address: The resource reference of the consumer address.
        :param pulumi.Input[str] consumer_forwarding_rule: The resource reference of the PSC Forwarding Rule within the consumer VPC.
        :param pulumi.Input[str] consumer_target_project: The project where the PSC connection is created.
        :param pulumi.Input['ServiceConnectionPolicyPscConnectionErrorArgs'] error: The most recent error during operating this connection.
               Structure is documented below.
        :param pulumi.Input['ServiceConnectionPolicyPscConnectionErrorInfoArgs'] error_info: The error info for the latest error during operating this connection.
               Structure is documented below.
        :param pulumi.Input[str] error_type: The error type indicates whether the error is consumer facing, producer
               facing or system internal.
               Possible values are: `CONNECTION_ERROR_TYPE_UNSPECIFIED`, `ERROR_INTERNAL`, `ERROR_CONSUMER_SIDE`, `ERROR_PRODUCER_SIDE`.
        :param pulumi.Input[str] gce_operation: The last Compute Engine operation to setup PSC connection.
        :param pulumi.Input[str] psc_connection_id: The PSC connection id of the PSC forwarding rule.
        :param pulumi.Input[str] state: The state of the PSC connection.
               Possible values are: `STATE_UNSPECIFIED`, `ACTIVE`, `CREATING`, `DELETING`, `FAILED`.
        """
        if consumer_address is not None:
            pulumi.set(__self__, "consumer_address", consumer_address)
        if consumer_forwarding_rule is not None:
            pulumi.set(__self__, "consumer_forwarding_rule", consumer_forwarding_rule)
        if consumer_target_project is not None:
            pulumi.set(__self__, "consumer_target_project", consumer_target_project)
        if error is not None:
            pulumi.set(__self__, "error", error)
        if error_info is not None:
            pulumi.set(__self__, "error_info", error_info)
        if error_type is not None:
            pulumi.set(__self__, "error_type", error_type)
        if gce_operation is not None:
            pulumi.set(__self__, "gce_operation", gce_operation)
        if psc_connection_id is not None:
            pulumi.set(__self__, "psc_connection_id", psc_connection_id)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="consumerAddress")
    def consumer_address(self) -> Optional[pulumi.Input[str]]:
        """
        The resource reference of the consumer address.
        """
        return pulumi.get(self, "consumer_address")

    @consumer_address.setter
    def consumer_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "consumer_address", value)

    @property
    @pulumi.getter(name="consumerForwardingRule")
    def consumer_forwarding_rule(self) -> Optional[pulumi.Input[str]]:
        """
        The resource reference of the PSC Forwarding Rule within the consumer VPC.
        """
        return pulumi.get(self, "consumer_forwarding_rule")

    @consumer_forwarding_rule.setter
    def consumer_forwarding_rule(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "consumer_forwarding_rule", value)

    @property
    @pulumi.getter(name="consumerTargetProject")
    def consumer_target_project(self) -> Optional[pulumi.Input[str]]:
        """
        The project where the PSC connection is created.
        """
        return pulumi.get(self, "consumer_target_project")

    @consumer_target_project.setter
    def consumer_target_project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "consumer_target_project", value)

    @property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input['ServiceConnectionPolicyPscConnectionErrorArgs']]:
        """
        The most recent error during operating this connection.
        Structure is documented below.
        """
        return pulumi.get(self, "error")

    @error.setter
    def error(self, value: Optional[pulumi.Input['ServiceConnectionPolicyPscConnectionErrorArgs']]):
        pulumi.set(self, "error", value)

    @property
    @pulumi.getter(name="errorInfo")
    def error_info(self) -> Optional[pulumi.Input['ServiceConnectionPolicyPscConnectionErrorInfoArgs']]:
        """
        The error info for the latest error during operating this connection.
        Structure is documented below.
        """
        return pulumi.get(self, "error_info")

    @error_info.setter
    def error_info(self, value: Optional[pulumi.Input['ServiceConnectionPolicyPscConnectionErrorInfoArgs']]):
        pulumi.set(self, "error_info", value)

    @property
    @pulumi.getter(name="errorType")
    def error_type(self) -> Optional[pulumi.Input[str]]:
        """
        The error type indicates whether the error is consumer facing, producer
        facing or system internal.
        Possible values are: `CONNECTION_ERROR_TYPE_UNSPECIFIED`, `ERROR_INTERNAL`, `ERROR_CONSUMER_SIDE`, `ERROR_PRODUCER_SIDE`.
        """
        return pulumi.get(self, "error_type")

    @error_type.setter
    def error_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "error_type", value)

    @property
    @pulumi.getter(name="gceOperation")
    def gce_operation(self) -> Optional[pulumi.Input[str]]:
        """
        The last Compute Engine operation to setup PSC connection.
        """
        return pulumi.get(self, "gce_operation")

    @gce_operation.setter
    def gce_operation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gce_operation", value)

    @property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> Optional[pulumi.Input[str]]:
        """
        The PSC connection id of the PSC forwarding rule.
        """
        return pulumi.get(self, "psc_connection_id")

    @psc_connection_id.setter
    def psc_connection_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "psc_connection_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state of the PSC connection.
        Possible values are: `STATE_UNSPECIFIED`, `ACTIVE`, `CREATING`, `DELETING`, `FAILED`.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


if not MYPY:
    class ServiceConnectionPolicyPscConnectionErrorArgsDict(TypedDict):
        code: NotRequired[pulumi.Input[int]]
        """
        The status code, which should be an enum value of [google.rpc.Code][].
        """
        details: NotRequired[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]]
        """
        (Output)
        A list of messages that carry the error details.
        """
        message: NotRequired[pulumi.Input[str]]
        """
        A developer-facing error message.
        """
elif False:
    ServiceConnectionPolicyPscConnectionErrorArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServiceConnectionPolicyPscConnectionErrorArgs:
    def __init__(__self__, *,
                 code: Optional[pulumi.Input[int]] = None,
                 details: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 message: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[int] code: The status code, which should be an enum value of [google.rpc.Code][].
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] details: (Output)
               A list of messages that carry the error details.
        :param pulumi.Input[str] message: A developer-facing error message.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)
        if details is not None:
            pulumi.set(__self__, "details", details)
        if message is not None:
            pulumi.set(__self__, "message", message)

    @property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[int]]:
        """
        The status code, which should be an enum value of [google.rpc.Code][].
        """
        return pulumi.get(self, "code")

    @code.setter
    def code(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "code", value)

    @property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]]:
        """
        (Output)
        A list of messages that carry the error details.
        """
        return pulumi.get(self, "details")

    @details.setter
    def details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]]):
        pulumi.set(self, "details", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        A developer-facing error message.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)


if not MYPY:
    class ServiceConnectionPolicyPscConnectionErrorInfoArgsDict(TypedDict):
        domain: NotRequired[pulumi.Input[str]]
        """
        The logical grouping to which the "reason" belongs.
        """
        metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[str]]]]
        """
        Additional structured details about this error.
        """
        reason: NotRequired[pulumi.Input[str]]
        """
        The reason of the error.
        """
elif False:
    ServiceConnectionPolicyPscConnectionErrorInfoArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServiceConnectionPolicyPscConnectionErrorInfoArgs:
    def __init__(__self__, *,
                 domain: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 reason: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] domain: The logical grouping to which the "reason" belongs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Additional structured details about this error.
        :param pulumi.Input[str] reason: The reason of the error.
        """
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if reason is not None:
            pulumi.set(__self__, "reason", reason)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The logical grouping to which the "reason" belongs.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Additional structured details about this error.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[str]]:
        """
        The reason of the error.
        """
        return pulumi.get(self, "reason")

    @reason.setter
    def reason(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reason", value)


if not MYPY:
    class SpokeLinkedInterconnectAttachmentsArgsDict(TypedDict):
        site_to_site_data_transfer: pulumi.Input[bool]
        """
        A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations.
        """
        uris: pulumi.Input[Sequence[pulumi.Input[str]]]
        """
        The URIs of linked interconnect attachment resources
        """
elif False:
    SpokeLinkedInterconnectAttachmentsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SpokeLinkedInterconnectAttachmentsArgs:
    def __init__(__self__, *,
                 site_to_site_data_transfer: pulumi.Input[bool],
                 uris: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        :param pulumi.Input[bool] site_to_site_data_transfer: A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] uris: The URIs of linked interconnect attachment resources
        """
        pulumi.set(__self__, "site_to_site_data_transfer", site_to_site_data_transfer)
        pulumi.set(__self__, "uris", uris)

    @property
    @pulumi.getter(name="siteToSiteDataTransfer")
    def site_to_site_data_transfer(self) -> pulumi.Input[bool]:
        """
        A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations.
        """
        return pulumi.get(self, "site_to_site_data_transfer")

    @site_to_site_data_transfer.setter
    def site_to_site_data_transfer(self, value: pulumi.Input[bool]):
        pulumi.set(self, "site_to_site_data_transfer", value)

    @property
    @pulumi.getter
    def uris(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The URIs of linked interconnect attachment resources
        """
        return pulumi.get(self, "uris")

    @uris.setter
    def uris(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "uris", value)


if not MYPY:
    class SpokeLinkedRouterApplianceInstancesArgsDict(TypedDict):
        instances: pulumi.Input[Sequence[pulumi.Input['SpokeLinkedRouterApplianceInstancesInstanceArgsDict']]]
        """
        The list of router appliance instances
        """
        site_to_site_data_transfer: pulumi.Input[bool]
        """
        A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations.
        """
elif False:
    SpokeLinkedRouterApplianceInstancesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SpokeLinkedRouterApplianceInstancesArgs:
    def __init__(__self__, *,
                 instances: pulumi.Input[Sequence[pulumi.Input['SpokeLinkedRouterApplianceInstancesInstanceArgs']]],
                 site_to_site_data_transfer: pulumi.Input[bool]):
        """
        :param pulumi.Input[Sequence[pulumi.Input['SpokeLinkedRouterApplianceInstancesInstanceArgs']]] instances: The list of router appliance instances
        :param pulumi.Input[bool] site_to_site_data_transfer: A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations.
        """
        pulumi.set(__self__, "instances", instances)
        pulumi.set(__self__, "site_to_site_data_transfer", site_to_site_data_transfer)

    @property
    @pulumi.getter
    def instances(self) -> pulumi.Input[Sequence[pulumi.Input['SpokeLinkedRouterApplianceInstancesInstanceArgs']]]:
        """
        The list of router appliance instances
        """
        return pulumi.get(self, "instances")

    @instances.setter
    def instances(self, value: pulumi.Input[Sequence[pulumi.Input['SpokeLinkedRouterApplianceInstancesInstanceArgs']]]):
        pulumi.set(self, "instances", value)

    @property
    @pulumi.getter(name="siteToSiteDataTransfer")
    def site_to_site_data_transfer(self) -> pulumi.Input[bool]:
        """
        A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations.
        """
        return pulumi.get(self, "site_to_site_data_transfer")

    @site_to_site_data_transfer.setter
    def site_to_site_data_transfer(self, value: pulumi.Input[bool]):
        pulumi.set(self, "site_to_site_data_transfer", value)


if not MYPY:
    class SpokeLinkedRouterApplianceInstancesInstanceArgsDict(TypedDict):
        ip_address: NotRequired[pulumi.Input[str]]
        """
        The IP address on the VM to use for peering.
        """
        virtual_machine: NotRequired[pulumi.Input[str]]
        """
        The URI of the virtual machine resource

        - - -
        """
elif False:
    SpokeLinkedRouterApplianceInstancesInstanceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SpokeLinkedRouterApplianceInstancesInstanceArgs:
    def __init__(__self__, *,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 virtual_machine: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] ip_address: The IP address on the VM to use for peering.
        :param pulumi.Input[str] virtual_machine: The URI of the virtual machine resource
               
               - - -
        """
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if virtual_machine is not None:
            pulumi.set(__self__, "virtual_machine", virtual_machine)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address on the VM to use for peering.
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(self) -> Optional[pulumi.Input[str]]:
        """
        The URI of the virtual machine resource

        - - -
        """
        return pulumi.get(self, "virtual_machine")

    @virtual_machine.setter
    def virtual_machine(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_machine", value)


if not MYPY:
    class SpokeLinkedVpcNetworkArgsDict(TypedDict):
        uri: pulumi.Input[str]
        """
        The URI of the VPC network resource.
        """
        exclude_export_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        IP ranges encompassing the subnets to be excluded from peering.
        """
elif False:
    SpokeLinkedVpcNetworkArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SpokeLinkedVpcNetworkArgs:
    def __init__(__self__, *,
                 uri: pulumi.Input[str],
                 exclude_export_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] uri: The URI of the VPC network resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] exclude_export_ranges: IP ranges encompassing the subnets to be excluded from peering.
        """
        pulumi.set(__self__, "uri", uri)
        if exclude_export_ranges is not None:
            pulumi.set(__self__, "exclude_export_ranges", exclude_export_ranges)

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Input[str]:
        """
        The URI of the VPC network resource.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "uri", value)

    @property
    @pulumi.getter(name="excludeExportRanges")
    def exclude_export_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        IP ranges encompassing the subnets to be excluded from peering.
        """
        return pulumi.get(self, "exclude_export_ranges")

    @exclude_export_ranges.setter
    def exclude_export_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "exclude_export_ranges", value)


if not MYPY:
    class SpokeLinkedVpnTunnelsArgsDict(TypedDict):
        site_to_site_data_transfer: pulumi.Input[bool]
        """
        A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations.
        """
        uris: pulumi.Input[Sequence[pulumi.Input[str]]]
        """
        The URIs of linked VPN tunnel resources.
        """
elif False:
    SpokeLinkedVpnTunnelsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SpokeLinkedVpnTunnelsArgs:
    def __init__(__self__, *,
                 site_to_site_data_transfer: pulumi.Input[bool],
                 uris: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        :param pulumi.Input[bool] site_to_site_data_transfer: A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] uris: The URIs of linked VPN tunnel resources.
        """
        pulumi.set(__self__, "site_to_site_data_transfer", site_to_site_data_transfer)
        pulumi.set(__self__, "uris", uris)

    @property
    @pulumi.getter(name="siteToSiteDataTransfer")
    def site_to_site_data_transfer(self) -> pulumi.Input[bool]:
        """
        A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations.
        """
        return pulumi.get(self, "site_to_site_data_transfer")

    @site_to_site_data_transfer.setter
    def site_to_site_data_transfer(self, value: pulumi.Input[bool]):
        pulumi.set(self, "site_to_site_data_transfer", value)

    @property
    @pulumi.getter
    def uris(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The URIs of linked VPN tunnel resources.
        """
        return pulumi.get(self, "uris")

    @uris.setter
    def uris(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "uris", value)


