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

__all__ = ['SchemaArgs', 'Schema']

@pulumi.input_type
class SchemaArgs:
    def __init__(__self__, *,
                 definition: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Schema resource.
        :param pulumi.Input[str] definition: The definition of the schema.
               This should contain a string representing the full definition of the schema
               that is a valid schema definition of the type specified in type. Changes
               to the definition commit new [schema revisions](https://cloud.google.com/pubsub/docs/commit-schema-revision).
               A schema can only have up to 20 revisions, so updates that fail with an
               error indicating that the limit has been reached require manually
               [deleting old revisions](https://cloud.google.com/pubsub/docs/delete-schema-revision).
        :param pulumi.Input[str] name: The ID to use for the schema, which will become the final component of the schema's resource name.
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] type: The type of the schema definition
               Default value is `TYPE_UNSPECIFIED`.
               Possible values are: `TYPE_UNSPECIFIED`, `PROTOCOL_BUFFER`, `AVRO`.
        """
        if definition is not None:
            pulumi.set(__self__, "definition", definition)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def definition(self) -> Optional[pulumi.Input[str]]:
        """
        The definition of the schema.
        This should contain a string representing the full definition of the schema
        that is a valid schema definition of the type specified in type. Changes
        to the definition commit new [schema revisions](https://cloud.google.com/pubsub/docs/commit-schema-revision).
        A schema can only have up to 20 revisions, so updates that fail with an
        error indicating that the limit has been reached require manually
        [deleting old revisions](https://cloud.google.com/pubsub/docs/delete-schema-revision).
        """
        return pulumi.get(self, "definition")

    @definition.setter
    def definition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "definition", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The ID to use for the schema, which will become the final component of the schema's resource name.


        - - -
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
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the schema definition
        Default value is `TYPE_UNSPECIFIED`.
        Possible values are: `TYPE_UNSPECIFIED`, `PROTOCOL_BUFFER`, `AVRO`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _SchemaState:
    def __init__(__self__, *,
                 definition: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Schema resources.
        :param pulumi.Input[str] definition: The definition of the schema.
               This should contain a string representing the full definition of the schema
               that is a valid schema definition of the type specified in type. Changes
               to the definition commit new [schema revisions](https://cloud.google.com/pubsub/docs/commit-schema-revision).
               A schema can only have up to 20 revisions, so updates that fail with an
               error indicating that the limit has been reached require manually
               [deleting old revisions](https://cloud.google.com/pubsub/docs/delete-schema-revision).
        :param pulumi.Input[str] name: The ID to use for the schema, which will become the final component of the schema's resource name.
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] type: The type of the schema definition
               Default value is `TYPE_UNSPECIFIED`.
               Possible values are: `TYPE_UNSPECIFIED`, `PROTOCOL_BUFFER`, `AVRO`.
        """
        if definition is not None:
            pulumi.set(__self__, "definition", definition)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def definition(self) -> Optional[pulumi.Input[str]]:
        """
        The definition of the schema.
        This should contain a string representing the full definition of the schema
        that is a valid schema definition of the type specified in type. Changes
        to the definition commit new [schema revisions](https://cloud.google.com/pubsub/docs/commit-schema-revision).
        A schema can only have up to 20 revisions, so updates that fail with an
        error indicating that the limit has been reached require manually
        [deleting old revisions](https://cloud.google.com/pubsub/docs/delete-schema-revision).
        """
        return pulumi.get(self, "definition")

    @definition.setter
    def definition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "definition", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The ID to use for the schema, which will become the final component of the schema's resource name.


        - - -
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
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the schema definition
        Default value is `TYPE_UNSPECIFIED`.
        Possible values are: `TYPE_UNSPECIFIED`, `PROTOCOL_BUFFER`, `AVRO`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Schema(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 definition: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A schema is a format that messages must follow,
        creating a contract between publisher and subscriber that Pub/Sub will enforce.

        To get more information about Schema, see:

        * [API documentation](https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.schemas)
        * How-to Guides
            * [Creating and managing schemas](https://cloud.google.com/pubsub/docs/schemas)

        ## Example Usage

        ### Pubsub Schema Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.pubsub.Schema("example",
            name="example-schema",
            type="AVRO",
            definition=\"\"\"{
          "type" : "record",
          "name" : "Avro",
          "fields" : [
            {
              "name" : "StringField",
              "type" : "string"
            },
            {
              "name" : "IntField",
              "type" : "int"
            }
          ]
        }
        \"\"\")
        ```
        ### Pubsub Schema Protobuf

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.pubsub.Schema("example",
            name="example",
            type="PROTOCOL_BUFFER",
            definition=\"\"\"syntax = "proto3";
        message Results {
        string message_request = 1;
        string message_response = 2;
        string timestamp_request = 3;
        string timestamp_response = 4;
        }\"\"\")
        example_topic = gcp.pubsub.Topic("example",
            name="example-topic",
            schema_settings={
                "schema": "projects/my-project-name/schemas/example",
                "encoding": "JSON",
            },
            opts = pulumi.ResourceOptions(depends_on=[example]))
        ```

        ## Import

        Schema can be imported using any of these accepted formats:

        * `projects/{{project}}/schemas/{{name}}`

        * `{{project}}/{{name}}`

        * `{{name}}`

        When using the `pulumi import` command, Schema can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:pubsub/schema:Schema default projects/{{project}}/schemas/{{name}}
        ```

        ```sh
        $ pulumi import gcp:pubsub/schema:Schema default {{project}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:pubsub/schema:Schema default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] definition: The definition of the schema.
               This should contain a string representing the full definition of the schema
               that is a valid schema definition of the type specified in type. Changes
               to the definition commit new [schema revisions](https://cloud.google.com/pubsub/docs/commit-schema-revision).
               A schema can only have up to 20 revisions, so updates that fail with an
               error indicating that the limit has been reached require manually
               [deleting old revisions](https://cloud.google.com/pubsub/docs/delete-schema-revision).
        :param pulumi.Input[str] name: The ID to use for the schema, which will become the final component of the schema's resource name.
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] type: The type of the schema definition
               Default value is `TYPE_UNSPECIFIED`.
               Possible values are: `TYPE_UNSPECIFIED`, `PROTOCOL_BUFFER`, `AVRO`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SchemaArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A schema is a format that messages must follow,
        creating a contract between publisher and subscriber that Pub/Sub will enforce.

        To get more information about Schema, see:

        * [API documentation](https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.schemas)
        * How-to Guides
            * [Creating and managing schemas](https://cloud.google.com/pubsub/docs/schemas)

        ## Example Usage

        ### Pubsub Schema Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.pubsub.Schema("example",
            name="example-schema",
            type="AVRO",
            definition=\"\"\"{
          "type" : "record",
          "name" : "Avro",
          "fields" : [
            {
              "name" : "StringField",
              "type" : "string"
            },
            {
              "name" : "IntField",
              "type" : "int"
            }
          ]
        }
        \"\"\")
        ```
        ### Pubsub Schema Protobuf

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.pubsub.Schema("example",
            name="example",
            type="PROTOCOL_BUFFER",
            definition=\"\"\"syntax = "proto3";
        message Results {
        string message_request = 1;
        string message_response = 2;
        string timestamp_request = 3;
        string timestamp_response = 4;
        }\"\"\")
        example_topic = gcp.pubsub.Topic("example",
            name="example-topic",
            schema_settings={
                "schema": "projects/my-project-name/schemas/example",
                "encoding": "JSON",
            },
            opts = pulumi.ResourceOptions(depends_on=[example]))
        ```

        ## Import

        Schema can be imported using any of these accepted formats:

        * `projects/{{project}}/schemas/{{name}}`

        * `{{project}}/{{name}}`

        * `{{name}}`

        When using the `pulumi import` command, Schema can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:pubsub/schema:Schema default projects/{{project}}/schemas/{{name}}
        ```

        ```sh
        $ pulumi import gcp:pubsub/schema:Schema default {{project}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:pubsub/schema:Schema default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param SchemaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SchemaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 definition: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SchemaArgs.__new__(SchemaArgs)

            __props__.__dict__["definition"] = definition
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["type"] = type
        super(Schema, __self__).__init__(
            'gcp:pubsub/schema:Schema',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            definition: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Schema':
        """
        Get an existing Schema resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] definition: The definition of the schema.
               This should contain a string representing the full definition of the schema
               that is a valid schema definition of the type specified in type. Changes
               to the definition commit new [schema revisions](https://cloud.google.com/pubsub/docs/commit-schema-revision).
               A schema can only have up to 20 revisions, so updates that fail with an
               error indicating that the limit has been reached require manually
               [deleting old revisions](https://cloud.google.com/pubsub/docs/delete-schema-revision).
        :param pulumi.Input[str] name: The ID to use for the schema, which will become the final component of the schema's resource name.
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] type: The type of the schema definition
               Default value is `TYPE_UNSPECIFIED`.
               Possible values are: `TYPE_UNSPECIFIED`, `PROTOCOL_BUFFER`, `AVRO`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SchemaState.__new__(_SchemaState)

        __props__.__dict__["definition"] = definition
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["type"] = type
        return Schema(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Output[Optional[str]]:
        """
        The definition of the schema.
        This should contain a string representing the full definition of the schema
        that is a valid schema definition of the type specified in type. Changes
        to the definition commit new [schema revisions](https://cloud.google.com/pubsub/docs/commit-schema-revision).
        A schema can only have up to 20 revisions, so updates that fail with an
        error indicating that the limit has been reached require manually
        [deleting old revisions](https://cloud.google.com/pubsub/docs/delete-schema-revision).
        """
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The ID to use for the schema, which will become the final component of the schema's resource name.


        - - -
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
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the schema definition
        Default value is `TYPE_UNSPECIFIED`.
        Possible values are: `TYPE_UNSPECIFIED`, `PROTOCOL_BUFFER`, `AVRO`.
        """
        return pulumi.get(self, "type")

