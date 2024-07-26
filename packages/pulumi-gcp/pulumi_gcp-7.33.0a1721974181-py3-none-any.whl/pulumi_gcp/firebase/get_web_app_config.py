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

__all__ = [
    'GetWebAppConfigResult',
    'AwaitableGetWebAppConfigResult',
    'get_web_app_config',
    'get_web_app_config_output',
]

@pulumi.output_type
class GetWebAppConfigResult:
    """
    A collection of values returned by getWebAppConfig.
    """
    def __init__(__self__, api_key=None, auth_domain=None, database_url=None, id=None, location_id=None, measurement_id=None, messaging_sender_id=None, project=None, storage_bucket=None, web_app_id=None):
        if api_key and not isinstance(api_key, str):
            raise TypeError("Expected argument 'api_key' to be a str")
        pulumi.set(__self__, "api_key", api_key)
        if auth_domain and not isinstance(auth_domain, str):
            raise TypeError("Expected argument 'auth_domain' to be a str")
        pulumi.set(__self__, "auth_domain", auth_domain)
        if database_url and not isinstance(database_url, str):
            raise TypeError("Expected argument 'database_url' to be a str")
        pulumi.set(__self__, "database_url", database_url)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location_id and not isinstance(location_id, str):
            raise TypeError("Expected argument 'location_id' to be a str")
        pulumi.set(__self__, "location_id", location_id)
        if measurement_id and not isinstance(measurement_id, str):
            raise TypeError("Expected argument 'measurement_id' to be a str")
        pulumi.set(__self__, "measurement_id", measurement_id)
        if messaging_sender_id and not isinstance(messaging_sender_id, str):
            raise TypeError("Expected argument 'messaging_sender_id' to be a str")
        pulumi.set(__self__, "messaging_sender_id", messaging_sender_id)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if storage_bucket and not isinstance(storage_bucket, str):
            raise TypeError("Expected argument 'storage_bucket' to be a str")
        pulumi.set(__self__, "storage_bucket", storage_bucket)
        if web_app_id and not isinstance(web_app_id, str):
            raise TypeError("Expected argument 'web_app_id' to be a str")
        pulumi.set(__self__, "web_app_id", web_app_id)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> str:
        """
        The API key associated with the web App.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="authDomain")
    def auth_domain(self) -> str:
        """
        The domain Firebase Auth configures for OAuth redirects, in the format:
        projectId.firebaseapp.com
        """
        return pulumi.get(self, "auth_domain")

    @property
    @pulumi.getter(name="databaseUrl")
    def database_url(self) -> str:
        """
        The default Firebase Realtime Database URL.
        """
        return pulumi.get(self, "database_url")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="locationId")
    def location_id(self) -> str:
        """
        The ID of the project's default GCP resource location. The location is one of the available GCP resource
        locations.
        This field is omitted if the default GCP resource location has not been finalized yet. To set your project's
        default GCP resource location, call defaultLocation.finalize after you add Firebase services to your project.
        """
        return pulumi.get(self, "location_id")

    @property
    @pulumi.getter(name="measurementId")
    def measurement_id(self) -> str:
        """
        The unique Google-assigned identifier of the Google Analytics web stream associated with the Firebase Web App.
        Firebase SDKs use this ID to interact with Google Analytics APIs.
        This field is only present if the App is linked to a web stream in a Google Analytics App + Web property.
        Learn more about this ID and Google Analytics web streams in the Analytics documentation.
        To generate a measurementId and link the Web App with a Google Analytics web stream,
        call projects.addGoogleAnalytics.
        """
        return pulumi.get(self, "measurement_id")

    @property
    @pulumi.getter(name="messagingSenderId")
    def messaging_sender_id(self) -> str:
        """
        The sender ID for use with Firebase Cloud Messaging.
        """
        return pulumi.get(self, "messaging_sender_id")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="storageBucket")
    def storage_bucket(self) -> str:
        """
        The default Cloud Storage for Firebase storage bucket name.
        """
        return pulumi.get(self, "storage_bucket")

    @property
    @pulumi.getter(name="webAppId")
    def web_app_id(self) -> str:
        return pulumi.get(self, "web_app_id")


class AwaitableGetWebAppConfigResult(GetWebAppConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebAppConfigResult(
            api_key=self.api_key,
            auth_domain=self.auth_domain,
            database_url=self.database_url,
            id=self.id,
            location_id=self.location_id,
            measurement_id=self.measurement_id,
            messaging_sender_id=self.messaging_sender_id,
            project=self.project,
            storage_bucket=self.storage_bucket,
            web_app_id=self.web_app_id)


def get_web_app_config(project: Optional[str] = None,
                       web_app_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebAppConfigResult:
    """
    A Google Cloud Firebase web application configuration

    To get more information about WebApp, see:

    * [API documentation](https://firebase.google.com/docs/projects/api/reference/rest/v1beta1/projects.webApps)
    * How-to Guides
        * [Official Documentation](https://firebase.google.com/)


    :param str project: The ID of the project in which the resource belongs. If it
           is not provided, the provider project is used.
    :param str web_app_id: the id of the firebase web app
           
           - - -
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['webAppId'] = web_app_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:firebase/getWebAppConfig:getWebAppConfig', __args__, opts=opts, typ=GetWebAppConfigResult).value

    return AwaitableGetWebAppConfigResult(
        api_key=pulumi.get(__ret__, 'api_key'),
        auth_domain=pulumi.get(__ret__, 'auth_domain'),
        database_url=pulumi.get(__ret__, 'database_url'),
        id=pulumi.get(__ret__, 'id'),
        location_id=pulumi.get(__ret__, 'location_id'),
        measurement_id=pulumi.get(__ret__, 'measurement_id'),
        messaging_sender_id=pulumi.get(__ret__, 'messaging_sender_id'),
        project=pulumi.get(__ret__, 'project'),
        storage_bucket=pulumi.get(__ret__, 'storage_bucket'),
        web_app_id=pulumi.get(__ret__, 'web_app_id'))


@_utilities.lift_output_func(get_web_app_config)
def get_web_app_config_output(project: Optional[pulumi.Input[Optional[str]]] = None,
                              web_app_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebAppConfigResult]:
    """
    A Google Cloud Firebase web application configuration

    To get more information about WebApp, see:

    * [API documentation](https://firebase.google.com/docs/projects/api/reference/rest/v1beta1/projects.webApps)
    * How-to Guides
        * [Official Documentation](https://firebase.google.com/)


    :param str project: The ID of the project in which the resource belongs. If it
           is not provided, the provider project is used.
    :param str web_app_id: the id of the firebase web app
           
           - - -
    """
    ...
