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

__all__ = ['RepositoryWorkflowConfigArgs', 'RepositoryWorkflowConfig']

@pulumi.input_type
class RepositoryWorkflowConfigArgs:
    def __init__(__self__, *,
                 release_config: pulumi.Input[str],
                 cron_schedule: Optional[pulumi.Input[str]] = None,
                 invocation_config: Optional[pulumi.Input['RepositoryWorkflowConfigInvocationConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RepositoryWorkflowConfig resource.
        :param pulumi.Input[str] release_config: The name of the release config whose releaseCompilationResult should be executed. Must be in the format projects/*/locations/*/repositories/*/releaseConfigs/*.
               
               
               - - -
        :param pulumi.Input[str] cron_schedule: Optional. Optional schedule (in cron format) for automatic creation of compilation results.
        :param pulumi.Input['RepositoryWorkflowConfigInvocationConfigArgs'] invocation_config: Optional. If left unset, a default InvocationConfig will be used.
               Structure is documented below.
        :param pulumi.Input[str] name: The workflow's name.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: A reference to the region
        :param pulumi.Input[str] repository: A reference to the Dataform repository
        :param pulumi.Input[str] time_zone: Optional. Specifies the time zone to be used when interpreting cronSchedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC.
        """
        pulumi.set(__self__, "release_config", release_config)
        if cron_schedule is not None:
            pulumi.set(__self__, "cron_schedule", cron_schedule)
        if invocation_config is not None:
            pulumi.set(__self__, "invocation_config", invocation_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if repository is not None:
            pulumi.set(__self__, "repository", repository)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter(name="releaseConfig")
    def release_config(self) -> pulumi.Input[str]:
        """
        The name of the release config whose releaseCompilationResult should be executed. Must be in the format projects/*/locations/*/repositories/*/releaseConfigs/*.


        - - -
        """
        return pulumi.get(self, "release_config")

    @release_config.setter
    def release_config(self, value: pulumi.Input[str]):
        pulumi.set(self, "release_config", value)

    @property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Optional schedule (in cron format) for automatic creation of compilation results.
        """
        return pulumi.get(self, "cron_schedule")

    @cron_schedule.setter
    def cron_schedule(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cron_schedule", value)

    @property
    @pulumi.getter(name="invocationConfig")
    def invocation_config(self) -> Optional[pulumi.Input['RepositoryWorkflowConfigInvocationConfigArgs']]:
        """
        Optional. If left unset, a default InvocationConfig will be used.
        Structure is documented below.
        """
        return pulumi.get(self, "invocation_config")

    @invocation_config.setter
    def invocation_config(self, value: Optional[pulumi.Input['RepositoryWorkflowConfigInvocationConfigArgs']]):
        pulumi.set(self, "invocation_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The workflow's name.
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
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        A reference to the region
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[str]]:
        """
        A reference to the Dataform repository
        """
        return pulumi.get(self, "repository")

    @repository.setter
    def repository(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Specifies the time zone to be used when interpreting cronSchedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC.
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone", value)


@pulumi.input_type
class _RepositoryWorkflowConfigState:
    def __init__(__self__, *,
                 cron_schedule: Optional[pulumi.Input[str]] = None,
                 invocation_config: Optional[pulumi.Input['RepositoryWorkflowConfigInvocationConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 recent_scheduled_execution_records: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryWorkflowConfigRecentScheduledExecutionRecordArgs']]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 release_config: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RepositoryWorkflowConfig resources.
        :param pulumi.Input[str] cron_schedule: Optional. Optional schedule (in cron format) for automatic creation of compilation results.
        :param pulumi.Input['RepositoryWorkflowConfigInvocationConfigArgs'] invocation_config: Optional. If left unset, a default InvocationConfig will be used.
               Structure is documented below.
        :param pulumi.Input[str] name: The workflow's name.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[Sequence[pulumi.Input['RepositoryWorkflowConfigRecentScheduledExecutionRecordArgs']]] recent_scheduled_execution_records: Records of the 10 most recent scheduled execution attempts, ordered in in descending order of executionTime. Updated whenever automatic creation of a workflow invocation is triggered by cronSchedule.
               Structure is documented below.
        :param pulumi.Input[str] region: A reference to the region
        :param pulumi.Input[str] release_config: The name of the release config whose releaseCompilationResult should be executed. Must be in the format projects/*/locations/*/repositories/*/releaseConfigs/*.
               
               
               - - -
        :param pulumi.Input[str] repository: A reference to the Dataform repository
        :param pulumi.Input[str] time_zone: Optional. Specifies the time zone to be used when interpreting cronSchedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC.
        """
        if cron_schedule is not None:
            pulumi.set(__self__, "cron_schedule", cron_schedule)
        if invocation_config is not None:
            pulumi.set(__self__, "invocation_config", invocation_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if recent_scheduled_execution_records is not None:
            pulumi.set(__self__, "recent_scheduled_execution_records", recent_scheduled_execution_records)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if release_config is not None:
            pulumi.set(__self__, "release_config", release_config)
        if repository is not None:
            pulumi.set(__self__, "repository", repository)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Optional schedule (in cron format) for automatic creation of compilation results.
        """
        return pulumi.get(self, "cron_schedule")

    @cron_schedule.setter
    def cron_schedule(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cron_schedule", value)

    @property
    @pulumi.getter(name="invocationConfig")
    def invocation_config(self) -> Optional[pulumi.Input['RepositoryWorkflowConfigInvocationConfigArgs']]:
        """
        Optional. If left unset, a default InvocationConfig will be used.
        Structure is documented below.
        """
        return pulumi.get(self, "invocation_config")

    @invocation_config.setter
    def invocation_config(self, value: Optional[pulumi.Input['RepositoryWorkflowConfigInvocationConfigArgs']]):
        pulumi.set(self, "invocation_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The workflow's name.
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
    @pulumi.getter(name="recentScheduledExecutionRecords")
    def recent_scheduled_execution_records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryWorkflowConfigRecentScheduledExecutionRecordArgs']]]]:
        """
        Records of the 10 most recent scheduled execution attempts, ordered in in descending order of executionTime. Updated whenever automatic creation of a workflow invocation is triggered by cronSchedule.
        Structure is documented below.
        """
        return pulumi.get(self, "recent_scheduled_execution_records")

    @recent_scheduled_execution_records.setter
    def recent_scheduled_execution_records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryWorkflowConfigRecentScheduledExecutionRecordArgs']]]]):
        pulumi.set(self, "recent_scheduled_execution_records", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        A reference to the region
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="releaseConfig")
    def release_config(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the release config whose releaseCompilationResult should be executed. Must be in the format projects/*/locations/*/repositories/*/releaseConfigs/*.


        - - -
        """
        return pulumi.get(self, "release_config")

    @release_config.setter
    def release_config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "release_config", value)

    @property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[str]]:
        """
        A reference to the Dataform repository
        """
        return pulumi.get(self, "repository")

    @repository.setter
    def repository(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Specifies the time zone to be used when interpreting cronSchedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC.
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone", value)


class RepositoryWorkflowConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cron_schedule: Optional[pulumi.Input[str]] = None,
                 invocation_config: Optional[pulumi.Input[Union['RepositoryWorkflowConfigInvocationConfigArgs', 'RepositoryWorkflowConfigInvocationConfigArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 release_config: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ### Dataform Repository Workflow Config

        ```python
        import pulumi
        import pulumi_gcp as gcp

        git_repository = gcp.sourcerepo.Repository("git_repository", name="my/repository")
        secret = gcp.secretmanager.Secret("secret",
            secret_id="my_secret",
            replication={
                "auto": {},
            })
        secret_version = gcp.secretmanager.SecretVersion("secret_version",
            secret=secret.id,
            secret_data="secret-data")
        repository = gcp.dataform.Repository("repository",
            name="dataform_repository",
            region="us-central1",
            git_remote_settings={
                "url": git_repository.url,
                "default_branch": "main",
                "authentication_token_secret_version": secret_version.id,
            },
            workspace_compilation_overrides={
                "default_database": "database",
                "schema_suffix": "_suffix",
                "table_prefix": "prefix_",
            })
        release_config = gcp.dataform.RepositoryReleaseConfig("release_config",
            project=repository.project,
            region=repository.region,
            repository=repository.name,
            name="my_release",
            git_commitish="main",
            cron_schedule="0 7 * * *",
            time_zone="America/New_York",
            code_compilation_config={
                "default_database": "gcp-example-project",
                "default_schema": "example-dataset",
                "default_location": "us-central1",
                "assertion_schema": "example-assertion-dataset",
                "database_suffix": "",
                "schema_suffix": "",
                "table_prefix": "",
                "vars": {
                    "var1": "value",
                },
            })
        dataform_sa = gcp.serviceaccount.Account("dataform_sa",
            account_id="dataform-sa",
            display_name="Dataform Service Account")
        workflow = gcp.dataform.RepositoryWorkflowConfig("workflow",
            project=repository.project,
            region=repository.region,
            repository=repository.name,
            name="my_workflow",
            release_config=release_config.id,
            invocation_config={
                "included_targets": [
                    {
                        "database": "gcp-example-project",
                        "schema": "example-dataset",
                        "name": "target_1",
                    },
                    {
                        "database": "gcp-example-project",
                        "schema": "example-dataset",
                        "name": "target_2",
                    },
                ],
                "included_tags": ["tag_1"],
                "transitive_dependencies_included": True,
                "transitive_dependents_included": True,
                "fully_refresh_incremental_tables_enabled": False,
                "service_account": dataform_sa.email,
            },
            cron_schedule="0 7 * * *",
            time_zone="America/New_York")
        ```

        ## Import

        RepositoryWorkflowConfig can be imported using any of these accepted formats:

        * `projects/{{project}}/locations/{{region}}/repositories/{{repository}}/workflowConfigs/{{name}}`

        * `{{project}}/{{region}}/{{repository}}/{{name}}`

        * `{{region}}/{{repository}}/{{name}}`

        * `{{repository}}/{{name}}`

        When using the `pulumi import` command, RepositoryWorkflowConfig can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:dataform/repositoryWorkflowConfig:RepositoryWorkflowConfig default projects/{{project}}/locations/{{region}}/repositories/{{repository}}/workflowConfigs/{{name}}
        ```

        ```sh
        $ pulumi import gcp:dataform/repositoryWorkflowConfig:RepositoryWorkflowConfig default {{project}}/{{region}}/{{repository}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:dataform/repositoryWorkflowConfig:RepositoryWorkflowConfig default {{region}}/{{repository}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:dataform/repositoryWorkflowConfig:RepositoryWorkflowConfig default {{repository}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cron_schedule: Optional. Optional schedule (in cron format) for automatic creation of compilation results.
        :param pulumi.Input[Union['RepositoryWorkflowConfigInvocationConfigArgs', 'RepositoryWorkflowConfigInvocationConfigArgsDict']] invocation_config: Optional. If left unset, a default InvocationConfig will be used.
               Structure is documented below.
        :param pulumi.Input[str] name: The workflow's name.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: A reference to the region
        :param pulumi.Input[str] release_config: The name of the release config whose releaseCompilationResult should be executed. Must be in the format projects/*/locations/*/repositories/*/releaseConfigs/*.
               
               
               - - -
        :param pulumi.Input[str] repository: A reference to the Dataform repository
        :param pulumi.Input[str] time_zone: Optional. Specifies the time zone to be used when interpreting cronSchedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RepositoryWorkflowConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ### Dataform Repository Workflow Config

        ```python
        import pulumi
        import pulumi_gcp as gcp

        git_repository = gcp.sourcerepo.Repository("git_repository", name="my/repository")
        secret = gcp.secretmanager.Secret("secret",
            secret_id="my_secret",
            replication={
                "auto": {},
            })
        secret_version = gcp.secretmanager.SecretVersion("secret_version",
            secret=secret.id,
            secret_data="secret-data")
        repository = gcp.dataform.Repository("repository",
            name="dataform_repository",
            region="us-central1",
            git_remote_settings={
                "url": git_repository.url,
                "default_branch": "main",
                "authentication_token_secret_version": secret_version.id,
            },
            workspace_compilation_overrides={
                "default_database": "database",
                "schema_suffix": "_suffix",
                "table_prefix": "prefix_",
            })
        release_config = gcp.dataform.RepositoryReleaseConfig("release_config",
            project=repository.project,
            region=repository.region,
            repository=repository.name,
            name="my_release",
            git_commitish="main",
            cron_schedule="0 7 * * *",
            time_zone="America/New_York",
            code_compilation_config={
                "default_database": "gcp-example-project",
                "default_schema": "example-dataset",
                "default_location": "us-central1",
                "assertion_schema": "example-assertion-dataset",
                "database_suffix": "",
                "schema_suffix": "",
                "table_prefix": "",
                "vars": {
                    "var1": "value",
                },
            })
        dataform_sa = gcp.serviceaccount.Account("dataform_sa",
            account_id="dataform-sa",
            display_name="Dataform Service Account")
        workflow = gcp.dataform.RepositoryWorkflowConfig("workflow",
            project=repository.project,
            region=repository.region,
            repository=repository.name,
            name="my_workflow",
            release_config=release_config.id,
            invocation_config={
                "included_targets": [
                    {
                        "database": "gcp-example-project",
                        "schema": "example-dataset",
                        "name": "target_1",
                    },
                    {
                        "database": "gcp-example-project",
                        "schema": "example-dataset",
                        "name": "target_2",
                    },
                ],
                "included_tags": ["tag_1"],
                "transitive_dependencies_included": True,
                "transitive_dependents_included": True,
                "fully_refresh_incremental_tables_enabled": False,
                "service_account": dataform_sa.email,
            },
            cron_schedule="0 7 * * *",
            time_zone="America/New_York")
        ```

        ## Import

        RepositoryWorkflowConfig can be imported using any of these accepted formats:

        * `projects/{{project}}/locations/{{region}}/repositories/{{repository}}/workflowConfigs/{{name}}`

        * `{{project}}/{{region}}/{{repository}}/{{name}}`

        * `{{region}}/{{repository}}/{{name}}`

        * `{{repository}}/{{name}}`

        When using the `pulumi import` command, RepositoryWorkflowConfig can be imported using one of the formats above. For example:

        ```sh
        $ pulumi import gcp:dataform/repositoryWorkflowConfig:RepositoryWorkflowConfig default projects/{{project}}/locations/{{region}}/repositories/{{repository}}/workflowConfigs/{{name}}
        ```

        ```sh
        $ pulumi import gcp:dataform/repositoryWorkflowConfig:RepositoryWorkflowConfig default {{project}}/{{region}}/{{repository}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:dataform/repositoryWorkflowConfig:RepositoryWorkflowConfig default {{region}}/{{repository}}/{{name}}
        ```

        ```sh
        $ pulumi import gcp:dataform/repositoryWorkflowConfig:RepositoryWorkflowConfig default {{repository}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param RepositoryWorkflowConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RepositoryWorkflowConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cron_schedule: Optional[pulumi.Input[str]] = None,
                 invocation_config: Optional[pulumi.Input[Union['RepositoryWorkflowConfigInvocationConfigArgs', 'RepositoryWorkflowConfigInvocationConfigArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 release_config: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RepositoryWorkflowConfigArgs.__new__(RepositoryWorkflowConfigArgs)

            __props__.__dict__["cron_schedule"] = cron_schedule
            __props__.__dict__["invocation_config"] = invocation_config
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["region"] = region
            if release_config is None and not opts.urn:
                raise TypeError("Missing required property 'release_config'")
            __props__.__dict__["release_config"] = release_config
            __props__.__dict__["repository"] = repository
            __props__.__dict__["time_zone"] = time_zone
            __props__.__dict__["recent_scheduled_execution_records"] = None
        super(RepositoryWorkflowConfig, __self__).__init__(
            'gcp:dataform/repositoryWorkflowConfig:RepositoryWorkflowConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cron_schedule: Optional[pulumi.Input[str]] = None,
            invocation_config: Optional[pulumi.Input[Union['RepositoryWorkflowConfigInvocationConfigArgs', 'RepositoryWorkflowConfigInvocationConfigArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            recent_scheduled_execution_records: Optional[pulumi.Input[Sequence[pulumi.Input[Union['RepositoryWorkflowConfigRecentScheduledExecutionRecordArgs', 'RepositoryWorkflowConfigRecentScheduledExecutionRecordArgsDict']]]]] = None,
            region: Optional[pulumi.Input[str]] = None,
            release_config: Optional[pulumi.Input[str]] = None,
            repository: Optional[pulumi.Input[str]] = None,
            time_zone: Optional[pulumi.Input[str]] = None) -> 'RepositoryWorkflowConfig':
        """
        Get an existing RepositoryWorkflowConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cron_schedule: Optional. Optional schedule (in cron format) for automatic creation of compilation results.
        :param pulumi.Input[Union['RepositoryWorkflowConfigInvocationConfigArgs', 'RepositoryWorkflowConfigInvocationConfigArgsDict']] invocation_config: Optional. If left unset, a default InvocationConfig will be used.
               Structure is documented below.
        :param pulumi.Input[str] name: The workflow's name.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[Sequence[pulumi.Input[Union['RepositoryWorkflowConfigRecentScheduledExecutionRecordArgs', 'RepositoryWorkflowConfigRecentScheduledExecutionRecordArgsDict']]]] recent_scheduled_execution_records: Records of the 10 most recent scheduled execution attempts, ordered in in descending order of executionTime. Updated whenever automatic creation of a workflow invocation is triggered by cronSchedule.
               Structure is documented below.
        :param pulumi.Input[str] region: A reference to the region
        :param pulumi.Input[str] release_config: The name of the release config whose releaseCompilationResult should be executed. Must be in the format projects/*/locations/*/repositories/*/releaseConfigs/*.
               
               
               - - -
        :param pulumi.Input[str] repository: A reference to the Dataform repository
        :param pulumi.Input[str] time_zone: Optional. Specifies the time zone to be used when interpreting cronSchedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RepositoryWorkflowConfigState.__new__(_RepositoryWorkflowConfigState)

        __props__.__dict__["cron_schedule"] = cron_schedule
        __props__.__dict__["invocation_config"] = invocation_config
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["recent_scheduled_execution_records"] = recent_scheduled_execution_records
        __props__.__dict__["region"] = region
        __props__.__dict__["release_config"] = release_config
        __props__.__dict__["repository"] = repository
        __props__.__dict__["time_zone"] = time_zone
        return RepositoryWorkflowConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> pulumi.Output[Optional[str]]:
        """
        Optional. Optional schedule (in cron format) for automatic creation of compilation results.
        """
        return pulumi.get(self, "cron_schedule")

    @property
    @pulumi.getter(name="invocationConfig")
    def invocation_config(self) -> pulumi.Output[Optional['outputs.RepositoryWorkflowConfigInvocationConfig']]:
        """
        Optional. If left unset, a default InvocationConfig will be used.
        Structure is documented below.
        """
        return pulumi.get(self, "invocation_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The workflow's name.
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
    @pulumi.getter(name="recentScheduledExecutionRecords")
    def recent_scheduled_execution_records(self) -> pulumi.Output[Sequence['outputs.RepositoryWorkflowConfigRecentScheduledExecutionRecord']]:
        """
        Records of the 10 most recent scheduled execution attempts, ordered in in descending order of executionTime. Updated whenever automatic creation of a workflow invocation is triggered by cronSchedule.
        Structure is documented below.
        """
        return pulumi.get(self, "recent_scheduled_execution_records")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        A reference to the region
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="releaseConfig")
    def release_config(self) -> pulumi.Output[str]:
        """
        The name of the release config whose releaseCompilationResult should be executed. Must be in the format projects/*/locations/*/repositories/*/releaseConfigs/*.


        - - -
        """
        return pulumi.get(self, "release_config")

    @property
    @pulumi.getter
    def repository(self) -> pulumi.Output[Optional[str]]:
        """
        A reference to the Dataform repository
        """
        return pulumi.get(self, "repository")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[Optional[str]]:
        """
        Optional. Specifies the time zone to be used when interpreting cronSchedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC.
        """
        return pulumi.get(self, "time_zone")

