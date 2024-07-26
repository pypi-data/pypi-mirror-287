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
    'GetAiIndexResult',
    'AwaitableGetAiIndexResult',
    'get_ai_index',
    'get_ai_index_output',
]

@pulumi.output_type
class GetAiIndexResult:
    """
    A collection of values returned by getAiIndex.
    """
    def __init__(__self__, create_time=None, deployed_indexes=None, description=None, display_name=None, effective_labels=None, etag=None, id=None, index_stats=None, index_update_method=None, labels=None, metadata_schema_uri=None, metadatas=None, name=None, project=None, pulumi_labels=None, region=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if deployed_indexes and not isinstance(deployed_indexes, list):
            raise TypeError("Expected argument 'deployed_indexes' to be a list")
        pulumi.set(__self__, "deployed_indexes", deployed_indexes)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if effective_labels and not isinstance(effective_labels, dict):
            raise TypeError("Expected argument 'effective_labels' to be a dict")
        pulumi.set(__self__, "effective_labels", effective_labels)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if index_stats and not isinstance(index_stats, list):
            raise TypeError("Expected argument 'index_stats' to be a list")
        pulumi.set(__self__, "index_stats", index_stats)
        if index_update_method and not isinstance(index_update_method, str):
            raise TypeError("Expected argument 'index_update_method' to be a str")
        pulumi.set(__self__, "index_update_method", index_update_method)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if metadata_schema_uri and not isinstance(metadata_schema_uri, str):
            raise TypeError("Expected argument 'metadata_schema_uri' to be a str")
        pulumi.set(__self__, "metadata_schema_uri", metadata_schema_uri)
        if metadatas and not isinstance(metadatas, list):
            raise TypeError("Expected argument 'metadatas' to be a list")
        pulumi.set(__self__, "metadatas", metadatas)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if pulumi_labels and not isinstance(pulumi_labels, dict):
            raise TypeError("Expected argument 'pulumi_labels' to be a dict")
        pulumi.set(__self__, "pulumi_labels", pulumi_labels)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="deployedIndexes")
    def deployed_indexes(self) -> Sequence['outputs.GetAiIndexDeployedIndexResult']:
        return pulumi.get(self, "deployed_indexes")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, str]:
        return pulumi.get(self, "effective_labels")

    @property
    @pulumi.getter
    def etag(self) -> str:
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="indexStats")
    def index_stats(self) -> Sequence['outputs.GetAiIndexIndexStatResult']:
        return pulumi.get(self, "index_stats")

    @property
    @pulumi.getter(name="indexUpdateMethod")
    def index_update_method(self) -> str:
        return pulumi.get(self, "index_update_method")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="metadataSchemaUri")
    def metadata_schema_uri(self) -> str:
        return pulumi.get(self, "metadata_schema_uri")

    @property
    @pulumi.getter
    def metadatas(self) -> Sequence['outputs.GetAiIndexMetadataResult']:
        return pulumi.get(self, "metadatas")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, str]:
        return pulumi.get(self, "pulumi_labels")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        return pulumi.get(self, "update_time")


class AwaitableGetAiIndexResult(GetAiIndexResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAiIndexResult(
            create_time=self.create_time,
            deployed_indexes=self.deployed_indexes,
            description=self.description,
            display_name=self.display_name,
            effective_labels=self.effective_labels,
            etag=self.etag,
            id=self.id,
            index_stats=self.index_stats,
            index_update_method=self.index_update_method,
            labels=self.labels,
            metadata_schema_uri=self.metadata_schema_uri,
            metadatas=self.metadatas,
            name=self.name,
            project=self.project,
            pulumi_labels=self.pulumi_labels,
            region=self.region,
            update_time=self.update_time)


def get_ai_index(name: Optional[str] = None,
                 project: Optional[str] = None,
                 region: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAiIndexResult:
    """
    A representation of a collection of database items organized in a way that allows for approximate nearest neighbor (a.k.a ANN) algorithms search.


    :param str name: The name of the index.
    :param str project: The ID of the project in which the resource belongs.
    :param str region: The region of the index.
           
           - - -
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    __args__['region'] = region
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:vertex/getAiIndex:getAiIndex', __args__, opts=opts, typ=GetAiIndexResult).value

    return AwaitableGetAiIndexResult(
        create_time=pulumi.get(__ret__, 'create_time'),
        deployed_indexes=pulumi.get(__ret__, 'deployed_indexes'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        effective_labels=pulumi.get(__ret__, 'effective_labels'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        index_stats=pulumi.get(__ret__, 'index_stats'),
        index_update_method=pulumi.get(__ret__, 'index_update_method'),
        labels=pulumi.get(__ret__, 'labels'),
        metadata_schema_uri=pulumi.get(__ret__, 'metadata_schema_uri'),
        metadatas=pulumi.get(__ret__, 'metadatas'),
        name=pulumi.get(__ret__, 'name'),
        project=pulumi.get(__ret__, 'project'),
        pulumi_labels=pulumi.get(__ret__, 'pulumi_labels'),
        region=pulumi.get(__ret__, 'region'),
        update_time=pulumi.get(__ret__, 'update_time'))


@_utilities.lift_output_func(get_ai_index)
def get_ai_index_output(name: Optional[pulumi.Input[str]] = None,
                        project: Optional[pulumi.Input[Optional[str]]] = None,
                        region: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAiIndexResult]:
    """
    A representation of a collection of database items organized in a way that allows for approximate nearest neighbor (a.k.a ANN) algorithms search.


    :param str name: The name of the index.
    :param str project: The ID of the project in which the resource belongs.
    :param str region: The region of the index.
           
           - - -
    """
    ...
