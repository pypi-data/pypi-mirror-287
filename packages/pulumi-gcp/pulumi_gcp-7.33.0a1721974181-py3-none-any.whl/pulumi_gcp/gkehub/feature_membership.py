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

__all__ = ['FeatureMembershipArgs', 'FeatureMembership']

@pulumi.input_type
class FeatureMembershipArgs:
    def __init__(__self__, *,
                 feature: pulumi.Input[str],
                 location: pulumi.Input[str],
                 membership: pulumi.Input[str],
                 configmanagement: Optional[pulumi.Input['FeatureMembershipConfigmanagementArgs']] = None,
                 membership_location: Optional[pulumi.Input[str]] = None,
                 mesh: Optional[pulumi.Input['FeatureMembershipMeshArgs']] = None,
                 policycontroller: Optional[pulumi.Input['FeatureMembershipPolicycontrollerArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FeatureMembership resource.
        :param pulumi.Input[str] feature: The name of the feature
        :param pulumi.Input[str] location: The location of the feature
        :param pulumi.Input[str] membership: The name of the membership
        :param pulumi.Input['FeatureMembershipConfigmanagementArgs'] configmanagement: Config Management-specific spec. Structure is documented below.
        :param pulumi.Input[str] membership_location: The location of the membership, for example, "us-central1". Default is "global".
        :param pulumi.Input['FeatureMembershipMeshArgs'] mesh: Service mesh specific spec. Structure is documented below.
        :param pulumi.Input['FeatureMembershipPolicycontrollerArgs'] policycontroller: Policy Controller-specific spec. Structure is documented below.
        :param pulumi.Input[str] project: The project of the feature
        """
        pulumi.set(__self__, "feature", feature)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "membership", membership)
        if configmanagement is not None:
            pulumi.set(__self__, "configmanagement", configmanagement)
        if membership_location is not None:
            pulumi.set(__self__, "membership_location", membership_location)
        if mesh is not None:
            pulumi.set(__self__, "mesh", mesh)
        if policycontroller is not None:
            pulumi.set(__self__, "policycontroller", policycontroller)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def feature(self) -> pulumi.Input[str]:
        """
        The name of the feature
        """
        return pulumi.get(self, "feature")

    @feature.setter
    def feature(self, value: pulumi.Input[str]):
        pulumi.set(self, "feature", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The location of the feature
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def membership(self) -> pulumi.Input[str]:
        """
        The name of the membership
        """
        return pulumi.get(self, "membership")

    @membership.setter
    def membership(self, value: pulumi.Input[str]):
        pulumi.set(self, "membership", value)

    @property
    @pulumi.getter
    def configmanagement(self) -> Optional[pulumi.Input['FeatureMembershipConfigmanagementArgs']]:
        """
        Config Management-specific spec. Structure is documented below.
        """
        return pulumi.get(self, "configmanagement")

    @configmanagement.setter
    def configmanagement(self, value: Optional[pulumi.Input['FeatureMembershipConfigmanagementArgs']]):
        pulumi.set(self, "configmanagement", value)

    @property
    @pulumi.getter(name="membershipLocation")
    def membership_location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the membership, for example, "us-central1". Default is "global".
        """
        return pulumi.get(self, "membership_location")

    @membership_location.setter
    def membership_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "membership_location", value)

    @property
    @pulumi.getter
    def mesh(self) -> Optional[pulumi.Input['FeatureMembershipMeshArgs']]:
        """
        Service mesh specific spec. Structure is documented below.
        """
        return pulumi.get(self, "mesh")

    @mesh.setter
    def mesh(self, value: Optional[pulumi.Input['FeatureMembershipMeshArgs']]):
        pulumi.set(self, "mesh", value)

    @property
    @pulumi.getter
    def policycontroller(self) -> Optional[pulumi.Input['FeatureMembershipPolicycontrollerArgs']]:
        """
        Policy Controller-specific spec. Structure is documented below.
        """
        return pulumi.get(self, "policycontroller")

    @policycontroller.setter
    def policycontroller(self, value: Optional[pulumi.Input['FeatureMembershipPolicycontrollerArgs']]):
        pulumi.set(self, "policycontroller", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project of the feature
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _FeatureMembershipState:
    def __init__(__self__, *,
                 configmanagement: Optional[pulumi.Input['FeatureMembershipConfigmanagementArgs']] = None,
                 feature: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 membership: Optional[pulumi.Input[str]] = None,
                 membership_location: Optional[pulumi.Input[str]] = None,
                 mesh: Optional[pulumi.Input['FeatureMembershipMeshArgs']] = None,
                 policycontroller: Optional[pulumi.Input['FeatureMembershipPolicycontrollerArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FeatureMembership resources.
        :param pulumi.Input['FeatureMembershipConfigmanagementArgs'] configmanagement: Config Management-specific spec. Structure is documented below.
        :param pulumi.Input[str] feature: The name of the feature
        :param pulumi.Input[str] location: The location of the feature
        :param pulumi.Input[str] membership: The name of the membership
        :param pulumi.Input[str] membership_location: The location of the membership, for example, "us-central1". Default is "global".
        :param pulumi.Input['FeatureMembershipMeshArgs'] mesh: Service mesh specific spec. Structure is documented below.
        :param pulumi.Input['FeatureMembershipPolicycontrollerArgs'] policycontroller: Policy Controller-specific spec. Structure is documented below.
        :param pulumi.Input[str] project: The project of the feature
        """
        if configmanagement is not None:
            pulumi.set(__self__, "configmanagement", configmanagement)
        if feature is not None:
            pulumi.set(__self__, "feature", feature)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if membership is not None:
            pulumi.set(__self__, "membership", membership)
        if membership_location is not None:
            pulumi.set(__self__, "membership_location", membership_location)
        if mesh is not None:
            pulumi.set(__self__, "mesh", mesh)
        if policycontroller is not None:
            pulumi.set(__self__, "policycontroller", policycontroller)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def configmanagement(self) -> Optional[pulumi.Input['FeatureMembershipConfigmanagementArgs']]:
        """
        Config Management-specific spec. Structure is documented below.
        """
        return pulumi.get(self, "configmanagement")

    @configmanagement.setter
    def configmanagement(self, value: Optional[pulumi.Input['FeatureMembershipConfigmanagementArgs']]):
        pulumi.set(self, "configmanagement", value)

    @property
    @pulumi.getter
    def feature(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the feature
        """
        return pulumi.get(self, "feature")

    @feature.setter
    def feature(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "feature", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the feature
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def membership(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the membership
        """
        return pulumi.get(self, "membership")

    @membership.setter
    def membership(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "membership", value)

    @property
    @pulumi.getter(name="membershipLocation")
    def membership_location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the membership, for example, "us-central1". Default is "global".
        """
        return pulumi.get(self, "membership_location")

    @membership_location.setter
    def membership_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "membership_location", value)

    @property
    @pulumi.getter
    def mesh(self) -> Optional[pulumi.Input['FeatureMembershipMeshArgs']]:
        """
        Service mesh specific spec. Structure is documented below.
        """
        return pulumi.get(self, "mesh")

    @mesh.setter
    def mesh(self, value: Optional[pulumi.Input['FeatureMembershipMeshArgs']]):
        pulumi.set(self, "mesh", value)

    @property
    @pulumi.getter
    def policycontroller(self) -> Optional[pulumi.Input['FeatureMembershipPolicycontrollerArgs']]:
        """
        Policy Controller-specific spec. Structure is documented below.
        """
        return pulumi.get(self, "policycontroller")

    @policycontroller.setter
    def policycontroller(self, value: Optional[pulumi.Input['FeatureMembershipPolicycontrollerArgs']]):
        pulumi.set(self, "policycontroller", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project of the feature
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class FeatureMembership(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configmanagement: Optional[pulumi.Input[Union['FeatureMembershipConfigmanagementArgs', 'FeatureMembershipConfigmanagementArgsDict']]] = None,
                 feature: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 membership: Optional[pulumi.Input[str]] = None,
                 membership_location: Optional[pulumi.Input[str]] = None,
                 mesh: Optional[pulumi.Input[Union['FeatureMembershipMeshArgs', 'FeatureMembershipMeshArgsDict']]] = None,
                 policycontroller: Optional[pulumi.Input[Union['FeatureMembershipPolicycontrollerArgs', 'FeatureMembershipPolicycontrollerArgsDict']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Contains information about a GKEHub Feature Memberships. Feature Memberships configure GKEHub Features that apply to specific memberships rather than the project as a whole. The google_gke_hub is the Fleet API.

        ## Example Usage

        ### Config Management

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            name="my-cluster",
            location="us-central1-a",
            initial_node_count=1)
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint={
                "gke_cluster": {
                    "resource_link": cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                },
            })
        feature = gcp.gkehub.Feature("feature",
            name="configmanagement",
            location="global",
            labels={
                "foo": "bar",
            })
        feature_member = gcp.gkehub.FeatureMembership("feature_member",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            configmanagement={
                "version": "1.6.2",
                "config_sync": {
                    "git": {
                        "sync_repo": "https://github.com/hashicorp/terraform",
                    },
                },
            })
        ```
        ### Config Management With OCI

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            name="my-cluster",
            location="us-central1-a",
            initial_node_count=1)
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint={
                "gke_cluster": {
                    "resource_link": cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                },
            })
        feature = gcp.gkehub.Feature("feature",
            name="configmanagement",
            location="global",
            labels={
                "foo": "bar",
            })
        feature_member = gcp.gkehub.FeatureMembership("feature_member",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            configmanagement={
                "version": "1.15.1",
                "config_sync": {
                    "oci": {
                        "sync_repo": "us-central1-docker.pkg.dev/sample-project/config-repo/config-sync-gke:latest",
                        "policy_dir": "config-connector",
                        "sync_wait_secs": "20",
                        "secret_type": "gcpserviceaccount",
                        "gcp_service_account_email": "sa@project-id.iam.gserviceaccount.com",
                    },
                },
            })
        ```

        ### Multi Cluster Service Discovery

        ```python
        import pulumi
        import pulumi_gcp as gcp

        feature = gcp.gkehub.Feature("feature",
            name="multiclusterservicediscovery",
            location="global",
            labels={
                "foo": "bar",
            })
        ```

        ### Service Mesh

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            name="my-cluster",
            location="us-central1-a",
            initial_node_count=1)
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint={
                "gke_cluster": {
                    "resource_link": cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                },
            })
        feature = gcp.gkehub.Feature("feature",
            name="servicemesh",
            location="global")
        feature_member = gcp.gkehub.FeatureMembership("feature_member",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            mesh={
                "management": "MANAGEMENT_AUTOMATIC",
            })
        ```

        ### Config Management With Regional Membership

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            name="my-cluster",
            location="us-central1-a",
            initial_node_count=1)
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            location="us-central1",
            endpoint={
                "gke_cluster": {
                    "resource_link": cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                },
            })
        feature = gcp.gkehub.Feature("feature",
            name="configmanagement",
            location="global",
            labels={
                "foo": "bar",
            })
        feature_member = gcp.gkehub.FeatureMembership("feature_member",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            membership_location=membership.location,
            configmanagement={
                "version": "1.6.2",
                "config_sync": {
                    "git": {
                        "sync_repo": "https://github.com/hashicorp/terraform",
                    },
                },
            })
        ```

        ### Policy Controller With Minimal Configuration

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            name="my-cluster",
            location="us-central1-a",
            initial_node_count=1)
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint={
                "gke_cluster": {
                    "resource_link": cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                },
            })
        feature = gcp.gkehub.Feature("feature",
            name="policycontroller",
            location="global")
        feature_member = gcp.gkehub.FeatureMembership("feature_member",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            policycontroller={
                "policy_controller_hub_config": {
                    "install_spec": "INSTALL_SPEC_ENABLED",
                },
            })
        ```

        ### Policy Controller With Custom Configurations

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            name="my-cluster",
            location="us-central1-a",
            initial_node_count=1)
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint={
                "gke_cluster": {
                    "resource_link": cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                },
            })
        feature = gcp.gkehub.Feature("feature",
            name="policycontroller",
            location="global")
        feature_member = gcp.gkehub.FeatureMembership("feature_member",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            policycontroller={
                "policy_controller_hub_config": {
                    "install_spec": "INSTALL_SPEC_SUSPENDED",
                    "policy_content": {
                        "template_library": {
                            "installation": "NOT_INSTALLED",
                        },
                    },
                    "constraint_violation_limit": 50,
                    "audit_interval_seconds": 120,
                    "referential_rules_enabled": True,
                    "log_denies_enabled": True,
                    "mutation_enabled": True,
                },
                "version": "1.17.0",
            })
        ```

        ## Import

        FeatureMembership can be imported using any of these accepted formats:

        * `projects/{{project}}/locations/{{location}}/features/{{feature}}/membershipId/{{membership}}`

        * `{{project}}/{{location}}/{{feature}}/{{membership}}`

        * `{{location}}/{{feature}}/{{membership}}`

        When using the `pulumi import` command, FeatureMembership can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:gkehub/featureMembership:FeatureMembership default projects/{{project}}/locations/{{location}}/features/{{feature}}/membershipId/{{membership}}
        ```

        ```sh
        $ pulumi import gcp:gkehub/featureMembership:FeatureMembership default {{project}}/{{location}}/{{feature}}/{{membership}}
        ```

        ```sh
        $ pulumi import gcp:gkehub/featureMembership:FeatureMembership default {{location}}/{{feature}}/{{membership}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['FeatureMembershipConfigmanagementArgs', 'FeatureMembershipConfigmanagementArgsDict']] configmanagement: Config Management-specific spec. Structure is documented below.
        :param pulumi.Input[str] feature: The name of the feature
        :param pulumi.Input[str] location: The location of the feature
        :param pulumi.Input[str] membership: The name of the membership
        :param pulumi.Input[str] membership_location: The location of the membership, for example, "us-central1". Default is "global".
        :param pulumi.Input[Union['FeatureMembershipMeshArgs', 'FeatureMembershipMeshArgsDict']] mesh: Service mesh specific spec. Structure is documented below.
        :param pulumi.Input[Union['FeatureMembershipPolicycontrollerArgs', 'FeatureMembershipPolicycontrollerArgsDict']] policycontroller: Policy Controller-specific spec. Structure is documented below.
        :param pulumi.Input[str] project: The project of the feature
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FeatureMembershipArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Contains information about a GKEHub Feature Memberships. Feature Memberships configure GKEHub Features that apply to specific memberships rather than the project as a whole. The google_gke_hub is the Fleet API.

        ## Example Usage

        ### Config Management

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            name="my-cluster",
            location="us-central1-a",
            initial_node_count=1)
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint={
                "gke_cluster": {
                    "resource_link": cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                },
            })
        feature = gcp.gkehub.Feature("feature",
            name="configmanagement",
            location="global",
            labels={
                "foo": "bar",
            })
        feature_member = gcp.gkehub.FeatureMembership("feature_member",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            configmanagement={
                "version": "1.6.2",
                "config_sync": {
                    "git": {
                        "sync_repo": "https://github.com/hashicorp/terraform",
                    },
                },
            })
        ```
        ### Config Management With OCI

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            name="my-cluster",
            location="us-central1-a",
            initial_node_count=1)
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint={
                "gke_cluster": {
                    "resource_link": cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                },
            })
        feature = gcp.gkehub.Feature("feature",
            name="configmanagement",
            location="global",
            labels={
                "foo": "bar",
            })
        feature_member = gcp.gkehub.FeatureMembership("feature_member",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            configmanagement={
                "version": "1.15.1",
                "config_sync": {
                    "oci": {
                        "sync_repo": "us-central1-docker.pkg.dev/sample-project/config-repo/config-sync-gke:latest",
                        "policy_dir": "config-connector",
                        "sync_wait_secs": "20",
                        "secret_type": "gcpserviceaccount",
                        "gcp_service_account_email": "sa@project-id.iam.gserviceaccount.com",
                    },
                },
            })
        ```

        ### Multi Cluster Service Discovery

        ```python
        import pulumi
        import pulumi_gcp as gcp

        feature = gcp.gkehub.Feature("feature",
            name="multiclusterservicediscovery",
            location="global",
            labels={
                "foo": "bar",
            })
        ```

        ### Service Mesh

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            name="my-cluster",
            location="us-central1-a",
            initial_node_count=1)
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint={
                "gke_cluster": {
                    "resource_link": cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                },
            })
        feature = gcp.gkehub.Feature("feature",
            name="servicemesh",
            location="global")
        feature_member = gcp.gkehub.FeatureMembership("feature_member",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            mesh={
                "management": "MANAGEMENT_AUTOMATIC",
            })
        ```

        ### Config Management With Regional Membership

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            name="my-cluster",
            location="us-central1-a",
            initial_node_count=1)
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            location="us-central1",
            endpoint={
                "gke_cluster": {
                    "resource_link": cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                },
            })
        feature = gcp.gkehub.Feature("feature",
            name="configmanagement",
            location="global",
            labels={
                "foo": "bar",
            })
        feature_member = gcp.gkehub.FeatureMembership("feature_member",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            membership_location=membership.location,
            configmanagement={
                "version": "1.6.2",
                "config_sync": {
                    "git": {
                        "sync_repo": "https://github.com/hashicorp/terraform",
                    },
                },
            })
        ```

        ### Policy Controller With Minimal Configuration

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            name="my-cluster",
            location="us-central1-a",
            initial_node_count=1)
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint={
                "gke_cluster": {
                    "resource_link": cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                },
            })
        feature = gcp.gkehub.Feature("feature",
            name="policycontroller",
            location="global")
        feature_member = gcp.gkehub.FeatureMembership("feature_member",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            policycontroller={
                "policy_controller_hub_config": {
                    "install_spec": "INSTALL_SPEC_ENABLED",
                },
            })
        ```

        ### Policy Controller With Custom Configurations

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            name="my-cluster",
            location="us-central1-a",
            initial_node_count=1)
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint={
                "gke_cluster": {
                    "resource_link": cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                },
            })
        feature = gcp.gkehub.Feature("feature",
            name="policycontroller",
            location="global")
        feature_member = gcp.gkehub.FeatureMembership("feature_member",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            policycontroller={
                "policy_controller_hub_config": {
                    "install_spec": "INSTALL_SPEC_SUSPENDED",
                    "policy_content": {
                        "template_library": {
                            "installation": "NOT_INSTALLED",
                        },
                    },
                    "constraint_violation_limit": 50,
                    "audit_interval_seconds": 120,
                    "referential_rules_enabled": True,
                    "log_denies_enabled": True,
                    "mutation_enabled": True,
                },
                "version": "1.17.0",
            })
        ```

        ## Import

        FeatureMembership can be imported using any of these accepted formats:

        * `projects/{{project}}/locations/{{location}}/features/{{feature}}/membershipId/{{membership}}`

        * `{{project}}/{{location}}/{{feature}}/{{membership}}`

        * `{{location}}/{{feature}}/{{membership}}`

        When using the `pulumi import` command, FeatureMembership can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:gkehub/featureMembership:FeatureMembership default projects/{{project}}/locations/{{location}}/features/{{feature}}/membershipId/{{membership}}
        ```

        ```sh
        $ pulumi import gcp:gkehub/featureMembership:FeatureMembership default {{project}}/{{location}}/{{feature}}/{{membership}}
        ```

        ```sh
        $ pulumi import gcp:gkehub/featureMembership:FeatureMembership default {{location}}/{{feature}}/{{membership}}
        ```

        :param str resource_name: The name of the resource.
        :param FeatureMembershipArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FeatureMembershipArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configmanagement: Optional[pulumi.Input[Union['FeatureMembershipConfigmanagementArgs', 'FeatureMembershipConfigmanagementArgsDict']]] = None,
                 feature: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 membership: Optional[pulumi.Input[str]] = None,
                 membership_location: Optional[pulumi.Input[str]] = None,
                 mesh: Optional[pulumi.Input[Union['FeatureMembershipMeshArgs', 'FeatureMembershipMeshArgsDict']]] = None,
                 policycontroller: Optional[pulumi.Input[Union['FeatureMembershipPolicycontrollerArgs', 'FeatureMembershipPolicycontrollerArgsDict']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FeatureMembershipArgs.__new__(FeatureMembershipArgs)

            __props__.__dict__["configmanagement"] = configmanagement
            if feature is None and not opts.urn:
                raise TypeError("Missing required property 'feature'")
            __props__.__dict__["feature"] = feature
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            if membership is None and not opts.urn:
                raise TypeError("Missing required property 'membership'")
            __props__.__dict__["membership"] = membership
            __props__.__dict__["membership_location"] = membership_location
            __props__.__dict__["mesh"] = mesh
            __props__.__dict__["policycontroller"] = policycontroller
            __props__.__dict__["project"] = project
        super(FeatureMembership, __self__).__init__(
            'gcp:gkehub/featureMembership:FeatureMembership',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            configmanagement: Optional[pulumi.Input[Union['FeatureMembershipConfigmanagementArgs', 'FeatureMembershipConfigmanagementArgsDict']]] = None,
            feature: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            membership: Optional[pulumi.Input[str]] = None,
            membership_location: Optional[pulumi.Input[str]] = None,
            mesh: Optional[pulumi.Input[Union['FeatureMembershipMeshArgs', 'FeatureMembershipMeshArgsDict']]] = None,
            policycontroller: Optional[pulumi.Input[Union['FeatureMembershipPolicycontrollerArgs', 'FeatureMembershipPolicycontrollerArgsDict']]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'FeatureMembership':
        """
        Get an existing FeatureMembership resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['FeatureMembershipConfigmanagementArgs', 'FeatureMembershipConfigmanagementArgsDict']] configmanagement: Config Management-specific spec. Structure is documented below.
        :param pulumi.Input[str] feature: The name of the feature
        :param pulumi.Input[str] location: The location of the feature
        :param pulumi.Input[str] membership: The name of the membership
        :param pulumi.Input[str] membership_location: The location of the membership, for example, "us-central1". Default is "global".
        :param pulumi.Input[Union['FeatureMembershipMeshArgs', 'FeatureMembershipMeshArgsDict']] mesh: Service mesh specific spec. Structure is documented below.
        :param pulumi.Input[Union['FeatureMembershipPolicycontrollerArgs', 'FeatureMembershipPolicycontrollerArgsDict']] policycontroller: Policy Controller-specific spec. Structure is documented below.
        :param pulumi.Input[str] project: The project of the feature
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FeatureMembershipState.__new__(_FeatureMembershipState)

        __props__.__dict__["configmanagement"] = configmanagement
        __props__.__dict__["feature"] = feature
        __props__.__dict__["location"] = location
        __props__.__dict__["membership"] = membership
        __props__.__dict__["membership_location"] = membership_location
        __props__.__dict__["mesh"] = mesh
        __props__.__dict__["policycontroller"] = policycontroller
        __props__.__dict__["project"] = project
        return FeatureMembership(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def configmanagement(self) -> pulumi.Output[Optional['outputs.FeatureMembershipConfigmanagement']]:
        """
        Config Management-specific spec. Structure is documented below.
        """
        return pulumi.get(self, "configmanagement")

    @property
    @pulumi.getter
    def feature(self) -> pulumi.Output[str]:
        """
        The name of the feature
        """
        return pulumi.get(self, "feature")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the feature
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def membership(self) -> pulumi.Output[str]:
        """
        The name of the membership
        """
        return pulumi.get(self, "membership")

    @property
    @pulumi.getter(name="membershipLocation")
    def membership_location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the membership, for example, "us-central1". Default is "global".
        """
        return pulumi.get(self, "membership_location")

    @property
    @pulumi.getter
    def mesh(self) -> pulumi.Output[Optional['outputs.FeatureMembershipMesh']]:
        """
        Service mesh specific spec. Structure is documented below.
        """
        return pulumi.get(self, "mesh")

    @property
    @pulumi.getter
    def policycontroller(self) -> pulumi.Output[Optional['outputs.FeatureMembershipPolicycontroller']]:
        """
        Policy Controller-specific spec. Structure is documented below.
        """
        return pulumi.get(self, "policycontroller")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The project of the feature
        """
        return pulumi.get(self, "project")

