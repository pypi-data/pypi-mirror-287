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

__all__ = ['DefaultSupportedIdpConfigArgs', 'DefaultSupportedIdpConfig']

@pulumi.input_type
class DefaultSupportedIdpConfigArgs:
    def __init__(__self__, *,
                 client_id: pulumi.Input[str],
                 client_secret: pulumi.Input[str],
                 idp_id: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DefaultSupportedIdpConfig resource.
        :param pulumi.Input[str] client_id: OAuth client ID
        :param pulumi.Input[str] client_secret: OAuth client secret
               
               
               - - -
        :param pulumi.Input[str] idp_id: ID of the IDP. Possible values include:
               * `apple.com`
               * `facebook.com`
               * `gc.apple.com`
               * `github.com`
               * `google.com`
               * `linkedin.com`
               * `microsoft.com`
               * `playgames.google.com`
               * `twitter.com`
               * `yahoo.com`
        :param pulumi.Input[bool] enabled: If this IDP allows the user to sign in
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "client_secret", client_secret)
        pulumi.set(__self__, "idp_id", idp_id)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[str]:
        """
        OAuth client ID
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[str]:
        """
        OAuth client secret


        - - -
        """
        return pulumi.get(self, "client_secret")

    @client_secret.setter
    def client_secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_secret", value)

    @property
    @pulumi.getter(name="idpId")
    def idp_id(self) -> pulumi.Input[str]:
        """
        ID of the IDP. Possible values include:
        * `apple.com`
        * `facebook.com`
        * `gc.apple.com`
        * `github.com`
        * `google.com`
        * `linkedin.com`
        * `microsoft.com`
        * `playgames.google.com`
        * `twitter.com`
        * `yahoo.com`
        """
        return pulumi.get(self, "idp_id")

    @idp_id.setter
    def idp_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "idp_id", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If this IDP allows the user to sign in
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

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


@pulumi.input_type
class _DefaultSupportedIdpConfigState:
    def __init__(__self__, *,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 idp_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DefaultSupportedIdpConfig resources.
        :param pulumi.Input[str] client_id: OAuth client ID
        :param pulumi.Input[str] client_secret: OAuth client secret
               
               
               - - -
        :param pulumi.Input[bool] enabled: If this IDP allows the user to sign in
        :param pulumi.Input[str] idp_id: ID of the IDP. Possible values include:
               * `apple.com`
               * `facebook.com`
               * `gc.apple.com`
               * `github.com`
               * `google.com`
               * `linkedin.com`
               * `microsoft.com`
               * `playgames.google.com`
               * `twitter.com`
               * `yahoo.com`
        :param pulumi.Input[str] name: The name of the DefaultSupportedIdpConfig resource
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if client_secret is not None:
            pulumi.set(__self__, "client_secret", client_secret)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if idp_id is not None:
            pulumi.set(__self__, "idp_id", idp_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        OAuth client ID
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[str]]:
        """
        OAuth client secret


        - - -
        """
        return pulumi.get(self, "client_secret")

    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_secret", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If this IDP allows the user to sign in
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="idpId")
    def idp_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the IDP. Possible values include:
        * `apple.com`
        * `facebook.com`
        * `gc.apple.com`
        * `github.com`
        * `google.com`
        * `linkedin.com`
        * `microsoft.com`
        * `playgames.google.com`
        * `twitter.com`
        * `yahoo.com`
        """
        return pulumi.get(self, "idp_id")

    @idp_id.setter
    def idp_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "idp_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the DefaultSupportedIdpConfig resource
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


class DefaultSupportedIdpConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 idp_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Configurations options for authenticating with a the standard set of Identity Toolkit-trusted IDPs.

        You must enable the
        [Google Identity Platform](https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity) in
        the marketplace prior to using this resource.

        ## Example Usage

        ### Identity Platform Default Supported Idp Config Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        idp_config = gcp.identityplatform.DefaultSupportedIdpConfig("idp_config",
            enabled=True,
            idp_id="playgames.google.com",
            client_id="client-id",
            client_secret="secret")
        ```

        ## Import

        DefaultSupportedIdpConfig can be imported using any of these accepted formats:

        * `projects/{{project}}/defaultSupportedIdpConfigs/{{idp_id}}`

        * `{{project}}/{{idp_id}}`

        * `{{idp_id}}`

        When using the `pulumi import` command, DefaultSupportedIdpConfig can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:identityplatform/defaultSupportedIdpConfig:DefaultSupportedIdpConfig default projects/{{project}}/defaultSupportedIdpConfigs/{{idp_id}}
        ```

        ```sh
        $ pulumi import gcp:identityplatform/defaultSupportedIdpConfig:DefaultSupportedIdpConfig default {{project}}/{{idp_id}}
        ```

        ```sh
        $ pulumi import gcp:identityplatform/defaultSupportedIdpConfig:DefaultSupportedIdpConfig default {{idp_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_id: OAuth client ID
        :param pulumi.Input[str] client_secret: OAuth client secret
               
               
               - - -
        :param pulumi.Input[bool] enabled: If this IDP allows the user to sign in
        :param pulumi.Input[str] idp_id: ID of the IDP. Possible values include:
               * `apple.com`
               * `facebook.com`
               * `gc.apple.com`
               * `github.com`
               * `google.com`
               * `linkedin.com`
               * `microsoft.com`
               * `playgames.google.com`
               * `twitter.com`
               * `yahoo.com`
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DefaultSupportedIdpConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Configurations options for authenticating with a the standard set of Identity Toolkit-trusted IDPs.

        You must enable the
        [Google Identity Platform](https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity) in
        the marketplace prior to using this resource.

        ## Example Usage

        ### Identity Platform Default Supported Idp Config Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        idp_config = gcp.identityplatform.DefaultSupportedIdpConfig("idp_config",
            enabled=True,
            idp_id="playgames.google.com",
            client_id="client-id",
            client_secret="secret")
        ```

        ## Import

        DefaultSupportedIdpConfig can be imported using any of these accepted formats:

        * `projects/{{project}}/defaultSupportedIdpConfigs/{{idp_id}}`

        * `{{project}}/{{idp_id}}`

        * `{{idp_id}}`

        When using the `pulumi import` command, DefaultSupportedIdpConfig can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:identityplatform/defaultSupportedIdpConfig:DefaultSupportedIdpConfig default projects/{{project}}/defaultSupportedIdpConfigs/{{idp_id}}
        ```

        ```sh
        $ pulumi import gcp:identityplatform/defaultSupportedIdpConfig:DefaultSupportedIdpConfig default {{project}}/{{idp_id}}
        ```

        ```sh
        $ pulumi import gcp:identityplatform/defaultSupportedIdpConfig:DefaultSupportedIdpConfig default {{idp_id}}
        ```

        :param str resource_name: The name of the resource.
        :param DefaultSupportedIdpConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DefaultSupportedIdpConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 idp_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DefaultSupportedIdpConfigArgs.__new__(DefaultSupportedIdpConfigArgs)

            if client_id is None and not opts.urn:
                raise TypeError("Missing required property 'client_id'")
            __props__.__dict__["client_id"] = client_id
            if client_secret is None and not opts.urn:
                raise TypeError("Missing required property 'client_secret'")
            __props__.__dict__["client_secret"] = client_secret
            __props__.__dict__["enabled"] = enabled
            if idp_id is None and not opts.urn:
                raise TypeError("Missing required property 'idp_id'")
            __props__.__dict__["idp_id"] = idp_id
            __props__.__dict__["project"] = project
            __props__.__dict__["name"] = None
        super(DefaultSupportedIdpConfig, __self__).__init__(
            'gcp:identityplatform/defaultSupportedIdpConfig:DefaultSupportedIdpConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            client_id: Optional[pulumi.Input[str]] = None,
            client_secret: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            idp_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'DefaultSupportedIdpConfig':
        """
        Get an existing DefaultSupportedIdpConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_id: OAuth client ID
        :param pulumi.Input[str] client_secret: OAuth client secret
               
               
               - - -
        :param pulumi.Input[bool] enabled: If this IDP allows the user to sign in
        :param pulumi.Input[str] idp_id: ID of the IDP. Possible values include:
               * `apple.com`
               * `facebook.com`
               * `gc.apple.com`
               * `github.com`
               * `google.com`
               * `linkedin.com`
               * `microsoft.com`
               * `playgames.google.com`
               * `twitter.com`
               * `yahoo.com`
        :param pulumi.Input[str] name: The name of the DefaultSupportedIdpConfig resource
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DefaultSupportedIdpConfigState.__new__(_DefaultSupportedIdpConfigState)

        __props__.__dict__["client_id"] = client_id
        __props__.__dict__["client_secret"] = client_secret
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["idp_id"] = idp_id
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        return DefaultSupportedIdpConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[str]:
        """
        OAuth client ID
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Output[str]:
        """
        OAuth client secret


        - - -
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        If this IDP allows the user to sign in
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="idpId")
    def idp_id(self) -> pulumi.Output[str]:
        """
        ID of the IDP. Possible values include:
        * `apple.com`
        * `facebook.com`
        * `gc.apple.com`
        * `github.com`
        * `google.com`
        * `linkedin.com`
        * `microsoft.com`
        * `playgames.google.com`
        * `twitter.com`
        * `yahoo.com`
        """
        return pulumi.get(self, "idp_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the DefaultSupportedIdpConfig resource
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

