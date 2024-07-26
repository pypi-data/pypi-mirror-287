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

__all__ = ['WebAppArgs', 'WebApp']

@pulumi.input_type
class WebAppArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 api_key_id: Optional[pulumi.Input[str]] = None,
                 deletion_policy: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WebApp resource.
        :param pulumi.Input[str] display_name: The user-assigned display name of the App.
               
               
               - - -
        :param pulumi.Input[str] api_key_id: The globally unique, Google-assigned identifier (UID) for the Firebase API key associated with the WebApp.
               If apiKeyId is not set during creation, then Firebase automatically associates an apiKeyId with the WebApp.
               This auto-associated key may be an existing valid key or, if no valid key exists, a new one will be provisioned.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        pulumi.set(__self__, "display_name", display_name)
        if api_key_id is not None:
            pulumi.set(__self__, "api_key_id", api_key_id)
        if deletion_policy is not None:
            pulumi.set(__self__, "deletion_policy", deletion_policy)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The user-assigned display name of the App.


        - - -
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="apiKeyId")
    def api_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The globally unique, Google-assigned identifier (UID) for the Firebase API key associated with the WebApp.
        If apiKeyId is not set during creation, then Firebase automatically associates an apiKeyId with the WebApp.
        This auto-associated key may be an existing valid key or, if no valid key exists, a new one will be provisioned.
        """
        return pulumi.get(self, "api_key_id")

    @api_key_id.setter
    def api_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key_id", value)

    @property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "deletion_policy")

    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deletion_policy", value)

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
class _WebAppState:
    def __init__(__self__, *,
                 api_key_id: Optional[pulumi.Input[str]] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 app_urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 deletion_policy: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WebApp resources.
        :param pulumi.Input[str] api_key_id: The globally unique, Google-assigned identifier (UID) for the Firebase API key associated with the WebApp.
               If apiKeyId is not set during creation, then Firebase automatically associates an apiKeyId with the WebApp.
               This auto-associated key may be an existing valid key or, if no valid key exists, a new one will be provisioned.
        :param pulumi.Input[str] app_id: The globally unique, Firebase-assigned identifier of the App.
               This identifier should be treated as an opaque token, as the data format is not specified.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] app_urls: The URLs where the `WebApp` is hosted.
        :param pulumi.Input[str] display_name: The user-assigned display name of the App.
               
               
               - - -
        :param pulumi.Input[str] name: The fully qualified resource name of the App, for example:
               projects/projectId/webApps/appId
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        if api_key_id is not None:
            pulumi.set(__self__, "api_key_id", api_key_id)
        if app_id is not None:
            pulumi.set(__self__, "app_id", app_id)
        if app_urls is not None:
            pulumi.set(__self__, "app_urls", app_urls)
        if deletion_policy is not None:
            pulumi.set(__self__, "deletion_policy", deletion_policy)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="apiKeyId")
    def api_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The globally unique, Google-assigned identifier (UID) for the Firebase API key associated with the WebApp.
        If apiKeyId is not set during creation, then Firebase automatically associates an apiKeyId with the WebApp.
        This auto-associated key may be an existing valid key or, if no valid key exists, a new one will be provisioned.
        """
        return pulumi.get(self, "api_key_id")

    @api_key_id.setter
    def api_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key_id", value)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[str]]:
        """
        The globally unique, Firebase-assigned identifier of the App.
        This identifier should be treated as an opaque token, as the data format is not specified.
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter(name="appUrls")
    def app_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The URLs where the `WebApp` is hosted.
        """
        return pulumi.get(self, "app_urls")

    @app_urls.setter
    def app_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "app_urls", value)

    @property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "deletion_policy")

    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deletion_policy", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The user-assigned display name of the App.


        - - -
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The fully qualified resource name of the App, for example:
        projects/projectId/webApps/appId
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


class WebApp(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key_id: Optional[pulumi.Input[str]] = None,
                 deletion_policy: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A Google Cloud Firebase web application instance

        To get more information about WebApp, see:

        * [API documentation](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps)
        * How-to Guides
            * [Official Documentation](https://firebase.google.com/)

        ## Example Usage

        ### Firebase Web App Custom Api Key

        ```python
        import pulumi
        import pulumi_gcp as gcp

        web = gcp.projects.ApiKey("web",
            project="my-project-name",
            name="api-key",
            display_name="Display Name",
            restrictions={
                "browser_key_restrictions": {
                    "allowed_referrers": ["*"],
                },
            })
        default = gcp.firebase.WebApp("default",
            project="my-project-name",
            display_name="Display Name",
            api_key_id=web.uid,
            deletion_policy="DELETE")
        ```

        ## Import

        WebApp can be imported using any of these accepted formats:

        * `{{project}} projects/{{project}}/webApps/{{app_id}}`

        * `projects/{{project}}/webApps/{{app_id}}`

        * `{{project}}/{{project}}/{{app_id}}`

        * `webApps/{{app_id}}`

        * `{{app_id}}`

        When using the `pulumi import` command, WebApp can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:firebase/webApp:WebApp default {{project}} projects/{{project}}/webApps/{{app_id}}
        ```

        ```sh
        $ pulumi import gcp:firebase/webApp:WebApp default projects/{{project}}/webApps/{{app_id}}
        ```

        ```sh
        $ pulumi import gcp:firebase/webApp:WebApp default {{project}}/{{project}}/{{app_id}}
        ```

        ```sh
        $ pulumi import gcp:firebase/webApp:WebApp default webApps/{{app_id}}
        ```

        ```sh
        $ pulumi import gcp:firebase/webApp:WebApp default {{app_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key_id: The globally unique, Google-assigned identifier (UID) for the Firebase API key associated with the WebApp.
               If apiKeyId is not set during creation, then Firebase automatically associates an apiKeyId with the WebApp.
               This auto-associated key may be an existing valid key or, if no valid key exists, a new one will be provisioned.
        :param pulumi.Input[str] display_name: The user-assigned display name of the App.
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebAppArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Google Cloud Firebase web application instance

        To get more information about WebApp, see:

        * [API documentation](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps)
        * How-to Guides
            * [Official Documentation](https://firebase.google.com/)

        ## Example Usage

        ### Firebase Web App Custom Api Key

        ```python
        import pulumi
        import pulumi_gcp as gcp

        web = gcp.projects.ApiKey("web",
            project="my-project-name",
            name="api-key",
            display_name="Display Name",
            restrictions={
                "browser_key_restrictions": {
                    "allowed_referrers": ["*"],
                },
            })
        default = gcp.firebase.WebApp("default",
            project="my-project-name",
            display_name="Display Name",
            api_key_id=web.uid,
            deletion_policy="DELETE")
        ```

        ## Import

        WebApp can be imported using any of these accepted formats:

        * `{{project}} projects/{{project}}/webApps/{{app_id}}`

        * `projects/{{project}}/webApps/{{app_id}}`

        * `{{project}}/{{project}}/{{app_id}}`

        * `webApps/{{app_id}}`

        * `{{app_id}}`

        When using the `pulumi import` command, WebApp can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:firebase/webApp:WebApp default {{project}} projects/{{project}}/webApps/{{app_id}}
        ```

        ```sh
        $ pulumi import gcp:firebase/webApp:WebApp default projects/{{project}}/webApps/{{app_id}}
        ```

        ```sh
        $ pulumi import gcp:firebase/webApp:WebApp default {{project}}/{{project}}/{{app_id}}
        ```

        ```sh
        $ pulumi import gcp:firebase/webApp:WebApp default webApps/{{app_id}}
        ```

        ```sh
        $ pulumi import gcp:firebase/webApp:WebApp default {{app_id}}
        ```

        :param str resource_name: The name of the resource.
        :param WebAppArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebAppArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key_id: Optional[pulumi.Input[str]] = None,
                 deletion_policy: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebAppArgs.__new__(WebAppArgs)

            __props__.__dict__["api_key_id"] = api_key_id
            __props__.__dict__["deletion_policy"] = deletion_policy
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["project"] = project
            __props__.__dict__["app_id"] = None
            __props__.__dict__["app_urls"] = None
            __props__.__dict__["name"] = None
        super(WebApp, __self__).__init__(
            'gcp:firebase/webApp:WebApp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_key_id: Optional[pulumi.Input[str]] = None,
            app_id: Optional[pulumi.Input[str]] = None,
            app_urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            deletion_policy: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'WebApp':
        """
        Get an existing WebApp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key_id: The globally unique, Google-assigned identifier (UID) for the Firebase API key associated with the WebApp.
               If apiKeyId is not set during creation, then Firebase automatically associates an apiKeyId with the WebApp.
               This auto-associated key may be an existing valid key or, if no valid key exists, a new one will be provisioned.
        :param pulumi.Input[str] app_id: The globally unique, Firebase-assigned identifier of the App.
               This identifier should be treated as an opaque token, as the data format is not specified.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] app_urls: The URLs where the `WebApp` is hosted.
        :param pulumi.Input[str] display_name: The user-assigned display name of the App.
               
               
               - - -
        :param pulumi.Input[str] name: The fully qualified resource name of the App, for example:
               projects/projectId/webApps/appId
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WebAppState.__new__(_WebAppState)

        __props__.__dict__["api_key_id"] = api_key_id
        __props__.__dict__["app_id"] = app_id
        __props__.__dict__["app_urls"] = app_urls
        __props__.__dict__["deletion_policy"] = deletion_policy
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        return WebApp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiKeyId")
    def api_key_id(self) -> pulumi.Output[str]:
        """
        The globally unique, Google-assigned identifier (UID) for the Firebase API key associated with the WebApp.
        If apiKeyId is not set during creation, then Firebase automatically associates an apiKeyId with the WebApp.
        This auto-associated key may be an existing valid key or, if no valid key exists, a new one will be provisioned.
        """
        return pulumi.get(self, "api_key_id")

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[str]:
        """
        The globally unique, Firebase-assigned identifier of the App.
        This identifier should be treated as an opaque token, as the data format is not specified.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="appUrls")
    def app_urls(self) -> pulumi.Output[Sequence[str]]:
        """
        The URLs where the `WebApp` is hosted.
        """
        return pulumi.get(self, "app_urls")

    @property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "deletion_policy")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The user-assigned display name of the App.


        - - -
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The fully qualified resource name of the App, for example:
        projects/projectId/webApps/appId
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

