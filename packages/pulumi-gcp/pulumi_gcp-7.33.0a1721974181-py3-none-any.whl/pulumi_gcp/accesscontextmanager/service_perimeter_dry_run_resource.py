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

__all__ = ['ServicePerimeterDryRunResourceArgs', 'ServicePerimeterDryRunResource']

@pulumi.input_type
class ServicePerimeterDryRunResourceArgs:
    def __init__(__self__, *,
                 perimeter_name: pulumi.Input[str],
                 resource: pulumi.Input[str]):
        """
        The set of arguments for constructing a ServicePerimeterDryRunResource resource.
        :param pulumi.Input[str] perimeter_name: The name of the Service Perimeter to add this resource to.
               
               
               - - -
        :param pulumi.Input[str] resource: A GCP resource that is inside of the service perimeter.
               Currently only projects are allowed.
               Format: projects/{project_number}
        """
        pulumi.set(__self__, "perimeter_name", perimeter_name)
        pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter(name="perimeterName")
    def perimeter_name(self) -> pulumi.Input[str]:
        """
        The name of the Service Perimeter to add this resource to.


        - - -
        """
        return pulumi.get(self, "perimeter_name")

    @perimeter_name.setter
    def perimeter_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "perimeter_name", value)

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Input[str]:
        """
        A GCP resource that is inside of the service perimeter.
        Currently only projects are allowed.
        Format: projects/{project_number}
        """
        return pulumi.get(self, "resource")

    @resource.setter
    def resource(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource", value)


@pulumi.input_type
class _ServicePerimeterDryRunResourceState:
    def __init__(__self__, *,
                 perimeter_name: Optional[pulumi.Input[str]] = None,
                 resource: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ServicePerimeterDryRunResource resources.
        :param pulumi.Input[str] perimeter_name: The name of the Service Perimeter to add this resource to.
               
               
               - - -
        :param pulumi.Input[str] resource: A GCP resource that is inside of the service perimeter.
               Currently only projects are allowed.
               Format: projects/{project_number}
        """
        if perimeter_name is not None:
            pulumi.set(__self__, "perimeter_name", perimeter_name)
        if resource is not None:
            pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter(name="perimeterName")
    def perimeter_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Service Perimeter to add this resource to.


        - - -
        """
        return pulumi.get(self, "perimeter_name")

    @perimeter_name.setter
    def perimeter_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "perimeter_name", value)

    @property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[str]]:
        """
        A GCP resource that is inside of the service perimeter.
        Currently only projects are allowed.
        Format: projects/{project_number}
        """
        return pulumi.get(self, "resource")

    @resource.setter
    def resource(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource", value)


class ServicePerimeterDryRunResource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 perimeter_name: Optional[pulumi.Input[str]] = None,
                 resource: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Allows configuring a single GCP resource that should be inside of the `spec` block of a dry run service perimeter.
        This resource is intended to be used in cases where it is not possible to compile a full list
        of projects to include in a `accesscontextmanager.ServicePerimeter` resource,
        to enable them to be added separately.
        If your perimeter is NOT in dry-run mode use `accesscontextmanager.ServicePerimeterResource` instead.

        > **Note:** If this resource is used alongside a `accesscontextmanager.ServicePerimeter` resource,
        the service perimeter resource must have a `lifecycle` block with `ignore_changes = [spec[0].resources]` so
        they don't fight over which resources should be in the policy.

        To get more information about ServicePerimeterDryRunResource, see:

        * [API documentation](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters)
        * How-to Guides
            * [Service Perimeter Quickstart](https://cloud.google.com/vpc-service-controls/docs/quickstart)

        > **Warning:** If you are using User ADCs (Application Default Credentials) with this resource,
        you must specify a `billing_project` and set `user_project_override` to true
        in the provider configuration. Otherwise the ACM API will return a 403 error.
        Your account must have the `serviceusage.services.use` permission on the
        `billing_project` you defined.

        ## Example Usage

        ### Access Context Manager Service Perimeter Dry Run Resource Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        access_policy = gcp.accesscontextmanager.AccessPolicy("access-policy",
            parent="organizations/123456789",
            title="my policy")
        service_perimeter_dry_run_resource_service_perimeter = gcp.accesscontextmanager.ServicePerimeter("service-perimeter-dry-run-resource",
            parent=access_policy.name.apply(lambda name: f"accessPolicies/{name}"),
            name=access_policy.name.apply(lambda name: f"accessPolicies/{name}/servicePerimeters/restrict_all"),
            title="restrict_all",
            spec={
                "restricted_services": ["storage.googleapis.com"],
            },
            use_explicit_dry_run_spec=True)
        service_perimeter_dry_run_resource = gcp.accesscontextmanager.ServicePerimeterDryRunResource("service-perimeter-dry-run-resource",
            perimeter_name=service_perimeter_dry_run_resource_service_perimeter.name,
            resource="projects/987654321")
        ```

        ## Import

        ServicePerimeterDryRunResource can be imported using any of these accepted formats:

        * `{{perimeter_name}}/{{resource}}`

        When using the `pulumi import` command, ServicePerimeterDryRunResource can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:accesscontextmanager/servicePerimeterDryRunResource:ServicePerimeterDryRunResource default {{perimeter_name}}/{{resource}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] perimeter_name: The name of the Service Perimeter to add this resource to.
               
               
               - - -
        :param pulumi.Input[str] resource: A GCP resource that is inside of the service perimeter.
               Currently only projects are allowed.
               Format: projects/{project_number}
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServicePerimeterDryRunResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Allows configuring a single GCP resource that should be inside of the `spec` block of a dry run service perimeter.
        This resource is intended to be used in cases where it is not possible to compile a full list
        of projects to include in a `accesscontextmanager.ServicePerimeter` resource,
        to enable them to be added separately.
        If your perimeter is NOT in dry-run mode use `accesscontextmanager.ServicePerimeterResource` instead.

        > **Note:** If this resource is used alongside a `accesscontextmanager.ServicePerimeter` resource,
        the service perimeter resource must have a `lifecycle` block with `ignore_changes = [spec[0].resources]` so
        they don't fight over which resources should be in the policy.

        To get more information about ServicePerimeterDryRunResource, see:

        * [API documentation](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters)
        * How-to Guides
            * [Service Perimeter Quickstart](https://cloud.google.com/vpc-service-controls/docs/quickstart)

        > **Warning:** If you are using User ADCs (Application Default Credentials) with this resource,
        you must specify a `billing_project` and set `user_project_override` to true
        in the provider configuration. Otherwise the ACM API will return a 403 error.
        Your account must have the `serviceusage.services.use` permission on the
        `billing_project` you defined.

        ## Example Usage

        ### Access Context Manager Service Perimeter Dry Run Resource Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        access_policy = gcp.accesscontextmanager.AccessPolicy("access-policy",
            parent="organizations/123456789",
            title="my policy")
        service_perimeter_dry_run_resource_service_perimeter = gcp.accesscontextmanager.ServicePerimeter("service-perimeter-dry-run-resource",
            parent=access_policy.name.apply(lambda name: f"accessPolicies/{name}"),
            name=access_policy.name.apply(lambda name: f"accessPolicies/{name}/servicePerimeters/restrict_all"),
            title="restrict_all",
            spec={
                "restricted_services": ["storage.googleapis.com"],
            },
            use_explicit_dry_run_spec=True)
        service_perimeter_dry_run_resource = gcp.accesscontextmanager.ServicePerimeterDryRunResource("service-perimeter-dry-run-resource",
            perimeter_name=service_perimeter_dry_run_resource_service_perimeter.name,
            resource="projects/987654321")
        ```

        ## Import

        ServicePerimeterDryRunResource can be imported using any of these accepted formats:

        * `{{perimeter_name}}/{{resource}}`

        When using the `pulumi import` command, ServicePerimeterDryRunResource can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:accesscontextmanager/servicePerimeterDryRunResource:ServicePerimeterDryRunResource default {{perimeter_name}}/{{resource}}
        ```

        :param str resource_name: The name of the resource.
        :param ServicePerimeterDryRunResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServicePerimeterDryRunResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 perimeter_name: Optional[pulumi.Input[str]] = None,
                 resource: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServicePerimeterDryRunResourceArgs.__new__(ServicePerimeterDryRunResourceArgs)

            if perimeter_name is None and not opts.urn:
                raise TypeError("Missing required property 'perimeter_name'")
            __props__.__dict__["perimeter_name"] = perimeter_name
            if resource is None and not opts.urn:
                raise TypeError("Missing required property 'resource'")
            __props__.__dict__["resource"] = resource
        super(ServicePerimeterDryRunResource, __self__).__init__(
            'gcp:accesscontextmanager/servicePerimeterDryRunResource:ServicePerimeterDryRunResource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            perimeter_name: Optional[pulumi.Input[str]] = None,
            resource: Optional[pulumi.Input[str]] = None) -> 'ServicePerimeterDryRunResource':
        """
        Get an existing ServicePerimeterDryRunResource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] perimeter_name: The name of the Service Perimeter to add this resource to.
               
               
               - - -
        :param pulumi.Input[str] resource: A GCP resource that is inside of the service perimeter.
               Currently only projects are allowed.
               Format: projects/{project_number}
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServicePerimeterDryRunResourceState.__new__(_ServicePerimeterDryRunResourceState)

        __props__.__dict__["perimeter_name"] = perimeter_name
        __props__.__dict__["resource"] = resource
        return ServicePerimeterDryRunResource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="perimeterName")
    def perimeter_name(self) -> pulumi.Output[str]:
        """
        The name of the Service Perimeter to add this resource to.


        - - -
        """
        return pulumi.get(self, "perimeter_name")

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Output[str]:
        """
        A GCP resource that is inside of the service perimeter.
        Currently only projects are allowed.
        Format: projects/{project_number}
        """
        return pulumi.get(self, "resource")

