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

__all__ = ['AppCheckRecaptchaV3ConfigArgs', 'AppCheckRecaptchaV3Config']

@pulumi.input_type
class AppCheckRecaptchaV3ConfigArgs:
    def __init__(__self__, *,
                 app_id: pulumi.Input[str],
                 site_secret: pulumi.Input[str],
                 project: Optional[pulumi.Input[str]] = None,
                 token_ttl: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AppCheckRecaptchaV3Config resource.
        :param pulumi.Input[str] app_id: The ID of an
               [Web App](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id).
               
               
               - - -
        :param pulumi.Input[str] site_secret: The site secret used to identify your service for reCAPTCHA v3 verification.
               For security reasons, this field will never be populated in any response.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] token_ttl: Specifies the duration for which App Check tokens exchanged from reCAPTCHA V3 artifacts will be valid.
               If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive.
               A duration in seconds with up to nine fractional digits, ending with 's'. Example: "3.5s".
        """
        pulumi.set(__self__, "app_id", app_id)
        pulumi.set(__self__, "site_secret", site_secret)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if token_ttl is not None:
            pulumi.set(__self__, "token_ttl", token_ttl)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[str]:
        """
        The ID of an
        [Web App](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id).


        - - -
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter(name="siteSecret")
    def site_secret(self) -> pulumi.Input[str]:
        """
        The site secret used to identify your service for reCAPTCHA v3 verification.
        For security reasons, this field will never be populated in any response.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "site_secret")

    @site_secret.setter
    def site_secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "site_secret", value)

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
    @pulumi.getter(name="tokenTtl")
    def token_ttl(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the duration for which App Check tokens exchanged from reCAPTCHA V3 artifacts will be valid.
        If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive.
        A duration in seconds with up to nine fractional digits, ending with 's'. Example: "3.5s".
        """
        return pulumi.get(self, "token_ttl")

    @token_ttl.setter
    def token_ttl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token_ttl", value)


@pulumi.input_type
class _AppCheckRecaptchaV3ConfigState:
    def __init__(__self__, *,
                 app_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 site_secret: Optional[pulumi.Input[str]] = None,
                 site_secret_set: Optional[pulumi.Input[bool]] = None,
                 token_ttl: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AppCheckRecaptchaV3Config resources.
        :param pulumi.Input[str] app_id: The ID of an
               [Web App](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id).
               
               
               - - -
        :param pulumi.Input[str] name: The relative resource name of the reCAPTCHA V3 configuration object
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] site_secret: The site secret used to identify your service for reCAPTCHA v3 verification.
               For security reasons, this field will never be populated in any response.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[bool] site_secret_set: Whether the siteSecret was previously set. Since we will never return the siteSecret field, this field is the only way to find out whether it was previously set.
        :param pulumi.Input[str] token_ttl: Specifies the duration for which App Check tokens exchanged from reCAPTCHA V3 artifacts will be valid.
               If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive.
               A duration in seconds with up to nine fractional digits, ending with 's'. Example: "3.5s".
        """
        if app_id is not None:
            pulumi.set(__self__, "app_id", app_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if site_secret is not None:
            pulumi.set(__self__, "site_secret", site_secret)
        if site_secret_set is not None:
            pulumi.set(__self__, "site_secret_set", site_secret_set)
        if token_ttl is not None:
            pulumi.set(__self__, "token_ttl", token_ttl)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of an
        [Web App](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id).


        - - -
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The relative resource name of the reCAPTCHA V3 configuration object
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
    @pulumi.getter(name="siteSecret")
    def site_secret(self) -> Optional[pulumi.Input[str]]:
        """
        The site secret used to identify your service for reCAPTCHA v3 verification.
        For security reasons, this field will never be populated in any response.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "site_secret")

    @site_secret.setter
    def site_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "site_secret", value)

    @property
    @pulumi.getter(name="siteSecretSet")
    def site_secret_set(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the siteSecret was previously set. Since we will never return the siteSecret field, this field is the only way to find out whether it was previously set.
        """
        return pulumi.get(self, "site_secret_set")

    @site_secret_set.setter
    def site_secret_set(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "site_secret_set", value)

    @property
    @pulumi.getter(name="tokenTtl")
    def token_ttl(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the duration for which App Check tokens exchanged from reCAPTCHA V3 artifacts will be valid.
        If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive.
        A duration in seconds with up to nine fractional digits, ending with 's'. Example: "3.5s".
        """
        return pulumi.get(self, "token_ttl")

    @token_ttl.setter
    def token_ttl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token_ttl", value)


class AppCheckRecaptchaV3Config(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 site_secret: Optional[pulumi.Input[str]] = None,
                 token_ttl: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An app's reCAPTCHA V3 configuration object.

        To get more information about RecaptchaV3Config, see:

        * [API documentation](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config)
        * How-to Guides
            * [Official Documentation](https://firebase.google.com/docs/app-check)

        ## Example Usage

        ### Firebase App Check Recaptcha V3 Config Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp
        import pulumi_time as time

        default = gcp.firebase.WebApp("default",
            project="my-project-name",
            display_name="Web App for reCAPTCHA V3")
        # It takes a while for App Check to recognize the new app
        # If your app already exists, you don't have to wait 30 seconds.
        wait30s = time.index.Sleep("wait_30s", create_duration=30s,
        opts = pulumi.ResourceOptions(depends_on=[default]))
        default_app_check_recaptcha_v3_config = gcp.firebase.AppCheckRecaptchaV3Config("default",
            project="my-project-name",
            app_id=default.app_id,
            site_secret="6Lf9YnQpAAAAAC3-MHmdAllTbPwTZxpUw5d34YzX",
            token_ttl="7200s",
            opts = pulumi.ResourceOptions(depends_on=[wait30s]))
        ```

        ## Import

        RecaptchaV3Config can be imported using any of these accepted formats:

        * `projects/{{project}}/apps/{{app_id}}/recaptchaV3Config`

        * `{{project}}/{{app_id}}`

        * `{{app_id}}`

        When using the `pulumi import` command, RecaptchaV3Config can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:firebase/appCheckRecaptchaV3Config:AppCheckRecaptchaV3Config default projects/{{project}}/apps/{{app_id}}/recaptchaV3Config
        ```

        ```sh
        $ pulumi import gcp:firebase/appCheckRecaptchaV3Config:AppCheckRecaptchaV3Config default {{project}}/{{app_id}}
        ```

        ```sh
        $ pulumi import gcp:firebase/appCheckRecaptchaV3Config:AppCheckRecaptchaV3Config default {{app_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_id: The ID of an
               [Web App](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id).
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] site_secret: The site secret used to identify your service for reCAPTCHA v3 verification.
               For security reasons, this field will never be populated in any response.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] token_ttl: Specifies the duration for which App Check tokens exchanged from reCAPTCHA V3 artifacts will be valid.
               If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive.
               A duration in seconds with up to nine fractional digits, ending with 's'. Example: "3.5s".
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppCheckRecaptchaV3ConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An app's reCAPTCHA V3 configuration object.

        To get more information about RecaptchaV3Config, see:

        * [API documentation](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config)
        * How-to Guides
            * [Official Documentation](https://firebase.google.com/docs/app-check)

        ## Example Usage

        ### Firebase App Check Recaptcha V3 Config Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp
        import pulumi_time as time

        default = gcp.firebase.WebApp("default",
            project="my-project-name",
            display_name="Web App for reCAPTCHA V3")
        # It takes a while for App Check to recognize the new app
        # If your app already exists, you don't have to wait 30 seconds.
        wait30s = time.index.Sleep("wait_30s", create_duration=30s,
        opts = pulumi.ResourceOptions(depends_on=[default]))
        default_app_check_recaptcha_v3_config = gcp.firebase.AppCheckRecaptchaV3Config("default",
            project="my-project-name",
            app_id=default.app_id,
            site_secret="6Lf9YnQpAAAAAC3-MHmdAllTbPwTZxpUw5d34YzX",
            token_ttl="7200s",
            opts = pulumi.ResourceOptions(depends_on=[wait30s]))
        ```

        ## Import

        RecaptchaV3Config can be imported using any of these accepted formats:

        * `projects/{{project}}/apps/{{app_id}}/recaptchaV3Config`

        * `{{project}}/{{app_id}}`

        * `{{app_id}}`

        When using the `pulumi import` command, RecaptchaV3Config can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:firebase/appCheckRecaptchaV3Config:AppCheckRecaptchaV3Config default projects/{{project}}/apps/{{app_id}}/recaptchaV3Config
        ```

        ```sh
        $ pulumi import gcp:firebase/appCheckRecaptchaV3Config:AppCheckRecaptchaV3Config default {{project}}/{{app_id}}
        ```

        ```sh
        $ pulumi import gcp:firebase/appCheckRecaptchaV3Config:AppCheckRecaptchaV3Config default {{app_id}}
        ```

        :param str resource_name: The name of the resource.
        :param AppCheckRecaptchaV3ConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppCheckRecaptchaV3ConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 site_secret: Optional[pulumi.Input[str]] = None,
                 token_ttl: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AppCheckRecaptchaV3ConfigArgs.__new__(AppCheckRecaptchaV3ConfigArgs)

            if app_id is None and not opts.urn:
                raise TypeError("Missing required property 'app_id'")
            __props__.__dict__["app_id"] = app_id
            __props__.__dict__["project"] = project
            if site_secret is None and not opts.urn:
                raise TypeError("Missing required property 'site_secret'")
            __props__.__dict__["site_secret"] = None if site_secret is None else pulumi.Output.secret(site_secret)
            __props__.__dict__["token_ttl"] = token_ttl
            __props__.__dict__["name"] = None
            __props__.__dict__["site_secret_set"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["siteSecret"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(AppCheckRecaptchaV3Config, __self__).__init__(
            'gcp:firebase/appCheckRecaptchaV3Config:AppCheckRecaptchaV3Config',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            site_secret: Optional[pulumi.Input[str]] = None,
            site_secret_set: Optional[pulumi.Input[bool]] = None,
            token_ttl: Optional[pulumi.Input[str]] = None) -> 'AppCheckRecaptchaV3Config':
        """
        Get an existing AppCheckRecaptchaV3Config resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_id: The ID of an
               [Web App](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id).
               
               
               - - -
        :param pulumi.Input[str] name: The relative resource name of the reCAPTCHA V3 configuration object
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] site_secret: The site secret used to identify your service for reCAPTCHA v3 verification.
               For security reasons, this field will never be populated in any response.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[bool] site_secret_set: Whether the siteSecret was previously set. Since we will never return the siteSecret field, this field is the only way to find out whether it was previously set.
        :param pulumi.Input[str] token_ttl: Specifies the duration for which App Check tokens exchanged from reCAPTCHA V3 artifacts will be valid.
               If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive.
               A duration in seconds with up to nine fractional digits, ending with 's'. Example: "3.5s".
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AppCheckRecaptchaV3ConfigState.__new__(_AppCheckRecaptchaV3ConfigState)

        __props__.__dict__["app_id"] = app_id
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["site_secret"] = site_secret
        __props__.__dict__["site_secret_set"] = site_secret_set
        __props__.__dict__["token_ttl"] = token_ttl
        return AppCheckRecaptchaV3Config(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[str]:
        """
        The ID of an
        [Web App](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id).


        - - -
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The relative resource name of the reCAPTCHA V3 configuration object
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
    @pulumi.getter(name="siteSecret")
    def site_secret(self) -> pulumi.Output[str]:
        """
        The site secret used to identify your service for reCAPTCHA v3 verification.
        For security reasons, this field will never be populated in any response.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "site_secret")

    @property
    @pulumi.getter(name="siteSecretSet")
    def site_secret_set(self) -> pulumi.Output[bool]:
        """
        Whether the siteSecret was previously set. Since we will never return the siteSecret field, this field is the only way to find out whether it was previously set.
        """
        return pulumi.get(self, "site_secret_set")

    @property
    @pulumi.getter(name="tokenTtl")
    def token_ttl(self) -> pulumi.Output[str]:
        """
        Specifies the duration for which App Check tokens exchanged from reCAPTCHA V3 artifacts will be valid.
        If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive.
        A duration in seconds with up to nine fractional digits, ending with 's'. Example: "3.5s".
        """
        return pulumi.get(self, "token_ttl")

