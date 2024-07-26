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

__all__ = ['AiFeatureGroupArgs', 'AiFeatureGroup']

@pulumi.input_type
class AiFeatureGroupArgs:
    def __init__(__self__, *,
                 big_query: Optional[pulumi.Input['AiFeatureGroupBigQueryArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AiFeatureGroup resource.
        :param pulumi.Input['AiFeatureGroupBigQueryArgs'] big_query: Indicates that features for this group come from BigQuery Table/View. By default treats the source as a sparse time series source, which is required to have an entityId and a feature_timestamp column in the source.
               Structure is documented below.
        :param pulumi.Input[str] description: The description of the FeatureGroup.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels with user-defined metadata to organize your FeatureGroup.
               **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
               Please refer to the field `effective_labels` for all of the labels present on the resource.
        :param pulumi.Input[str] name: The resource name of the Feature Group.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: The region of feature group. eg us-central1
        """
        if big_query is not None:
            pulumi.set(__self__, "big_query", big_query)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="bigQuery")
    def big_query(self) -> Optional[pulumi.Input['AiFeatureGroupBigQueryArgs']]:
        """
        Indicates that features for this group come from BigQuery Table/View. By default treats the source as a sparse time series source, which is required to have an entityId and a feature_timestamp column in the source.
        Structure is documented below.
        """
        return pulumi.get(self, "big_query")

    @big_query.setter
    def big_query(self, value: Optional[pulumi.Input['AiFeatureGroupBigQueryArgs']]):
        pulumi.set(self, "big_query", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the FeatureGroup.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The labels with user-defined metadata to organize your FeatureGroup.
        **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
        Please refer to the field `effective_labels` for all of the labels present on the resource.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the Feature Group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of feature group. eg us-central1
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _AiFeatureGroupState:
    def __init__(__self__, *,
                 big_query: Optional[pulumi.Input['AiFeatureGroupBigQueryArgs']] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AiFeatureGroup resources.
        :param pulumi.Input['AiFeatureGroupBigQueryArgs'] big_query: Indicates that features for this group come from BigQuery Table/View. By default treats the source as a sparse time series source, which is required to have an entityId and a feature_timestamp column in the source.
               Structure is documented below.
        :param pulumi.Input[str] create_time: The timestamp of when the FeatureGroup was created in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        :param pulumi.Input[str] description: The description of the FeatureGroup.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] effective_labels: All of labels (key/value pairs) present on the resource in GCP, including the labels configured through Pulumi, other clients and services.
        :param pulumi.Input[str] etag: Used to perform consistent read-modify-write updates.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels with user-defined metadata to organize your FeatureGroup.
               **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
               Please refer to the field `effective_labels` for all of the labels present on the resource.
        :param pulumi.Input[str] name: The resource name of the Feature Group.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] pulumi_labels: The combination of labels configured directly on the resource
               and default labels configured on the provider.
        :param pulumi.Input[str] region: The region of feature group. eg us-central1
        :param pulumi.Input[str] update_time: The timestamp of when the FeatureGroup was last updated in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        if big_query is not None:
            pulumi.set(__self__, "big_query", big_query)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if effective_labels is not None:
            pulumi.set(__self__, "effective_labels", effective_labels)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if pulumi_labels is not None:
            pulumi.set(__self__, "pulumi_labels", pulumi_labels)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="bigQuery")
    def big_query(self) -> Optional[pulumi.Input['AiFeatureGroupBigQueryArgs']]:
        """
        Indicates that features for this group come from BigQuery Table/View. By default treats the source as a sparse time series source, which is required to have an entityId and a feature_timestamp column in the source.
        Structure is documented below.
        """
        return pulumi.get(self, "big_query")

    @big_query.setter
    def big_query(self, value: Optional[pulumi.Input['AiFeatureGroupBigQueryArgs']]):
        pulumi.set(self, "big_query", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of when the FeatureGroup was created in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the FeatureGroup.
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
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The labels with user-defined metadata to organize your FeatureGroup.
        **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
        Please refer to the field `effective_labels` for all of the labels present on the resource.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the Feature Group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

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
        The region of feature group. eg us-central1
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of when the FeatureGroup was last updated in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class AiFeatureGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 big_query: Optional[pulumi.Input[Union['AiFeatureGroupBigQueryArgs', 'AiFeatureGroupBigQueryArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Vertex AI Feature Group.

        To get more information about FeatureGroup, see:

        * [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featureGroups)
        * How-to Guides
            * [Creating a Feature Group](https://cloud.google.com/vertex-ai/docs/featurestore/latest/create-featuregroup)

        ## Example Usage

        ### Vertex Ai Feature Group

        ```python
        import pulumi
        import pulumi_gcp as gcp

        sample_dataset = gcp.bigquery.Dataset("sample_dataset",
            dataset_id="job_load_dataset",
            friendly_name="test",
            description="This is a test description",
            location="US")
        sample_table = gcp.bigquery.Table("sample_table",
            deletion_protection=False,
            dataset_id=sample_dataset.dataset_id,
            table_id="job_load_table",
            schema=\"\"\"[
            {
                "name": "feature_id",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "feature_timestamp",
                "type": "TIMESTAMP",
                "mode": "NULLABLE"
            }
        ]
        \"\"\")
        feature_group = gcp.vertex.AiFeatureGroup("feature_group",
            name="example_feature_group",
            description="A sample feature group",
            region="us-central1",
            labels={
                "label-one": "value-one",
            },
            big_query={
                "big_query_source": {
                    "input_uri": pulumi.Output.all(sample_table.project, sample_table.dataset_id, sample_table.table_id).apply(lambda project, dataset_id, table_id: f"bq://{project}.{dataset_id}.{table_id}"),
                },
                "entity_id_columns": ["feature_id"],
            })
        ```

        ## Import

        FeatureGroup can be imported using any of these accepted formats:

        * `projects/{{project}}/locations/{{region}}/featureGroups/{{name}}`

        * `{{project}}/{{region}}/{{name}}`

        * `{{region}}/{{name}}`

        * `{{name}}`

        When using the `pulumi import` command, FeatureGroup can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:vertex/aiFeatureGroup:AiFeatureGroup default projects/{{project}}/locations/{{region}}/featureGroups/{{name}}
        ```

        ```sh
        $ pulumi import gcp:vertex/aiFeatureGroup:AiFeatureGroup default {{project}}/{{region}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:vertex/aiFeatureGroup:AiFeatureGroup default {{region}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:vertex/aiFeatureGroup:AiFeatureGroup default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['AiFeatureGroupBigQueryArgs', 'AiFeatureGroupBigQueryArgsDict']] big_query: Indicates that features for this group come from BigQuery Table/View. By default treats the source as a sparse time series source, which is required to have an entityId and a feature_timestamp column in the source.
               Structure is documented below.
        :param pulumi.Input[str] description: The description of the FeatureGroup.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels with user-defined metadata to organize your FeatureGroup.
               **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
               Please refer to the field `effective_labels` for all of the labels present on the resource.
        :param pulumi.Input[str] name: The resource name of the Feature Group.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: The region of feature group. eg us-central1
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AiFeatureGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Vertex AI Feature Group.

        To get more information about FeatureGroup, see:

        * [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featureGroups)
        * How-to Guides
            * [Creating a Feature Group](https://cloud.google.com/vertex-ai/docs/featurestore/latest/create-featuregroup)

        ## Example Usage

        ### Vertex Ai Feature Group

        ```python
        import pulumi
        import pulumi_gcp as gcp

        sample_dataset = gcp.bigquery.Dataset("sample_dataset",
            dataset_id="job_load_dataset",
            friendly_name="test",
            description="This is a test description",
            location="US")
        sample_table = gcp.bigquery.Table("sample_table",
            deletion_protection=False,
            dataset_id=sample_dataset.dataset_id,
            table_id="job_load_table",
            schema=\"\"\"[
            {
                "name": "feature_id",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "feature_timestamp",
                "type": "TIMESTAMP",
                "mode": "NULLABLE"
            }
        ]
        \"\"\")
        feature_group = gcp.vertex.AiFeatureGroup("feature_group",
            name="example_feature_group",
            description="A sample feature group",
            region="us-central1",
            labels={
                "label-one": "value-one",
            },
            big_query={
                "big_query_source": {
                    "input_uri": pulumi.Output.all(sample_table.project, sample_table.dataset_id, sample_table.table_id).apply(lambda project, dataset_id, table_id: f"bq://{project}.{dataset_id}.{table_id}"),
                },
                "entity_id_columns": ["feature_id"],
            })
        ```

        ## Import

        FeatureGroup can be imported using any of these accepted formats:

        * `projects/{{project}}/locations/{{region}}/featureGroups/{{name}}`

        * `{{project}}/{{region}}/{{name}}`

        * `{{region}}/{{name}}`

        * `{{name}}`

        When using the `pulumi import` command, FeatureGroup can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:vertex/aiFeatureGroup:AiFeatureGroup default projects/{{project}}/locations/{{region}}/featureGroups/{{name}}
        ```

        ```sh
        $ pulumi import gcp:vertex/aiFeatureGroup:AiFeatureGroup default {{project}}/{{region}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:vertex/aiFeatureGroup:AiFeatureGroup default {{region}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:vertex/aiFeatureGroup:AiFeatureGroup default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param AiFeatureGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AiFeatureGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 big_query: Optional[pulumi.Input[Union['AiFeatureGroupBigQueryArgs', 'AiFeatureGroupBigQueryArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AiFeatureGroupArgs.__new__(AiFeatureGroupArgs)

            __props__.__dict__["big_query"] = big_query
            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["region"] = region
            __props__.__dict__["create_time"] = None
            __props__.__dict__["effective_labels"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["pulumi_labels"] = None
            __props__.__dict__["update_time"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["effectiveLabels", "pulumiLabels"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(AiFeatureGroup, __self__).__init__(
            'gcp:vertex/aiFeatureGroup:AiFeatureGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            big_query: Optional[pulumi.Input[Union['AiFeatureGroupBigQueryArgs', 'AiFeatureGroupBigQueryArgsDict']]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            region: Optional[pulumi.Input[str]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'AiFeatureGroup':
        """
        Get an existing AiFeatureGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['AiFeatureGroupBigQueryArgs', 'AiFeatureGroupBigQueryArgsDict']] big_query: Indicates that features for this group come from BigQuery Table/View. By default treats the source as a sparse time series source, which is required to have an entityId and a feature_timestamp column in the source.
               Structure is documented below.
        :param pulumi.Input[str] create_time: The timestamp of when the FeatureGroup was created in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        :param pulumi.Input[str] description: The description of the FeatureGroup.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] effective_labels: All of labels (key/value pairs) present on the resource in GCP, including the labels configured through Pulumi, other clients and services.
        :param pulumi.Input[str] etag: Used to perform consistent read-modify-write updates.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels with user-defined metadata to organize your FeatureGroup.
               **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
               Please refer to the field `effective_labels` for all of the labels present on the resource.
        :param pulumi.Input[str] name: The resource name of the Feature Group.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] pulumi_labels: The combination of labels configured directly on the resource
               and default labels configured on the provider.
        :param pulumi.Input[str] region: The region of feature group. eg us-central1
        :param pulumi.Input[str] update_time: The timestamp of when the FeatureGroup was last updated in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AiFeatureGroupState.__new__(_AiFeatureGroupState)

        __props__.__dict__["big_query"] = big_query
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["description"] = description
        __props__.__dict__["effective_labels"] = effective_labels
        __props__.__dict__["etag"] = etag
        __props__.__dict__["labels"] = labels
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["pulumi_labels"] = pulumi_labels
        __props__.__dict__["region"] = region
        __props__.__dict__["update_time"] = update_time
        return AiFeatureGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bigQuery")
    def big_query(self) -> pulumi.Output[Optional['outputs.AiFeatureGroupBigQuery']]:
        """
        Indicates that features for this group come from BigQuery Table/View. By default treats the source as a sparse time series source, which is required to have an entityId and a feature_timestamp column in the source.
        Structure is documented below.
        """
        return pulumi.get(self, "big_query")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The timestamp of when the FeatureGroup was created in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the FeatureGroup.
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
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The labels with user-defined metadata to organize your FeatureGroup.
        **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
        Please refer to the field `effective_labels` for all of the labels present on the resource.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the Feature Group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

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
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        The region of feature group. eg us-central1
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The timestamp of when the FeatureGroup was last updated in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "update_time")

