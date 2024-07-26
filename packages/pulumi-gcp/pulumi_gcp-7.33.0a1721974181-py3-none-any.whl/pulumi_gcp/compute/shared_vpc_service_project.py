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

__all__ = ['SharedVPCServiceProjectArgs', 'SharedVPCServiceProject']

@pulumi.input_type
class SharedVPCServiceProjectArgs:
    def __init__(__self__, *,
                 host_project: pulumi.Input[str],
                 service_project: pulumi.Input[str],
                 deletion_policy: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SharedVPCServiceProject resource.
        :param pulumi.Input[str] host_project: The ID of a host project to associate.
        :param pulumi.Input[str] service_project: The ID of the project that will serve as a Shared VPC service project.
        :param pulumi.Input[str] deletion_policy: The deletion policy for the shared VPC service. Setting ABANDON allows the resource to be abandoned rather than deleted. Possible values are: "ABANDON".
        """
        pulumi.set(__self__, "host_project", host_project)
        pulumi.set(__self__, "service_project", service_project)
        if deletion_policy is not None:
            pulumi.set(__self__, "deletion_policy", deletion_policy)

    @property
    @pulumi.getter(name="hostProject")
    def host_project(self) -> pulumi.Input[str]:
        """
        The ID of a host project to associate.
        """
        return pulumi.get(self, "host_project")

    @host_project.setter
    def host_project(self, value: pulumi.Input[str]):
        pulumi.set(self, "host_project", value)

    @property
    @pulumi.getter(name="serviceProject")
    def service_project(self) -> pulumi.Input[str]:
        """
        The ID of the project that will serve as a Shared VPC service project.
        """
        return pulumi.get(self, "service_project")

    @service_project.setter
    def service_project(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_project", value)

    @property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The deletion policy for the shared VPC service. Setting ABANDON allows the resource to be abandoned rather than deleted. Possible values are: "ABANDON".
        """
        return pulumi.get(self, "deletion_policy")

    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deletion_policy", value)


@pulumi.input_type
class _SharedVPCServiceProjectState:
    def __init__(__self__, *,
                 deletion_policy: Optional[pulumi.Input[str]] = None,
                 host_project: Optional[pulumi.Input[str]] = None,
                 service_project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SharedVPCServiceProject resources.
        :param pulumi.Input[str] deletion_policy: The deletion policy for the shared VPC service. Setting ABANDON allows the resource to be abandoned rather than deleted. Possible values are: "ABANDON".
        :param pulumi.Input[str] host_project: The ID of a host project to associate.
        :param pulumi.Input[str] service_project: The ID of the project that will serve as a Shared VPC service project.
        """
        if deletion_policy is not None:
            pulumi.set(__self__, "deletion_policy", deletion_policy)
        if host_project is not None:
            pulumi.set(__self__, "host_project", host_project)
        if service_project is not None:
            pulumi.set(__self__, "service_project", service_project)

    @property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The deletion policy for the shared VPC service. Setting ABANDON allows the resource to be abandoned rather than deleted. Possible values are: "ABANDON".
        """
        return pulumi.get(self, "deletion_policy")

    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deletion_policy", value)

    @property
    @pulumi.getter(name="hostProject")
    def host_project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of a host project to associate.
        """
        return pulumi.get(self, "host_project")

    @host_project.setter
    def host_project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_project", value)

    @property
    @pulumi.getter(name="serviceProject")
    def service_project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project that will serve as a Shared VPC service project.
        """
        return pulumi.get(self, "service_project")

    @service_project.setter
    def service_project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_project", value)


class SharedVPCServiceProject(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deletion_policy: Optional[pulumi.Input[str]] = None,
                 host_project: Optional[pulumi.Input[str]] = None,
                 service_project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Enables the Google Compute Engine
        [Shared VPC](https://cloud.google.com/compute/docs/shared-vpc)
        feature for a project, assigning it as a Shared VPC service project associated
        with a given host project.

        For more information, see,
        [the Project API documentation](https://cloud.google.com/compute/docs/reference/latest/projects),
        where the Shared VPC feature is referred to by its former name "XPN".

        > **Note:** If Shared VPC Admin role is set at the folder level, use the google-beta provider. The google provider only supports this permission at project or organizational level currently. [[0]](https://cloud.google.com/vpc/docs/provisioning-shared-vpc#enable-shared-vpc-host)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        service1 = gcp.compute.SharedVPCServiceProject("service1",
            host_project="host-project-id",
            service_project="service-project-id-1")
        ```

        For a complete Shared VPC example with both host and service projects, see
        [`compute.SharedVPCHostProject`](https://www.terraform.io/docs/providers/google/r/compute_shared_vpc_host_project.html).

        ## Import

        Google Compute Engine Shared VPC service project feature can be imported using the `host_project` and `service_project`, e.g.

        * `{{host_project}/{{service_project}}`

        When using the `pulumi import` command, Google Compute Engine Shared VPC service project can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:compute/sharedVPCServiceProject:SharedVPCServiceProject default {{host_project}/{{service_project}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deletion_policy: The deletion policy for the shared VPC service. Setting ABANDON allows the resource to be abandoned rather than deleted. Possible values are: "ABANDON".
        :param pulumi.Input[str] host_project: The ID of a host project to associate.
        :param pulumi.Input[str] service_project: The ID of the project that will serve as a Shared VPC service project.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SharedVPCServiceProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Enables the Google Compute Engine
        [Shared VPC](https://cloud.google.com/compute/docs/shared-vpc)
        feature for a project, assigning it as a Shared VPC service project associated
        with a given host project.

        For more information, see,
        [the Project API documentation](https://cloud.google.com/compute/docs/reference/latest/projects),
        where the Shared VPC feature is referred to by its former name "XPN".

        > **Note:** If Shared VPC Admin role is set at the folder level, use the google-beta provider. The google provider only supports this permission at project or organizational level currently. [[0]](https://cloud.google.com/vpc/docs/provisioning-shared-vpc#enable-shared-vpc-host)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        service1 = gcp.compute.SharedVPCServiceProject("service1",
            host_project="host-project-id",
            service_project="service-project-id-1")
        ```

        For a complete Shared VPC example with both host and service projects, see
        [`compute.SharedVPCHostProject`](https://www.terraform.io/docs/providers/google/r/compute_shared_vpc_host_project.html).

        ## Import

        Google Compute Engine Shared VPC service project feature can be imported using the `host_project` and `service_project`, e.g.

        * `{{host_project}/{{service_project}}`

        When using the `pulumi import` command, Google Compute Engine Shared VPC service project can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:compute/sharedVPCServiceProject:SharedVPCServiceProject default {{host_project}/{{service_project}}
        ```

        :param str resource_name: The name of the resource.
        :param SharedVPCServiceProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SharedVPCServiceProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deletion_policy: Optional[pulumi.Input[str]] = None,
                 host_project: Optional[pulumi.Input[str]] = None,
                 service_project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SharedVPCServiceProjectArgs.__new__(SharedVPCServiceProjectArgs)

            __props__.__dict__["deletion_policy"] = deletion_policy
            if host_project is None and not opts.urn:
                raise TypeError("Missing required property 'host_project'")
            __props__.__dict__["host_project"] = host_project
            if service_project is None and not opts.urn:
                raise TypeError("Missing required property 'service_project'")
            __props__.__dict__["service_project"] = service_project
        super(SharedVPCServiceProject, __self__).__init__(
            'gcp:compute/sharedVPCServiceProject:SharedVPCServiceProject',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            deletion_policy: Optional[pulumi.Input[str]] = None,
            host_project: Optional[pulumi.Input[str]] = None,
            service_project: Optional[pulumi.Input[str]] = None) -> 'SharedVPCServiceProject':
        """
        Get an existing SharedVPCServiceProject resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deletion_policy: The deletion policy for the shared VPC service. Setting ABANDON allows the resource to be abandoned rather than deleted. Possible values are: "ABANDON".
        :param pulumi.Input[str] host_project: The ID of a host project to associate.
        :param pulumi.Input[str] service_project: The ID of the project that will serve as a Shared VPC service project.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SharedVPCServiceProjectState.__new__(_SharedVPCServiceProjectState)

        __props__.__dict__["deletion_policy"] = deletion_policy
        __props__.__dict__["host_project"] = host_project
        __props__.__dict__["service_project"] = service_project
        return SharedVPCServiceProject(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[str]]:
        """
        The deletion policy for the shared VPC service. Setting ABANDON allows the resource to be abandoned rather than deleted. Possible values are: "ABANDON".
        """
        return pulumi.get(self, "deletion_policy")

    @property
    @pulumi.getter(name="hostProject")
    def host_project(self) -> pulumi.Output[str]:
        """
        The ID of a host project to associate.
        """
        return pulumi.get(self, "host_project")

    @property
    @pulumi.getter(name="serviceProject")
    def service_project(self) -> pulumi.Output[str]:
        """
        The ID of the project that will serve as a Shared VPC service project.
        """
        return pulumi.get(self, "service_project")

