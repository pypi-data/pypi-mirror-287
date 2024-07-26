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

__all__ = ['SharedVPCHostProjectArgs', 'SharedVPCHostProject']

@pulumi.input_type
class SharedVPCHostProjectArgs:
    def __init__(__self__, *,
                 project: pulumi.Input[str]):
        """
        The set of arguments for constructing a SharedVPCHostProject resource.
        :param pulumi.Input[str] project: The ID of the project that will serve as a Shared VPC host project
        """
        pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        The ID of the project that will serve as a Shared VPC host project
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _SharedVPCHostProjectState:
    def __init__(__self__, *,
                 project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SharedVPCHostProject resources.
        :param pulumi.Input[str] project: The ID of the project that will serve as a Shared VPC host project
        """
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project that will serve as a Shared VPC host project
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class SharedVPCHostProject(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Enables the Google Compute Engine
        [Shared VPC](https://cloud.google.com/compute/docs/shared-vpc)
        feature for a project, assigning it as a Shared VPC host project.

        For more information, see,
        [the Project API documentation](https://cloud.google.com/compute/docs/reference/latest/projects),
        where the Shared VPC feature is referred to by its former name "XPN".

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        # A host project provides network resources to associated service projects.
        host = gcp.compute.SharedVPCHostProject("host", project="host-project-id")
        # A service project gains access to network resources provided by its
        # associated host project.
        service1 = gcp.compute.SharedVPCServiceProject("service1",
            host_project=host.project,
            service_project="service-project-id-1")
        service2 = gcp.compute.SharedVPCServiceProject("service2",
            host_project=host.project,
            service_project="service-project-id-2")
        ```

        ## Import

        Google Compute Engine Shared VPC host project feature can be imported using `project`, e.g.

        * `{{project_id}}`

        When using the `pulumi import` command, Google Compute Engine Shared VPC host projects can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:compute/sharedVPCHostProject:SharedVPCHostProject default {{project_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project: The ID of the project that will serve as a Shared VPC host project
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SharedVPCHostProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Enables the Google Compute Engine
        [Shared VPC](https://cloud.google.com/compute/docs/shared-vpc)
        feature for a project, assigning it as a Shared VPC host project.

        For more information, see,
        [the Project API documentation](https://cloud.google.com/compute/docs/reference/latest/projects),
        where the Shared VPC feature is referred to by its former name "XPN".

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        # A host project provides network resources to associated service projects.
        host = gcp.compute.SharedVPCHostProject("host", project="host-project-id")
        # A service project gains access to network resources provided by its
        # associated host project.
        service1 = gcp.compute.SharedVPCServiceProject("service1",
            host_project=host.project,
            service_project="service-project-id-1")
        service2 = gcp.compute.SharedVPCServiceProject("service2",
            host_project=host.project,
            service_project="service-project-id-2")
        ```

        ## Import

        Google Compute Engine Shared VPC host project feature can be imported using `project`, e.g.

        * `{{project_id}}`

        When using the `pulumi import` command, Google Compute Engine Shared VPC host projects can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:compute/sharedVPCHostProject:SharedVPCHostProject default {{project_id}}
        ```

        :param str resource_name: The name of the resource.
        :param SharedVPCHostProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SharedVPCHostProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SharedVPCHostProjectArgs.__new__(SharedVPCHostProjectArgs)

            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
        super(SharedVPCHostProject, __self__).__init__(
            'gcp:compute/sharedVPCHostProject:SharedVPCHostProject',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'SharedVPCHostProject':
        """
        Get an existing SharedVPCHostProject resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project: The ID of the project that will serve as a Shared VPC host project
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SharedVPCHostProjectState.__new__(_SharedVPCHostProjectState)

        __props__.__dict__["project"] = project
        return SharedVPCHostProject(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project that will serve as a Shared VPC host project
        """
        return pulumi.get(self, "project")

