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

__all__ = ['SSLCertificateArgs', 'SSLCertificate']

@pulumi.input_type
class SSLCertificateArgs:
    def __init__(__self__, *,
                 certificate: pulumi.Input[str],
                 private_key: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SSLCertificate resource.
        :param pulumi.Input[str] certificate: The certificate in PEM format.
               The certificate chain must be no greater than 5 certs long.
               The chain must include at least one intermediate cert.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] private_key: The write-only private key in PEM format.
               **Note**: This property is sensitive and will not be displayed in the plan.
               
               
               - - -
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
               These are in the same namespace as the managed SSL certificates.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the
               specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        pulumi.set(__self__, "certificate", certificate)
        pulumi.set(__self__, "private_key", private_key)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if name_prefix is not None:
            pulumi.set(__self__, "name_prefix", name_prefix)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Input[str]:
        """
        The certificate in PEM format.
        The certificate chain must be no greater than 5 certs long.
        The chain must include at least one intermediate cert.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: pulumi.Input[str]):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Input[str]:
        """
        The write-only private key in PEM format.
        **Note**: This property is sensitive and will not be displayed in the plan.


        - - -
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_key", value)

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
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Creates a unique name beginning with the
        specified prefix. Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_prefix", value)

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
class _SSLCertificateState:
    def __init__(__self__, *,
                 certificate: Optional[pulumi.Input[str]] = None,
                 certificate_id: Optional[pulumi.Input[int]] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SSLCertificate resources.
        :param pulumi.Input[str] certificate: The certificate in PEM format.
               The certificate chain must be no greater than 5 certs long.
               The chain must include at least one intermediate cert.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[int] certificate_id: The unique identifier for the resource.
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] expire_time: Expire time of the certificate in RFC3339 text format.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
               These are in the same namespace as the managed SSL certificates.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the
               specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] private_key: The write-only private key in PEM format.
               **Note**: This property is sensitive and will not be displayed in the plan.
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        """
        if certificate is not None:
            pulumi.set(__self__, "certificate", certificate)
        if certificate_id is not None:
            pulumi.set(__self__, "certificate_id", certificate_id)
        if creation_timestamp is not None:
            pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expire_time is not None:
            pulumi.set(__self__, "expire_time", expire_time)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if name_prefix is not None:
            pulumi.set(__self__, "name_prefix", name_prefix)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)

    @property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[str]]:
        """
        The certificate in PEM format.
        The certificate chain must be no greater than 5 certs long.
        The chain must include at least one intermediate cert.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate", value)

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
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Creates a unique name beginning with the
        specified prefix. Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_prefix", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[str]]:
        """
        The write-only private key in PEM format.
        **Note**: This property is sensitive and will not be displayed in the plan.


        - - -
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_key", value)

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


class SSLCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An SslCertificate resource, used for HTTPS load balancing. This resource
        provides a mechanism to upload an SSL key and certificate to
        the load balancer to serve secure connections from the user.

        To get more information about SslCertificate, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/sslCertificates)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/load-balancing/docs/ssl-certificates)

        ## Example Usage

        ## Import

        SslCertificate can be imported using any of these accepted formats:

        * `projects/{{project}}/global/sslCertificates/{{name}}`

        * `{{project}}/{{name}}`

        * `{{name}}`

        When using the `pulumi import` command, SslCertificate can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:compute/sSLCertificate:SSLCertificate default projects/{{project}}/global/sslCertificates/{{name}}
        ```

        ```sh
        $ pulumi import gcp:compute/sSLCertificate:SSLCertificate default {{project}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:compute/sSLCertificate:SSLCertificate default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate: The certificate in PEM format.
               The certificate chain must be no greater than 5 certs long.
               The chain must include at least one intermediate cert.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
               These are in the same namespace as the managed SSL certificates.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the
               specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] private_key: The write-only private key in PEM format.
               **Note**: This property is sensitive and will not be displayed in the plan.
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SSLCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An SslCertificate resource, used for HTTPS load balancing. This resource
        provides a mechanism to upload an SSL key and certificate to
        the load balancer to serve secure connections from the user.

        To get more information about SslCertificate, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/sslCertificates)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/load-balancing/docs/ssl-certificates)

        ## Example Usage

        ## Import

        SslCertificate can be imported using any of these accepted formats:

        * `projects/{{project}}/global/sslCertificates/{{name}}`

        * `{{project}}/{{name}}`

        * `{{name}}`

        When using the `pulumi import` command, SslCertificate can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:compute/sSLCertificate:SSLCertificate default projects/{{project}}/global/sslCertificates/{{name}}
        ```

        ```sh
        $ pulumi import gcp:compute/sSLCertificate:SSLCertificate default {{project}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:compute/sSLCertificate:SSLCertificate default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param SSLCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SSLCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SSLCertificateArgs.__new__(SSLCertificateArgs)

            if certificate is None and not opts.urn:
                raise TypeError("Missing required property 'certificate'")
            __props__.__dict__["certificate"] = None if certificate is None else pulumi.Output.secret(certificate)
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["name_prefix"] = name_prefix
            if private_key is None and not opts.urn:
                raise TypeError("Missing required property 'private_key'")
            __props__.__dict__["private_key"] = None if private_key is None else pulumi.Output.secret(private_key)
            __props__.__dict__["project"] = project
            __props__.__dict__["certificate_id"] = None
            __props__.__dict__["creation_timestamp"] = None
            __props__.__dict__["expire_time"] = None
            __props__.__dict__["self_link"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["certificate", "privateKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(SSLCertificate, __self__).__init__(
            'gcp:compute/sSLCertificate:SSLCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            certificate: Optional[pulumi.Input[str]] = None,
            certificate_id: Optional[pulumi.Input[int]] = None,
            creation_timestamp: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            expire_time: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_prefix: Optional[pulumi.Input[str]] = None,
            private_key: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None) -> 'SSLCertificate':
        """
        Get an existing SSLCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate: The certificate in PEM format.
               The certificate chain must be no greater than 5 certs long.
               The chain must include at least one intermediate cert.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[int] certificate_id: The unique identifier for the resource.
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] expire_time: Expire time of the certificate in RFC3339 text format.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
               These are in the same namespace as the managed SSL certificates.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the
               specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] private_key: The write-only private key in PEM format.
               **Note**: This property is sensitive and will not be displayed in the plan.
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SSLCertificateState.__new__(_SSLCertificateState)

        __props__.__dict__["certificate"] = certificate
        __props__.__dict__["certificate_id"] = certificate_id
        __props__.__dict__["creation_timestamp"] = creation_timestamp
        __props__.__dict__["description"] = description
        __props__.__dict__["expire_time"] = expire_time
        __props__.__dict__["name"] = name
        __props__.__dict__["name_prefix"] = name_prefix
        __props__.__dict__["private_key"] = private_key
        __props__.__dict__["project"] = project
        __props__.__dict__["self_link"] = self_link
        return SSLCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[str]:
        """
        The certificate in PEM format.
        The certificate chain must be no greater than 5 certs long.
        The chain must include at least one intermediate cert.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "certificate")

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
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[str]:
        """
        Creates a unique name beginning with the
        specified prefix. Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[str]:
        """
        The write-only private key in PEM format.
        **Note**: This property is sensitive and will not be displayed in the plan.


        - - -
        """
        return pulumi.get(self, "private_key")

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

