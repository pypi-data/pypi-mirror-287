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
from ._inputs import *

__all__ = ['AiFeatureStoreEntityTypeArgs', 'AiFeatureStoreEntityType']

@pulumi.input_type
class AiFeatureStoreEntityTypeArgs:
    def __init__(__self__, *,
                 featurestore: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 monitoring_config: Optional[pulumi.Input['AiFeatureStoreEntityTypeMonitoringConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 offline_storage_ttl_days: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a AiFeatureStoreEntityType resource.
        :param pulumi.Input[str] featurestore: The name of the Featurestore to use, in the format projects/{project}/locations/{location}/featurestores/{featurestore}.
               
               
               - - -
        :param pulumi.Input[str] description: Optional. Description of the EntityType.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A set of key/value label pairs to assign to this EntityType.
               
               **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
               Please refer to the field `effective_labels` for all of the labels present on the resource.
        :param pulumi.Input['AiFeatureStoreEntityTypeMonitoringConfigArgs'] monitoring_config: The default monitoring configuration for all Features under this EntityType.
               If this is populated with [FeaturestoreMonitoringConfig.monitoring_interval] specified, snapshot analysis monitoring is enabled. Otherwise, snapshot analysis monitoring is disabled.
               Structure is documented below.
        :param pulumi.Input[str] name: The name of the EntityType. This value may be up to 60 characters, and valid characters are [a-z0-9_]. The first character cannot be a number.
        :param pulumi.Input[int] offline_storage_ttl_days: Config for data retention policy in offline storage. TTL in days for feature values that will be stored in offline storage. The Feature Store offline storage periodically removes obsolete feature values older than offlineStorageTtlDays since the feature generation time. If unset (or explicitly set to 0), default to 4000 days TTL.
        """
        pulumi.set(__self__, "featurestore", featurestore)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if monitoring_config is not None:
            pulumi.set(__self__, "monitoring_config", monitoring_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if offline_storage_ttl_days is not None:
            pulumi.set(__self__, "offline_storage_ttl_days", offline_storage_ttl_days)

    @property
    @pulumi.getter
    def featurestore(self) -> pulumi.Input[str]:
        """
        The name of the Featurestore to use, in the format projects/{project}/locations/{location}/featurestores/{featurestore}.


        - - -
        """
        return pulumi.get(self, "featurestore")

    @featurestore.setter
    def featurestore(self, value: pulumi.Input[str]):
        pulumi.set(self, "featurestore", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Description of the EntityType.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A set of key/value label pairs to assign to this EntityType.

        **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
        Please refer to the field `effective_labels` for all of the labels present on the resource.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="monitoringConfig")
    def monitoring_config(self) -> Optional[pulumi.Input['AiFeatureStoreEntityTypeMonitoringConfigArgs']]:
        """
        The default monitoring configuration for all Features under this EntityType.
        If this is populated with [FeaturestoreMonitoringConfig.monitoring_interval] specified, snapshot analysis monitoring is enabled. Otherwise, snapshot analysis monitoring is disabled.
        Structure is documented below.
        """
        return pulumi.get(self, "monitoring_config")

    @monitoring_config.setter
    def monitoring_config(self, value: Optional[pulumi.Input['AiFeatureStoreEntityTypeMonitoringConfigArgs']]):
        pulumi.set(self, "monitoring_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the EntityType. This value may be up to 60 characters, and valid characters are [a-z0-9_]. The first character cannot be a number.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="offlineStorageTtlDays")
    def offline_storage_ttl_days(self) -> Optional[pulumi.Input[int]]:
        """
        Config for data retention policy in offline storage. TTL in days for feature values that will be stored in offline storage. The Feature Store offline storage periodically removes obsolete feature values older than offlineStorageTtlDays since the feature generation time. If unset (or explicitly set to 0), default to 4000 days TTL.
        """
        return pulumi.get(self, "offline_storage_ttl_days")

    @offline_storage_ttl_days.setter
    def offline_storage_ttl_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "offline_storage_ttl_days", value)


@pulumi.input_type
class _AiFeatureStoreEntityTypeState:
    def __init__(__self__, *,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 featurestore: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 monitoring_config: Optional[pulumi.Input['AiFeatureStoreEntityTypeMonitoringConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 offline_storage_ttl_days: Optional[pulumi.Input[int]] = None,
                 pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AiFeatureStoreEntityType resources.
        :param pulumi.Input[str] create_time: The timestamp of when the featurestore was created in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        :param pulumi.Input[str] description: Optional. Description of the EntityType.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] effective_labels: All of labels (key/value pairs) present on the resource in GCP, including the labels configured through Pulumi, other clients and services.
        :param pulumi.Input[str] etag: Used to perform consistent read-modify-write updates.
        :param pulumi.Input[str] featurestore: The name of the Featurestore to use, in the format projects/{project}/locations/{location}/featurestores/{featurestore}.
               
               
               - - -
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A set of key/value label pairs to assign to this EntityType.
               
               **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
               Please refer to the field `effective_labels` for all of the labels present on the resource.
        :param pulumi.Input['AiFeatureStoreEntityTypeMonitoringConfigArgs'] monitoring_config: The default monitoring configuration for all Features under this EntityType.
               If this is populated with [FeaturestoreMonitoringConfig.monitoring_interval] specified, snapshot analysis monitoring is enabled. Otherwise, snapshot analysis monitoring is disabled.
               Structure is documented below.
        :param pulumi.Input[str] name: The name of the EntityType. This value may be up to 60 characters, and valid characters are [a-z0-9_]. The first character cannot be a number.
        :param pulumi.Input[int] offline_storage_ttl_days: Config for data retention policy in offline storage. TTL in days for feature values that will be stored in offline storage. The Feature Store offline storage periodically removes obsolete feature values older than offlineStorageTtlDays since the feature generation time. If unset (or explicitly set to 0), default to 4000 days TTL.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] pulumi_labels: The combination of labels configured directly on the resource
               and default labels configured on the provider.
        :param pulumi.Input[str] region: The region of the EntityType.
        :param pulumi.Input[str] update_time: The timestamp of when the featurestore was last updated in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if effective_labels is not None:
            pulumi.set(__self__, "effective_labels", effective_labels)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if featurestore is not None:
            pulumi.set(__self__, "featurestore", featurestore)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if monitoring_config is not None:
            pulumi.set(__self__, "monitoring_config", monitoring_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if offline_storage_ttl_days is not None:
            pulumi.set(__self__, "offline_storage_ttl_days", offline_storage_ttl_days)
        if pulumi_labels is not None:
            pulumi.set(__self__, "pulumi_labels", pulumi_labels)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of when the featurestore was created in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Description of the EntityType.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        All of labels (key/value pairs) present on the resource in GCP, including the labels configured through Pulumi, other clients and services.
        """
        return pulumi.get(self, "effective_labels")

    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "effective_labels", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        Used to perform consistent read-modify-write updates.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def featurestore(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Featurestore to use, in the format projects/{project}/locations/{location}/featurestores/{featurestore}.


        - - -
        """
        return pulumi.get(self, "featurestore")

    @featurestore.setter
    def featurestore(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "featurestore", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A set of key/value label pairs to assign to this EntityType.

        **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
        Please refer to the field `effective_labels` for all of the labels present on the resource.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="monitoringConfig")
    def monitoring_config(self) -> Optional[pulumi.Input['AiFeatureStoreEntityTypeMonitoringConfigArgs']]:
        """
        The default monitoring configuration for all Features under this EntityType.
        If this is populated with [FeaturestoreMonitoringConfig.monitoring_interval] specified, snapshot analysis monitoring is enabled. Otherwise, snapshot analysis monitoring is disabled.
        Structure is documented below.
        """
        return pulumi.get(self, "monitoring_config")

    @monitoring_config.setter
    def monitoring_config(self, value: Optional[pulumi.Input['AiFeatureStoreEntityTypeMonitoringConfigArgs']]):
        pulumi.set(self, "monitoring_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the EntityType. This value may be up to 60 characters, and valid characters are [a-z0-9_]. The first character cannot be a number.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="offlineStorageTtlDays")
    def offline_storage_ttl_days(self) -> Optional[pulumi.Input[int]]:
        """
        Config for data retention policy in offline storage. TTL in days for feature values that will be stored in offline storage. The Feature Store offline storage periodically removes obsolete feature values older than offlineStorageTtlDays since the feature generation time. If unset (or explicitly set to 0), default to 4000 days TTL.
        """
        return pulumi.get(self, "offline_storage_ttl_days")

    @offline_storage_ttl_days.setter
    def offline_storage_ttl_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "offline_storage_ttl_days", value)

    @property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The combination of labels configured directly on the resource
        and default labels configured on the provider.
        """
        return pulumi.get(self, "pulumi_labels")

    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "pulumi_labels", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the EntityType.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of when the featurestore was last updated in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class AiFeatureStoreEntityType(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 featurestore: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 monitoring_config: Optional[pulumi.Input[Union['AiFeatureStoreEntityTypeMonitoringConfigArgs', 'AiFeatureStoreEntityTypeMonitoringConfigArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 offline_storage_ttl_days: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        An entity type is a type of object in a system that needs to be modeled and have stored information about. For example, driver is an entity type, and driver0 is an instance of an entity type driver.

        To get more information about FeaturestoreEntitytype, see:

        * [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/vertex-ai/docs)

        ## Example Usage

        ### Vertex Ai Featurestore Entitytype

        ```python
        import pulumi
        import pulumi_gcp as gcp

        featurestore = gcp.vertex.AiFeatureStore("featurestore",
            name="terraform",
            labels={
                "foo": "bar",
            },
            region="us-central1",
            online_serving_config={
                "fixed_node_count": 2,
            },
            encryption_spec={
                "kms_key_name": "kms-name",
            })
        entity = gcp.vertex.AiFeatureStoreEntityType("entity",
            name="terraform",
            labels={
                "foo": "bar",
            },
            description="test description",
            featurestore=featurestore.id,
            monitoring_config={
                "snapshot_analysis": {
                    "disabled": False,
                    "monitoring_interval_days": 1,
                    "staleness_days": 21,
                },
                "numerical_threshold_config": {
                    "value": 0.8,
                },
                "categorical_threshold_config": {
                    "value": 10,
                },
                "import_features_analysis": {
                    "state": "ENABLED",
                    "anomaly_detection_baseline": "PREVIOUS_IMPORT_FEATURES_STATS",
                },
            })
        ```
        ### Vertex Ai Featurestore Entitytype With Beta Fields

        ```python
        import pulumi
        import pulumi_gcp as gcp

        featurestore = gcp.vertex.AiFeatureStore("featurestore",
            name="terraform2",
            labels={
                "foo": "bar",
            },
            region="us-central1",
            online_serving_config={
                "fixed_node_count": 2,
            },
            encryption_spec={
                "kms_key_name": "kms-name",
            })
        entity = gcp.vertex.AiFeatureStoreEntityType("entity",
            name="terraform2",
            labels={
                "foo": "bar",
            },
            featurestore=featurestore.id,
            monitoring_config={
                "snapshot_analysis": {
                    "disabled": False,
                    "monitoring_interval": "86400s",
                },
                "categorical_threshold_config": {
                    "value": 0.3,
                },
                "numerical_threshold_config": {
                    "value": 0.3,
                },
            },
            offline_storage_ttl_days=30)
        ```

        ## Import

        FeaturestoreEntitytype can be imported using any of these accepted formats:

        * `{{featurestore}}/entityTypes/{{name}}`

        When using the `pulumi import` command, FeaturestoreEntitytype can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:vertex/aiFeatureStoreEntityType:AiFeatureStoreEntityType default {{featurestore}}/entityTypes/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Optional. Description of the EntityType.
        :param pulumi.Input[str] featurestore: The name of the Featurestore to use, in the format projects/{project}/locations/{location}/featurestores/{featurestore}.
               
               
               - - -
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A set of key/value label pairs to assign to this EntityType.
               
               **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
               Please refer to the field `effective_labels` for all of the labels present on the resource.
        :param pulumi.Input[Union['AiFeatureStoreEntityTypeMonitoringConfigArgs', 'AiFeatureStoreEntityTypeMonitoringConfigArgsDict']] monitoring_config: The default monitoring configuration for all Features under this EntityType.
               If this is populated with [FeaturestoreMonitoringConfig.monitoring_interval] specified, snapshot analysis monitoring is enabled. Otherwise, snapshot analysis monitoring is disabled.
               Structure is documented below.
        :param pulumi.Input[str] name: The name of the EntityType. This value may be up to 60 characters, and valid characters are [a-z0-9_]. The first character cannot be a number.
        :param pulumi.Input[int] offline_storage_ttl_days: Config for data retention policy in offline storage. TTL in days for feature values that will be stored in offline storage. The Feature Store offline storage periodically removes obsolete feature values older than offlineStorageTtlDays since the feature generation time. If unset (or explicitly set to 0), default to 4000 days TTL.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AiFeatureStoreEntityTypeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An entity type is a type of object in a system that needs to be modeled and have stored information about. For example, driver is an entity type, and driver0 is an instance of an entity type driver.

        To get more information about FeaturestoreEntitytype, see:

        * [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/vertex-ai/docs)

        ## Example Usage

        ### Vertex Ai Featurestore Entitytype

        ```python
        import pulumi
        import pulumi_gcp as gcp

        featurestore = gcp.vertex.AiFeatureStore("featurestore",
            name="terraform",
            labels={
                "foo": "bar",
            },
            region="us-central1",
            online_serving_config={
                "fixed_node_count": 2,
            },
            encryption_spec={
                "kms_key_name": "kms-name",
            })
        entity = gcp.vertex.AiFeatureStoreEntityType("entity",
            name="terraform",
            labels={
                "foo": "bar",
            },
            description="test description",
            featurestore=featurestore.id,
            monitoring_config={
                "snapshot_analysis": {
                    "disabled": False,
                    "monitoring_interval_days": 1,
                    "staleness_days": 21,
                },
                "numerical_threshold_config": {
                    "value": 0.8,
                },
                "categorical_threshold_config": {
                    "value": 10,
                },
                "import_features_analysis": {
                    "state": "ENABLED",
                    "anomaly_detection_baseline": "PREVIOUS_IMPORT_FEATURES_STATS",
                },
            })
        ```
        ### Vertex Ai Featurestore Entitytype With Beta Fields

        ```python
        import pulumi
        import pulumi_gcp as gcp

        featurestore = gcp.vertex.AiFeatureStore("featurestore",
            name="terraform2",
            labels={
                "foo": "bar",
            },
            region="us-central1",
            online_serving_config={
                "fixed_node_count": 2,
            },
            encryption_spec={
                "kms_key_name": "kms-name",
            })
        entity = gcp.vertex.AiFeatureStoreEntityType("entity",
            name="terraform2",
            labels={
                "foo": "bar",
            },
            featurestore=featurestore.id,
            monitoring_config={
                "snapshot_analysis": {
                    "disabled": False,
                    "monitoring_interval": "86400s",
                },
                "categorical_threshold_config": {
                    "value": 0.3,
                },
                "numerical_threshold_config": {
                    "value": 0.3,
                },
            },
            offline_storage_ttl_days=30)
        ```

        ## Import

        FeaturestoreEntitytype can be imported using any of these accepted formats:

        * `{{featurestore}}/entityTypes/{{name}}`

        When using the `pulumi import` command, FeaturestoreEntitytype can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:vertex/aiFeatureStoreEntityType:AiFeatureStoreEntityType default {{featurestore}}/entityTypes/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param AiFeatureStoreEntityTypeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AiFeatureStoreEntityTypeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 featurestore: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 monitoring_config: Optional[pulumi.Input[Union['AiFeatureStoreEntityTypeMonitoringConfigArgs', 'AiFeatureStoreEntityTypeMonitoringConfigArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 offline_storage_ttl_days: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AiFeatureStoreEntityTypeArgs.__new__(AiFeatureStoreEntityTypeArgs)

            __props__.__dict__["description"] = description
            if featurestore is None and not opts.urn:
                raise TypeError("Missing required property 'featurestore'")
            __props__.__dict__["featurestore"] = featurestore
            __props__.__dict__["labels"] = labels
            __props__.__dict__["monitoring_config"] = monitoring_config
            __props__.__dict__["name"] = name
            __props__.__dict__["offline_storage_ttl_days"] = offline_storage_ttl_days
            __props__.__dict__["create_time"] = None
            __props__.__dict__["effective_labels"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["pulumi_labels"] = None
            __props__.__dict__["region"] = None
            __props__.__dict__["update_time"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["effectiveLabels", "pulumiLabels"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(AiFeatureStoreEntityType, __self__).__init__(
            'gcp:vertex/aiFeatureStoreEntityType:AiFeatureStoreEntityType',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            featurestore: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            monitoring_config: Optional[pulumi.Input[Union['AiFeatureStoreEntityTypeMonitoringConfigArgs', 'AiFeatureStoreEntityTypeMonitoringConfigArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            offline_storage_ttl_days: Optional[pulumi.Input[int]] = None,
            pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            region: Optional[pulumi.Input[str]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'AiFeatureStoreEntityType':
        """
        Get an existing AiFeatureStoreEntityType resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: The timestamp of when the featurestore was created in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        :param pulumi.Input[str] description: Optional. Description of the EntityType.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] effective_labels: All of labels (key/value pairs) present on the resource in GCP, including the labels configured through Pulumi, other clients and services.
        :param pulumi.Input[str] etag: Used to perform consistent read-modify-write updates.
        :param pulumi.Input[str] featurestore: The name of the Featurestore to use, in the format projects/{project}/locations/{location}/featurestores/{featurestore}.
               
               
               - - -
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A set of key/value label pairs to assign to this EntityType.
               
               **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
               Please refer to the field `effective_labels` for all of the labels present on the resource.
        :param pulumi.Input[Union['AiFeatureStoreEntityTypeMonitoringConfigArgs', 'AiFeatureStoreEntityTypeMonitoringConfigArgsDict']] monitoring_config: The default monitoring configuration for all Features under this EntityType.
               If this is populated with [FeaturestoreMonitoringConfig.monitoring_interval] specified, snapshot analysis monitoring is enabled. Otherwise, snapshot analysis monitoring is disabled.
               Structure is documented below.
        :param pulumi.Input[str] name: The name of the EntityType. This value may be up to 60 characters, and valid characters are [a-z0-9_]. The first character cannot be a number.
        :param pulumi.Input[int] offline_storage_ttl_days: Config for data retention policy in offline storage. TTL in days for feature values that will be stored in offline storage. The Feature Store offline storage periodically removes obsolete feature values older than offlineStorageTtlDays since the feature generation time. If unset (or explicitly set to 0), default to 4000 days TTL.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] pulumi_labels: The combination of labels configured directly on the resource
               and default labels configured on the provider.
        :param pulumi.Input[str] region: The region of the EntityType.
        :param pulumi.Input[str] update_time: The timestamp of when the featurestore was last updated in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AiFeatureStoreEntityTypeState.__new__(_AiFeatureStoreEntityTypeState)

        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["description"] = description
        __props__.__dict__["effective_labels"] = effective_labels
        __props__.__dict__["etag"] = etag
        __props__.__dict__["featurestore"] = featurestore
        __props__.__dict__["labels"] = labels
        __props__.__dict__["monitoring_config"] = monitoring_config
        __props__.__dict__["name"] = name
        __props__.__dict__["offline_storage_ttl_days"] = offline_storage_ttl_days
        __props__.__dict__["pulumi_labels"] = pulumi_labels
        __props__.__dict__["region"] = region
        __props__.__dict__["update_time"] = update_time
        return AiFeatureStoreEntityType(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The timestamp of when the featurestore was created in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Optional. Description of the EntityType.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        All of labels (key/value pairs) present on the resource in GCP, including the labels configured through Pulumi, other clients and services.
        """
        return pulumi.get(self, "effective_labels")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Used to perform consistent read-modify-write updates.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def featurestore(self) -> pulumi.Output[str]:
        """
        The name of the Featurestore to use, in the format projects/{project}/locations/{location}/featurestores/{featurestore}.


        - - -
        """
        return pulumi.get(self, "featurestore")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A set of key/value label pairs to assign to this EntityType.

        **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
        Please refer to the field `effective_labels` for all of the labels present on the resource.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="monitoringConfig")
    def monitoring_config(self) -> pulumi.Output[Optional['outputs.AiFeatureStoreEntityTypeMonitoringConfig']]:
        """
        The default monitoring configuration for all Features under this EntityType.
        If this is populated with [FeaturestoreMonitoringConfig.monitoring_interval] specified, snapshot analysis monitoring is enabled. Otherwise, snapshot analysis monitoring is disabled.
        Structure is documented below.
        """
        return pulumi.get(self, "monitoring_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the EntityType. This value may be up to 60 characters, and valid characters are [a-z0-9_]. The first character cannot be a number.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="offlineStorageTtlDays")
    def offline_storage_ttl_days(self) -> pulumi.Output[Optional[int]]:
        """
        Config for data retention policy in offline storage. TTL in days for feature values that will be stored in offline storage. The Feature Store offline storage periodically removes obsolete feature values older than offlineStorageTtlDays since the feature generation time. If unset (or explicitly set to 0), default to 4000 days TTL.
        """
        return pulumi.get(self, "offline_storage_ttl_days")

    @property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The combination of labels configured directly on the resource
        and default labels configured on the provider.
        """
        return pulumi.get(self, "pulumi_labels")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region of the EntityType.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The timestamp of when the featurestore was last updated in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "update_time")

