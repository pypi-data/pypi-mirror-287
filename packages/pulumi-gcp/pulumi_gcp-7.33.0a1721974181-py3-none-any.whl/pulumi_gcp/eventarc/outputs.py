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

__all__ = [
    'TriggerDestination',
    'TriggerDestinationCloudRunService',
    'TriggerDestinationGke',
    'TriggerDestinationHttpEndpoint',
    'TriggerDestinationNetworkConfig',
    'TriggerMatchingCriteria',
    'TriggerTransport',
    'TriggerTransportPubsub',
]

@pulumi.output_type
class TriggerDestination(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cloudFunction":
            suggest = "cloud_function"
        elif key == "cloudRunService":
            suggest = "cloud_run_service"
        elif key == "httpEndpoint":
            suggest = "http_endpoint"
        elif key == "networkConfig":
            suggest = "network_config"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TriggerDestination. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TriggerDestination.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TriggerDestination.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cloud_function: Optional[str] = None,
                 cloud_run_service: Optional['outputs.TriggerDestinationCloudRunService'] = None,
                 gke: Optional['outputs.TriggerDestinationGke'] = None,
                 http_endpoint: Optional['outputs.TriggerDestinationHttpEndpoint'] = None,
                 network_config: Optional['outputs.TriggerDestinationNetworkConfig'] = None,
                 workflow: Optional[str] = None):
        """
        :param str cloud_function: The Cloud Function resource name. Only Cloud Functions V2 is supported. Format projects/{project}/locations/{location}/functions/{function} This is a read-only field. [WARNING] Creating Cloud Functions V2 triggers is only supported via the Cloud Functions product. An error will be returned if the user sets this value.
        :param 'TriggerDestinationCloudRunServiceArgs' cloud_run_service: Cloud Run fully-managed service that receives the events. The service should be running in the same project of the trigger.
        :param 'TriggerDestinationGkeArgs' gke: A GKE service capable of receiving events. The service should be running in the same project as the trigger.
        :param 'TriggerDestinationHttpEndpointArgs' http_endpoint: An HTTP endpoint destination described by an URI.
        :param 'TriggerDestinationNetworkConfigArgs' network_config: Optional. Network config is used to configure how Eventarc resolves and connect to a destination. This should only be used with HttpEndpoint destination type.
        :param str workflow: The resource name of the Workflow whose Executions are triggered by the events. The Workflow resource should be deployed in the same project as the trigger. Format: `projects/{project}/locations/{location}/workflows/{workflow}`
        """
        if cloud_function is not None:
            pulumi.set(__self__, "cloud_function", cloud_function)
        if cloud_run_service is not None:
            pulumi.set(__self__, "cloud_run_service", cloud_run_service)
        if gke is not None:
            pulumi.set(__self__, "gke", gke)
        if http_endpoint is not None:
            pulumi.set(__self__, "http_endpoint", http_endpoint)
        if network_config is not None:
            pulumi.set(__self__, "network_config", network_config)
        if workflow is not None:
            pulumi.set(__self__, "workflow", workflow)

    @property
    @pulumi.getter(name="cloudFunction")
    def cloud_function(self) -> Optional[str]:
        """
        The Cloud Function resource name. Only Cloud Functions V2 is supported. Format projects/{project}/locations/{location}/functions/{function} This is a read-only field. [WARNING] Creating Cloud Functions V2 triggers is only supported via the Cloud Functions product. An error will be returned if the user sets this value.
        """
        return pulumi.get(self, "cloud_function")

    @property
    @pulumi.getter(name="cloudRunService")
    def cloud_run_service(self) -> Optional['outputs.TriggerDestinationCloudRunService']:
        """
        Cloud Run fully-managed service that receives the events. The service should be running in the same project of the trigger.
        """
        return pulumi.get(self, "cloud_run_service")

    @property
    @pulumi.getter
    def gke(self) -> Optional['outputs.TriggerDestinationGke']:
        """
        A GKE service capable of receiving events. The service should be running in the same project as the trigger.
        """
        return pulumi.get(self, "gke")

    @property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional['outputs.TriggerDestinationHttpEndpoint']:
        """
        An HTTP endpoint destination described by an URI.
        """
        return pulumi.get(self, "http_endpoint")

    @property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional['outputs.TriggerDestinationNetworkConfig']:
        """
        Optional. Network config is used to configure how Eventarc resolves and connect to a destination. This should only be used with HttpEndpoint destination type.
        """
        return pulumi.get(self, "network_config")

    @property
    @pulumi.getter
    def workflow(self) -> Optional[str]:
        """
        The resource name of the Workflow whose Executions are triggered by the events. The Workflow resource should be deployed in the same project as the trigger. Format: `projects/{project}/locations/{location}/workflows/{workflow}`
        """
        return pulumi.get(self, "workflow")


@pulumi.output_type
class TriggerDestinationCloudRunService(dict):
    def __init__(__self__, *,
                 service: str,
                 path: Optional[str] = None,
                 region: Optional[str] = None):
        """
        :param str service: Required. The name of the Cloud Run service being addressed. See https://cloud.google.com/run/docs/reference/rest/v1/namespaces.services. Only services located in the same project of the trigger object can be addressed.
        :param str path: Optional. The relative path on the Cloud Run service the events should be sent to. The value must conform to the definition of URI path segment (section 3.3 of RFC2396). Examples: "/route", "route", "route/subroute".
        :param str region: Required. The region the Cloud Run service is deployed in.
        """
        pulumi.set(__self__, "service", service)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def service(self) -> str:
        """
        Required. The name of the Cloud Run service being addressed. See https://cloud.google.com/run/docs/reference/rest/v1/namespaces.services. Only services located in the same project of the trigger object can be addressed.
        """
        return pulumi.get(self, "service")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        Optional. The relative path on the Cloud Run service the events should be sent to. The value must conform to the definition of URI path segment (section 3.3 of RFC2396). Examples: "/route", "route", "route/subroute".
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        Required. The region the Cloud Run service is deployed in.
        """
        return pulumi.get(self, "region")


@pulumi.output_type
class TriggerDestinationGke(dict):
    def __init__(__self__, *,
                 cluster: str,
                 location: str,
                 namespace: str,
                 service: str,
                 path: Optional[str] = None):
        """
        :param str cluster: Required. The name of the cluster the GKE service is running in. The cluster must be running in the same project as the trigger being created.
        :param str location: Required. The name of the Google Compute Engine in which the cluster resides, which can either be compute zone (for example, us-central1-a) for the zonal clusters or region (for example, us-central1) for regional clusters.
        :param str namespace: Required. The namespace the GKE service is running in.
        :param str service: Required. Name of the GKE service.
        :param str path: Optional. The relative path on the GKE service the events should be sent to. The value must conform to the definition of a URI path segment (section 3.3 of RFC2396). Examples: "/route", "route", "route/subroute".
        """
        pulumi.set(__self__, "cluster", cluster)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "service", service)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def cluster(self) -> str:
        """
        Required. The name of the cluster the GKE service is running in. The cluster must be running in the same project as the trigger being created.
        """
        return pulumi.get(self, "cluster")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Required. The name of the Google Compute Engine in which the cluster resides, which can either be compute zone (for example, us-central1-a) for the zonal clusters or region (for example, us-central1) for regional clusters.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        """
        Required. The namespace the GKE service is running in.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def service(self) -> str:
        """
        Required. Name of the GKE service.
        """
        return pulumi.get(self, "service")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        Optional. The relative path on the GKE service the events should be sent to. The value must conform to the definition of a URI path segment (section 3.3 of RFC2396). Examples: "/route", "route", "route/subroute".
        """
        return pulumi.get(self, "path")


@pulumi.output_type
class TriggerDestinationHttpEndpoint(dict):
    def __init__(__self__, *,
                 uri: str):
        """
        :param str uri: Required. The URI of the HTTP enpdoint. The value must be a RFC2396 URI string. Examples: `http://10.10.10.8:80/route`, `http://svc.us-central1.p.local:8080/`. Only HTTP and HTTPS protocols are supported. The host can be either a static IP addressable from the VPC specified by the network config, or an internal DNS hostname of the service resolvable via Cloud DNS.
        """
        pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter
    def uri(self) -> str:
        """
        Required. The URI of the HTTP enpdoint. The value must be a RFC2396 URI string. Examples: `http://10.10.10.8:80/route`, `http://svc.us-central1.p.local:8080/`. Only HTTP and HTTPS protocols are supported. The host can be either a static IP addressable from the VPC specified by the network config, or an internal DNS hostname of the service resolvable via Cloud DNS.
        """
        return pulumi.get(self, "uri")


@pulumi.output_type
class TriggerDestinationNetworkConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "networkAttachment":
            suggest = "network_attachment"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TriggerDestinationNetworkConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TriggerDestinationNetworkConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TriggerDestinationNetworkConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 network_attachment: str):
        """
        :param str network_attachment: Required. Name of the NetworkAttachment that allows access to the destination VPC. Format: `projects/{PROJECT_ID}/regions/{REGION}/networkAttachments/{NETWORK_ATTACHMENT_NAME}`
        """
        pulumi.set(__self__, "network_attachment", network_attachment)

    @property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> str:
        """
        Required. Name of the NetworkAttachment that allows access to the destination VPC. Format: `projects/{PROJECT_ID}/regions/{REGION}/networkAttachments/{NETWORK_ATTACHMENT_NAME}`
        """
        return pulumi.get(self, "network_attachment")


@pulumi.output_type
class TriggerMatchingCriteria(dict):
    def __init__(__self__, *,
                 attribute: str,
                 value: str,
                 operator: Optional[str] = None):
        """
        :param str attribute: Required. The name of a CloudEvents attribute. Currently, only a subset of attributes are supported for filtering. All triggers MUST provide a filter for the 'type' attribute.
        :param str value: Required. The value for the attribute. See https://cloud.google.com/eventarc/docs/creating-triggers#trigger-gcloud for available values.
               
               - - -
        :param str operator: Optional. The operator used for matching the events with the value of the filter. If not specified, only events that have an exact key-value pair specified in the filter are matched. The only allowed value is `match-path-pattern`.
        """
        pulumi.set(__self__, "attribute", attribute)
        pulumi.set(__self__, "value", value)
        if operator is not None:
            pulumi.set(__self__, "operator", operator)

    @property
    @pulumi.getter
    def attribute(self) -> str:
        """
        Required. The name of a CloudEvents attribute. Currently, only a subset of attributes are supported for filtering. All triggers MUST provide a filter for the 'type' attribute.
        """
        return pulumi.get(self, "attribute")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Required. The value for the attribute. See https://cloud.google.com/eventarc/docs/creating-triggers#trigger-gcloud for available values.

        - - -
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter
    def operator(self) -> Optional[str]:
        """
        Optional. The operator used for matching the events with the value of the filter. If not specified, only events that have an exact key-value pair specified in the filter are matched. The only allowed value is `match-path-pattern`.
        """
        return pulumi.get(self, "operator")


@pulumi.output_type
class TriggerTransport(dict):
    def __init__(__self__, *,
                 pubsub: Optional['outputs.TriggerTransportPubsub'] = None):
        """
        :param 'TriggerTransportPubsubArgs' pubsub: The Pub/Sub topic and subscription used by Eventarc as delivery intermediary.
        """
        if pubsub is not None:
            pulumi.set(__self__, "pubsub", pubsub)

    @property
    @pulumi.getter
    def pubsub(self) -> Optional['outputs.TriggerTransportPubsub']:
        """
        The Pub/Sub topic and subscription used by Eventarc as delivery intermediary.
        """
        return pulumi.get(self, "pubsub")


@pulumi.output_type
class TriggerTransportPubsub(dict):
    def __init__(__self__, *,
                 subscription: Optional[str] = None,
                 topic: Optional[str] = None):
        """
        :param str subscription: Output only. The name of the Pub/Sub subscription created and managed by Eventarc system as a transport for the event delivery. Format: `projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_NAME}`.
        :param str topic: Optional. The name of the Pub/Sub topic created and managed by Eventarc system as a transport for the event delivery. Format: `projects/{PROJECT_ID}/topics/{TOPIC_NAME}. You may set an existing topic for triggers of the type google.cloud.pubsub.topic.v1.messagePublished` only. The topic you provide here will not be deleted by Eventarc at trigger deletion.
        """
        if subscription is not None:
            pulumi.set(__self__, "subscription", subscription)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter
    def subscription(self) -> Optional[str]:
        """
        Output only. The name of the Pub/Sub subscription created and managed by Eventarc system as a transport for the event delivery. Format: `projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_NAME}`.
        """
        return pulumi.get(self, "subscription")

    @property
    @pulumi.getter
    def topic(self) -> Optional[str]:
        """
        Optional. The name of the Pub/Sub topic created and managed by Eventarc system as a transport for the event delivery. Format: `projects/{PROJECT_ID}/topics/{TOPIC_NAME}. You may set an existing topic for triggers of the type google.cloud.pubsub.topic.v1.messagePublished` only. The topic you provide here will not be deleted by Eventarc at trigger deletion.
        """
        return pulumi.get(self, "topic")


