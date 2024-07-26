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

__all__ = ['WebBackendServiceIamPolicyArgs', 'WebBackendServiceIamPolicy']

@pulumi.input_type
class WebBackendServiceIamPolicyArgs:
    def __init__(__self__, *,
                 policy_data: pulumi.Input[str],
                 web_backend_service: pulumi.Input[str],
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WebBackendServiceIamPolicy resource.
        :param pulumi.Input[str] policy_data: The policy data generated by
               a `organizations_get_iam_policy` data source.
        :param pulumi.Input[str] web_backend_service: Used to find the parent resource to bind the IAM policy to
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        """
        pulumi.set(__self__, "policy_data", policy_data)
        pulumi.set(__self__, "web_backend_service", web_backend_service)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> pulumi.Input[str]:
        """
        The policy data generated by
        a `organizations_get_iam_policy` data source.
        """
        return pulumi.get(self, "policy_data")

    @policy_data.setter
    def policy_data(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_data", value)

    @property
    @pulumi.getter(name="webBackendService")
    def web_backend_service(self) -> pulumi.Input[str]:
        """
        Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "web_backend_service")

    @web_backend_service.setter
    def web_backend_service(self, value: pulumi.Input[str]):
        pulumi.set(self, "web_backend_service", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _WebBackendServiceIamPolicyState:
    def __init__(__self__, *,
                 etag: Optional[pulumi.Input[str]] = None,
                 policy_data: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 web_backend_service: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WebBackendServiceIamPolicy resources.
        :param pulumi.Input[str] etag: (Computed) The etag of the IAM policy.
        :param pulumi.Input[str] policy_data: The policy data generated by
               a `organizations_get_iam_policy` data source.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        :param pulumi.Input[str] web_backend_service: Used to find the parent resource to bind the IAM policy to
        """
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if policy_data is not None:
            pulumi.set(__self__, "policy_data", policy_data)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if web_backend_service is not None:
            pulumi.set(__self__, "web_backend_service", web_backend_service)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        (Computed) The etag of the IAM policy.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> Optional[pulumi.Input[str]]:
        """
        The policy data generated by
        a `organizations_get_iam_policy` data source.
        """
        return pulumi.get(self, "policy_data")

    @policy_data.setter
    def policy_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_data", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="webBackendService")
    def web_backend_service(self) -> Optional[pulumi.Input[str]]:
        """
        Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "web_backend_service")

    @web_backend_service.setter
    def web_backend_service(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "web_backend_service", value)


class WebBackendServiceIamPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_data: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 web_backend_service: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Three different resources help you manage your IAM policy for Identity-Aware Proxy WebBackendService. Each of these resources serves a different use case:

        * `iap.WebBackendServiceIamPolicy`: Authoritative. Sets the IAM policy for the webbackendservice and replaces any existing policy already attached.
        * `iap.WebBackendServiceIamBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the webbackendservice are preserved.
        * `iap.WebBackendServiceIamMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the webbackendservice are preserved.

        A data source can be used to retrieve policy data in advent you do not need creation

        * `iap.WebBackendServiceIamPolicy`: Retrieves the IAM policy for the webbackendservice

        > **Note:** `iap.WebBackendServiceIamPolicy` **cannot** be used in conjunction with `iap.WebBackendServiceIamBinding` and `iap.WebBackendServiceIamMember` or they will fight over what your policy should be.

        > **Note:** `iap.WebBackendServiceIamBinding` resources **can be** used in conjunction with `iap.WebBackendServiceIamMember` resources **only if** they do not grant privilege to the same role.

        > **Note:**  This resource supports IAM Conditions but they have some known limitations which can be found [here](https://cloud.google.com/iam/docs/conditions-overview#limitations). Please review this article if you are having issues with IAM Conditions.

        ## iap.WebBackendServiceIamPolicy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[{
            "role": "roles/iap.httpsResourceAccessor",
            "members": ["user:jane@example.com"],
        }])
        policy = gcp.iap.WebBackendServiceIamPolicy("policy",
            project=default["project"],
            web_backend_service=default["name"],
            policy_data=admin.policy_data)
        ```

        With IAM Conditions:

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[{
            "role": "roles/iap.httpsResourceAccessor",
            "members": ["user:jane@example.com"],
            "condition": {
                "title": "expires_after_2019_12_31",
                "description": "Expiring at midnight of 2019-12-31",
                "expression": "request.time < timestamp(\\"2020-01-01T00:00:00Z\\")",
            },
        }])
        policy = gcp.iap.WebBackendServiceIamPolicy("policy",
            project=default["project"],
            web_backend_service=default["name"],
            policy_data=admin.policy_data)
        ```
        ## iap.WebBackendServiceIamBinding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.iap.WebBackendServiceIamBinding("binding",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            members=["user:jane@example.com"])
        ```

        With IAM Conditions:

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.iap.WebBackendServiceIamBinding("binding",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            members=["user:jane@example.com"],
            condition={
                "title": "expires_after_2019_12_31",
                "description": "Expiring at midnight of 2019-12-31",
                "expression": "request.time < timestamp(\\"2020-01-01T00:00:00Z\\")",
            })
        ```
        ## iap.WebBackendServiceIamMember

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.iap.WebBackendServiceIamMember("member",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            member="user:jane@example.com")
        ```

        With IAM Conditions:

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.iap.WebBackendServiceIamMember("member",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            member="user:jane@example.com",
            condition={
                "title": "expires_after_2019_12_31",
                "description": "Expiring at midnight of 2019-12-31",
                "expression": "request.time < timestamp(\\"2020-01-01T00:00:00Z\\")",
            })
        ```

        ## iap.WebBackendServiceIamPolicy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[{
            "role": "roles/iap.httpsResourceAccessor",
            "members": ["user:jane@example.com"],
        }])
        policy = gcp.iap.WebBackendServiceIamPolicy("policy",
            project=default["project"],
            web_backend_service=default["name"],
            policy_data=admin.policy_data)
        ```

        With IAM Conditions:

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[{
            "role": "roles/iap.httpsResourceAccessor",
            "members": ["user:jane@example.com"],
            "condition": {
                "title": "expires_after_2019_12_31",
                "description": "Expiring at midnight of 2019-12-31",
                "expression": "request.time < timestamp(\\"2020-01-01T00:00:00Z\\")",
            },
        }])
        policy = gcp.iap.WebBackendServiceIamPolicy("policy",
            project=default["project"],
            web_backend_service=default["name"],
            policy_data=admin.policy_data)
        ```
        ## iap.WebBackendServiceIamBinding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.iap.WebBackendServiceIamBinding("binding",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            members=["user:jane@example.com"])
        ```

        With IAM Conditions:

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.iap.WebBackendServiceIamBinding("binding",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            members=["user:jane@example.com"],
            condition={
                "title": "expires_after_2019_12_31",
                "description": "Expiring at midnight of 2019-12-31",
                "expression": "request.time < timestamp(\\"2020-01-01T00:00:00Z\\")",
            })
        ```
        ## iap.WebBackendServiceIamMember

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.iap.WebBackendServiceIamMember("member",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            member="user:jane@example.com")
        ```

        With IAM Conditions:

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.iap.WebBackendServiceIamMember("member",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            member="user:jane@example.com",
            condition={
                "title": "expires_after_2019_12_31",
                "description": "Expiring at midnight of 2019-12-31",
                "expression": "request.time < timestamp(\\"2020-01-01T00:00:00Z\\")",
            })
        ```

        ## Import

        For all import syntaxes, the "resource in question" can take any of the following forms:

        * projects/{{project}}/iap_web/compute/services/{{name}}

        * {{project}}/{{name}}

        * {{name}}

        Any variables not passed in the import command will be taken from the provider configuration.

        Identity-Aware Proxy webbackendservice IAM resources can be imported using the resource identifiers, role, and member.

        IAM member imports use space-delimited identifiers: the resource in question, the role, and the member identity, e.g.

        ```sh
        $ pulumi import gcp:iap/webBackendServiceIamPolicy:WebBackendServiceIamPolicy editor "projects/{{project}}/iap_web/compute/services/{{web_backend_service}} roles/iap.httpsResourceAccessor user:jane@example.com"
        ```

        IAM binding imports use space-delimited identifiers: the resource in question and the role, e.g.

        ```sh
        $ pulumi import gcp:iap/webBackendServiceIamPolicy:WebBackendServiceIamPolicy editor "projects/{{project}}/iap_web/compute/services/{{web_backend_service}} roles/iap.httpsResourceAccessor"
        ```

        IAM policy imports use the identifier of the resource in question, e.g.

        ```sh
        $ pulumi import gcp:iap/webBackendServiceIamPolicy:WebBackendServiceIamPolicy editor projects/{{project}}/iap_web/compute/services/{{web_backend_service}}
        ```

        -> **Custom Roles**: If you're importing a IAM resource with a custom role, make sure to use the

         full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] policy_data: The policy data generated by
               a `organizations_get_iam_policy` data source.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        :param pulumi.Input[str] web_backend_service: Used to find the parent resource to bind the IAM policy to
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebBackendServiceIamPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Three different resources help you manage your IAM policy for Identity-Aware Proxy WebBackendService. Each of these resources serves a different use case:

        * `iap.WebBackendServiceIamPolicy`: Authoritative. Sets the IAM policy for the webbackendservice and replaces any existing policy already attached.
        * `iap.WebBackendServiceIamBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the webbackendservice are preserved.
        * `iap.WebBackendServiceIamMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the webbackendservice are preserved.

        A data source can be used to retrieve policy data in advent you do not need creation

        * `iap.WebBackendServiceIamPolicy`: Retrieves the IAM policy for the webbackendservice

        > **Note:** `iap.WebBackendServiceIamPolicy` **cannot** be used in conjunction with `iap.WebBackendServiceIamBinding` and `iap.WebBackendServiceIamMember` or they will fight over what your policy should be.

        > **Note:** `iap.WebBackendServiceIamBinding` resources **can be** used in conjunction with `iap.WebBackendServiceIamMember` resources **only if** they do not grant privilege to the same role.

        > **Note:**  This resource supports IAM Conditions but they have some known limitations which can be found [here](https://cloud.google.com/iam/docs/conditions-overview#limitations). Please review this article if you are having issues with IAM Conditions.

        ## iap.WebBackendServiceIamPolicy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[{
            "role": "roles/iap.httpsResourceAccessor",
            "members": ["user:jane@example.com"],
        }])
        policy = gcp.iap.WebBackendServiceIamPolicy("policy",
            project=default["project"],
            web_backend_service=default["name"],
            policy_data=admin.policy_data)
        ```

        With IAM Conditions:

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[{
            "role": "roles/iap.httpsResourceAccessor",
            "members": ["user:jane@example.com"],
            "condition": {
                "title": "expires_after_2019_12_31",
                "description": "Expiring at midnight of 2019-12-31",
                "expression": "request.time < timestamp(\\"2020-01-01T00:00:00Z\\")",
            },
        }])
        policy = gcp.iap.WebBackendServiceIamPolicy("policy",
            project=default["project"],
            web_backend_service=default["name"],
            policy_data=admin.policy_data)
        ```
        ## iap.WebBackendServiceIamBinding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.iap.WebBackendServiceIamBinding("binding",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            members=["user:jane@example.com"])
        ```

        With IAM Conditions:

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.iap.WebBackendServiceIamBinding("binding",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            members=["user:jane@example.com"],
            condition={
                "title": "expires_after_2019_12_31",
                "description": "Expiring at midnight of 2019-12-31",
                "expression": "request.time < timestamp(\\"2020-01-01T00:00:00Z\\")",
            })
        ```
        ## iap.WebBackendServiceIamMember

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.iap.WebBackendServiceIamMember("member",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            member="user:jane@example.com")
        ```

        With IAM Conditions:

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.iap.WebBackendServiceIamMember("member",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            member="user:jane@example.com",
            condition={
                "title": "expires_after_2019_12_31",
                "description": "Expiring at midnight of 2019-12-31",
                "expression": "request.time < timestamp(\\"2020-01-01T00:00:00Z\\")",
            })
        ```

        ## iap.WebBackendServiceIamPolicy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[{
            "role": "roles/iap.httpsResourceAccessor",
            "members": ["user:jane@example.com"],
        }])
        policy = gcp.iap.WebBackendServiceIamPolicy("policy",
            project=default["project"],
            web_backend_service=default["name"],
            policy_data=admin.policy_data)
        ```

        With IAM Conditions:

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[{
            "role": "roles/iap.httpsResourceAccessor",
            "members": ["user:jane@example.com"],
            "condition": {
                "title": "expires_after_2019_12_31",
                "description": "Expiring at midnight of 2019-12-31",
                "expression": "request.time < timestamp(\\"2020-01-01T00:00:00Z\\")",
            },
        }])
        policy = gcp.iap.WebBackendServiceIamPolicy("policy",
            project=default["project"],
            web_backend_service=default["name"],
            policy_data=admin.policy_data)
        ```
        ## iap.WebBackendServiceIamBinding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.iap.WebBackendServiceIamBinding("binding",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            members=["user:jane@example.com"])
        ```

        With IAM Conditions:

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.iap.WebBackendServiceIamBinding("binding",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            members=["user:jane@example.com"],
            condition={
                "title": "expires_after_2019_12_31",
                "description": "Expiring at midnight of 2019-12-31",
                "expression": "request.time < timestamp(\\"2020-01-01T00:00:00Z\\")",
            })
        ```
        ## iap.WebBackendServiceIamMember

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.iap.WebBackendServiceIamMember("member",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            member="user:jane@example.com")
        ```

        With IAM Conditions:

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.iap.WebBackendServiceIamMember("member",
            project=default["project"],
            web_backend_service=default["name"],
            role="roles/iap.httpsResourceAccessor",
            member="user:jane@example.com",
            condition={
                "title": "expires_after_2019_12_31",
                "description": "Expiring at midnight of 2019-12-31",
                "expression": "request.time < timestamp(\\"2020-01-01T00:00:00Z\\")",
            })
        ```

        ## Import

        For all import syntaxes, the "resource in question" can take any of the following forms:

        * projects/{{project}}/iap_web/compute/services/{{name}}

        * {{project}}/{{name}}

        * {{name}}

        Any variables not passed in the import command will be taken from the provider configuration.

        Identity-Aware Proxy webbackendservice IAM resources can be imported using the resource identifiers, role, and member.

        IAM member imports use space-delimited identifiers: the resource in question, the role, and the member identity, e.g.

        ```sh
        $ pulumi import gcp:iap/webBackendServiceIamPolicy:WebBackendServiceIamPolicy editor "projects/{{project}}/iap_web/compute/services/{{web_backend_service}} roles/iap.httpsResourceAccessor user:jane@example.com"
        ```

        IAM binding imports use space-delimited identifiers: the resource in question and the role, e.g.

        ```sh
        $ pulumi import gcp:iap/webBackendServiceIamPolicy:WebBackendServiceIamPolicy editor "projects/{{project}}/iap_web/compute/services/{{web_backend_service}} roles/iap.httpsResourceAccessor"
        ```

        IAM policy imports use the identifier of the resource in question, e.g.

        ```sh
        $ pulumi import gcp:iap/webBackendServiceIamPolicy:WebBackendServiceIamPolicy editor projects/{{project}}/iap_web/compute/services/{{web_backend_service}}
        ```

        -> **Custom Roles**: If you're importing a IAM resource with a custom role, make sure to use the

         full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.

        :param str resource_name: The name of the resource.
        :param WebBackendServiceIamPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebBackendServiceIamPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_data: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 web_backend_service: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebBackendServiceIamPolicyArgs.__new__(WebBackendServiceIamPolicyArgs)

            if policy_data is None and not opts.urn:
                raise TypeError("Missing required property 'policy_data'")
            __props__.__dict__["policy_data"] = policy_data
            __props__.__dict__["project"] = project
            if web_backend_service is None and not opts.urn:
                raise TypeError("Missing required property 'web_backend_service'")
            __props__.__dict__["web_backend_service"] = web_backend_service
            __props__.__dict__["etag"] = None
        super(WebBackendServiceIamPolicy, __self__).__init__(
            'gcp:iap/webBackendServiceIamPolicy:WebBackendServiceIamPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            etag: Optional[pulumi.Input[str]] = None,
            policy_data: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            web_backend_service: Optional[pulumi.Input[str]] = None) -> 'WebBackendServiceIamPolicy':
        """
        Get an existing WebBackendServiceIamPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] etag: (Computed) The etag of the IAM policy.
        :param pulumi.Input[str] policy_data: The policy data generated by
               a `organizations_get_iam_policy` data source.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        :param pulumi.Input[str] web_backend_service: Used to find the parent resource to bind the IAM policy to
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WebBackendServiceIamPolicyState.__new__(_WebBackendServiceIamPolicyState)

        __props__.__dict__["etag"] = etag
        __props__.__dict__["policy_data"] = policy_data
        __props__.__dict__["project"] = project
        __props__.__dict__["web_backend_service"] = web_backend_service
        return WebBackendServiceIamPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        (Computed) The etag of the IAM policy.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> pulumi.Output[str]:
        """
        The policy data generated by
        a `organizations_get_iam_policy` data source.
        """
        return pulumi.get(self, "policy_data")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="webBackendService")
    def web_backend_service(self) -> pulumi.Output[str]:
        """
        Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "web_backend_service")

