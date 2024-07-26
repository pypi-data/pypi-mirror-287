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

__all__ = ['UserArgs', 'User']

@pulumi.input_type
class UserArgs:
    def __init__(__self__, *,
                 cluster: pulumi.Input[str],
                 user_id: pulumi.Input[str],
                 user_type: pulumi.Input[str],
                 database_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 password: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a User resource.
        :param pulumi.Input[str] cluster: Identifies the alloydb cluster. Must be in the format
               'projects/{project}/locations/{location}/clusters/{cluster_id}'
        :param pulumi.Input[str] user_id: The database role name of the user.
        :param pulumi.Input[str] user_type: The type of this user.
               Possible values are: `ALLOYDB_BUILT_IN`, `ALLOYDB_IAM_USER`.
               
               
               - - -
        :param pulumi.Input[Sequence[pulumi.Input[str]]] database_roles: List of database roles this database user has.
        :param pulumi.Input[str] password: Password for this database user.
        """
        pulumi.set(__self__, "cluster", cluster)
        pulumi.set(__self__, "user_id", user_id)
        pulumi.set(__self__, "user_type", user_type)
        if database_roles is not None:
            pulumi.set(__self__, "database_roles", database_roles)
        if password is not None:
            pulumi.set(__self__, "password", password)

    @property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[str]:
        """
        Identifies the alloydb cluster. Must be in the format
        'projects/{project}/locations/{location}/clusters/{cluster_id}'
        """
        return pulumi.get(self, "cluster")

    @cluster.setter
    def cluster(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[str]:
        """
        The database role name of the user.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter(name="userType")
    def user_type(self) -> pulumi.Input[str]:
        """
        The type of this user.
        Possible values are: `ALLOYDB_BUILT_IN`, `ALLOYDB_IAM_USER`.


        - - -
        """
        return pulumi.get(self, "user_type")

    @user_type.setter
    def user_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_type", value)

    @property
    @pulumi.getter(name="databaseRoles")
    def database_roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of database roles this database user has.
        """
        return pulumi.get(self, "database_roles")

    @database_roles.setter
    def database_roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "database_roles", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password for this database user.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)


@pulumi.input_type
class _UserState:
    def __init__(__self__, *,
                 cluster: Optional[pulumi.Input[str]] = None,
                 database_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 user_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering User resources.
        :param pulumi.Input[str] cluster: Identifies the alloydb cluster. Must be in the format
               'projects/{project}/locations/{location}/clusters/{cluster_id}'
        :param pulumi.Input[Sequence[pulumi.Input[str]]] database_roles: List of database roles this database user has.
        :param pulumi.Input[str] name: Name of the resource in the form of projects/{project}/locations/{location}/clusters/{cluster}/users/{user}.
        :param pulumi.Input[str] password: Password for this database user.
        :param pulumi.Input[str] user_id: The database role name of the user.
        :param pulumi.Input[str] user_type: The type of this user.
               Possible values are: `ALLOYDB_BUILT_IN`, `ALLOYDB_IAM_USER`.
               
               
               - - -
        """
        if cluster is not None:
            pulumi.set(__self__, "cluster", cluster)
        if database_roles is not None:
            pulumi.set(__self__, "database_roles", database_roles)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)
        if user_type is not None:
            pulumi.set(__self__, "user_type", user_type)

    @property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[str]]:
        """
        Identifies the alloydb cluster. Must be in the format
        'projects/{project}/locations/{location}/clusters/{cluster_id}'
        """
        return pulumi.get(self, "cluster")

    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster", value)

    @property
    @pulumi.getter(name="databaseRoles")
    def database_roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of database roles this database user has.
        """
        return pulumi.get(self, "database_roles")

    @database_roles.setter
    def database_roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "database_roles", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource in the form of projects/{project}/locations/{location}/clusters/{cluster}/users/{user}.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password for this database user.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        The database role name of the user.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter(name="userType")
    def user_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of this user.
        Possible values are: `ALLOYDB_BUILT_IN`, `ALLOYDB_IAM_USER`.


        - - -
        """
        return pulumi.get(self, "user_type")

    @user_type.setter
    def user_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_type", value)


class User(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster: Optional[pulumi.Input[str]] = None,
                 database_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 user_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A database user in an AlloyDB cluster.

        To get more information about User, see:

        * [API documentation](https://cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.users/create)
        * How-to Guides
            * [AlloyDB](https://cloud.google.com/alloydb/docs/)

        ## Example Usage

        ### Alloydb User Builtin

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default_network = gcp.compute.Network("default", name="alloydb-network")
        default_cluster = gcp.alloydb.Cluster("default",
            cluster_id="alloydb-cluster",
            location="us-central1",
            network=default_network.id,
            initial_user={
                "password": "cluster_secret",
            })
        private_ip_alloc = gcp.compute.GlobalAddress("private_ip_alloc",
            name="alloydb-cluster",
            address_type="INTERNAL",
            purpose="VPC_PEERING",
            prefix_length=16,
            network=default_network.id)
        vpc_connection = gcp.servicenetworking.Connection("vpc_connection",
            network=default_network.id,
            service="servicenetworking.googleapis.com",
            reserved_peering_ranges=[private_ip_alloc.name])
        default = gcp.alloydb.Instance("default",
            cluster=default_cluster.name,
            instance_id="alloydb-instance",
            instance_type="PRIMARY",
            opts = pulumi.ResourceOptions(depends_on=[vpc_connection]))
        project = gcp.organizations.get_project()
        user1 = gcp.alloydb.User("user1",
            cluster=default_cluster.name,
            user_id="user1",
            user_type="ALLOYDB_BUILT_IN",
            password="user_secret",
            database_roles=["alloydbsuperuser"],
            opts = pulumi.ResourceOptions(depends_on=[default]))
        ```
        ### Alloydb User Iam

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default_network = gcp.compute.Network("default", name="alloydb-network")
        default_cluster = gcp.alloydb.Cluster("default",
            cluster_id="alloydb-cluster",
            location="us-central1",
            network=default_network.id,
            initial_user={
                "password": "cluster_secret",
            })
        private_ip_alloc = gcp.compute.GlobalAddress("private_ip_alloc",
            name="alloydb-cluster",
            address_type="INTERNAL",
            purpose="VPC_PEERING",
            prefix_length=16,
            network=default_network.id)
        vpc_connection = gcp.servicenetworking.Connection("vpc_connection",
            network=default_network.id,
            service="servicenetworking.googleapis.com",
            reserved_peering_ranges=[private_ip_alloc.name])
        default = gcp.alloydb.Instance("default",
            cluster=default_cluster.name,
            instance_id="alloydb-instance",
            instance_type="PRIMARY",
            opts = pulumi.ResourceOptions(depends_on=[vpc_connection]))
        project = gcp.organizations.get_project()
        user2 = gcp.alloydb.User("user2",
            cluster=default_cluster.name,
            user_id="user2@foo.com",
            user_type="ALLOYDB_IAM_USER",
            database_roles=["alloydbiamuser"],
            opts = pulumi.ResourceOptions(depends_on=[default]))
        ```

        ## Import

        User can be imported using any of these accepted formats:

        * `projects/{{project}}/locations/{{location}}/clusters/{{cluster}}/users/{{user_id}}`

        * `{{project}}/{{location}}/{{cluster}}/{{user_id}}`

        * `{{location}}/{{cluster}}/{{user_id}}`

        When using the `pulumi import` command, User can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:alloydb/user:User default projects/{{project}}/locations/{{location}}/clusters/{{cluster}}/users/{{user_id}}
        ```

        ```sh
        $ pulumi import gcp:alloydb/user:User default {{project}}/{{location}}/{{cluster}}/{{user_id}}
        ```

        ```sh
        $ pulumi import gcp:alloydb/user:User default {{location}}/{{cluster}}/{{user_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster: Identifies the alloydb cluster. Must be in the format
               'projects/{project}/locations/{location}/clusters/{cluster_id}'
        :param pulumi.Input[Sequence[pulumi.Input[str]]] database_roles: List of database roles this database user has.
        :param pulumi.Input[str] password: Password for this database user.
        :param pulumi.Input[str] user_id: The database role name of the user.
        :param pulumi.Input[str] user_type: The type of this user.
               Possible values are: `ALLOYDB_BUILT_IN`, `ALLOYDB_IAM_USER`.
               
               
               - - -
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A database user in an AlloyDB cluster.

        To get more information about User, see:

        * [API documentation](https://cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.users/create)
        * How-to Guides
            * [AlloyDB](https://cloud.google.com/alloydb/docs/)

        ## Example Usage

        ### Alloydb User Builtin

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default_network = gcp.compute.Network("default", name="alloydb-network")
        default_cluster = gcp.alloydb.Cluster("default",
            cluster_id="alloydb-cluster",
            location="us-central1",
            network=default_network.id,
            initial_user={
                "password": "cluster_secret",
            })
        private_ip_alloc = gcp.compute.GlobalAddress("private_ip_alloc",
            name="alloydb-cluster",
            address_type="INTERNAL",
            purpose="VPC_PEERING",
            prefix_length=16,
            network=default_network.id)
        vpc_connection = gcp.servicenetworking.Connection("vpc_connection",
            network=default_network.id,
            service="servicenetworking.googleapis.com",
            reserved_peering_ranges=[private_ip_alloc.name])
        default = gcp.alloydb.Instance("default",
            cluster=default_cluster.name,
            instance_id="alloydb-instance",
            instance_type="PRIMARY",
            opts = pulumi.ResourceOptions(depends_on=[vpc_connection]))
        project = gcp.organizations.get_project()
        user1 = gcp.alloydb.User("user1",
            cluster=default_cluster.name,
            user_id="user1",
            user_type="ALLOYDB_BUILT_IN",
            password="user_secret",
            database_roles=["alloydbsuperuser"],
            opts = pulumi.ResourceOptions(depends_on=[default]))
        ```
        ### Alloydb User Iam

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default_network = gcp.compute.Network("default", name="alloydb-network")
        default_cluster = gcp.alloydb.Cluster("default",
            cluster_id="alloydb-cluster",
            location="us-central1",
            network=default_network.id,
            initial_user={
                "password": "cluster_secret",
            })
        private_ip_alloc = gcp.compute.GlobalAddress("private_ip_alloc",
            name="alloydb-cluster",
            address_type="INTERNAL",
            purpose="VPC_PEERING",
            prefix_length=16,
            network=default_network.id)
        vpc_connection = gcp.servicenetworking.Connection("vpc_connection",
            network=default_network.id,
            service="servicenetworking.googleapis.com",
            reserved_peering_ranges=[private_ip_alloc.name])
        default = gcp.alloydb.Instance("default",
            cluster=default_cluster.name,
            instance_id="alloydb-instance",
            instance_type="PRIMARY",
            opts = pulumi.ResourceOptions(depends_on=[vpc_connection]))
        project = gcp.organizations.get_project()
        user2 = gcp.alloydb.User("user2",
            cluster=default_cluster.name,
            user_id="user2@foo.com",
            user_type="ALLOYDB_IAM_USER",
            database_roles=["alloydbiamuser"],
            opts = pulumi.ResourceOptions(depends_on=[default]))
        ```

        ## Import

        User can be imported using any of these accepted formats:

        * `projects/{{project}}/locations/{{location}}/clusters/{{cluster}}/users/{{user_id}}`

        * `{{project}}/{{location}}/{{cluster}}/{{user_id}}`

        * `{{location}}/{{cluster}}/{{user_id}}`

        When using the `pulumi import` command, User can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:alloydb/user:User default projects/{{project}}/locations/{{location}}/clusters/{{cluster}}/users/{{user_id}}
        ```

        ```sh
        $ pulumi import gcp:alloydb/user:User default {{project}}/{{location}}/{{cluster}}/{{user_id}}
        ```

        ```sh
        $ pulumi import gcp:alloydb/user:User default {{location}}/{{cluster}}/{{user_id}}
        ```

        :param str resource_name: The name of the resource.
        :param UserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster: Optional[pulumi.Input[str]] = None,
                 database_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 user_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserArgs.__new__(UserArgs)

            if cluster is None and not opts.urn:
                raise TypeError("Missing required property 'cluster'")
            __props__.__dict__["cluster"] = cluster
            __props__.__dict__["database_roles"] = database_roles
            __props__.__dict__["password"] = password
            if user_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_id'")
            __props__.__dict__["user_id"] = user_id
            if user_type is None and not opts.urn:
                raise TypeError("Missing required property 'user_type'")
            __props__.__dict__["user_type"] = user_type
            __props__.__dict__["name"] = None
        super(User, __self__).__init__(
            'gcp:alloydb/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster: Optional[pulumi.Input[str]] = None,
            database_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[str]] = None,
            user_type: Optional[pulumi.Input[str]] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster: Identifies the alloydb cluster. Must be in the format
               'projects/{project}/locations/{location}/clusters/{cluster_id}'
        :param pulumi.Input[Sequence[pulumi.Input[str]]] database_roles: List of database roles this database user has.
        :param pulumi.Input[str] name: Name of the resource in the form of projects/{project}/locations/{location}/clusters/{cluster}/users/{user}.
        :param pulumi.Input[str] password: Password for this database user.
        :param pulumi.Input[str] user_id: The database role name of the user.
        :param pulumi.Input[str] user_type: The type of this user.
               Possible values are: `ALLOYDB_BUILT_IN`, `ALLOYDB_IAM_USER`.
               
               
               - - -
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserState.__new__(_UserState)

        __props__.__dict__["cluster"] = cluster
        __props__.__dict__["database_roles"] = database_roles
        __props__.__dict__["name"] = name
        __props__.__dict__["password"] = password
        __props__.__dict__["user_id"] = user_id
        __props__.__dict__["user_type"] = user_type
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[str]:
        """
        Identifies the alloydb cluster. Must be in the format
        'projects/{project}/locations/{location}/clusters/{cluster_id}'
        """
        return pulumi.get(self, "cluster")

    @property
    @pulumi.getter(name="databaseRoles")
    def database_roles(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of database roles this database user has.
        """
        return pulumi.get(self, "database_roles")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource in the form of projects/{project}/locations/{location}/clusters/{cluster}/users/{user}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        Password for this database user.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        The database role name of the user.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter(name="userType")
    def user_type(self) -> pulumi.Output[str]:
        """
        The type of this user.
        Possible values are: `ALLOYDB_BUILT_IN`, `ALLOYDB_IAM_USER`.


        - - -
        """
        return pulumi.get(self, "user_type")

