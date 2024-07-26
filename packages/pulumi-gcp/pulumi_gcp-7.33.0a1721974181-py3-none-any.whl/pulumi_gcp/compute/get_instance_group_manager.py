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
    'GetInstanceGroupManagerResult',
    'AwaitableGetInstanceGroupManagerResult',
    'get_instance_group_manager',
    'get_instance_group_manager_output',
]

@pulumi.output_type
class GetInstanceGroupManagerResult:
    """
    A collection of values returned by getInstanceGroupManager.
    """
    def __init__(__self__, all_instances_configs=None, auto_healing_policies=None, base_instance_name=None, creation_timestamp=None, description=None, fingerprint=None, id=None, instance_group=None, instance_lifecycle_policies=None, list_managed_instances_results=None, name=None, named_ports=None, operation=None, params=None, project=None, self_link=None, standby_policies=None, stateful_disks=None, stateful_external_ips=None, stateful_internal_ips=None, statuses=None, target_pools=None, target_size=None, target_stopped_size=None, target_suspended_size=None, update_policies=None, versions=None, wait_for_instances=None, wait_for_instances_status=None, zone=None):
        if all_instances_configs and not isinstance(all_instances_configs, list):
            raise TypeError("Expected argument 'all_instances_configs' to be a list")
        pulumi.set(__self__, "all_instances_configs", all_instances_configs)
        if auto_healing_policies and not isinstance(auto_healing_policies, list):
            raise TypeError("Expected argument 'auto_healing_policies' to be a list")
        pulumi.set(__self__, "auto_healing_policies", auto_healing_policies)
        if base_instance_name and not isinstance(base_instance_name, str):
            raise TypeError("Expected argument 'base_instance_name' to be a str")
        pulumi.set(__self__, "base_instance_name", base_instance_name)
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        pulumi.set(__self__, "fingerprint", fingerprint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_group and not isinstance(instance_group, str):
            raise TypeError("Expected argument 'instance_group' to be a str")
        pulumi.set(__self__, "instance_group", instance_group)
        if instance_lifecycle_policies and not isinstance(instance_lifecycle_policies, list):
            raise TypeError("Expected argument 'instance_lifecycle_policies' to be a list")
        pulumi.set(__self__, "instance_lifecycle_policies", instance_lifecycle_policies)
        if list_managed_instances_results and not isinstance(list_managed_instances_results, str):
            raise TypeError("Expected argument 'list_managed_instances_results' to be a str")
        pulumi.set(__self__, "list_managed_instances_results", list_managed_instances_results)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if named_ports and not isinstance(named_ports, list):
            raise TypeError("Expected argument 'named_ports' to be a list")
        pulumi.set(__self__, "named_ports", named_ports)
        if operation and not isinstance(operation, str):
            raise TypeError("Expected argument 'operation' to be a str")
        pulumi.set(__self__, "operation", operation)
        if params and not isinstance(params, list):
            raise TypeError("Expected argument 'params' to be a list")
        pulumi.set(__self__, "params", params)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if standby_policies and not isinstance(standby_policies, list):
            raise TypeError("Expected argument 'standby_policies' to be a list")
        pulumi.set(__self__, "standby_policies", standby_policies)
        if stateful_disks and not isinstance(stateful_disks, list):
            raise TypeError("Expected argument 'stateful_disks' to be a list")
        pulumi.set(__self__, "stateful_disks", stateful_disks)
        if stateful_external_ips and not isinstance(stateful_external_ips, list):
            raise TypeError("Expected argument 'stateful_external_ips' to be a list")
        pulumi.set(__self__, "stateful_external_ips", stateful_external_ips)
        if stateful_internal_ips and not isinstance(stateful_internal_ips, list):
            raise TypeError("Expected argument 'stateful_internal_ips' to be a list")
        pulumi.set(__self__, "stateful_internal_ips", stateful_internal_ips)
        if statuses and not isinstance(statuses, list):
            raise TypeError("Expected argument 'statuses' to be a list")
        pulumi.set(__self__, "statuses", statuses)
        if target_pools and not isinstance(target_pools, list):
            raise TypeError("Expected argument 'target_pools' to be a list")
        pulumi.set(__self__, "target_pools", target_pools)
        if target_size and not isinstance(target_size, int):
            raise TypeError("Expected argument 'target_size' to be a int")
        pulumi.set(__self__, "target_size", target_size)
        if target_stopped_size and not isinstance(target_stopped_size, int):
            raise TypeError("Expected argument 'target_stopped_size' to be a int")
        pulumi.set(__self__, "target_stopped_size", target_stopped_size)
        if target_suspended_size and not isinstance(target_suspended_size, int):
            raise TypeError("Expected argument 'target_suspended_size' to be a int")
        pulumi.set(__self__, "target_suspended_size", target_suspended_size)
        if update_policies and not isinstance(update_policies, list):
            raise TypeError("Expected argument 'update_policies' to be a list")
        pulumi.set(__self__, "update_policies", update_policies)
        if versions and not isinstance(versions, list):
            raise TypeError("Expected argument 'versions' to be a list")
        pulumi.set(__self__, "versions", versions)
        if wait_for_instances and not isinstance(wait_for_instances, bool):
            raise TypeError("Expected argument 'wait_for_instances' to be a bool")
        pulumi.set(__self__, "wait_for_instances", wait_for_instances)
        if wait_for_instances_status and not isinstance(wait_for_instances_status, str):
            raise TypeError("Expected argument 'wait_for_instances_status' to be a str")
        pulumi.set(__self__, "wait_for_instances_status", wait_for_instances_status)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="allInstancesConfigs")
    def all_instances_configs(self) -> Sequence['outputs.GetInstanceGroupManagerAllInstancesConfigResult']:
        return pulumi.get(self, "all_instances_configs")

    @property
    @pulumi.getter(name="autoHealingPolicies")
    def auto_healing_policies(self) -> Sequence['outputs.GetInstanceGroupManagerAutoHealingPolicyResult']:
        return pulumi.get(self, "auto_healing_policies")

    @property
    @pulumi.getter(name="baseInstanceName")
    def base_instance_name(self) -> str:
        return pulumi.get(self, "base_instance_name")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> str:
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def fingerprint(self) -> str:
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceGroup")
    def instance_group(self) -> str:
        return pulumi.get(self, "instance_group")

    @property
    @pulumi.getter(name="instanceLifecyclePolicies")
    def instance_lifecycle_policies(self) -> Sequence['outputs.GetInstanceGroupManagerInstanceLifecyclePolicyResult']:
        return pulumi.get(self, "instance_lifecycle_policies")

    @property
    @pulumi.getter(name="listManagedInstancesResults")
    def list_managed_instances_results(self) -> str:
        return pulumi.get(self, "list_managed_instances_results")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namedPorts")
    def named_ports(self) -> Sequence['outputs.GetInstanceGroupManagerNamedPortResult']:
        return pulumi.get(self, "named_ports")

    @property
    @pulumi.getter
    def operation(self) -> str:
        return pulumi.get(self, "operation")

    @property
    @pulumi.getter
    def params(self) -> Sequence['outputs.GetInstanceGroupManagerParamResult']:
        return pulumi.get(self, "params")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[str]:
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="standbyPolicies")
    def standby_policies(self) -> Sequence['outputs.GetInstanceGroupManagerStandbyPolicyResult']:
        return pulumi.get(self, "standby_policies")

    @property
    @pulumi.getter(name="statefulDisks")
    def stateful_disks(self) -> Sequence['outputs.GetInstanceGroupManagerStatefulDiskResult']:
        return pulumi.get(self, "stateful_disks")

    @property
    @pulumi.getter(name="statefulExternalIps")
    def stateful_external_ips(self) -> Sequence['outputs.GetInstanceGroupManagerStatefulExternalIpResult']:
        return pulumi.get(self, "stateful_external_ips")

    @property
    @pulumi.getter(name="statefulInternalIps")
    def stateful_internal_ips(self) -> Sequence['outputs.GetInstanceGroupManagerStatefulInternalIpResult']:
        return pulumi.get(self, "stateful_internal_ips")

    @property
    @pulumi.getter
    def statuses(self) -> Sequence['outputs.GetInstanceGroupManagerStatusResult']:
        return pulumi.get(self, "statuses")

    @property
    @pulumi.getter(name="targetPools")
    def target_pools(self) -> Sequence[str]:
        return pulumi.get(self, "target_pools")

    @property
    @pulumi.getter(name="targetSize")
    def target_size(self) -> int:
        return pulumi.get(self, "target_size")

    @property
    @pulumi.getter(name="targetStoppedSize")
    def target_stopped_size(self) -> int:
        return pulumi.get(self, "target_stopped_size")

    @property
    @pulumi.getter(name="targetSuspendedSize")
    def target_suspended_size(self) -> int:
        return pulumi.get(self, "target_suspended_size")

    @property
    @pulumi.getter(name="updatePolicies")
    def update_policies(self) -> Sequence['outputs.GetInstanceGroupManagerUpdatePolicyResult']:
        return pulumi.get(self, "update_policies")

    @property
    @pulumi.getter
    def versions(self) -> Sequence['outputs.GetInstanceGroupManagerVersionResult']:
        return pulumi.get(self, "versions")

    @property
    @pulumi.getter(name="waitForInstances")
    def wait_for_instances(self) -> bool:
        return pulumi.get(self, "wait_for_instances")

    @property
    @pulumi.getter(name="waitForInstancesStatus")
    def wait_for_instances_status(self) -> str:
        return pulumi.get(self, "wait_for_instances_status")

    @property
    @pulumi.getter
    def zone(self) -> Optional[str]:
        return pulumi.get(self, "zone")


class AwaitableGetInstanceGroupManagerResult(GetInstanceGroupManagerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceGroupManagerResult(
            all_instances_configs=self.all_instances_configs,
            auto_healing_policies=self.auto_healing_policies,
            base_instance_name=self.base_instance_name,
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            fingerprint=self.fingerprint,
            id=self.id,
            instance_group=self.instance_group,
            instance_lifecycle_policies=self.instance_lifecycle_policies,
            list_managed_instances_results=self.list_managed_instances_results,
            name=self.name,
            named_ports=self.named_ports,
            operation=self.operation,
            params=self.params,
            project=self.project,
            self_link=self.self_link,
            standby_policies=self.standby_policies,
            stateful_disks=self.stateful_disks,
            stateful_external_ips=self.stateful_external_ips,
            stateful_internal_ips=self.stateful_internal_ips,
            statuses=self.statuses,
            target_pools=self.target_pools,
            target_size=self.target_size,
            target_stopped_size=self.target_stopped_size,
            target_suspended_size=self.target_suspended_size,
            update_policies=self.update_policies,
            versions=self.versions,
            wait_for_instances=self.wait_for_instances,
            wait_for_instances_status=self.wait_for_instances_status,
            zone=self.zone)


def get_instance_group_manager(name: Optional[str] = None,
                               project: Optional[str] = None,
                               self_link: Optional[str] = None,
                               zone: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceGroupManagerResult:
    """
    Get a Compute Instance Group Manager within GCE.
    For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups#managed_instance_groups)
    and [API](https://cloud.google.com/compute/docs/reference/latest/instanceGroupManagers)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    igm1 = gcp.compute.get_instance_group_manager(name="my-igm",
        zone="us-central1-a")
    igm2 = gcp.compute.get_instance_group_manager(self_link="https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instanceGroupManagers/my-igm")
    ```


    :param str name: The name of the instance group. Either `name` or `self_link` must be provided.
    :param str project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
    :param str self_link: The self link of the instance group. Either `name` or `self_link` must be provided.
    :param str zone: The zone of the instance group. If referencing the instance group by name and `zone` is not provided, the provider zone is used.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    __args__['selfLink'] = self_link
    __args__['zone'] = zone
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:compute/getInstanceGroupManager:getInstanceGroupManager', __args__, opts=opts, typ=GetInstanceGroupManagerResult).value

    return AwaitableGetInstanceGroupManagerResult(
        all_instances_configs=pulumi.get(__ret__, 'all_instances_configs'),
        auto_healing_policies=pulumi.get(__ret__, 'auto_healing_policies'),
        base_instance_name=pulumi.get(__ret__, 'base_instance_name'),
        creation_timestamp=pulumi.get(__ret__, 'creation_timestamp'),
        description=pulumi.get(__ret__, 'description'),
        fingerprint=pulumi.get(__ret__, 'fingerprint'),
        id=pulumi.get(__ret__, 'id'),
        instance_group=pulumi.get(__ret__, 'instance_group'),
        instance_lifecycle_policies=pulumi.get(__ret__, 'instance_lifecycle_policies'),
        list_managed_instances_results=pulumi.get(__ret__, 'list_managed_instances_results'),
        name=pulumi.get(__ret__, 'name'),
        named_ports=pulumi.get(__ret__, 'named_ports'),
        operation=pulumi.get(__ret__, 'operation'),
        params=pulumi.get(__ret__, 'params'),
        project=pulumi.get(__ret__, 'project'),
        self_link=pulumi.get(__ret__, 'self_link'),
        standby_policies=pulumi.get(__ret__, 'standby_policies'),
        stateful_disks=pulumi.get(__ret__, 'stateful_disks'),
        stateful_external_ips=pulumi.get(__ret__, 'stateful_external_ips'),
        stateful_internal_ips=pulumi.get(__ret__, 'stateful_internal_ips'),
        statuses=pulumi.get(__ret__, 'statuses'),
        target_pools=pulumi.get(__ret__, 'target_pools'),
        target_size=pulumi.get(__ret__, 'target_size'),
        target_stopped_size=pulumi.get(__ret__, 'target_stopped_size'),
        target_suspended_size=pulumi.get(__ret__, 'target_suspended_size'),
        update_policies=pulumi.get(__ret__, 'update_policies'),
        versions=pulumi.get(__ret__, 'versions'),
        wait_for_instances=pulumi.get(__ret__, 'wait_for_instances'),
        wait_for_instances_status=pulumi.get(__ret__, 'wait_for_instances_status'),
        zone=pulumi.get(__ret__, 'zone'))


@_utilities.lift_output_func(get_instance_group_manager)
def get_instance_group_manager_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                                      project: Optional[pulumi.Input[Optional[str]]] = None,
                                      self_link: Optional[pulumi.Input[Optional[str]]] = None,
                                      zone: Optional[pulumi.Input[Optional[str]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceGroupManagerResult]:
    """
    Get a Compute Instance Group Manager within GCE.
    For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups#managed_instance_groups)
    and [API](https://cloud.google.com/compute/docs/reference/latest/instanceGroupManagers)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    igm1 = gcp.compute.get_instance_group_manager(name="my-igm",
        zone="us-central1-a")
    igm2 = gcp.compute.get_instance_group_manager(self_link="https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instanceGroupManagers/my-igm")
    ```


    :param str name: The name of the instance group. Either `name` or `self_link` must be provided.
    :param str project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
    :param str self_link: The self link of the instance group. Either `name` or `self_link` must be provided.
    :param str zone: The zone of the instance group. If referencing the instance group by name and `zone` is not provided, the provider zone is used.
    """
    ...
