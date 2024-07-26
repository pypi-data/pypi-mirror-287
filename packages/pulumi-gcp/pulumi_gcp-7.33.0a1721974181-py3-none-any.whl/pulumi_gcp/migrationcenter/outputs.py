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
    'PreferenceSetVirtualMachinePreferences',
    'PreferenceSetVirtualMachinePreferencesComputeEnginePreferences',
    'PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferences',
    'PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesAllowedMachineSeries',
    'PreferenceSetVirtualMachinePreferencesRegionPreferences',
    'PreferenceSetVirtualMachinePreferencesSoleTenancyPreferences',
    'PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeType',
    'PreferenceSetVirtualMachinePreferencesVmwareEnginePreferences',
]

@pulumi.output_type
class PreferenceSetVirtualMachinePreferences(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "commitmentPlan":
            suggest = "commitment_plan"
        elif key == "computeEnginePreferences":
            suggest = "compute_engine_preferences"
        elif key == "regionPreferences":
            suggest = "region_preferences"
        elif key == "sizingOptimizationStrategy":
            suggest = "sizing_optimization_strategy"
        elif key == "soleTenancyPreferences":
            suggest = "sole_tenancy_preferences"
        elif key == "targetProduct":
            suggest = "target_product"
        elif key == "vmwareEnginePreferences":
            suggest = "vmware_engine_preferences"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PreferenceSetVirtualMachinePreferences. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PreferenceSetVirtualMachinePreferences.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PreferenceSetVirtualMachinePreferences.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 commitment_plan: Optional[str] = None,
                 compute_engine_preferences: Optional['outputs.PreferenceSetVirtualMachinePreferencesComputeEnginePreferences'] = None,
                 region_preferences: Optional['outputs.PreferenceSetVirtualMachinePreferencesRegionPreferences'] = None,
                 sizing_optimization_strategy: Optional[str] = None,
                 sole_tenancy_preferences: Optional['outputs.PreferenceSetVirtualMachinePreferencesSoleTenancyPreferences'] = None,
                 target_product: Optional[str] = None,
                 vmware_engine_preferences: Optional['outputs.PreferenceSetVirtualMachinePreferencesVmwareEnginePreferences'] = None):
        """
        :param str commitment_plan: Commitment plan to consider when calculating costs for virtual machine insights and recommendations. If you are unsure which value to set, a 3 year commitment plan is often a good value to start with.
               Possible values:
               COMMITMENT_PLAN_UNSPECIFIED
               COMMITMENT_PLAN_NONE
               COMMITMENT_PLAN_ONE_YEAR
               COMMITMENT_PLAN_THREE_YEARS
        :param 'PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesArgs' compute_engine_preferences: The user preferences relating to Compute Engine target platform.
               Structure is documented below.
        :param 'PreferenceSetVirtualMachinePreferencesRegionPreferencesArgs' region_preferences: The user preferences relating to target regions.
               Structure is documented below.
        :param str sizing_optimization_strategy: Sizing optimization strategy specifies the preferred strategy used when extrapolating usage data to calculate insights and recommendations for a virtual machine. If you are unsure which value to set, a moderate sizing optimization strategy is often a good value to start with.
               Possible values:
               SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED
               SIZING_OPTIMIZATION_STRATEGY_SAME_AS_SOURCE
               SIZING_OPTIMIZATION_STRATEGY_MODERATE
               SIZING_OPTIMIZATION_STRATEGY_AGGRESSIVE
        :param 'PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesArgs' sole_tenancy_preferences: Preferences concerning Sole Tenancy nodes and VMs.
               Structure is documented below.
        :param str target_product: Target product for assets using this preference set. Specify either target product or business goal, but not both.
               Possible values:
               COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED
               COMPUTE_MIGRATION_TARGET_PRODUCT_COMPUTE_ENGINE
               COMPUTE_MIGRATION_TARGET_PRODUCT_VMWARE_ENGINE
               COMPUTE_MIGRATION_TARGET_PRODUCT_SOLE_TENANCY
        :param 'PreferenceSetVirtualMachinePreferencesVmwareEnginePreferencesArgs' vmware_engine_preferences: The user preferences relating to Google Cloud VMware Engine target platform.
               Structure is documented below.
        """
        if commitment_plan is not None:
            pulumi.set(__self__, "commitment_plan", commitment_plan)
        if compute_engine_preferences is not None:
            pulumi.set(__self__, "compute_engine_preferences", compute_engine_preferences)
        if region_preferences is not None:
            pulumi.set(__self__, "region_preferences", region_preferences)
        if sizing_optimization_strategy is not None:
            pulumi.set(__self__, "sizing_optimization_strategy", sizing_optimization_strategy)
        if sole_tenancy_preferences is not None:
            pulumi.set(__self__, "sole_tenancy_preferences", sole_tenancy_preferences)
        if target_product is not None:
            pulumi.set(__self__, "target_product", target_product)
        if vmware_engine_preferences is not None:
            pulumi.set(__self__, "vmware_engine_preferences", vmware_engine_preferences)

    @property
    @pulumi.getter(name="commitmentPlan")
    def commitment_plan(self) -> Optional[str]:
        """
        Commitment plan to consider when calculating costs for virtual machine insights and recommendations. If you are unsure which value to set, a 3 year commitment plan is often a good value to start with.
        Possible values:
        COMMITMENT_PLAN_UNSPECIFIED
        COMMITMENT_PLAN_NONE
        COMMITMENT_PLAN_ONE_YEAR
        COMMITMENT_PLAN_THREE_YEARS
        """
        return pulumi.get(self, "commitment_plan")

    @property
    @pulumi.getter(name="computeEnginePreferences")
    def compute_engine_preferences(self) -> Optional['outputs.PreferenceSetVirtualMachinePreferencesComputeEnginePreferences']:
        """
        The user preferences relating to Compute Engine target platform.
        Structure is documented below.
        """
        return pulumi.get(self, "compute_engine_preferences")

    @property
    @pulumi.getter(name="regionPreferences")
    def region_preferences(self) -> Optional['outputs.PreferenceSetVirtualMachinePreferencesRegionPreferences']:
        """
        The user preferences relating to target regions.
        Structure is documented below.
        """
        return pulumi.get(self, "region_preferences")

    @property
    @pulumi.getter(name="sizingOptimizationStrategy")
    def sizing_optimization_strategy(self) -> Optional[str]:
        """
        Sizing optimization strategy specifies the preferred strategy used when extrapolating usage data to calculate insights and recommendations for a virtual machine. If you are unsure which value to set, a moderate sizing optimization strategy is often a good value to start with.
        Possible values:
        SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED
        SIZING_OPTIMIZATION_STRATEGY_SAME_AS_SOURCE
        SIZING_OPTIMIZATION_STRATEGY_MODERATE
        SIZING_OPTIMIZATION_STRATEGY_AGGRESSIVE
        """
        return pulumi.get(self, "sizing_optimization_strategy")

    @property
    @pulumi.getter(name="soleTenancyPreferences")
    def sole_tenancy_preferences(self) -> Optional['outputs.PreferenceSetVirtualMachinePreferencesSoleTenancyPreferences']:
        """
        Preferences concerning Sole Tenancy nodes and VMs.
        Structure is documented below.
        """
        return pulumi.get(self, "sole_tenancy_preferences")

    @property
    @pulumi.getter(name="targetProduct")
    def target_product(self) -> Optional[str]:
        """
        Target product for assets using this preference set. Specify either target product or business goal, but not both.
        Possible values:
        COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED
        COMPUTE_MIGRATION_TARGET_PRODUCT_COMPUTE_ENGINE
        COMPUTE_MIGRATION_TARGET_PRODUCT_VMWARE_ENGINE
        COMPUTE_MIGRATION_TARGET_PRODUCT_SOLE_TENANCY
        """
        return pulumi.get(self, "target_product")

    @property
    @pulumi.getter(name="vmwareEnginePreferences")
    def vmware_engine_preferences(self) -> Optional['outputs.PreferenceSetVirtualMachinePreferencesVmwareEnginePreferences']:
        """
        The user preferences relating to Google Cloud VMware Engine target platform.
        Structure is documented below.
        """
        return pulumi.get(self, "vmware_engine_preferences")


@pulumi.output_type
class PreferenceSetVirtualMachinePreferencesComputeEnginePreferences(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "licenseType":
            suggest = "license_type"
        elif key == "machinePreferences":
            suggest = "machine_preferences"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PreferenceSetVirtualMachinePreferencesComputeEnginePreferences. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PreferenceSetVirtualMachinePreferencesComputeEnginePreferences.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PreferenceSetVirtualMachinePreferencesComputeEnginePreferences.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 license_type: Optional[str] = None,
                 machine_preferences: Optional['outputs.PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferences'] = None):
        """
        :param str license_type: License type to consider when calculating costs for virtual machine insights and recommendations. If unspecified, costs are calculated based on the default licensing plan.
               Possible values:
               LICENSE_TYPE_UNSPECIFIED
               LICENSE_TYPE_DEFAULT
               LICENSE_TYPE_BRING_YOUR_OWN_LICENSE
        :param 'PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesArgs' machine_preferences: The type of machines to consider when calculating virtual machine migration insights and recommendations. Not all machine types are available in all zones and regions.
               Structure is documented below.
        """
        if license_type is not None:
            pulumi.set(__self__, "license_type", license_type)
        if machine_preferences is not None:
            pulumi.set(__self__, "machine_preferences", machine_preferences)

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[str]:
        """
        License type to consider when calculating costs for virtual machine insights and recommendations. If unspecified, costs are calculated based on the default licensing plan.
        Possible values:
        LICENSE_TYPE_UNSPECIFIED
        LICENSE_TYPE_DEFAULT
        LICENSE_TYPE_BRING_YOUR_OWN_LICENSE
        """
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter(name="machinePreferences")
    def machine_preferences(self) -> Optional['outputs.PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferences']:
        """
        The type of machines to consider when calculating virtual machine migration insights and recommendations. Not all machine types are available in all zones and regions.
        Structure is documented below.
        """
        return pulumi.get(self, "machine_preferences")


@pulumi.output_type
class PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferences(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowedMachineSeries":
            suggest = "allowed_machine_series"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferences. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferences.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferences.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allowed_machine_series: Optional[Sequence['outputs.PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesAllowedMachineSeries']] = None):
        """
        :param Sequence['PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesAllowedMachineSeriesArgs'] allowed_machine_series: Compute Engine machine series to consider for insights and recommendations. If empty, no restriction is applied on the machine series.
               Structure is documented below.
        """
        if allowed_machine_series is not None:
            pulumi.set(__self__, "allowed_machine_series", allowed_machine_series)

    @property
    @pulumi.getter(name="allowedMachineSeries")
    def allowed_machine_series(self) -> Optional[Sequence['outputs.PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesAllowedMachineSeries']]:
        """
        Compute Engine machine series to consider for insights and recommendations. If empty, no restriction is applied on the machine series.
        Structure is documented below.
        """
        return pulumi.get(self, "allowed_machine_series")


@pulumi.output_type
class PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesAllowedMachineSeries(dict):
    def __init__(__self__, *,
                 code: Optional[str] = None):
        """
        :param str code: Code to identify a Compute Engine machine series. Consult https://cloud.google.com/compute/docs/machine-resource#machine_type_comparison for more details on the available series.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)

    @property
    @pulumi.getter
    def code(self) -> Optional[str]:
        """
        Code to identify a Compute Engine machine series. Consult https://cloud.google.com/compute/docs/machine-resource#machine_type_comparison for more details on the available series.
        """
        return pulumi.get(self, "code")


@pulumi.output_type
class PreferenceSetVirtualMachinePreferencesRegionPreferences(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "preferredRegions":
            suggest = "preferred_regions"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PreferenceSetVirtualMachinePreferencesRegionPreferences. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PreferenceSetVirtualMachinePreferencesRegionPreferences.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PreferenceSetVirtualMachinePreferencesRegionPreferences.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 preferred_regions: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] preferred_regions: A list of preferred regions, ordered by the most preferred region first. Set only valid Google Cloud region names. See https://cloud.google.com/compute/docs/regions-zones for available regions.
        """
        if preferred_regions is not None:
            pulumi.set(__self__, "preferred_regions", preferred_regions)

    @property
    @pulumi.getter(name="preferredRegions")
    def preferred_regions(self) -> Optional[Sequence[str]]:
        """
        A list of preferred regions, ordered by the most preferred region first. Set only valid Google Cloud region names. See https://cloud.google.com/compute/docs/regions-zones for available regions.
        """
        return pulumi.get(self, "preferred_regions")


@pulumi.output_type
class PreferenceSetVirtualMachinePreferencesSoleTenancyPreferences(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "commitmentPlan":
            suggest = "commitment_plan"
        elif key == "cpuOvercommitRatio":
            suggest = "cpu_overcommit_ratio"
        elif key == "hostMaintenancePolicy":
            suggest = "host_maintenance_policy"
        elif key == "nodeTypes":
            suggest = "node_types"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PreferenceSetVirtualMachinePreferencesSoleTenancyPreferences. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PreferenceSetVirtualMachinePreferencesSoleTenancyPreferences.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PreferenceSetVirtualMachinePreferencesSoleTenancyPreferences.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 commitment_plan: Optional[str] = None,
                 cpu_overcommit_ratio: Optional[float] = None,
                 host_maintenance_policy: Optional[str] = None,
                 node_types: Optional[Sequence['outputs.PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeType']] = None):
        """
        :param str commitment_plan: Commitment plan to consider when calculating costs for virtual machine insights and recommendations. If you are unsure which value to set, a 3 year commitment plan is often a good value to start with.
               Possible values:
               COMMITMENT_PLAN_UNSPECIFIED
               ON_DEMAND
               COMMITMENT_1_YEAR
               COMMITMENT_3_YEAR
        :param float cpu_overcommit_ratio: CPU overcommit ratio. Acceptable values are between 1.0 and 2.0 inclusive.
        :param str host_maintenance_policy: Sole Tenancy nodes maintenance policy.
               Possible values:
               HOST_MAINTENANCE_POLICY_UNSPECIFIED
               HOST_MAINTENANCE_POLICY_DEFAULT
               HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE
               HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP
        :param Sequence['PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeTypeArgs'] node_types: A list of sole tenant node types. An empty list means that all possible node types will be considered.
               Structure is documented below.
        """
        if commitment_plan is not None:
            pulumi.set(__self__, "commitment_plan", commitment_plan)
        if cpu_overcommit_ratio is not None:
            pulumi.set(__self__, "cpu_overcommit_ratio", cpu_overcommit_ratio)
        if host_maintenance_policy is not None:
            pulumi.set(__self__, "host_maintenance_policy", host_maintenance_policy)
        if node_types is not None:
            pulumi.set(__self__, "node_types", node_types)

    @property
    @pulumi.getter(name="commitmentPlan")
    def commitment_plan(self) -> Optional[str]:
        """
        Commitment plan to consider when calculating costs for virtual machine insights and recommendations. If you are unsure which value to set, a 3 year commitment plan is often a good value to start with.
        Possible values:
        COMMITMENT_PLAN_UNSPECIFIED
        ON_DEMAND
        COMMITMENT_1_YEAR
        COMMITMENT_3_YEAR
        """
        return pulumi.get(self, "commitment_plan")

    @property
    @pulumi.getter(name="cpuOvercommitRatio")
    def cpu_overcommit_ratio(self) -> Optional[float]:
        """
        CPU overcommit ratio. Acceptable values are between 1.0 and 2.0 inclusive.
        """
        return pulumi.get(self, "cpu_overcommit_ratio")

    @property
    @pulumi.getter(name="hostMaintenancePolicy")
    def host_maintenance_policy(self) -> Optional[str]:
        """
        Sole Tenancy nodes maintenance policy.
        Possible values:
        HOST_MAINTENANCE_POLICY_UNSPECIFIED
        HOST_MAINTENANCE_POLICY_DEFAULT
        HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE
        HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP
        """
        return pulumi.get(self, "host_maintenance_policy")

    @property
    @pulumi.getter(name="nodeTypes")
    def node_types(self) -> Optional[Sequence['outputs.PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeType']]:
        """
        A list of sole tenant node types. An empty list means that all possible node types will be considered.
        Structure is documented below.
        """
        return pulumi.get(self, "node_types")


@pulumi.output_type
class PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeType(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "nodeName":
            suggest = "node_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeType. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeType.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeType.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 node_name: Optional[str] = None):
        """
        :param str node_name: Name of the Sole Tenant node. Consult https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes
        """
        if node_name is not None:
            pulumi.set(__self__, "node_name", node_name)

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[str]:
        """
        Name of the Sole Tenant node. Consult https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes
        """
        return pulumi.get(self, "node_name")


@pulumi.output_type
class PreferenceSetVirtualMachinePreferencesVmwareEnginePreferences(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "commitmentPlan":
            suggest = "commitment_plan"
        elif key == "cpuOvercommitRatio":
            suggest = "cpu_overcommit_ratio"
        elif key == "memoryOvercommitRatio":
            suggest = "memory_overcommit_ratio"
        elif key == "storageDeduplicationCompressionRatio":
            suggest = "storage_deduplication_compression_ratio"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PreferenceSetVirtualMachinePreferencesVmwareEnginePreferences. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PreferenceSetVirtualMachinePreferencesVmwareEnginePreferences.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PreferenceSetVirtualMachinePreferencesVmwareEnginePreferences.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 commitment_plan: Optional[str] = None,
                 cpu_overcommit_ratio: Optional[float] = None,
                 memory_overcommit_ratio: Optional[float] = None,
                 storage_deduplication_compression_ratio: Optional[float] = None):
        """
        :param str commitment_plan: Commitment plan to consider when calculating costs for virtual machine insights and recommendations. If you are unsure which value to set, a 3 year commitment plan is often a good value to start with.
               Possible values:
               COMMITMENT_PLAN_UNSPECIFIED
               ON_DEMAND
               COMMITMENT_1_YEAR_MONTHLY_PAYMENTS
               COMMITMENT_3_YEAR_MONTHLY_PAYMENTS
               COMMITMENT_1_YEAR_UPFRONT_PAYMENT
               COMMITMENT_3_YEAR_UPFRONT_PAYMENT
        :param float cpu_overcommit_ratio: CPU overcommit ratio. Acceptable values are between 1.0 and 8.0, with 0.1 increment.
        :param float memory_overcommit_ratio: Memory overcommit ratio. Acceptable values are 1.0, 1.25, 1.5, 1.75 and 2.0.
        :param float storage_deduplication_compression_ratio: The Deduplication and Compression ratio is based on the logical (Used Before) space required to store data before applying deduplication and compression, in relation to the physical (Used After) space required after applying deduplication and compression. Specifically, the ratio is the Used Before space divided by the Used After space. For example, if the Used Before space is 3 GB, but the physical Used After space is 1 GB, the deduplication and compression ratio is 3x. Acceptable values are between 1.0 and 4.0.
        """
        if commitment_plan is not None:
            pulumi.set(__self__, "commitment_plan", commitment_plan)
        if cpu_overcommit_ratio is not None:
            pulumi.set(__self__, "cpu_overcommit_ratio", cpu_overcommit_ratio)
        if memory_overcommit_ratio is not None:
            pulumi.set(__self__, "memory_overcommit_ratio", memory_overcommit_ratio)
        if storage_deduplication_compression_ratio is not None:
            pulumi.set(__self__, "storage_deduplication_compression_ratio", storage_deduplication_compression_ratio)

    @property
    @pulumi.getter(name="commitmentPlan")
    def commitment_plan(self) -> Optional[str]:
        """
        Commitment plan to consider when calculating costs for virtual machine insights and recommendations. If you are unsure which value to set, a 3 year commitment plan is often a good value to start with.
        Possible values:
        COMMITMENT_PLAN_UNSPECIFIED
        ON_DEMAND
        COMMITMENT_1_YEAR_MONTHLY_PAYMENTS
        COMMITMENT_3_YEAR_MONTHLY_PAYMENTS
        COMMITMENT_1_YEAR_UPFRONT_PAYMENT
        COMMITMENT_3_YEAR_UPFRONT_PAYMENT
        """
        return pulumi.get(self, "commitment_plan")

    @property
    @pulumi.getter(name="cpuOvercommitRatio")
    def cpu_overcommit_ratio(self) -> Optional[float]:
        """
        CPU overcommit ratio. Acceptable values are between 1.0 and 8.0, with 0.1 increment.
        """
        return pulumi.get(self, "cpu_overcommit_ratio")

    @property
    @pulumi.getter(name="memoryOvercommitRatio")
    def memory_overcommit_ratio(self) -> Optional[float]:
        """
        Memory overcommit ratio. Acceptable values are 1.0, 1.25, 1.5, 1.75 and 2.0.
        """
        return pulumi.get(self, "memory_overcommit_ratio")

    @property
    @pulumi.getter(name="storageDeduplicationCompressionRatio")
    def storage_deduplication_compression_ratio(self) -> Optional[float]:
        """
        The Deduplication and Compression ratio is based on the logical (Used Before) space required to store data before applying deduplication and compression, in relation to the physical (Used After) space required after applying deduplication and compression. Specifically, the ratio is the Used Before space divided by the Used After space. For example, if the Used Before space is 3 GB, but the physical Used After space is 1 GB, the deduplication and compression ratio is 3x. Acceptable values are between 1.0 and 4.0.
        """
        return pulumi.get(self, "storage_deduplication_compression_ratio")


