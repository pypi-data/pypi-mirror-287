# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetAdvancedClusterResult',
    'AwaitableGetAdvancedClusterResult',
    'get_advanced_cluster',
    'get_advanced_cluster_output',
]

@pulumi.output_type
class GetAdvancedClusterResult:
    """
    A collection of values returned by getAdvancedCluster.
    """
    def __init__(__self__, advanced_configurations=None, backup_enabled=None, bi_connector_configs=None, cluster_type=None, connection_strings=None, create_date=None, disk_size_gb=None, encryption_at_rest_provider=None, global_cluster_self_managed_sharding=None, id=None, labels=None, mongo_db_major_version=None, mongo_db_version=None, name=None, paused=None, pit_enabled=None, project_id=None, replication_specs=None, root_cert_type=None, state_name=None, tags=None, termination_protection_enabled=None, version_release_system=None):
        if advanced_configurations and not isinstance(advanced_configurations, list):
            raise TypeError("Expected argument 'advanced_configurations' to be a list")
        pulumi.set(__self__, "advanced_configurations", advanced_configurations)
        if backup_enabled and not isinstance(backup_enabled, bool):
            raise TypeError("Expected argument 'backup_enabled' to be a bool")
        pulumi.set(__self__, "backup_enabled", backup_enabled)
        if bi_connector_configs and not isinstance(bi_connector_configs, list):
            raise TypeError("Expected argument 'bi_connector_configs' to be a list")
        pulumi.set(__self__, "bi_connector_configs", bi_connector_configs)
        if cluster_type and not isinstance(cluster_type, str):
            raise TypeError("Expected argument 'cluster_type' to be a str")
        pulumi.set(__self__, "cluster_type", cluster_type)
        if connection_strings and not isinstance(connection_strings, list):
            raise TypeError("Expected argument 'connection_strings' to be a list")
        pulumi.set(__self__, "connection_strings", connection_strings)
        if create_date and not isinstance(create_date, str):
            raise TypeError("Expected argument 'create_date' to be a str")
        pulumi.set(__self__, "create_date", create_date)
        if disk_size_gb and not isinstance(disk_size_gb, float):
            raise TypeError("Expected argument 'disk_size_gb' to be a float")
        pulumi.set(__self__, "disk_size_gb", disk_size_gb)
        if encryption_at_rest_provider and not isinstance(encryption_at_rest_provider, str):
            raise TypeError("Expected argument 'encryption_at_rest_provider' to be a str")
        pulumi.set(__self__, "encryption_at_rest_provider", encryption_at_rest_provider)
        if global_cluster_self_managed_sharding and not isinstance(global_cluster_self_managed_sharding, bool):
            raise TypeError("Expected argument 'global_cluster_self_managed_sharding' to be a bool")
        pulumi.set(__self__, "global_cluster_self_managed_sharding", global_cluster_self_managed_sharding)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, list):
            raise TypeError("Expected argument 'labels' to be a list")
        pulumi.set(__self__, "labels", labels)
        if mongo_db_major_version and not isinstance(mongo_db_major_version, str):
            raise TypeError("Expected argument 'mongo_db_major_version' to be a str")
        pulumi.set(__self__, "mongo_db_major_version", mongo_db_major_version)
        if mongo_db_version and not isinstance(mongo_db_version, str):
            raise TypeError("Expected argument 'mongo_db_version' to be a str")
        pulumi.set(__self__, "mongo_db_version", mongo_db_version)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if paused and not isinstance(paused, bool):
            raise TypeError("Expected argument 'paused' to be a bool")
        pulumi.set(__self__, "paused", paused)
        if pit_enabled and not isinstance(pit_enabled, bool):
            raise TypeError("Expected argument 'pit_enabled' to be a bool")
        pulumi.set(__self__, "pit_enabled", pit_enabled)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if replication_specs and not isinstance(replication_specs, list):
            raise TypeError("Expected argument 'replication_specs' to be a list")
        pulumi.set(__self__, "replication_specs", replication_specs)
        if root_cert_type and not isinstance(root_cert_type, str):
            raise TypeError("Expected argument 'root_cert_type' to be a str")
        pulumi.set(__self__, "root_cert_type", root_cert_type)
        if state_name and not isinstance(state_name, str):
            raise TypeError("Expected argument 'state_name' to be a str")
        pulumi.set(__self__, "state_name", state_name)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if termination_protection_enabled and not isinstance(termination_protection_enabled, bool):
            raise TypeError("Expected argument 'termination_protection_enabled' to be a bool")
        pulumi.set(__self__, "termination_protection_enabled", termination_protection_enabled)
        if version_release_system and not isinstance(version_release_system, str):
            raise TypeError("Expected argument 'version_release_system' to be a str")
        pulumi.set(__self__, "version_release_system", version_release_system)

    @property
    @pulumi.getter(name="advancedConfigurations")
    def advanced_configurations(self) -> Sequence['outputs.GetAdvancedClusterAdvancedConfigurationResult']:
        """
        Get the advanced configuration options. See Advanced Configuration below for more details.
        """
        return pulumi.get(self, "advanced_configurations")

    @property
    @pulumi.getter(name="backupEnabled")
    def backup_enabled(self) -> bool:
        return pulumi.get(self, "backup_enabled")

    @property
    @pulumi.getter(name="biConnectorConfigs")
    def bi_connector_configs(self) -> Sequence['outputs.GetAdvancedClusterBiConnectorConfigResult']:
        """
        Configuration settings applied to BI Connector for Atlas on this cluster. See below. **NOTE** Prior version of provider had parameter as `bi_connector`
        """
        return pulumi.get(self, "bi_connector_configs")

    @property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> str:
        """
        Type of the cluster that you want to create.
        """
        return pulumi.get(self, "cluster_type")

    @property
    @pulumi.getter(name="connectionStrings")
    def connection_strings(self) -> Sequence['outputs.GetAdvancedClusterConnectionStringResult']:
        """
        Set of connection strings that your applications use to connect to this cluster. More info in [Connection-strings](https://docs.mongodb.com/manual/reference/connection-string/). Use the parameters in this object to connect your applications to this cluster. To learn more about the formats of connection strings, see [Connection String Options](https://docs.atlas.mongodb.com/reference/faq/connection-changes/). NOTE: Atlas returns the contents of this object after the cluster is operational, not while it builds the cluster.
        """
        return pulumi.get(self, "connection_strings")

    @property
    @pulumi.getter(name="createDate")
    def create_date(self) -> str:
        return pulumi.get(self, "create_date")

    @property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> float:
        """
        Capacity, in gigabytes, of the host's root volume.
        """
        return pulumi.get(self, "disk_size_gb")

    @property
    @pulumi.getter(name="encryptionAtRestProvider")
    def encryption_at_rest_provider(self) -> str:
        """
        Possible values are AWS, GCP, AZURE or NONE.
        """
        return pulumi.get(self, "encryption_at_rest_provider")

    @property
    @pulumi.getter(name="globalClusterSelfManagedSharding")
    def global_cluster_self_managed_sharding(self) -> bool:
        """
        Flag that indicates if cluster uses Atlas-Managed Sharding (false) or Self-Managed Sharding (true).
        """
        return pulumi.get(self, "global_cluster_self_managed_sharding")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    @_utilities.deprecated("""This parameter is deprecated and will be removed by September 2024. Please transition to tags.""")
    def labels(self) -> Sequence['outputs.GetAdvancedClusterLabelResult']:
        """
        Set that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the cluster. See below. **DEPRECATED** Use `tags` instead.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="mongoDbMajorVersion")
    def mongo_db_major_version(self) -> str:
        """
        Version of the cluster to deploy.
        """
        return pulumi.get(self, "mongo_db_major_version")

    @property
    @pulumi.getter(name="mongoDbVersion")
    def mongo_db_version(self) -> str:
        """
        Version of MongoDB the cluster runs, in `major-version`.`minor-version` format.
        """
        return pulumi.get(self, "mongo_db_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def paused(self) -> bool:
        """
        Flag that indicates whether the cluster is paused or not.
        """
        return pulumi.get(self, "paused")

    @property
    @pulumi.getter(name="pitEnabled")
    def pit_enabled(self) -> bool:
        """
        Flag that indicates if the cluster uses Continuous Cloud Backup.
        """
        return pulumi.get(self, "pit_enabled")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="replicationSpecs")
    def replication_specs(self) -> Sequence['outputs.GetAdvancedClusterReplicationSpecResult']:
        """
        Configuration for cluster regions and the hardware provisioned in them. See below.
        """
        return pulumi.get(self, "replication_specs")

    @property
    @pulumi.getter(name="rootCertType")
    def root_cert_type(self) -> str:
        """
        Certificate Authority that MongoDB Atlas clusters use.
        """
        return pulumi.get(self, "root_cert_type")

    @property
    @pulumi.getter(name="stateName")
    def state_name(self) -> str:
        """
        Current state of the cluster. The possible states are:
        """
        return pulumi.get(self, "state_name")

    @property
    @pulumi.getter
    def tags(self) -> Sequence['outputs.GetAdvancedClusterTagResult']:
        """
        Set that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the cluster. See below.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="terminationProtectionEnabled")
    def termination_protection_enabled(self) -> bool:
        """
        Flag that indicates whether termination protection is enabled on the cluster. If set to true, MongoDB Cloud won't delete the cluster. If set to false, MongoDB Cloud will delete the cluster.
        """
        return pulumi.get(self, "termination_protection_enabled")

    @property
    @pulumi.getter(name="versionReleaseSystem")
    def version_release_system(self) -> str:
        """
        Release cadence that Atlas uses for this cluster.
        """
        return pulumi.get(self, "version_release_system")


class AwaitableGetAdvancedClusterResult(GetAdvancedClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAdvancedClusterResult(
            advanced_configurations=self.advanced_configurations,
            backup_enabled=self.backup_enabled,
            bi_connector_configs=self.bi_connector_configs,
            cluster_type=self.cluster_type,
            connection_strings=self.connection_strings,
            create_date=self.create_date,
            disk_size_gb=self.disk_size_gb,
            encryption_at_rest_provider=self.encryption_at_rest_provider,
            global_cluster_self_managed_sharding=self.global_cluster_self_managed_sharding,
            id=self.id,
            labels=self.labels,
            mongo_db_major_version=self.mongo_db_major_version,
            mongo_db_version=self.mongo_db_version,
            name=self.name,
            paused=self.paused,
            pit_enabled=self.pit_enabled,
            project_id=self.project_id,
            replication_specs=self.replication_specs,
            root_cert_type=self.root_cert_type,
            state_name=self.state_name,
            tags=self.tags,
            termination_protection_enabled=self.termination_protection_enabled,
            version_release_system=self.version_release_system)


def get_advanced_cluster(name: Optional[str] = None,
                         pit_enabled: Optional[bool] = None,
                         project_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAdvancedClusterResult:
    """
    `AdvancedCluster` describes an Advanced Cluster. The data source requires your Project ID.

    > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.

    > **IMPORTANT:**
    <br> &#8226; Changes to cluster configurations can affect costs. Before making changes, please see [Billing](https://docs.atlas.mongodb.com/billing/).
    <br> &#8226; If your Atlas project contains a custom role that uses actions introduced in a specific MongoDB version, you cannot create a cluster with a MongoDB version less than that version unless you delete the custom role.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_mongodbatlas as mongodbatlas

    example_advanced_cluster = mongodbatlas.AdvancedCluster("example",
        project_id="<YOUR-PROJECT-ID>",
        name="cluster-test",
        cluster_type="REPLICASET",
        replication_specs=[mongodbatlas.AdvancedClusterReplicationSpecArgs(
            region_configs=[mongodbatlas.AdvancedClusterReplicationSpecRegionConfigArgs(
                electable_specs=mongodbatlas.AdvancedClusterReplicationSpecRegionConfigElectableSpecsArgs(
                    instance_size="M5",
                ),
                provider_name="TENANT",
                backing_provider_name="AWS",
                region_name="US_EAST_1",
                priority=7,
            )],
        )])
    example = mongodbatlas.get_advanced_cluster_output(project_id=example_advanced_cluster.project_id,
        name=example_advanced_cluster.name)
    ```


    :param str name: Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed.
    :param bool pit_enabled: Flag that indicates if the cluster uses Continuous Cloud Backup.
    :param str project_id: The unique ID for the project to create the database user.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['pitEnabled'] = pit_enabled
    __args__['projectId'] = project_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getAdvancedCluster:getAdvancedCluster', __args__, opts=opts, typ=GetAdvancedClusterResult).value

    return AwaitableGetAdvancedClusterResult(
        advanced_configurations=pulumi.get(__ret__, 'advanced_configurations'),
        backup_enabled=pulumi.get(__ret__, 'backup_enabled'),
        bi_connector_configs=pulumi.get(__ret__, 'bi_connector_configs'),
        cluster_type=pulumi.get(__ret__, 'cluster_type'),
        connection_strings=pulumi.get(__ret__, 'connection_strings'),
        create_date=pulumi.get(__ret__, 'create_date'),
        disk_size_gb=pulumi.get(__ret__, 'disk_size_gb'),
        encryption_at_rest_provider=pulumi.get(__ret__, 'encryption_at_rest_provider'),
        global_cluster_self_managed_sharding=pulumi.get(__ret__, 'global_cluster_self_managed_sharding'),
        id=pulumi.get(__ret__, 'id'),
        labels=pulumi.get(__ret__, 'labels'),
        mongo_db_major_version=pulumi.get(__ret__, 'mongo_db_major_version'),
        mongo_db_version=pulumi.get(__ret__, 'mongo_db_version'),
        name=pulumi.get(__ret__, 'name'),
        paused=pulumi.get(__ret__, 'paused'),
        pit_enabled=pulumi.get(__ret__, 'pit_enabled'),
        project_id=pulumi.get(__ret__, 'project_id'),
        replication_specs=pulumi.get(__ret__, 'replication_specs'),
        root_cert_type=pulumi.get(__ret__, 'root_cert_type'),
        state_name=pulumi.get(__ret__, 'state_name'),
        tags=pulumi.get(__ret__, 'tags'),
        termination_protection_enabled=pulumi.get(__ret__, 'termination_protection_enabled'),
        version_release_system=pulumi.get(__ret__, 'version_release_system'))


@_utilities.lift_output_func(get_advanced_cluster)
def get_advanced_cluster_output(name: Optional[pulumi.Input[str]] = None,
                                pit_enabled: Optional[pulumi.Input[Optional[bool]]] = None,
                                project_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAdvancedClusterResult]:
    """
    `AdvancedCluster` describes an Advanced Cluster. The data source requires your Project ID.

    > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.

    > **IMPORTANT:**
    <br> &#8226; Changes to cluster configurations can affect costs. Before making changes, please see [Billing](https://docs.atlas.mongodb.com/billing/).
    <br> &#8226; If your Atlas project contains a custom role that uses actions introduced in a specific MongoDB version, you cannot create a cluster with a MongoDB version less than that version unless you delete the custom role.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_mongodbatlas as mongodbatlas

    example_advanced_cluster = mongodbatlas.AdvancedCluster("example",
        project_id="<YOUR-PROJECT-ID>",
        name="cluster-test",
        cluster_type="REPLICASET",
        replication_specs=[mongodbatlas.AdvancedClusterReplicationSpecArgs(
            region_configs=[mongodbatlas.AdvancedClusterReplicationSpecRegionConfigArgs(
                electable_specs=mongodbatlas.AdvancedClusterReplicationSpecRegionConfigElectableSpecsArgs(
                    instance_size="M5",
                ),
                provider_name="TENANT",
                backing_provider_name="AWS",
                region_name="US_EAST_1",
                priority=7,
            )],
        )])
    example = mongodbatlas.get_advanced_cluster_output(project_id=example_advanced_cluster.project_id,
        name=example_advanced_cluster.name)
    ```


    :param str name: Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed.
    :param bool pit_enabled: Flag that indicates if the cluster uses Continuous Cloud Backup.
    :param str project_id: The unique ID for the project to create the database user.
    """
    ...
