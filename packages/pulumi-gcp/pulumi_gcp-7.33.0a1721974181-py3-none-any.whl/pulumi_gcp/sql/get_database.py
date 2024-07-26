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
    'GetDatabaseResult',
    'AwaitableGetDatabaseResult',
    'get_database',
    'get_database_output',
]

@pulumi.output_type
class GetDatabaseResult:
    """
    A collection of values returned by getDatabase.
    """
    def __init__(__self__, charset=None, collation=None, deletion_policy=None, id=None, instance=None, name=None, project=None, self_link=None):
        if charset and not isinstance(charset, str):
            raise TypeError("Expected argument 'charset' to be a str")
        pulumi.set(__self__, "charset", charset)
        if collation and not isinstance(collation, str):
            raise TypeError("Expected argument 'collation' to be a str")
        pulumi.set(__self__, "collation", collation)
        if deletion_policy and not isinstance(deletion_policy, str):
            raise TypeError("Expected argument 'deletion_policy' to be a str")
        pulumi.set(__self__, "deletion_policy", deletion_policy)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance and not isinstance(instance, str):
            raise TypeError("Expected argument 'instance' to be a str")
        pulumi.set(__self__, "instance", instance)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)

    @property
    @pulumi.getter
    def charset(self) -> str:
        return pulumi.get(self, "charset")

    @property
    @pulumi.getter
    def collation(self) -> str:
        return pulumi.get(self, "collation")

    @property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> str:
        return pulumi.get(self, "deletion_policy")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def instance(self) -> str:
        return pulumi.get(self, "instance")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        return pulumi.get(self, "self_link")


class AwaitableGetDatabaseResult(GetDatabaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseResult(
            charset=self.charset,
            collation=self.collation,
            deletion_policy=self.deletion_policy,
            id=self.id,
            instance=self.instance,
            name=self.name,
            project=self.project,
            self_link=self.self_link)


def get_database(instance: Optional[str] = None,
                 name: Optional[str] = None,
                 project: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseResult:
    """
    Use this data source to get information about a database in a Cloud SQL instance.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    qa = gcp.sql.get_database(name="test-sql-database",
        instance=main["name"])
    ```


    :param str instance: The name of the Cloud SQL database instance in which the database belongs.
    :param str name: The name of the database.
    :param str project: The ID of the project in which the instance belongs.
    """
    __args__ = dict()
    __args__['instance'] = instance
    __args__['name'] = name
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:sql/getDatabase:getDatabase', __args__, opts=opts, typ=GetDatabaseResult).value

    return AwaitableGetDatabaseResult(
        charset=pulumi.get(__ret__, 'charset'),
        collation=pulumi.get(__ret__, 'collation'),
        deletion_policy=pulumi.get(__ret__, 'deletion_policy'),
        id=pulumi.get(__ret__, 'id'),
        instance=pulumi.get(__ret__, 'instance'),
        name=pulumi.get(__ret__, 'name'),
        project=pulumi.get(__ret__, 'project'),
        self_link=pulumi.get(__ret__, 'self_link'))


@_utilities.lift_output_func(get_database)
def get_database_output(instance: Optional[pulumi.Input[str]] = None,
                        name: Optional[pulumi.Input[str]] = None,
                        project: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseResult]:
    """
    Use this data source to get information about a database in a Cloud SQL instance.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    qa = gcp.sql.get_database(name="test-sql-database",
        instance=main["name"])
    ```


    :param str instance: The name of the Cloud SQL database instance in which the database belongs.
    :param str name: The name of the database.
    :param str project: The ID of the project in which the instance belongs.
    """
    ...
