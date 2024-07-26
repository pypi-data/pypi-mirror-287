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

__all__ = ['MangedSslCertificateArgs', 'MangedSslCertificate']

@pulumi.input_type
class MangedSslCertificateArgs:
    def __init__(__self__, *,
                 certificate_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 managed: Optional[pulumi.Input['MangedSslCertificateManagedArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MangedSslCertificate resource.
        :param pulumi.Input[int] certificate_id: The unique identifier for the resource.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input['MangedSslCertificateManagedArgs'] managed: Properties relevant to a managed certificate.  These will be used if the
               certificate is managed (as indicated by a value of `MANAGED` in `type`).
               Structure is documented below.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
               These are in the same namespace as the managed SSL certificates.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] type: Enum field whose value is always `MANAGED` - used to signal to the API
               which type this is.
               Default value is `MANAGED`.
               Possible values are: `MANAGED`.
        """
        if certificate_id is not None:
            pulumi.set(__self__, "certificate_id", certificate_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if managed is not None:
            pulumi.set(__self__, "managed", managed)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[pulumi.Input[int]]:
        """
        The unique identifier for the resource.
        """
        return pulumi.get(self, "certificate_id")

    @certificate_id.setter
    def certificate_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "certificate_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of this resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def managed(self) -> Optional[pulumi.Input['MangedSslCertificateManagedArgs']]:
        """
        Properties relevant to a managed certificate.  These will be used if the
        certificate is managed (as indicated by a value of `MANAGED` in `type`).
        Structure is documented below.
        """
        return pulumi.get(self, "managed")

    @managed.setter
    def managed(self, value: Optional[pulumi.Input['MangedSslCertificateManagedArgs']]):
        pulumi.set(self, "managed", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource. Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression `a-z?` which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.
        These are in the same namespace as the managed SSL certificates.
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
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Enum field whose value is always `MANAGED` - used to signal to the API
        which type this is.
        Default value is `MANAGED`.
        Possible values are: `MANAGED`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _MangedSslCertificateState:
    def __init__(__self__, *,
                 certificate_id: Optional[pulumi.Input[int]] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 managed: Optional[pulumi.Input['MangedSslCertificateManagedArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MangedSslCertificate resources.
        :param pulumi.Input[int] certificate_id: The unique identifier for the resource.
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] expire_time: Expire time of the certificate in RFC3339 text format.
        :param pulumi.Input['MangedSslCertificateManagedArgs'] managed: Properties relevant to a managed certificate.  These will be used if the
               certificate is managed (as indicated by a value of `MANAGED` in `type`).
               Structure is documented below.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
               These are in the same namespace as the managed SSL certificates.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subject_alternative_names: Domains associated with the certificate via Subject Alternative Name.
        :param pulumi.Input[str] type: Enum field whose value is always `MANAGED` - used to signal to the API
               which type this is.
               Default value is `MANAGED`.
               Possible values are: `MANAGED`.
        """
        if certificate_id is not None:
            pulumi.set(__self__, "certificate_id", certificate_id)
        if creation_timestamp is not None:
            pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expire_time is not None:
            pulumi.set(__self__, "expire_time", expire_time)
        if managed is not None:
            pulumi.set(__self__, "managed", managed)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)
        if subject_alternative_names is not None:
            pulumi.set(__self__, "subject_alternative_names", subject_alternative_names)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[pulumi.Input[int]]:
        """
        The unique identifier for the resource.
        """
        return pulumi.get(self, "certificate_id")

    @certificate_id.setter
    def certificate_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "certificate_id", value)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[str]]:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "creation_timestamp", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of this resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[str]]:
        """
        Expire time of the certificate in RFC3339 text format.
        """
        return pulumi.get(self, "expire_time")

    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expire_time", value)

    @property
    @pulumi.getter
    def managed(self) -> Optional[pulumi.Input['MangedSslCertificateManagedArgs']]:
        """
        Properties relevant to a managed certificate.  These will be used if the
        certificate is managed (as indicated by a value of `MANAGED` in `type`).
        Structure is documented below.
        """
        return pulumi.get(self, "managed")

    @managed.setter
    def managed(self, value: Optional[pulumi.Input['MangedSslCertificateManagedArgs']]):
        pulumi.set(self, "managed", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource. Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression `a-z?` which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.
        These are in the same namespace as the managed SSL certificates.
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
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)

    @property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Domains associated with the certificate via Subject Alternative Name.
        """
        return pulumi.get(self, "subject_alternative_names")

    @subject_alternative_names.setter
    def subject_alternative_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subject_alternative_names", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Enum field whose value is always `MANAGED` - used to signal to the API
        which type this is.
        Default value is `MANAGED`.
        Possible values are: `MANAGED`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


warnings.warn("""gcp.compute.MangedSslCertificate has been deprecated in favor of gcp.compute.ManagedSslCertificate""", DeprecationWarning)


class MangedSslCertificate(pulumi.CustomResource):
    warnings.warn("""gcp.compute.MangedSslCertificate has been deprecated in favor of gcp.compute.ManagedSslCertificate""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 managed: Optional[pulumi.Input[Union['MangedSslCertificateManagedArgs', 'MangedSslCertificateManagedArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An SslCertificate resource, used for HTTPS load balancing.  This resource
        represents a certificate for which the certificate secrets are created and
        managed by Google.

        For a resource where you provide the key, see the
        SSL Certificate resource.

        To get more information about ManagedSslCertificate, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/sslCertificates)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/load-balancing/docs/ssl-certificates)

        > **Warning:** This resource should be used with extreme caution!  Provisioning an SSL
        certificate is complex.  Ensure that you understand the lifecycle of a
        certificate before attempting complex tasks like cert rotation automatically.
        This resource will "return" as soon as the certificate object is created,
        but post-creation the certificate object will go through a "provisioning"
        process.  The provisioning process can complete only when the domain name
        for which the certificate is created points to a target pool which, itself,
        points at the certificate.  Depending on your DNS provider, this may take
        some time, and migrating from self-managed certificates to Google-managed
        certificates may entail some downtime while the certificate provisions.

        In conclusion: Be extremely cautious.

        ## Example Usage

        ### Managed Ssl Certificate Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.compute.ManagedSslCertificate("default",
            name="test-cert",
            managed={
                "domains": ["sslcert.tf-test.club."],
            })
        default_http_health_check = gcp.compute.HttpHealthCheck("default",
            name="http-health-check",
            request_path="/",
            check_interval_sec=1,
            timeout_sec=1)
        default_backend_service = gcp.compute.BackendService("default",
            name="backend-service",
            port_name="http",
            protocol="HTTP",
            timeout_sec=10,
            health_checks=default_http_health_check.id)
        default_url_map = gcp.compute.URLMap("default",
            name="url-map",
            description="a description",
            default_service=default_backend_service.id,
            host_rules=[{
                "hosts": ["sslcert.tf-test.club"],
                "path_matcher": "allpaths",
            }],
            path_matchers=[{
                "name": "allpaths",
                "default_service": default_backend_service.id,
                "path_rules": [{
                    "paths": ["/*"],
                    "service": default_backend_service.id,
                }],
            }])
        default_target_https_proxy = gcp.compute.TargetHttpsProxy("default",
            name="test-proxy",
            url_map=default_url_map.id,
            ssl_certificates=[default.id])
        default_global_forwarding_rule = gcp.compute.GlobalForwardingRule("default",
            name="forwarding-rule",
            target=default_target_https_proxy.id,
            port_range="443")
        ```
        ## Import

        ManagedSslCertificate can be imported using any of these accepted formats:

        * `projects/{{project}}/global/sslCertificates/{{name}}`

        * `{{project}}/{{name}}`

        * `{{name}}`

        When using the `pulumi import` command, ManagedSslCertificate can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:compute/mangedSslCertificate:MangedSslCertificate default projects/{{project}}/global/sslCertificates/{{name}}
        ```

        ```sh
        $ pulumi import gcp:compute/mangedSslCertificate:MangedSslCertificate default {{project}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:compute/mangedSslCertificate:MangedSslCertificate default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] certificate_id: The unique identifier for the resource.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[Union['MangedSslCertificateManagedArgs', 'MangedSslCertificateManagedArgsDict']] managed: Properties relevant to a managed certificate.  These will be used if the
               certificate is managed (as indicated by a value of `MANAGED` in `type`).
               Structure is documented below.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
               These are in the same namespace as the managed SSL certificates.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] type: Enum field whose value is always `MANAGED` - used to signal to the API
               which type this is.
               Default value is `MANAGED`.
               Possible values are: `MANAGED`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[MangedSslCertificateArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An SslCertificate resource, used for HTTPS load balancing.  This resource
        represents a certificate for which the certificate secrets are created and
        managed by Google.

        For a resource where you provide the key, see the
        SSL Certificate resource.

        To get more information about ManagedSslCertificate, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/sslCertificates)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/load-balancing/docs/ssl-certificates)

        > **Warning:** This resource should be used with extreme caution!  Provisioning an SSL
        certificate is complex.  Ensure that you understand the lifecycle of a
        certificate before attempting complex tasks like cert rotation automatically.
        This resource will "return" as soon as the certificate object is created,
        but post-creation the certificate object will go through a "provisioning"
        process.  The provisioning process can complete only when the domain name
        for which the certificate is created points to a target pool which, itself,
        points at the certificate.  Depending on your DNS provider, this may take
        some time, and migrating from self-managed certificates to Google-managed
        certificates may entail some downtime while the certificate provisions.

        In conclusion: Be extremely cautious.

        ## Example Usage

        ### Managed Ssl Certificate Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.compute.ManagedSslCertificate("default",
            name="test-cert",
            managed={
                "domains": ["sslcert.tf-test.club."],
            })
        default_http_health_check = gcp.compute.HttpHealthCheck("default",
            name="http-health-check",
            request_path="/",
            check_interval_sec=1,
            timeout_sec=1)
        default_backend_service = gcp.compute.BackendService("default",
            name="backend-service",
            port_name="http",
            protocol="HTTP",
            timeout_sec=10,
            health_checks=default_http_health_check.id)
        default_url_map = gcp.compute.URLMap("default",
            name="url-map",
            description="a description",
            default_service=default_backend_service.id,
            host_rules=[{
                "hosts": ["sslcert.tf-test.club"],
                "path_matcher": "allpaths",
            }],
            path_matchers=[{
                "name": "allpaths",
                "default_service": default_backend_service.id,
                "path_rules": [{
                    "paths": ["/*"],
                    "service": default_backend_service.id,
                }],
            }])
        default_target_https_proxy = gcp.compute.TargetHttpsProxy("default",
            name="test-proxy",
            url_map=default_url_map.id,
            ssl_certificates=[default.id])
        default_global_forwarding_rule = gcp.compute.GlobalForwardingRule("default",
            name="forwarding-rule",
            target=default_target_https_proxy.id,
            port_range="443")
        ```
        ## Import

        ManagedSslCertificate can be imported using any of these accepted formats:

        * `projects/{{project}}/global/sslCertificates/{{name}}`

        * `{{project}}/{{name}}`

        * `{{name}}`

        When using the `pulumi import` command, ManagedSslCertificate can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:compute/mangedSslCertificate:MangedSslCertificate default projects/{{project}}/global/sslCertificates/{{name}}
        ```

        ```sh
        $ pulumi import gcp:compute/mangedSslCertificate:MangedSslCertificate default {{project}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:compute/mangedSslCertificate:MangedSslCertificate default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param MangedSslCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MangedSslCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 managed: Optional[pulumi.Input[Union['MangedSslCertificateManagedArgs', 'MangedSslCertificateManagedArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""MangedSslCertificate is deprecated: gcp.compute.MangedSslCertificate has been deprecated in favor of gcp.compute.ManagedSslCertificate""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MangedSslCertificateArgs.__new__(MangedSslCertificateArgs)

            __props__.__dict__["certificate_id"] = certificate_id
            __props__.__dict__["description"] = description
            __props__.__dict__["managed"] = managed
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["type"] = type
            __props__.__dict__["creation_timestamp"] = None
            __props__.__dict__["expire_time"] = None
            __props__.__dict__["self_link"] = None
            __props__.__dict__["subject_alternative_names"] = None
        super(MangedSslCertificate, __self__).__init__(
            'gcp:compute/mangedSslCertificate:MangedSslCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            certificate_id: Optional[pulumi.Input[int]] = None,
            creation_timestamp: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            expire_time: Optional[pulumi.Input[str]] = None,
            managed: Optional[pulumi.Input[Union['MangedSslCertificateManagedArgs', 'MangedSslCertificateManagedArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'MangedSslCertificate':
        """
        Get an existing MangedSslCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] certificate_id: The unique identifier for the resource.
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] expire_time: Expire time of the certificate in RFC3339 text format.
        :param pulumi.Input[Union['MangedSslCertificateManagedArgs', 'MangedSslCertificateManagedArgsDict']] managed: Properties relevant to a managed certificate.  These will be used if the
               certificate is managed (as indicated by a value of `MANAGED` in `type`).
               Structure is documented below.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
               These are in the same namespace as the managed SSL certificates.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subject_alternative_names: Domains associated with the certificate via Subject Alternative Name.
        :param pulumi.Input[str] type: Enum field whose value is always `MANAGED` - used to signal to the API
               which type this is.
               Default value is `MANAGED`.
               Possible values are: `MANAGED`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MangedSslCertificateState.__new__(_MangedSslCertificateState)

        __props__.__dict__["certificate_id"] = certificate_id
        __props__.__dict__["creation_timestamp"] = creation_timestamp
        __props__.__dict__["description"] = description
        __props__.__dict__["expire_time"] = expire_time
        __props__.__dict__["managed"] = managed
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["self_link"] = self_link
        __props__.__dict__["subject_alternative_names"] = subject_alternative_names
        __props__.__dict__["type"] = type
        return MangedSslCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> pulumi.Output[int]:
        """
        The unique identifier for the resource.
        """
        return pulumi.get(self, "certificate_id")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description of this resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[str]:
        """
        Expire time of the certificate in RFC3339 text format.
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter
    def managed(self) -> pulumi.Output[Optional['outputs.MangedSslCertificateManaged']]:
        """
        Properties relevant to a managed certificate.  These will be used if the
        certificate is managed (as indicated by a value of `MANAGED` in `type`).
        Structure is documented below.
        """
        return pulumi.get(self, "managed")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource. Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression `a-z?` which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.
        These are in the same namespace as the managed SSL certificates.
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
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> pulumi.Output[Sequence[str]]:
        """
        Domains associated with the certificate via Subject Alternative Name.
        """
        return pulumi.get(self, "subject_alternative_names")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        Enum field whose value is always `MANAGED` - used to signal to the API
        which type this is.
        Default value is `MANAGED`.
        Possible values are: `MANAGED`.
        """
        return pulumi.get(self, "type")

