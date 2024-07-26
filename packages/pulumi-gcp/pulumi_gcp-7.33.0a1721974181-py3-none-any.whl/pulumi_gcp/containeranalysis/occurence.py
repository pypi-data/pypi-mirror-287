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

__all__ = ['OccurenceArgs', 'Occurence']

@pulumi.input_type
class OccurenceArgs:
    def __init__(__self__, *,
                 attestation: pulumi.Input['OccurenceAttestationArgs'],
                 note_name: pulumi.Input[str],
                 resource_uri: pulumi.Input[str],
                 project: Optional[pulumi.Input[str]] = None,
                 remediation: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Occurence resource.
        :param pulumi.Input['OccurenceAttestationArgs'] attestation: Occurrence that represents a single "attestation". The authenticity
               of an attestation can be verified using the attached signature.
               If the verifier trusts the public key of the signer, then verifying
               the signature is sufficient to establish trust. In this circumstance,
               the authority to which this attestation is attached is primarily
               useful for lookup (how to find this attestation if you already
               know the authority and artifact to be verified) and intent (for
               which authority this attestation was intended to sign.
               Structure is documented below.
        :param pulumi.Input[str] note_name: The analysis note associated with this occurrence, in the form of
               projects/[PROJECT]/notes/[NOTE_ID]. This field can be used as a
               filter in list requests.
        :param pulumi.Input[str] resource_uri: Required. Immutable. A URI that represents the resource for which
               the occurrence applies. For example,
               https://gcr.io/project/image@sha256:123abc for a Docker image.
        :param pulumi.Input[str] remediation: A description of actions that can be taken to remedy the note.
        """
        pulumi.set(__self__, "attestation", attestation)
        pulumi.set(__self__, "note_name", note_name)
        pulumi.set(__self__, "resource_uri", resource_uri)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if remediation is not None:
            pulumi.set(__self__, "remediation", remediation)

    @property
    @pulumi.getter
    def attestation(self) -> pulumi.Input['OccurenceAttestationArgs']:
        """
        Occurrence that represents a single "attestation". The authenticity
        of an attestation can be verified using the attached signature.
        If the verifier trusts the public key of the signer, then verifying
        the signature is sufficient to establish trust. In this circumstance,
        the authority to which this attestation is attached is primarily
        useful for lookup (how to find this attestation if you already
        know the authority and artifact to be verified) and intent (for
        which authority this attestation was intended to sign.
        Structure is documented below.
        """
        return pulumi.get(self, "attestation")

    @attestation.setter
    def attestation(self, value: pulumi.Input['OccurenceAttestationArgs']):
        pulumi.set(self, "attestation", value)

    @property
    @pulumi.getter(name="noteName")
    def note_name(self) -> pulumi.Input[str]:
        """
        The analysis note associated with this occurrence, in the form of
        projects/[PROJECT]/notes/[NOTE_ID]. This field can be used as a
        filter in list requests.
        """
        return pulumi.get(self, "note_name")

    @note_name.setter
    def note_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "note_name", value)

    @property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[str]:
        """
        Required. Immutable. A URI that represents the resource for which
        the occurrence applies. For example,
        https://gcr.io/project/image@sha256:123abc for a Docker image.
        """
        return pulumi.get(self, "resource_uri")

    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_uri", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def remediation(self) -> Optional[pulumi.Input[str]]:
        """
        A description of actions that can be taken to remedy the note.
        """
        return pulumi.get(self, "remediation")

    @remediation.setter
    def remediation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remediation", value)


@pulumi.input_type
class _OccurenceState:
    def __init__(__self__, *,
                 attestation: Optional[pulumi.Input['OccurenceAttestationArgs']] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 note_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 remediation: Optional[pulumi.Input[str]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Occurence resources.
        :param pulumi.Input['OccurenceAttestationArgs'] attestation: Occurrence that represents a single "attestation". The authenticity
               of an attestation can be verified using the attached signature.
               If the verifier trusts the public key of the signer, then verifying
               the signature is sufficient to establish trust. In this circumstance,
               the authority to which this attestation is attached is primarily
               useful for lookup (how to find this attestation if you already
               know the authority and artifact to be verified) and intent (for
               which authority this attestation was intended to sign.
               Structure is documented below.
        :param pulumi.Input[str] create_time: The time when the repository was created.
        :param pulumi.Input[str] kind: The note kind which explicitly denotes which of the occurrence
               details are specified. This field can be used as a filter in list
               requests.
        :param pulumi.Input[str] name: The name of the occurrence.
        :param pulumi.Input[str] note_name: The analysis note associated with this occurrence, in the form of
               projects/[PROJECT]/notes/[NOTE_ID]. This field can be used as a
               filter in list requests.
        :param pulumi.Input[str] remediation: A description of actions that can be taken to remedy the note.
        :param pulumi.Input[str] resource_uri: Required. Immutable. A URI that represents the resource for which
               the occurrence applies. For example,
               https://gcr.io/project/image@sha256:123abc for a Docker image.
        :param pulumi.Input[str] update_time: The time when the repository was last updated.
        """
        if attestation is not None:
            pulumi.set(__self__, "attestation", attestation)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if note_name is not None:
            pulumi.set(__self__, "note_name", note_name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if remediation is not None:
            pulumi.set(__self__, "remediation", remediation)
        if resource_uri is not None:
            pulumi.set(__self__, "resource_uri", resource_uri)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def attestation(self) -> Optional[pulumi.Input['OccurenceAttestationArgs']]:
        """
        Occurrence that represents a single "attestation". The authenticity
        of an attestation can be verified using the attached signature.
        If the verifier trusts the public key of the signer, then verifying
        the signature is sufficient to establish trust. In this circumstance,
        the authority to which this attestation is attached is primarily
        useful for lookup (how to find this attestation if you already
        know the authority and artifact to be verified) and intent (for
        which authority this attestation was intended to sign.
        Structure is documented below.
        """
        return pulumi.get(self, "attestation")

    @attestation.setter
    def attestation(self, value: Optional[pulumi.Input['OccurenceAttestationArgs']]):
        pulumi.set(self, "attestation", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time when the repository was created.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        The note kind which explicitly denotes which of the occurrence
        details are specified. This field can be used as a filter in list
        requests.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the occurrence.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="noteName")
    def note_name(self) -> Optional[pulumi.Input[str]]:
        """
        The analysis note associated with this occurrence, in the form of
        projects/[PROJECT]/notes/[NOTE_ID]. This field can be used as a
        filter in list requests.
        """
        return pulumi.get(self, "note_name")

    @note_name.setter
    def note_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "note_name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def remediation(self) -> Optional[pulumi.Input[str]]:
        """
        A description of actions that can be taken to remedy the note.
        """
        return pulumi.get(self, "remediation")

    @remediation.setter
    def remediation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remediation", value)

    @property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Immutable. A URI that represents the resource for which
        the occurrence applies. For example,
        https://gcr.io/project/image@sha256:123abc for a Docker image.
        """
        return pulumi.get(self, "resource_uri")

    @resource_uri.setter
    def resource_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_uri", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time when the repository was last updated.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class Occurence(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attestation: Optional[pulumi.Input[Union['OccurenceAttestationArgs', 'OccurenceAttestationArgsDict']]] = None,
                 note_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 remediation: Optional[pulumi.Input[str]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An occurrence is an instance of a Note, or type of analysis that
        can be done for a resource.

        To get more information about Occurrence, see:

        * [API documentation](https://cloud.google.com/container-analysis/api/reference/rest/)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/container-analysis/)

        ## Example Usage

        ## Import

        Occurrence can be imported using any of these accepted formats:

        * `projects/{{project}}/occurrences/{{name}}`

        * `{{project}}/{{name}}`

        * `{{name}}`

        When using the `pulumi import` command, Occurrence can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:containeranalysis/occurence:Occurence default projects/{{project}}/occurrences/{{name}}
        ```

        ```sh
        $ pulumi import gcp:containeranalysis/occurence:Occurence default {{project}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:containeranalysis/occurence:Occurence default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['OccurenceAttestationArgs', 'OccurenceAttestationArgsDict']] attestation: Occurrence that represents a single "attestation". The authenticity
               of an attestation can be verified using the attached signature.
               If the verifier trusts the public key of the signer, then verifying
               the signature is sufficient to establish trust. In this circumstance,
               the authority to which this attestation is attached is primarily
               useful for lookup (how to find this attestation if you already
               know the authority and artifact to be verified) and intent (for
               which authority this attestation was intended to sign.
               Structure is documented below.
        :param pulumi.Input[str] note_name: The analysis note associated with this occurrence, in the form of
               projects/[PROJECT]/notes/[NOTE_ID]. This field can be used as a
               filter in list requests.
        :param pulumi.Input[str] remediation: A description of actions that can be taken to remedy the note.
        :param pulumi.Input[str] resource_uri: Required. Immutable. A URI that represents the resource for which
               the occurrence applies. For example,
               https://gcr.io/project/image@sha256:123abc for a Docker image.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OccurenceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An occurrence is an instance of a Note, or type of analysis that
        can be done for a resource.

        To get more information about Occurrence, see:

        * [API documentation](https://cloud.google.com/container-analysis/api/reference/rest/)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/container-analysis/)

        ## Example Usage

        ## Import

        Occurrence can be imported using any of these accepted formats:

        * `projects/{{project}}/occurrences/{{name}}`

        * `{{project}}/{{name}}`

        * `{{name}}`

        When using the `pulumi import` command, Occurrence can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:containeranalysis/occurence:Occurence default projects/{{project}}/occurrences/{{name}}
        ```

        ```sh
        $ pulumi import gcp:containeranalysis/occurence:Occurence default {{project}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:containeranalysis/occurence:Occurence default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param OccurenceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OccurenceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attestation: Optional[pulumi.Input[Union['OccurenceAttestationArgs', 'OccurenceAttestationArgsDict']]] = None,
                 note_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 remediation: Optional[pulumi.Input[str]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OccurenceArgs.__new__(OccurenceArgs)

            if attestation is None and not opts.urn:
                raise TypeError("Missing required property 'attestation'")
            __props__.__dict__["attestation"] = attestation
            if note_name is None and not opts.urn:
                raise TypeError("Missing required property 'note_name'")
            __props__.__dict__["note_name"] = note_name
            __props__.__dict__["project"] = project
            __props__.__dict__["remediation"] = remediation
            if resource_uri is None and not opts.urn:
                raise TypeError("Missing required property 'resource_uri'")
            __props__.__dict__["resource_uri"] = resource_uri
            __props__.__dict__["create_time"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["update_time"] = None
        super(Occurence, __self__).__init__(
            'gcp:containeranalysis/occurence:Occurence',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            attestation: Optional[pulumi.Input[Union['OccurenceAttestationArgs', 'OccurenceAttestationArgsDict']]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            kind: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            note_name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            remediation: Optional[pulumi.Input[str]] = None,
            resource_uri: Optional[pulumi.Input[str]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'Occurence':
        """
        Get an existing Occurence resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['OccurenceAttestationArgs', 'OccurenceAttestationArgsDict']] attestation: Occurrence that represents a single "attestation". The authenticity
               of an attestation can be verified using the attached signature.
               If the verifier trusts the public key of the signer, then verifying
               the signature is sufficient to establish trust. In this circumstance,
               the authority to which this attestation is attached is primarily
               useful for lookup (how to find this attestation if you already
               know the authority and artifact to be verified) and intent (for
               which authority this attestation was intended to sign.
               Structure is documented below.
        :param pulumi.Input[str] create_time: The time when the repository was created.
        :param pulumi.Input[str] kind: The note kind which explicitly denotes which of the occurrence
               details are specified. This field can be used as a filter in list
               requests.
        :param pulumi.Input[str] name: The name of the occurrence.
        :param pulumi.Input[str] note_name: The analysis note associated with this occurrence, in the form of
               projects/[PROJECT]/notes/[NOTE_ID]. This field can be used as a
               filter in list requests.
        :param pulumi.Input[str] remediation: A description of actions that can be taken to remedy the note.
        :param pulumi.Input[str] resource_uri: Required. Immutable. A URI that represents the resource for which
               the occurrence applies. For example,
               https://gcr.io/project/image@sha256:123abc for a Docker image.
        :param pulumi.Input[str] update_time: The time when the repository was last updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OccurenceState.__new__(_OccurenceState)

        __props__.__dict__["attestation"] = attestation
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["kind"] = kind
        __props__.__dict__["name"] = name
        __props__.__dict__["note_name"] = note_name
        __props__.__dict__["project"] = project
        __props__.__dict__["remediation"] = remediation
        __props__.__dict__["resource_uri"] = resource_uri
        __props__.__dict__["update_time"] = update_time
        return Occurence(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def attestation(self) -> pulumi.Output['outputs.OccurenceAttestation']:
        """
        Occurrence that represents a single "attestation". The authenticity
        of an attestation can be verified using the attached signature.
        If the verifier trusts the public key of the signer, then verifying
        the signature is sufficient to establish trust. In this circumstance,
        the authority to which this attestation is attached is primarily
        useful for lookup (how to find this attestation if you already
        know the authority and artifact to be verified) and intent (for
        which authority this attestation was intended to sign.
        Structure is documented below.
        """
        return pulumi.get(self, "attestation")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time when the repository was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The note kind which explicitly denotes which of the occurrence
        details are specified. This field can be used as a filter in list
        requests.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the occurrence.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="noteName")
    def note_name(self) -> pulumi.Output[str]:
        """
        The analysis note associated with this occurrence, in the form of
        projects/[PROJECT]/notes/[NOTE_ID]. This field can be used as a
        filter in list requests.
        """
        return pulumi.get(self, "note_name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def remediation(self) -> pulumi.Output[Optional[str]]:
        """
        A description of actions that can be taken to remedy the note.
        """
        return pulumi.get(self, "remediation")

    @property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Output[str]:
        """
        Required. Immutable. A URI that represents the resource for which
        the occurrence applies. For example,
        https://gcr.io/project/image@sha256:123abc for a Docker image.
        """
        return pulumi.get(self, "resource_uri")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time when the repository was last updated.
        """
        return pulumi.get(self, "update_time")

