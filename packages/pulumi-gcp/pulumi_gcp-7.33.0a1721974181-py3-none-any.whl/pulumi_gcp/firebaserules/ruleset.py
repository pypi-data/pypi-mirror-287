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

__all__ = ['RulesetArgs', 'Ruleset']

@pulumi.input_type
class RulesetArgs:
    def __init__(__self__, *,
                 source: pulumi.Input['RulesetSourceArgs'],
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Ruleset resource.
        :param pulumi.Input['RulesetSourceArgs'] source: `Source` for the `Ruleset`.
        :param pulumi.Input[str] project: The project for the resource
        """
        pulumi.set(__self__, "source", source)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input['RulesetSourceArgs']:
        """
        `Source` for the `Ruleset`.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input['RulesetSourceArgs']):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project for the resource
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _RulesetState:
    def __init__(__self__, *,
                 create_time: Optional[pulumi.Input[str]] = None,
                 metadatas: Optional[pulumi.Input[Sequence[pulumi.Input['RulesetMetadataArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input['RulesetSourceArgs']] = None):
        """
        Input properties used for looking up and filtering Ruleset resources.
        :param pulumi.Input[str] create_time: Output only. Time the `Ruleset` was created.
        :param pulumi.Input[Sequence[pulumi.Input['RulesetMetadataArgs']]] metadatas: Output only. The metadata for this ruleset.
        :param pulumi.Input[str] name: Output only. Name of the `Ruleset`. The ruleset_id is auto generated by the service. Format: `projects/{project_id}/rulesets/{ruleset_id}`
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input['RulesetSourceArgs'] source: `Source` for the `Ruleset`.
        """
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if metadatas is not None:
            pulumi.set(__self__, "metadatas", metadatas)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if source is not None:
            pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. Time the `Ruleset` was created.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def metadatas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RulesetMetadataArgs']]]]:
        """
        Output only. The metadata for this ruleset.
        """
        return pulumi.get(self, "metadatas")

    @metadatas.setter
    def metadatas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RulesetMetadataArgs']]]]):
        pulumi.set(self, "metadatas", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. Name of the `Ruleset`. The ruleset_id is auto generated by the service. Format: `projects/{project_id}/rulesets/{ruleset_id}`
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project for the resource
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input['RulesetSourceArgs']]:
        """
        `Source` for the `Ruleset`.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input['RulesetSourceArgs']]):
        pulumi.set(self, "source", value)


class Ruleset(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[Union['RulesetSourceArgs', 'RulesetSourceArgsDict']]] = None,
                 __props__=None):
        """
        For more information, see:
        * [Get started with Firebase Security Rules](https://firebase.google.com/docs/rules/get-started)
        ## Example Usage

        ### Basic_ruleset
        Creates a basic Firestore ruleset
        ```python
        import pulumi
        import pulumi_gcp as gcp

        primary = gcp.firebaserules.Ruleset("primary",
            source={
                "files": [{
                    "content": "service cloud.firestore {match /databases/{database}/documents { match /{document=**} { allow read, write: if false; } } }",
                    "name": "firestore.rules",
                    "fingerprint": "",
                }],
                "language": "",
            },
            project="my-project-name")
        ```
        ### Minimal_ruleset
        Creates a minimal Firestore ruleset
        ```python
        import pulumi
        import pulumi_gcp as gcp

        primary = gcp.firebaserules.Ruleset("primary",
            source={
                "files": [{
                    "content": "service cloud.firestore {match /databases/{database}/documents { match /{document=**} { allow read, write: if false; } } }",
                    "name": "firestore.rules",
                }],
            },
            project="my-project-name")
        ```

        ## Import

        Ruleset can be imported using any of these accepted formats:

        * `projects/{{project}}/rulesets/{{name}}`

        * `{{project}}/{{name}}`

        * `{{name}}`

        When using the `pulumi import` command, Ruleset can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:firebaserules/ruleset:Ruleset default projects/{{project}}/rulesets/{{name}}
        ```

        ```sh
        $ pulumi import gcp:firebaserules/ruleset:Ruleset default {{project}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:firebaserules/ruleset:Ruleset default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input[Union['RulesetSourceArgs', 'RulesetSourceArgsDict']] source: `Source` for the `Ruleset`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RulesetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        For more information, see:
        * [Get started with Firebase Security Rules](https://firebase.google.com/docs/rules/get-started)
        ## Example Usage

        ### Basic_ruleset
        Creates a basic Firestore ruleset
        ```python
        import pulumi
        import pulumi_gcp as gcp

        primary = gcp.firebaserules.Ruleset("primary",
            source={
                "files": [{
                    "content": "service cloud.firestore {match /databases/{database}/documents { match /{document=**} { allow read, write: if false; } } }",
                    "name": "firestore.rules",
                    "fingerprint": "",
                }],
                "language": "",
            },
            project="my-project-name")
        ```
        ### Minimal_ruleset
        Creates a minimal Firestore ruleset
        ```python
        import pulumi
        import pulumi_gcp as gcp

        primary = gcp.firebaserules.Ruleset("primary",
            source={
                "files": [{
                    "content": "service cloud.firestore {match /databases/{database}/documents { match /{document=**} { allow read, write: if false; } } }",
                    "name": "firestore.rules",
                }],
            },
            project="my-project-name")
        ```

        ## Import

        Ruleset can be imported using any of these accepted formats:

        * `projects/{{project}}/rulesets/{{name}}`

        * `{{project}}/{{name}}`

        * `{{name}}`

        When using the `pulumi import` command, Ruleset can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:firebaserules/ruleset:Ruleset default projects/{{project}}/rulesets/{{name}}
        ```

        ```sh
        $ pulumi import gcp:firebaserules/ruleset:Ruleset default {{project}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:firebaserules/ruleset:Ruleset default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param RulesetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RulesetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[Union['RulesetSourceArgs', 'RulesetSourceArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RulesetArgs.__new__(RulesetArgs)

            __props__.__dict__["project"] = project
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            __props__.__dict__["create_time"] = None
            __props__.__dict__["metadatas"] = None
            __props__.__dict__["name"] = None
        super(Ruleset, __self__).__init__(
            'gcp:firebaserules/ruleset:Ruleset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            metadatas: Optional[pulumi.Input[Sequence[pulumi.Input[Union['RulesetMetadataArgs', 'RulesetMetadataArgsDict']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            source: Optional[pulumi.Input[Union['RulesetSourceArgs', 'RulesetSourceArgsDict']]] = None) -> 'Ruleset':
        """
        Get an existing Ruleset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: Output only. Time the `Ruleset` was created.
        :param pulumi.Input[Sequence[pulumi.Input[Union['RulesetMetadataArgs', 'RulesetMetadataArgsDict']]]] metadatas: Output only. The metadata for this ruleset.
        :param pulumi.Input[str] name: Output only. Name of the `Ruleset`. The ruleset_id is auto generated by the service. Format: `projects/{project_id}/rulesets/{ruleset_id}`
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input[Union['RulesetSourceArgs', 'RulesetSourceArgsDict']] source: `Source` for the `Ruleset`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RulesetState.__new__(_RulesetState)

        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["metadatas"] = metadatas
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["source"] = source
        return Ruleset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Output only. Time the `Ruleset` was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def metadatas(self) -> pulumi.Output[Sequence['outputs.RulesetMetadata']]:
        """
        Output only. The metadata for this ruleset.
        """
        return pulumi.get(self, "metadatas")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Output only. Name of the `Ruleset`. The ruleset_id is auto generated by the service. Format: `projects/{project_id}/rulesets/{ruleset_id}`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The project for the resource
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output['outputs.RulesetSource']:
        """
        `Source` for the `Ruleset`.
        """
        return pulumi.get(self, "source")

