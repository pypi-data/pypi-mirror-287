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

__all__ = ['VolumeSnapshotArgs', 'VolumeSnapshot']

@pulumi.input_type
class VolumeSnapshotArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 volume_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VolumeSnapshot resource.
        :param pulumi.Input[str] location: Name of the snapshot location. Snapshots are child resources of volumes and live in the same location.
        :param pulumi.Input[str] volume_name: The name of the volume to create the snapshot in.
        :param pulumi.Input[str] description: Description for the snapshot.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels as key value pairs. Example: `{ "owner": "Bob", "department": "finance", "purpose": "testing" }`.
               
               **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
               Please refer to the field `effective_labels` for all of the labels present on the resource.
        :param pulumi.Input[str] name: The name of the snapshot.
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "volume_name", volume_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        Name of the snapshot location. Snapshots are child resources of volumes and live in the same location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> pulumi.Input[str]:
        """
        The name of the volume to create the snapshot in.
        """
        return pulumi.get(self, "volume_name")

    @volume_name.setter
    def volume_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "volume_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description for the snapshot.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels as key value pairs. Example: `{ "owner": "Bob", "department": "finance", "purpose": "testing" }`.

        **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
        Please refer to the field `effective_labels` for all of the labels present on the resource.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the snapshot.


        - - -
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


@pulumi.input_type
class _VolumeSnapshotState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 used_bytes: Optional[pulumi.Input[int]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VolumeSnapshot resources.
        :param pulumi.Input[str] description: Description for the snapshot.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] effective_labels: All of labels (key/value pairs) present on the resource in GCP, including the labels configured through Pulumi, other clients and services.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels as key value pairs. Example: `{ "owner": "Bob", "department": "finance", "purpose": "testing" }`.
               
               **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
               Please refer to the field `effective_labels` for all of the labels present on the resource.
        :param pulumi.Input[str] location: Name of the snapshot location. Snapshots are child resources of volumes and live in the same location.
        :param pulumi.Input[str] name: The name of the snapshot.
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] pulumi_labels: The combination of labels configured directly on the resource
               and default labels configured on the provider.
        :param pulumi.Input[int] used_bytes: Storage used to store blocks unique to this snapshot.
        :param pulumi.Input[str] volume_name: The name of the volume to create the snapshot in.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if effective_labels is not None:
            pulumi.set(__self__, "effective_labels", effective_labels)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if pulumi_labels is not None:
            pulumi.set(__self__, "pulumi_labels", pulumi_labels)
        if used_bytes is not None:
            pulumi.set(__self__, "used_bytes", used_bytes)
        if volume_name is not None:
            pulumi.set(__self__, "volume_name", volume_name)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description for the snapshot.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        All of labels (key/value pairs) present on the resource in GCP, including the labels configured through Pulumi, other clients and services.
        """
        return pulumi.get(self, "effective_labels")

    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "effective_labels", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels as key value pairs. Example: `{ "owner": "Bob", "department": "finance", "purpose": "testing" }`.

        **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
        Please refer to the field `effective_labels` for all of the labels present on the resource.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the snapshot location. Snapshots are child resources of volumes and live in the same location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the snapshot.


        - - -
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
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The combination of labels configured directly on the resource
        and default labels configured on the provider.
        """
        return pulumi.get(self, "pulumi_labels")

    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "pulumi_labels", value)

    @property
    @pulumi.getter(name="usedBytes")
    def used_bytes(self) -> Optional[pulumi.Input[int]]:
        """
        Storage used to store blocks unique to this snapshot.
        """
        return pulumi.get(self, "used_bytes")

    @used_bytes.setter
    def used_bytes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "used_bytes", value)

    @property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the volume to create the snapshot in.
        """
        return pulumi.get(self, "volume_name")

    @volume_name.setter
    def volume_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_name", value)


class VolumeSnapshot(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        NetApp Volumes helps you manage your data usage with snapshots that can quickly restore lost data.
        Snapshots are point-in-time versions of your volume's content. They are resources of volumes and are
        instant captures of your data that consume space only for modified data. Because data changes over
        time, snapshots usually consume more space as they get older.
        NetApp Volumes volumes use just-in-time copy-on-write so that unmodified files in snapshots don't
        consume any of the volume's capacity.

        To get more information about VolumeSnapshot, see:

        * [API documentation](https://cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.snapshots)
        * How-to Guides
            * [Documentation](https://cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/overview)

        ## Example Usage

        ### Volume Snapshot Create

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.compute.get_network(name="test-network")
        default_storage_pool = gcp.netapp.StoragePool("default",
            name="test-pool",
            location="us-west2",
            service_level="PREMIUM",
            capacity_gib="2048",
            network=default.id)
        default_volume = gcp.netapp.Volume("default",
            location=default_storage_pool.location,
            name="test-volume",
            capacity_gib="100",
            share_name="test-volume",
            storage_pool=default_storage_pool.name,
            protocols=["NFSV3"])
        test_snapshot = gcp.netapp.VolumeSnapshot("test_snapshot",
            location=default_volume.location,
            volume_name=default_volume.name,
            name="testvolumesnap",
            opts = pulumi.ResourceOptions(depends_on=[default_volume]))
        ```

        ## Import

        VolumeSnapshot can be imported using any of these accepted formats:

        * `projects/{{project}}/locations/{{location}}/volumes/{{volume_name}}/snapshots/{{name}}`

        * `{{project}}/{{location}}/{{volume_name}}/{{name}}`

        * `{{location}}/{{volume_name}}/{{name}}`

        When using the `pulumi import` command, VolumeSnapshot can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:netapp/volumeSnapshot:VolumeSnapshot default projects/{{project}}/locations/{{location}}/volumes/{{volume_name}}/snapshots/{{name}}
        ```

        ```sh
        $ pulumi import gcp:netapp/volumeSnapshot:VolumeSnapshot default {{project}}/{{location}}/{{volume_name}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:netapp/volumeSnapshot:VolumeSnapshot default {{location}}/{{volume_name}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description for the snapshot.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels as key value pairs. Example: `{ "owner": "Bob", "department": "finance", "purpose": "testing" }`.
               
               **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
               Please refer to the field `effective_labels` for all of the labels present on the resource.
        :param pulumi.Input[str] location: Name of the snapshot location. Snapshots are child resources of volumes and live in the same location.
        :param pulumi.Input[str] name: The name of the snapshot.
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] volume_name: The name of the volume to create the snapshot in.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeSnapshotArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        NetApp Volumes helps you manage your data usage with snapshots that can quickly restore lost data.
        Snapshots are point-in-time versions of your volume's content. They are resources of volumes and are
        instant captures of your data that consume space only for modified data. Because data changes over
        time, snapshots usually consume more space as they get older.
        NetApp Volumes volumes use just-in-time copy-on-write so that unmodified files in snapshots don't
        consume any of the volume's capacity.

        To get more information about VolumeSnapshot, see:

        * [API documentation](https://cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.snapshots)
        * How-to Guides
            * [Documentation](https://cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/overview)

        ## Example Usage

        ### Volume Snapshot Create

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.compute.get_network(name="test-network")
        default_storage_pool = gcp.netapp.StoragePool("default",
            name="test-pool",
            location="us-west2",
            service_level="PREMIUM",
            capacity_gib="2048",
            network=default.id)
        default_volume = gcp.netapp.Volume("default",
            location=default_storage_pool.location,
            name="test-volume",
            capacity_gib="100",
            share_name="test-volume",
            storage_pool=default_storage_pool.name,
            protocols=["NFSV3"])
        test_snapshot = gcp.netapp.VolumeSnapshot("test_snapshot",
            location=default_volume.location,
            volume_name=default_volume.name,
            name="testvolumesnap",
            opts = pulumi.ResourceOptions(depends_on=[default_volume]))
        ```

        ## Import

        VolumeSnapshot can be imported using any of these accepted formats:

        * `projects/{{project}}/locations/{{location}}/volumes/{{volume_name}}/snapshots/{{name}}`

        * `{{project}}/{{location}}/{{volume_name}}/{{name}}`

        * `{{location}}/{{volume_name}}/{{name}}`

        When using the `pulumi import` command, VolumeSnapshot can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:netapp/volumeSnapshot:VolumeSnapshot default projects/{{project}}/locations/{{location}}/volumes/{{volume_name}}/snapshots/{{name}}
        ```

        ```sh
        $ pulumi import gcp:netapp/volumeSnapshot:VolumeSnapshot default {{project}}/{{location}}/{{volume_name}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:netapp/volumeSnapshot:VolumeSnapshot default {{location}}/{{volume_name}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param VolumeSnapshotArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeSnapshotArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeSnapshotArgs.__new__(VolumeSnapshotArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            if volume_name is None and not opts.urn:
                raise TypeError("Missing required property 'volume_name'")
            __props__.__dict__["volume_name"] = volume_name
            __props__.__dict__["effective_labels"] = None
            __props__.__dict__["pulumi_labels"] = None
            __props__.__dict__["used_bytes"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["effectiveLabels", "pulumiLabels"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(VolumeSnapshot, __self__).__init__(
            'gcp:netapp/volumeSnapshot:VolumeSnapshot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            used_bytes: Optional[pulumi.Input[int]] = None,
            volume_name: Optional[pulumi.Input[str]] = None) -> 'VolumeSnapshot':
        """
        Get an existing VolumeSnapshot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description for the snapshot.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] effective_labels: All of labels (key/value pairs) present on the resource in GCP, including the labels configured through Pulumi, other clients and services.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels as key value pairs. Example: `{ "owner": "Bob", "department": "finance", "purpose": "testing" }`.
               
               **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
               Please refer to the field `effective_labels` for all of the labels present on the resource.
        :param pulumi.Input[str] location: Name of the snapshot location. Snapshots are child resources of volumes and live in the same location.
        :param pulumi.Input[str] name: The name of the snapshot.
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] pulumi_labels: The combination of labels configured directly on the resource
               and default labels configured on the provider.
        :param pulumi.Input[int] used_bytes: Storage used to store blocks unique to this snapshot.
        :param pulumi.Input[str] volume_name: The name of the volume to create the snapshot in.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VolumeSnapshotState.__new__(_VolumeSnapshotState)

        __props__.__dict__["description"] = description
        __props__.__dict__["effective_labels"] = effective_labels
        __props__.__dict__["labels"] = labels
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["pulumi_labels"] = pulumi_labels
        __props__.__dict__["used_bytes"] = used_bytes
        __props__.__dict__["volume_name"] = volume_name
        return VolumeSnapshot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description for the snapshot.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        All of labels (key/value pairs) present on the resource in GCP, including the labels configured through Pulumi, other clients and services.
        """
        return pulumi.get(self, "effective_labels")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Labels as key value pairs. Example: `{ "owner": "Bob", "department": "finance", "purpose": "testing" }`.

        **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
        Please refer to the field `effective_labels` for all of the labels present on the resource.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Name of the snapshot location. Snapshots are child resources of volumes and live in the same location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the snapshot.


        - - -
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
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The combination of labels configured directly on the resource
        and default labels configured on the provider.
        """
        return pulumi.get(self, "pulumi_labels")

    @property
    @pulumi.getter(name="usedBytes")
    def used_bytes(self) -> pulumi.Output[int]:
        """
        Storage used to store blocks unique to this snapshot.
        """
        return pulumi.get(self, "used_bytes")

    @property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> pulumi.Output[str]:
        """
        The name of the volume to create the snapshot in.
        """
        return pulumi.get(self, "volume_name")

