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
    'WorkloadComplianceStatus',
    'WorkloadEkmProvisioningResponse',
    'WorkloadKmsSettings',
    'WorkloadPartnerPermissions',
    'WorkloadResource',
    'WorkloadResourceSetting',
    'WorkloadSaaEnrollmentResponse',
]

@pulumi.output_type
class WorkloadComplianceStatus(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "acknowledgedViolationCounts":
            suggest = "acknowledged_violation_counts"
        elif key == "activeViolationCounts":
            suggest = "active_violation_counts"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkloadComplianceStatus. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkloadComplianceStatus.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkloadComplianceStatus.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 acknowledged_violation_counts: Optional[Sequence[int]] = None,
                 active_violation_counts: Optional[Sequence[int]] = None):
        """
        :param Sequence[int] acknowledged_violation_counts: Number of current orgPolicy violations which are acknowledged.
        :param Sequence[int] active_violation_counts: Number of current orgPolicy violations which are not acknowledged.
        """
        if acknowledged_violation_counts is not None:
            pulumi.set(__self__, "acknowledged_violation_counts", acknowledged_violation_counts)
        if active_violation_counts is not None:
            pulumi.set(__self__, "active_violation_counts", active_violation_counts)

    @property
    @pulumi.getter(name="acknowledgedViolationCounts")
    def acknowledged_violation_counts(self) -> Optional[Sequence[int]]:
        """
        Number of current orgPolicy violations which are acknowledged.
        """
        return pulumi.get(self, "acknowledged_violation_counts")

    @property
    @pulumi.getter(name="activeViolationCounts")
    def active_violation_counts(self) -> Optional[Sequence[int]]:
        """
        Number of current orgPolicy violations which are not acknowledged.
        """
        return pulumi.get(self, "active_violation_counts")


@pulumi.output_type
class WorkloadEkmProvisioningResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ekmProvisioningErrorDomain":
            suggest = "ekm_provisioning_error_domain"
        elif key == "ekmProvisioningErrorMapping":
            suggest = "ekm_provisioning_error_mapping"
        elif key == "ekmProvisioningState":
            suggest = "ekm_provisioning_state"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkloadEkmProvisioningResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkloadEkmProvisioningResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkloadEkmProvisioningResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 ekm_provisioning_error_domain: Optional[str] = None,
                 ekm_provisioning_error_mapping: Optional[str] = None,
                 ekm_provisioning_state: Optional[str] = None):
        """
        :param str ekm_provisioning_error_domain: Indicates Ekm provisioning error if any. Possible values: EKM_PROVISIONING_ERROR_DOMAIN_UNSPECIFIED, UNSPECIFIED_ERROR, GOOGLE_SERVER_ERROR, EXTERNAL_USER_ERROR, EXTERNAL_PARTNER_ERROR, TIMEOUT_ERROR
        :param str ekm_provisioning_error_mapping: Detailed error message if Ekm provisioning fails Possible values: EKM_PROVISIONING_ERROR_MAPPING_UNSPECIFIED, INVALID_SERVICE_ACCOUNT, MISSING_METRICS_SCOPE_ADMIN_PERMISSION, MISSING_EKM_CONNECTION_ADMIN_PERMISSION
        :param str ekm_provisioning_state: Indicates Ekm enrollment Provisioning of a given workload. Possible values: EKM_PROVISIONING_STATE_UNSPECIFIED, EKM_PROVISIONING_STATE_PENDING, EKM_PROVISIONING_STATE_FAILED, EKM_PROVISIONING_STATE_COMPLETED
        """
        if ekm_provisioning_error_domain is not None:
            pulumi.set(__self__, "ekm_provisioning_error_domain", ekm_provisioning_error_domain)
        if ekm_provisioning_error_mapping is not None:
            pulumi.set(__self__, "ekm_provisioning_error_mapping", ekm_provisioning_error_mapping)
        if ekm_provisioning_state is not None:
            pulumi.set(__self__, "ekm_provisioning_state", ekm_provisioning_state)

    @property
    @pulumi.getter(name="ekmProvisioningErrorDomain")
    def ekm_provisioning_error_domain(self) -> Optional[str]:
        """
        Indicates Ekm provisioning error if any. Possible values: EKM_PROVISIONING_ERROR_DOMAIN_UNSPECIFIED, UNSPECIFIED_ERROR, GOOGLE_SERVER_ERROR, EXTERNAL_USER_ERROR, EXTERNAL_PARTNER_ERROR, TIMEOUT_ERROR
        """
        return pulumi.get(self, "ekm_provisioning_error_domain")

    @property
    @pulumi.getter(name="ekmProvisioningErrorMapping")
    def ekm_provisioning_error_mapping(self) -> Optional[str]:
        """
        Detailed error message if Ekm provisioning fails Possible values: EKM_PROVISIONING_ERROR_MAPPING_UNSPECIFIED, INVALID_SERVICE_ACCOUNT, MISSING_METRICS_SCOPE_ADMIN_PERMISSION, MISSING_EKM_CONNECTION_ADMIN_PERMISSION
        """
        return pulumi.get(self, "ekm_provisioning_error_mapping")

    @property
    @pulumi.getter(name="ekmProvisioningState")
    def ekm_provisioning_state(self) -> Optional[str]:
        """
        Indicates Ekm enrollment Provisioning of a given workload. Possible values: EKM_PROVISIONING_STATE_UNSPECIFIED, EKM_PROVISIONING_STATE_PENDING, EKM_PROVISIONING_STATE_FAILED, EKM_PROVISIONING_STATE_COMPLETED
        """
        return pulumi.get(self, "ekm_provisioning_state")


@pulumi.output_type
class WorkloadKmsSettings(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "nextRotationTime":
            suggest = "next_rotation_time"
        elif key == "rotationPeriod":
            suggest = "rotation_period"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkloadKmsSettings. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkloadKmsSettings.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkloadKmsSettings.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 next_rotation_time: str,
                 rotation_period: str):
        """
        :param str next_rotation_time: Required. Input only. Immutable. The time at which the Key Management Service will automatically create a new version of the crypto key and mark it as the primary.
        :param str rotation_period: Required. Input only. Immutable. will be advanced by this period when the Key Management Service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours.
        """
        pulumi.set(__self__, "next_rotation_time", next_rotation_time)
        pulumi.set(__self__, "rotation_period", rotation_period)

    @property
    @pulumi.getter(name="nextRotationTime")
    def next_rotation_time(self) -> str:
        """
        Required. Input only. Immutable. The time at which the Key Management Service will automatically create a new version of the crypto key and mark it as the primary.
        """
        return pulumi.get(self, "next_rotation_time")

    @property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> str:
        """
        Required. Input only. Immutable. will be advanced by this period when the Key Management Service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours.
        """
        return pulumi.get(self, "rotation_period")


@pulumi.output_type
class WorkloadPartnerPermissions(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "assuredWorkloadsMonitoring":
            suggest = "assured_workloads_monitoring"
        elif key == "dataLogsViewer":
            suggest = "data_logs_viewer"
        elif key == "serviceAccessApprover":
            suggest = "service_access_approver"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkloadPartnerPermissions. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkloadPartnerPermissions.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkloadPartnerPermissions.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 assured_workloads_monitoring: Optional[bool] = None,
                 data_logs_viewer: Optional[bool] = None,
                 service_access_approver: Optional[bool] = None):
        """
        :param bool assured_workloads_monitoring: Optional. Allow partner to view violation alerts.
        :param bool data_logs_viewer: Allow the partner to view inspectability logs and monitoring violations.
        :param bool service_access_approver: Optional. Allow partner to view access approval logs.
        """
        if assured_workloads_monitoring is not None:
            pulumi.set(__self__, "assured_workloads_monitoring", assured_workloads_monitoring)
        if data_logs_viewer is not None:
            pulumi.set(__self__, "data_logs_viewer", data_logs_viewer)
        if service_access_approver is not None:
            pulumi.set(__self__, "service_access_approver", service_access_approver)

    @property
    @pulumi.getter(name="assuredWorkloadsMonitoring")
    def assured_workloads_monitoring(self) -> Optional[bool]:
        """
        Optional. Allow partner to view violation alerts.
        """
        return pulumi.get(self, "assured_workloads_monitoring")

    @property
    @pulumi.getter(name="dataLogsViewer")
    def data_logs_viewer(self) -> Optional[bool]:
        """
        Allow the partner to view inspectability logs and monitoring violations.
        """
        return pulumi.get(self, "data_logs_viewer")

    @property
    @pulumi.getter(name="serviceAccessApprover")
    def service_access_approver(self) -> Optional[bool]:
        """
        Optional. Allow partner to view access approval logs.
        """
        return pulumi.get(self, "service_access_approver")


@pulumi.output_type
class WorkloadResource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "resourceId":
            suggest = "resource_id"
        elif key == "resourceType":
            suggest = "resource_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkloadResource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkloadResource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkloadResource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 resource_id: Optional[int] = None,
                 resource_type: Optional[str] = None):
        """
        :param int resource_id: Resource identifier. For a project this represents project_number.
        :param str resource_type: Indicates the type of resource. Possible values: RESOURCE_TYPE_UNSPECIFIED, CONSUMER_PROJECT, ENCRYPTION_KEYS_PROJECT, KEYRING, CONSUMER_FOLDER
        """
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if resource_type is not None:
            pulumi.set(__self__, "resource_type", resource_type)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[int]:
        """
        Resource identifier. For a project this represents project_number.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[str]:
        """
        Indicates the type of resource. Possible values: RESOURCE_TYPE_UNSPECIFIED, CONSUMER_PROJECT, ENCRYPTION_KEYS_PROJECT, KEYRING, CONSUMER_FOLDER
        """
        return pulumi.get(self, "resource_type")


@pulumi.output_type
class WorkloadResourceSetting(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "displayName":
            suggest = "display_name"
        elif key == "resourceId":
            suggest = "resource_id"
        elif key == "resourceType":
            suggest = "resource_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkloadResourceSetting. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkloadResourceSetting.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkloadResourceSetting.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 display_name: Optional[str] = None,
                 resource_id: Optional[str] = None,
                 resource_type: Optional[str] = None):
        """
        :param str display_name: User-assigned resource display name. If not empty it will be used to create a resource with the specified name.
        :param str resource_id: Resource identifier. For a project this represents projectId. If the project is already taken, the workload creation will fail. For KeyRing, this represents the keyring_id. For a folder, don't set this value as folder_id is assigned by Google.
        :param str resource_type: Indicates the type of resource. This field should be specified to correspond the id to the right project type (CONSUMER_PROJECT or ENCRYPTION_KEYS_PROJECT) Possible values: RESOURCE_TYPE_UNSPECIFIED, CONSUMER_PROJECT, ENCRYPTION_KEYS_PROJECT, KEYRING, CONSUMER_FOLDER
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if resource_type is not None:
            pulumi.set(__self__, "resource_type", resource_type)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        User-assigned resource display name. If not empty it will be used to create a resource with the specified name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        """
        Resource identifier. For a project this represents projectId. If the project is already taken, the workload creation will fail. For KeyRing, this represents the keyring_id. For a folder, don't set this value as folder_id is assigned by Google.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[str]:
        """
        Indicates the type of resource. This field should be specified to correspond the id to the right project type (CONSUMER_PROJECT or ENCRYPTION_KEYS_PROJECT) Possible values: RESOURCE_TYPE_UNSPECIFIED, CONSUMER_PROJECT, ENCRYPTION_KEYS_PROJECT, KEYRING, CONSUMER_FOLDER
        """
        return pulumi.get(self, "resource_type")


@pulumi.output_type
class WorkloadSaaEnrollmentResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "setupErrors":
            suggest = "setup_errors"
        elif key == "setupStatus":
            suggest = "setup_status"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkloadSaaEnrollmentResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkloadSaaEnrollmentResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkloadSaaEnrollmentResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 setup_errors: Optional[Sequence[str]] = None,
                 setup_status: Optional[str] = None):
        """
        :param Sequence[str] setup_errors: Indicates SAA enrollment setup error if any.
        :param str setup_status: Indicates SAA enrollment status of a given workload. Possible values: SETUP_STATE_UNSPECIFIED, STATUS_PENDING, STATUS_COMPLETE
        """
        if setup_errors is not None:
            pulumi.set(__self__, "setup_errors", setup_errors)
        if setup_status is not None:
            pulumi.set(__self__, "setup_status", setup_status)

    @property
    @pulumi.getter(name="setupErrors")
    def setup_errors(self) -> Optional[Sequence[str]]:
        """
        Indicates SAA enrollment setup error if any.
        """
        return pulumi.get(self, "setup_errors")

    @property
    @pulumi.getter(name="setupStatus")
    def setup_status(self) -> Optional[str]:
        """
        Indicates SAA enrollment status of a given workload. Possible values: SETUP_STATE_UNSPECIFIED, STATUS_PENDING, STATUS_COMPLETE
        """
        return pulumi.get(self, "setup_status")


