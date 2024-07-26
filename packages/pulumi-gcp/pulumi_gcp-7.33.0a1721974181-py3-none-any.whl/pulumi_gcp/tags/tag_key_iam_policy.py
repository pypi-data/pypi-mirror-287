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

__all__ = ['TagKeyIamPolicyArgs', 'TagKeyIamPolicy']

@pulumi.input_type
class TagKeyIamPolicyArgs:
    def __init__(__self__, *,
                 policy_data: pulumi.Input[str],
                 tag_key: pulumi.Input[str]):
        """
        The set of arguments for constructing a TagKeyIamPolicy resource.
        :param pulumi.Input[str] policy_data: The policy data generated by
               a `organizations_get_iam_policy` data source.
        :param pulumi.Input[str] tag_key: Used to find the parent resource to bind the IAM policy to
        """
        pulumi.set(__self__, "policy_data", policy_data)
        pulumi.set(__self__, "tag_key", tag_key)

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
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> pulumi.Input[str]:
        """
        Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "tag_key")

    @tag_key.setter
    def tag_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "tag_key", value)


@pulumi.input_type
class _TagKeyIamPolicyState:
    def __init__(__self__, *,
                 etag: Optional[pulumi.Input[str]] = None,
                 policy_data: Optional[pulumi.Input[str]] = None,
                 tag_key: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TagKeyIamPolicy resources.
        :param pulumi.Input[str] etag: (Computed) The etag of the IAM policy.
        :param pulumi.Input[str] policy_data: The policy data generated by
               a `organizations_get_iam_policy` data source.
        :param pulumi.Input[str] tag_key: Used to find the parent resource to bind the IAM policy to
        """
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if policy_data is not None:
            pulumi.set(__self__, "policy_data", policy_data)
        if tag_key is not None:
            pulumi.set(__self__, "tag_key", tag_key)

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
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> Optional[pulumi.Input[str]]:
        """
        Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "tag_key")

    @tag_key.setter
    def tag_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tag_key", value)


class TagKeyIamPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_data: Optional[pulumi.Input[str]] = None,
                 tag_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Three different resources help you manage your IAM policy for Tags TagKey. Each of these resources serves a different use case:

        * `tags.TagKeyIamPolicy`: Authoritative. Sets the IAM policy for the tagkey and replaces any existing policy already attached.
        * `tags.TagKeyIamBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the tagkey are preserved.
        * `tags.TagKeyIamMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the tagkey are preserved.

        A data source can be used to retrieve policy data in advent you do not need creation

        * `tags.TagKeyIamPolicy`: Retrieves the IAM policy for the tagkey

        > **Note:** `tags.TagKeyIamPolicy` **cannot** be used in conjunction with `tags.TagKeyIamBinding` and `tags.TagKeyIamMember` or they will fight over what your policy should be.

        > **Note:** `tags.TagKeyIamBinding` resources **can be** used in conjunction with `tags.TagKeyIamMember` resources **only if** they do not grant privilege to the same role.

        ## tags.TagKeyIamPolicy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[{
            "role": "roles/viewer",
            "members": ["user:jane@example.com"],
        }])
        policy = gcp.tags.TagKeyIamPolicy("policy",
            tag_key=key["name"],
            policy_data=admin.policy_data)
        ```

        ## tags.TagKeyIamBinding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.tags.TagKeyIamBinding("binding",
            tag_key=key["name"],
            role="roles/viewer",
            members=["user:jane@example.com"])
        ```

        ## tags.TagKeyIamMember

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.tags.TagKeyIamMember("member",
            tag_key=key["name"],
            role="roles/viewer",
            member="user:jane@example.com")
        ```

        ## tags.TagKeyIamPolicy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[{
            "role": "roles/viewer",
            "members": ["user:jane@example.com"],
        }])
        policy = gcp.tags.TagKeyIamPolicy("policy",
            tag_key=key["name"],
            policy_data=admin.policy_data)
        ```

        ## tags.TagKeyIamBinding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.tags.TagKeyIamBinding("binding",
            tag_key=key["name"],
            role="roles/viewer",
            members=["user:jane@example.com"])
        ```

        ## tags.TagKeyIamMember

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.tags.TagKeyIamMember("member",
            tag_key=key["name"],
            role="roles/viewer",
            member="user:jane@example.com")
        ```

        ## Import

        For all import syntaxes, the "resource in question" can take any of the following forms:

        * tagKeys/{{name}}

        * {{name}}

        Any variables not passed in the import command will be taken from the provider configuration.

        Tags tagkey IAM resources can be imported using the resource identifiers, role, and member.

        IAM member imports use space-delimited identifiers: the resource in question, the role, and the member identity, e.g.

        ```sh
        $ pulumi import gcp:tags/tagKeyIamPolicy:TagKeyIamPolicy editor "tagKeys/{{tag_key}} roles/viewer user:jane@example.com"
        ```

        IAM binding imports use space-delimited identifiers: the resource in question and the role, e.g.

        ```sh
        $ pulumi import gcp:tags/tagKeyIamPolicy:TagKeyIamPolicy editor "tagKeys/{{tag_key}} roles/viewer"
        ```

        IAM policy imports use the identifier of the resource in question, e.g.

        ```sh
        $ pulumi import gcp:tags/tagKeyIamPolicy:TagKeyIamPolicy editor tagKeys/{{tag_key}}
        ```

        -> **Custom Roles**: If you're importing a IAM resource with a custom role, make sure to use the

         full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] policy_data: The policy data generated by
               a `organizations_get_iam_policy` data source.
        :param pulumi.Input[str] tag_key: Used to find the parent resource to bind the IAM policy to
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TagKeyIamPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Three different resources help you manage your IAM policy for Tags TagKey. Each of these resources serves a different use case:

        * `tags.TagKeyIamPolicy`: Authoritative. Sets the IAM policy for the tagkey and replaces any existing policy already attached.
        * `tags.TagKeyIamBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the tagkey are preserved.
        * `tags.TagKeyIamMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the tagkey are preserved.

        A data source can be used to retrieve policy data in advent you do not need creation

        * `tags.TagKeyIamPolicy`: Retrieves the IAM policy for the tagkey

        > **Note:** `tags.TagKeyIamPolicy` **cannot** be used in conjunction with `tags.TagKeyIamBinding` and `tags.TagKeyIamMember` or they will fight over what your policy should be.

        > **Note:** `tags.TagKeyIamBinding` resources **can be** used in conjunction with `tags.TagKeyIamMember` resources **only if** they do not grant privilege to the same role.

        ## tags.TagKeyIamPolicy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[{
            "role": "roles/viewer",
            "members": ["user:jane@example.com"],
        }])
        policy = gcp.tags.TagKeyIamPolicy("policy",
            tag_key=key["name"],
            policy_data=admin.policy_data)
        ```

        ## tags.TagKeyIamBinding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.tags.TagKeyIamBinding("binding",
            tag_key=key["name"],
            role="roles/viewer",
            members=["user:jane@example.com"])
        ```

        ## tags.TagKeyIamMember

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.tags.TagKeyIamMember("member",
            tag_key=key["name"],
            role="roles/viewer",
            member="user:jane@example.com")
        ```

        ## tags.TagKeyIamPolicy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[{
            "role": "roles/viewer",
            "members": ["user:jane@example.com"],
        }])
        policy = gcp.tags.TagKeyIamPolicy("policy",
            tag_key=key["name"],
            policy_data=admin.policy_data)
        ```

        ## tags.TagKeyIamBinding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.tags.TagKeyIamBinding("binding",
            tag_key=key["name"],
            role="roles/viewer",
            members=["user:jane@example.com"])
        ```

        ## tags.TagKeyIamMember

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.tags.TagKeyIamMember("member",
            tag_key=key["name"],
            role="roles/viewer",
            member="user:jane@example.com")
        ```

        ## Import

        For all import syntaxes, the "resource in question" can take any of the following forms:

        * tagKeys/{{name}}

        * {{name}}

        Any variables not passed in the import command will be taken from the provider configuration.

        Tags tagkey IAM resources can be imported using the resource identifiers, role, and member.

        IAM member imports use space-delimited identifiers: the resource in question, the role, and the member identity, e.g.

        ```sh
        $ pulumi import gcp:tags/tagKeyIamPolicy:TagKeyIamPolicy editor "tagKeys/{{tag_key}} roles/viewer user:jane@example.com"
        ```

        IAM binding imports use space-delimited identifiers: the resource in question and the role, e.g.

        ```sh
        $ pulumi import gcp:tags/tagKeyIamPolicy:TagKeyIamPolicy editor "tagKeys/{{tag_key}} roles/viewer"
        ```

        IAM policy imports use the identifier of the resource in question, e.g.

        ```sh
        $ pulumi import gcp:tags/tagKeyIamPolicy:TagKeyIamPolicy editor tagKeys/{{tag_key}}
        ```

        -> **Custom Roles**: If you're importing a IAM resource with a custom role, make sure to use the

         full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.

        :param str resource_name: The name of the resource.
        :param TagKeyIamPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TagKeyIamPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_data: Optional[pulumi.Input[str]] = None,
                 tag_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TagKeyIamPolicyArgs.__new__(TagKeyIamPolicyArgs)

            if policy_data is None and not opts.urn:
                raise TypeError("Missing required property 'policy_data'")
            __props__.__dict__["policy_data"] = policy_data
            if tag_key is None and not opts.urn:
                raise TypeError("Missing required property 'tag_key'")
            __props__.__dict__["tag_key"] = tag_key
            __props__.__dict__["etag"] = None
        super(TagKeyIamPolicy, __self__).__init__(
            'gcp:tags/tagKeyIamPolicy:TagKeyIamPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            etag: Optional[pulumi.Input[str]] = None,
            policy_data: Optional[pulumi.Input[str]] = None,
            tag_key: Optional[pulumi.Input[str]] = None) -> 'TagKeyIamPolicy':
        """
        Get an existing TagKeyIamPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] etag: (Computed) The etag of the IAM policy.
        :param pulumi.Input[str] policy_data: The policy data generated by
               a `organizations_get_iam_policy` data source.
        :param pulumi.Input[str] tag_key: Used to find the parent resource to bind the IAM policy to
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TagKeyIamPolicyState.__new__(_TagKeyIamPolicyState)

        __props__.__dict__["etag"] = etag
        __props__.__dict__["policy_data"] = policy_data
        __props__.__dict__["tag_key"] = tag_key
        return TagKeyIamPolicy(resource_name, opts=opts, __props__=__props__)

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
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> pulumi.Output[str]:
        """
        Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "tag_key")

