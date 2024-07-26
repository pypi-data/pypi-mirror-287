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

__all__ = ['TenantInboundSamlConfigArgs', 'TenantInboundSamlConfig']

@pulumi.input_type
class TenantInboundSamlConfigArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 idp_config: pulumi.Input['TenantInboundSamlConfigIdpConfigArgs'],
                 sp_config: pulumi.Input['TenantInboundSamlConfigSpConfigArgs'],
                 tenant: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TenantInboundSamlConfig resource.
        :param pulumi.Input[str] display_name: Human friendly display name.
        :param pulumi.Input['TenantInboundSamlConfigIdpConfigArgs'] idp_config: SAML IdP configuration when the project acts as the relying party
               Structure is documented below.
        :param pulumi.Input['TenantInboundSamlConfigSpConfigArgs'] sp_config: SAML SP (Service Provider) configuration when the project acts as the relying party to receive
               and accept an authentication assertion issued by a SAML identity provider.
               Structure is documented below.
        :param pulumi.Input[str] tenant: The name of the tenant where this inbound SAML config resource exists
        :param pulumi.Input[bool] enabled: If this config allows users to sign in with the provider.
        :param pulumi.Input[str] name: The name of the InboundSamlConfig resource. Must start with 'saml.' and can only have alphanumeric characters,
               hyphens, underscores or periods. The part after 'saml.' must also start with a lowercase letter, end with an
               alphanumeric character, and have at least 2 characters.
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "idp_config", idp_config)
        pulumi.set(__self__, "sp_config", sp_config)
        pulumi.set(__self__, "tenant", tenant)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        Human friendly display name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="idpConfig")
    def idp_config(self) -> pulumi.Input['TenantInboundSamlConfigIdpConfigArgs']:
        """
        SAML IdP configuration when the project acts as the relying party
        Structure is documented below.
        """
        return pulumi.get(self, "idp_config")

    @idp_config.setter
    def idp_config(self, value: pulumi.Input['TenantInboundSamlConfigIdpConfigArgs']):
        pulumi.set(self, "idp_config", value)

    @property
    @pulumi.getter(name="spConfig")
    def sp_config(self) -> pulumi.Input['TenantInboundSamlConfigSpConfigArgs']:
        """
        SAML SP (Service Provider) configuration when the project acts as the relying party to receive
        and accept an authentication assertion issued by a SAML identity provider.
        Structure is documented below.
        """
        return pulumi.get(self, "sp_config")

    @sp_config.setter
    def sp_config(self, value: pulumi.Input['TenantInboundSamlConfigSpConfigArgs']):
        pulumi.set(self, "sp_config", value)

    @property
    @pulumi.getter
    def tenant(self) -> pulumi.Input[str]:
        """
        The name of the tenant where this inbound SAML config resource exists
        """
        return pulumi.get(self, "tenant")

    @tenant.setter
    def tenant(self, value: pulumi.Input[str]):
        pulumi.set(self, "tenant", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If this config allows users to sign in with the provider.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the InboundSamlConfig resource. Must start with 'saml.' and can only have alphanumeric characters,
        hyphens, underscores or periods. The part after 'saml.' must also start with a lowercase letter, end with an
        alphanumeric character, and have at least 2 characters.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _TenantInboundSamlConfigState:
    def __init__(__self__, *,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 idp_config: Optional[pulumi.Input['TenantInboundSamlConfigIdpConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 sp_config: Optional[pulumi.Input['TenantInboundSamlConfigSpConfigArgs']] = None,
                 tenant: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TenantInboundSamlConfig resources.
        :param pulumi.Input[str] display_name: Human friendly display name.
        :param pulumi.Input[bool] enabled: If this config allows users to sign in with the provider.
        :param pulumi.Input['TenantInboundSamlConfigIdpConfigArgs'] idp_config: SAML IdP configuration when the project acts as the relying party
               Structure is documented below.
        :param pulumi.Input[str] name: The name of the InboundSamlConfig resource. Must start with 'saml.' and can only have alphanumeric characters,
               hyphens, underscores or periods. The part after 'saml.' must also start with a lowercase letter, end with an
               alphanumeric character, and have at least 2 characters.
        :param pulumi.Input['TenantInboundSamlConfigSpConfigArgs'] sp_config: SAML SP (Service Provider) configuration when the project acts as the relying party to receive
               and accept an authentication assertion issued by a SAML identity provider.
               Structure is documented below.
        :param pulumi.Input[str] tenant: The name of the tenant where this inbound SAML config resource exists
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if idp_config is not None:
            pulumi.set(__self__, "idp_config", idp_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if sp_config is not None:
            pulumi.set(__self__, "sp_config", sp_config)
        if tenant is not None:
            pulumi.set(__self__, "tenant", tenant)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Human friendly display name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If this config allows users to sign in with the provider.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="idpConfig")
    def idp_config(self) -> Optional[pulumi.Input['TenantInboundSamlConfigIdpConfigArgs']]:
        """
        SAML IdP configuration when the project acts as the relying party
        Structure is documented below.
        """
        return pulumi.get(self, "idp_config")

    @idp_config.setter
    def idp_config(self, value: Optional[pulumi.Input['TenantInboundSamlConfigIdpConfigArgs']]):
        pulumi.set(self, "idp_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the InboundSamlConfig resource. Must start with 'saml.' and can only have alphanumeric characters,
        hyphens, underscores or periods. The part after 'saml.' must also start with a lowercase letter, end with an
        alphanumeric character, and have at least 2 characters.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="spConfig")
    def sp_config(self) -> Optional[pulumi.Input['TenantInboundSamlConfigSpConfigArgs']]:
        """
        SAML SP (Service Provider) configuration when the project acts as the relying party to receive
        and accept an authentication assertion issued by a SAML identity provider.
        Structure is documented below.
        """
        return pulumi.get(self, "sp_config")

    @sp_config.setter
    def sp_config(self, value: Optional[pulumi.Input['TenantInboundSamlConfigSpConfigArgs']]):
        pulumi.set(self, "sp_config", value)

    @property
    @pulumi.getter
    def tenant(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the tenant where this inbound SAML config resource exists
        """
        return pulumi.get(self, "tenant")

    @tenant.setter
    def tenant(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant", value)


class TenantInboundSamlConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 idp_config: Optional[pulumi.Input[Union['TenantInboundSamlConfigIdpConfigArgs', 'TenantInboundSamlConfigIdpConfigArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 sp_config: Optional[pulumi.Input[Union['TenantInboundSamlConfigSpConfigArgs', 'TenantInboundSamlConfigSpConfigArgsDict']]] = None,
                 tenant: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Inbound SAML configuration for a Identity Toolkit tenant.

        You must enable the
        [Google Identity Platform](https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity) in
        the marketplace prior to using this resource.

        ## Example Usage

        ### Identity Platform Tenant Inbound Saml Config Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp
        import pulumi_std as std

        tenant = gcp.identityplatform.Tenant("tenant", display_name="tenant")
        tenant_saml_config = gcp.identityplatform.TenantInboundSamlConfig("tenant_saml_config",
            name="saml.tf-config",
            display_name="Display Name",
            tenant=tenant.name,
            idp_config={
                "idp_entity_id": "tf-idp",
                "sign_request": True,
                "sso_url": "https://example.com",
                "idp_certificates": [{
                    "x509_certificate": std.file(input="test-fixtures/rsa_cert.pem").result,
                }],
            },
            sp_config={
                "sp_entity_id": "tf-sp",
                "callback_uri": "https://example.com",
            })
        ```

        ## Import

        TenantInboundSamlConfig can be imported using any of these accepted formats:

        * `projects/{{project}}/tenants/{{tenant}}/inboundSamlConfigs/{{name}}`

        * `{{project}}/{{tenant}}/{{name}}`

        * `{{tenant}}/{{name}}`

        When using the `pulumi import` command, TenantInboundSamlConfig can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:identityplatform/tenantInboundSamlConfig:TenantInboundSamlConfig default projects/{{project}}/tenants/{{tenant}}/inboundSamlConfigs/{{name}}
        ```

        ```sh
        $ pulumi import gcp:identityplatform/tenantInboundSamlConfig:TenantInboundSamlConfig default {{project}}/{{tenant}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:identityplatform/tenantInboundSamlConfig:TenantInboundSamlConfig default {{tenant}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Human friendly display name.
        :param pulumi.Input[bool] enabled: If this config allows users to sign in with the provider.
        :param pulumi.Input[Union['TenantInboundSamlConfigIdpConfigArgs', 'TenantInboundSamlConfigIdpConfigArgsDict']] idp_config: SAML IdP configuration when the project acts as the relying party
               Structure is documented below.
        :param pulumi.Input[str] name: The name of the InboundSamlConfig resource. Must start with 'saml.' and can only have alphanumeric characters,
               hyphens, underscores or periods. The part after 'saml.' must also start with a lowercase letter, end with an
               alphanumeric character, and have at least 2 characters.
        :param pulumi.Input[Union['TenantInboundSamlConfigSpConfigArgs', 'TenantInboundSamlConfigSpConfigArgsDict']] sp_config: SAML SP (Service Provider) configuration when the project acts as the relying party to receive
               and accept an authentication assertion issued by a SAML identity provider.
               Structure is documented below.
        :param pulumi.Input[str] tenant: The name of the tenant where this inbound SAML config resource exists
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TenantInboundSamlConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Inbound SAML configuration for a Identity Toolkit tenant.

        You must enable the
        [Google Identity Platform](https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity) in
        the marketplace prior to using this resource.

        ## Example Usage

        ### Identity Platform Tenant Inbound Saml Config Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp
        import pulumi_std as std

        tenant = gcp.identityplatform.Tenant("tenant", display_name="tenant")
        tenant_saml_config = gcp.identityplatform.TenantInboundSamlConfig("tenant_saml_config",
            name="saml.tf-config",
            display_name="Display Name",
            tenant=tenant.name,
            idp_config={
                "idp_entity_id": "tf-idp",
                "sign_request": True,
                "sso_url": "https://example.com",
                "idp_certificates": [{
                    "x509_certificate": std.file(input="test-fixtures/rsa_cert.pem").result,
                }],
            },
            sp_config={
                "sp_entity_id": "tf-sp",
                "callback_uri": "https://example.com",
            })
        ```

        ## Import

        TenantInboundSamlConfig can be imported using any of these accepted formats:

        * `projects/{{project}}/tenants/{{tenant}}/inboundSamlConfigs/{{name}}`

        * `{{project}}/{{tenant}}/{{name}}`

        * `{{tenant}}/{{name}}`

        When using the `pulumi import` command, TenantInboundSamlConfig can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:identityplatform/tenantInboundSamlConfig:TenantInboundSamlConfig default projects/{{project}}/tenants/{{tenant}}/inboundSamlConfigs/{{name}}
        ```

        ```sh
        $ pulumi import gcp:identityplatform/tenantInboundSamlConfig:TenantInboundSamlConfig default {{project}}/{{tenant}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:identityplatform/tenantInboundSamlConfig:TenantInboundSamlConfig default {{tenant}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param TenantInboundSamlConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TenantInboundSamlConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 idp_config: Optional[pulumi.Input[Union['TenantInboundSamlConfigIdpConfigArgs', 'TenantInboundSamlConfigIdpConfigArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 sp_config: Optional[pulumi.Input[Union['TenantInboundSamlConfigSpConfigArgs', 'TenantInboundSamlConfigSpConfigArgsDict']]] = None,
                 tenant: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TenantInboundSamlConfigArgs.__new__(TenantInboundSamlConfigArgs)

            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["enabled"] = enabled
            if idp_config is None and not opts.urn:
                raise TypeError("Missing required property 'idp_config'")
            __props__.__dict__["idp_config"] = idp_config
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            if sp_config is None and not opts.urn:
                raise TypeError("Missing required property 'sp_config'")
            __props__.__dict__["sp_config"] = sp_config
            if tenant is None and not opts.urn:
                raise TypeError("Missing required property 'tenant'")
            __props__.__dict__["tenant"] = tenant
        super(TenantInboundSamlConfig, __self__).__init__(
            'gcp:identityplatform/tenantInboundSamlConfig:TenantInboundSamlConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            idp_config: Optional[pulumi.Input[Union['TenantInboundSamlConfigIdpConfigArgs', 'TenantInboundSamlConfigIdpConfigArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            sp_config: Optional[pulumi.Input[Union['TenantInboundSamlConfigSpConfigArgs', 'TenantInboundSamlConfigSpConfigArgsDict']]] = None,
            tenant: Optional[pulumi.Input[str]] = None) -> 'TenantInboundSamlConfig':
        """
        Get an existing TenantInboundSamlConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Human friendly display name.
        :param pulumi.Input[bool] enabled: If this config allows users to sign in with the provider.
        :param pulumi.Input[Union['TenantInboundSamlConfigIdpConfigArgs', 'TenantInboundSamlConfigIdpConfigArgsDict']] idp_config: SAML IdP configuration when the project acts as the relying party
               Structure is documented below.
        :param pulumi.Input[str] name: The name of the InboundSamlConfig resource. Must start with 'saml.' and can only have alphanumeric characters,
               hyphens, underscores or periods. The part after 'saml.' must also start with a lowercase letter, end with an
               alphanumeric character, and have at least 2 characters.
        :param pulumi.Input[Union['TenantInboundSamlConfigSpConfigArgs', 'TenantInboundSamlConfigSpConfigArgsDict']] sp_config: SAML SP (Service Provider) configuration when the project acts as the relying party to receive
               and accept an authentication assertion issued by a SAML identity provider.
               Structure is documented below.
        :param pulumi.Input[str] tenant: The name of the tenant where this inbound SAML config resource exists
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TenantInboundSamlConfigState.__new__(_TenantInboundSamlConfigState)

        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["idp_config"] = idp_config
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["sp_config"] = sp_config
        __props__.__dict__["tenant"] = tenant
        return TenantInboundSamlConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Human friendly display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        If this config allows users to sign in with the provider.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="idpConfig")
    def idp_config(self) -> pulumi.Output['outputs.TenantInboundSamlConfigIdpConfig']:
        """
        SAML IdP configuration when the project acts as the relying party
        Structure is documented below.
        """
        return pulumi.get(self, "idp_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the InboundSamlConfig resource. Must start with 'saml.' and can only have alphanumeric characters,
        hyphens, underscores or periods. The part after 'saml.' must also start with a lowercase letter, end with an
        alphanumeric character, and have at least 2 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="spConfig")
    def sp_config(self) -> pulumi.Output['outputs.TenantInboundSamlConfigSpConfig']:
        """
        SAML SP (Service Provider) configuration when the project acts as the relying party to receive
        and accept an authentication assertion issued by a SAML identity provider.
        Structure is documented below.
        """
        return pulumi.get(self, "sp_config")

    @property
    @pulumi.getter
    def tenant(self) -> pulumi.Output[str]:
        """
        The name of the tenant where this inbound SAML config resource exists
        """
        return pulumi.get(self, "tenant")

