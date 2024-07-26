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

__all__ = ['FolderSettingsArgs', 'FolderSettings']

@pulumi.input_type
class FolderSettingsArgs:
    def __init__(__self__, *,
                 folder: pulumi.Input[str],
                 disable_default_sink: Optional[pulumi.Input[bool]] = None,
                 kms_key_name: Optional[pulumi.Input[str]] = None,
                 storage_location: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FolderSettings resource.
        :param pulumi.Input[str] folder: The folder for which to retrieve settings.
               
               
               - - -
        :param pulumi.Input[bool] disable_default_sink: If set to true, the _Default sink in newly created projects and folders will created in a disabled state. This can be used to automatically disable log storage if there is already an aggregated sink configured in the hierarchy. The _Default sink can be re-enabled manually if needed.
        :param pulumi.Input[str] kms_key_name: The resource name for the configured Cloud KMS key.
        :param pulumi.Input[str] storage_location: The storage location that Cloud Logging will use to create new resources when a location is needed but not explicitly provided.
        """
        pulumi.set(__self__, "folder", folder)
        if disable_default_sink is not None:
            pulumi.set(__self__, "disable_default_sink", disable_default_sink)
        if kms_key_name is not None:
            pulumi.set(__self__, "kms_key_name", kms_key_name)
        if storage_location is not None:
            pulumi.set(__self__, "storage_location", storage_location)

    @property
    @pulumi.getter
    def folder(self) -> pulumi.Input[str]:
        """
        The folder for which to retrieve settings.


        - - -
        """
        return pulumi.get(self, "folder")

    @folder.setter
    def folder(self, value: pulumi.Input[str]):
        pulumi.set(self, "folder", value)

    @property
    @pulumi.getter(name="disableDefaultSink")
    def disable_default_sink(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to true, the _Default sink in newly created projects and folders will created in a disabled state. This can be used to automatically disable log storage if there is already an aggregated sink configured in the hierarchy. The _Default sink can be re-enabled manually if needed.
        """
        return pulumi.get(self, "disable_default_sink")

    @disable_default_sink.setter
    def disable_default_sink(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_default_sink", value)

    @property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name for the configured Cloud KMS key.
        """
        return pulumi.get(self, "kms_key_name")

    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_name", value)

    @property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> Optional[pulumi.Input[str]]:
        """
        The storage location that Cloud Logging will use to create new resources when a location is needed but not explicitly provided.
        """
        return pulumi.get(self, "storage_location")

    @storage_location.setter
    def storage_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_location", value)


@pulumi.input_type
class _FolderSettingsState:
    def __init__(__self__, *,
                 disable_default_sink: Optional[pulumi.Input[bool]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 kms_key_name: Optional[pulumi.Input[str]] = None,
                 kms_service_account_id: Optional[pulumi.Input[str]] = None,
                 logging_service_account_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage_location: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FolderSettings resources.
        :param pulumi.Input[bool] disable_default_sink: If set to true, the _Default sink in newly created projects and folders will created in a disabled state. This can be used to automatically disable log storage if there is already an aggregated sink configured in the hierarchy. The _Default sink can be re-enabled manually if needed.
        :param pulumi.Input[str] folder: The folder for which to retrieve settings.
               
               
               - - -
        :param pulumi.Input[str] kms_key_name: The resource name for the configured Cloud KMS key.
        :param pulumi.Input[str] kms_service_account_id: The service account that will be used by the Log Router to access your Cloud KMS key.
        :param pulumi.Input[str] logging_service_account_id: The service account for the given container. Sinks use this service account as their writerIdentity if no custom service account is provided.
        :param pulumi.Input[str] name: The resource name of the settings.
        :param pulumi.Input[str] storage_location: The storage location that Cloud Logging will use to create new resources when a location is needed but not explicitly provided.
        """
        if disable_default_sink is not None:
            pulumi.set(__self__, "disable_default_sink", disable_default_sink)
        if folder is not None:
            pulumi.set(__self__, "folder", folder)
        if kms_key_name is not None:
            pulumi.set(__self__, "kms_key_name", kms_key_name)
        if kms_service_account_id is not None:
            pulumi.set(__self__, "kms_service_account_id", kms_service_account_id)
        if logging_service_account_id is not None:
            pulumi.set(__self__, "logging_service_account_id", logging_service_account_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if storage_location is not None:
            pulumi.set(__self__, "storage_location", storage_location)

    @property
    @pulumi.getter(name="disableDefaultSink")
    def disable_default_sink(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to true, the _Default sink in newly created projects and folders will created in a disabled state. This can be used to automatically disable log storage if there is already an aggregated sink configured in the hierarchy. The _Default sink can be re-enabled manually if needed.
        """
        return pulumi.get(self, "disable_default_sink")

    @disable_default_sink.setter
    def disable_default_sink(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_default_sink", value)

    @property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[str]]:
        """
        The folder for which to retrieve settings.


        - - -
        """
        return pulumi.get(self, "folder")

    @folder.setter
    def folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder", value)

    @property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name for the configured Cloud KMS key.
        """
        return pulumi.get(self, "kms_key_name")

    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_name", value)

    @property
    @pulumi.getter(name="kmsServiceAccountId")
    def kms_service_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The service account that will be used by the Log Router to access your Cloud KMS key.
        """
        return pulumi.get(self, "kms_service_account_id")

    @kms_service_account_id.setter
    def kms_service_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_service_account_id", value)

    @property
    @pulumi.getter(name="loggingServiceAccountId")
    def logging_service_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The service account for the given container. Sinks use this service account as their writerIdentity if no custom service account is provided.
        """
        return pulumi.get(self, "logging_service_account_id")

    @logging_service_account_id.setter
    def logging_service_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logging_service_account_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the settings.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> Optional[pulumi.Input[str]]:
        """
        The storage location that Cloud Logging will use to create new resources when a location is needed but not explicitly provided.
        """
        return pulumi.get(self, "storage_location")

    @storage_location.setter
    def storage_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_location", value)


class FolderSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disable_default_sink: Optional[pulumi.Input[bool]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 kms_key_name: Optional[pulumi.Input[str]] = None,
                 storage_location: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Default resource settings control whether CMEK is required for new log buckets. These settings also determine the storage location for the _Default and _Required log buckets, and whether the _Default sink is enabled or disabled.

        To get more information about FolderSettings, see:

        * [API documentation](https://cloud.google.com/logging/docs/reference/v2/rest/v2/TopLevel/getSettings)
        * How-to Guides
            * [Configure default settings for organizations and folders](https://cloud.google.com/logging/docs/default-settings)

        ## Example Usage

        ### Logging Folder Settings All

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_folder = gcp.organizations.Folder("my_folder",
            display_name="folder-name",
            parent="organizations/123456789")
        settings = gcp.logging.get_folder_settings_output(folder=my_folder.folder_id)
        iam = gcp.kms.CryptoKeyIAMMember("iam",
            crypto_key_id="kms-key",
            role="roles/cloudkms.cryptoKeyEncrypterDecrypter",
            member=settings.apply(lambda settings: f"serviceAccount:{settings.kms_service_account_id}"))
        example = gcp.logging.FolderSettings("example",
            disable_default_sink=True,
            folder=my_folder.folder_id,
            kms_key_name="kms-key",
            storage_location="us-central1",
            opts = pulumi.ResourceOptions(depends_on=[iam]))
        ```

        ## Import

        FolderSettings can be imported using any of these accepted formats:

        * `folders/{{folder}}/settings`

        * `{{folder}}`

        When using the `pulumi import` command, FolderSettings can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:logging/folderSettings:FolderSettings default folders/{{folder}}/settings
        ```

        ```sh
        $ pulumi import gcp:logging/folderSettings:FolderSettings default {{folder}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] disable_default_sink: If set to true, the _Default sink in newly created projects and folders will created in a disabled state. This can be used to automatically disable log storage if there is already an aggregated sink configured in the hierarchy. The _Default sink can be re-enabled manually if needed.
        :param pulumi.Input[str] folder: The folder for which to retrieve settings.
               
               
               - - -
        :param pulumi.Input[str] kms_key_name: The resource name for the configured Cloud KMS key.
        :param pulumi.Input[str] storage_location: The storage location that Cloud Logging will use to create new resources when a location is needed but not explicitly provided.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FolderSettingsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Default resource settings control whether CMEK is required for new log buckets. These settings also determine the storage location for the _Default and _Required log buckets, and whether the _Default sink is enabled or disabled.

        To get more information about FolderSettings, see:

        * [API documentation](https://cloud.google.com/logging/docs/reference/v2/rest/v2/TopLevel/getSettings)
        * How-to Guides
            * [Configure default settings for organizations and folders](https://cloud.google.com/logging/docs/default-settings)

        ## Example Usage

        ### Logging Folder Settings All

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_folder = gcp.organizations.Folder("my_folder",
            display_name="folder-name",
            parent="organizations/123456789")
        settings = gcp.logging.get_folder_settings_output(folder=my_folder.folder_id)
        iam = gcp.kms.CryptoKeyIAMMember("iam",
            crypto_key_id="kms-key",
            role="roles/cloudkms.cryptoKeyEncrypterDecrypter",
            member=settings.apply(lambda settings: f"serviceAccount:{settings.kms_service_account_id}"))
        example = gcp.logging.FolderSettings("example",
            disable_default_sink=True,
            folder=my_folder.folder_id,
            kms_key_name="kms-key",
            storage_location="us-central1",
            opts = pulumi.ResourceOptions(depends_on=[iam]))
        ```

        ## Import

        FolderSettings can be imported using any of these accepted formats:

        * `folders/{{folder}}/settings`

        * `{{folder}}`

        When using the `pulumi import` command, FolderSettings can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:logging/folderSettings:FolderSettings default folders/{{folder}}/settings
        ```

        ```sh
        $ pulumi import gcp:logging/folderSettings:FolderSettings default {{folder}}
        ```

        :param str resource_name: The name of the resource.
        :param FolderSettingsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FolderSettingsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disable_default_sink: Optional[pulumi.Input[bool]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 kms_key_name: Optional[pulumi.Input[str]] = None,
                 storage_location: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FolderSettingsArgs.__new__(FolderSettingsArgs)

            __props__.__dict__["disable_default_sink"] = disable_default_sink
            if folder is None and not opts.urn:
                raise TypeError("Missing required property 'folder'")
            __props__.__dict__["folder"] = folder
            __props__.__dict__["kms_key_name"] = kms_key_name
            __props__.__dict__["storage_location"] = storage_location
            __props__.__dict__["kms_service_account_id"] = None
            __props__.__dict__["logging_service_account_id"] = None
            __props__.__dict__["name"] = None
        super(FolderSettings, __self__).__init__(
            'gcp:logging/folderSettings:FolderSettings',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            disable_default_sink: Optional[pulumi.Input[bool]] = None,
            folder: Optional[pulumi.Input[str]] = None,
            kms_key_name: Optional[pulumi.Input[str]] = None,
            kms_service_account_id: Optional[pulumi.Input[str]] = None,
            logging_service_account_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            storage_location: Optional[pulumi.Input[str]] = None) -> 'FolderSettings':
        """
        Get an existing FolderSettings resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] disable_default_sink: If set to true, the _Default sink in newly created projects and folders will created in a disabled state. This can be used to automatically disable log storage if there is already an aggregated sink configured in the hierarchy. The _Default sink can be re-enabled manually if needed.
        :param pulumi.Input[str] folder: The folder for which to retrieve settings.
               
               
               - - -
        :param pulumi.Input[str] kms_key_name: The resource name for the configured Cloud KMS key.
        :param pulumi.Input[str] kms_service_account_id: The service account that will be used by the Log Router to access your Cloud KMS key.
        :param pulumi.Input[str] logging_service_account_id: The service account for the given container. Sinks use this service account as their writerIdentity if no custom service account is provided.
        :param pulumi.Input[str] name: The resource name of the settings.
        :param pulumi.Input[str] storage_location: The storage location that Cloud Logging will use to create new resources when a location is needed but not explicitly provided.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FolderSettingsState.__new__(_FolderSettingsState)

        __props__.__dict__["disable_default_sink"] = disable_default_sink
        __props__.__dict__["folder"] = folder
        __props__.__dict__["kms_key_name"] = kms_key_name
        __props__.__dict__["kms_service_account_id"] = kms_service_account_id
        __props__.__dict__["logging_service_account_id"] = logging_service_account_id
        __props__.__dict__["name"] = name
        __props__.__dict__["storage_location"] = storage_location
        return FolderSettings(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="disableDefaultSink")
    def disable_default_sink(self) -> pulumi.Output[bool]:
        """
        If set to true, the _Default sink in newly created projects and folders will created in a disabled state. This can be used to automatically disable log storage if there is already an aggregated sink configured in the hierarchy. The _Default sink can be re-enabled manually if needed.
        """
        return pulumi.get(self, "disable_default_sink")

    @property
    @pulumi.getter
    def folder(self) -> pulumi.Output[str]:
        """
        The folder for which to retrieve settings.


        - - -
        """
        return pulumi.get(self, "folder")

    @property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[str]:
        """
        The resource name for the configured Cloud KMS key.
        """
        return pulumi.get(self, "kms_key_name")

    @property
    @pulumi.getter(name="kmsServiceAccountId")
    def kms_service_account_id(self) -> pulumi.Output[str]:
        """
        The service account that will be used by the Log Router to access your Cloud KMS key.
        """
        return pulumi.get(self, "kms_service_account_id")

    @property
    @pulumi.getter(name="loggingServiceAccountId")
    def logging_service_account_id(self) -> pulumi.Output[str]:
        """
        The service account for the given container. Sinks use this service account as their writerIdentity if no custom service account is provided.
        """
        return pulumi.get(self, "logging_service_account_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the settings.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> pulumi.Output[str]:
        """
        The storage location that Cloud Logging will use to create new resources when a location is needed but not explicitly provided.
        """
        return pulumi.get(self, "storage_location")

