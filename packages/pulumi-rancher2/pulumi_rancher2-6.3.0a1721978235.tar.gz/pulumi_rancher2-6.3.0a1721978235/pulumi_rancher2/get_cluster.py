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
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
    'get_cluster_output',
]

@pulumi.output_type
class GetClusterResult:
    """
    A collection of values returned by getCluster.
    """
    def __init__(__self__, agent_env_vars=None, aks_config=None, aks_config_v2=None, annotations=None, ca_cert=None, cluster_auth_endpoint=None, cluster_monitoring_input=None, cluster_registration_token=None, cluster_template_answers=None, cluster_template_id=None, cluster_template_questions=None, cluster_template_revision_id=None, default_pod_security_admission_configuration_template_name=None, default_pod_security_policy_template_id=None, default_project_id=None, description=None, driver=None, eks_config=None, eks_config_v2=None, enable_cluster_alerting=None, enable_cluster_monitoring=None, enable_network_policy=None, fleet_workspace_name=None, gke_config=None, gke_config_v2=None, id=None, k3s_config=None, kube_config=None, labels=None, name=None, oke_config=None, rke2_config=None, rke_config=None, system_project_id=None):
        if agent_env_vars and not isinstance(agent_env_vars, list):
            raise TypeError("Expected argument 'agent_env_vars' to be a list")
        pulumi.set(__self__, "agent_env_vars", agent_env_vars)
        if aks_config and not isinstance(aks_config, dict):
            raise TypeError("Expected argument 'aks_config' to be a dict")
        pulumi.set(__self__, "aks_config", aks_config)
        if aks_config_v2 and not isinstance(aks_config_v2, dict):
            raise TypeError("Expected argument 'aks_config_v2' to be a dict")
        pulumi.set(__self__, "aks_config_v2", aks_config_v2)
        if annotations and not isinstance(annotations, dict):
            raise TypeError("Expected argument 'annotations' to be a dict")
        pulumi.set(__self__, "annotations", annotations)
        if ca_cert and not isinstance(ca_cert, str):
            raise TypeError("Expected argument 'ca_cert' to be a str")
        pulumi.set(__self__, "ca_cert", ca_cert)
        if cluster_auth_endpoint and not isinstance(cluster_auth_endpoint, dict):
            raise TypeError("Expected argument 'cluster_auth_endpoint' to be a dict")
        pulumi.set(__self__, "cluster_auth_endpoint", cluster_auth_endpoint)
        if cluster_monitoring_input and not isinstance(cluster_monitoring_input, dict):
            raise TypeError("Expected argument 'cluster_monitoring_input' to be a dict")
        pulumi.set(__self__, "cluster_monitoring_input", cluster_monitoring_input)
        if cluster_registration_token and not isinstance(cluster_registration_token, dict):
            raise TypeError("Expected argument 'cluster_registration_token' to be a dict")
        pulumi.set(__self__, "cluster_registration_token", cluster_registration_token)
        if cluster_template_answers and not isinstance(cluster_template_answers, dict):
            raise TypeError("Expected argument 'cluster_template_answers' to be a dict")
        pulumi.set(__self__, "cluster_template_answers", cluster_template_answers)
        if cluster_template_id and not isinstance(cluster_template_id, str):
            raise TypeError("Expected argument 'cluster_template_id' to be a str")
        pulumi.set(__self__, "cluster_template_id", cluster_template_id)
        if cluster_template_questions and not isinstance(cluster_template_questions, list):
            raise TypeError("Expected argument 'cluster_template_questions' to be a list")
        pulumi.set(__self__, "cluster_template_questions", cluster_template_questions)
        if cluster_template_revision_id and not isinstance(cluster_template_revision_id, str):
            raise TypeError("Expected argument 'cluster_template_revision_id' to be a str")
        pulumi.set(__self__, "cluster_template_revision_id", cluster_template_revision_id)
        if default_pod_security_admission_configuration_template_name and not isinstance(default_pod_security_admission_configuration_template_name, str):
            raise TypeError("Expected argument 'default_pod_security_admission_configuration_template_name' to be a str")
        pulumi.set(__self__, "default_pod_security_admission_configuration_template_name", default_pod_security_admission_configuration_template_name)
        if default_pod_security_policy_template_id and not isinstance(default_pod_security_policy_template_id, str):
            raise TypeError("Expected argument 'default_pod_security_policy_template_id' to be a str")
        pulumi.set(__self__, "default_pod_security_policy_template_id", default_pod_security_policy_template_id)
        if default_project_id and not isinstance(default_project_id, str):
            raise TypeError("Expected argument 'default_project_id' to be a str")
        pulumi.set(__self__, "default_project_id", default_project_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if driver and not isinstance(driver, str):
            raise TypeError("Expected argument 'driver' to be a str")
        pulumi.set(__self__, "driver", driver)
        if eks_config and not isinstance(eks_config, dict):
            raise TypeError("Expected argument 'eks_config' to be a dict")
        pulumi.set(__self__, "eks_config", eks_config)
        if eks_config_v2 and not isinstance(eks_config_v2, dict):
            raise TypeError("Expected argument 'eks_config_v2' to be a dict")
        pulumi.set(__self__, "eks_config_v2", eks_config_v2)
        if enable_cluster_alerting and not isinstance(enable_cluster_alerting, bool):
            raise TypeError("Expected argument 'enable_cluster_alerting' to be a bool")
        pulumi.set(__self__, "enable_cluster_alerting", enable_cluster_alerting)
        if enable_cluster_monitoring and not isinstance(enable_cluster_monitoring, bool):
            raise TypeError("Expected argument 'enable_cluster_monitoring' to be a bool")
        pulumi.set(__self__, "enable_cluster_monitoring", enable_cluster_monitoring)
        if enable_network_policy and not isinstance(enable_network_policy, bool):
            raise TypeError("Expected argument 'enable_network_policy' to be a bool")
        pulumi.set(__self__, "enable_network_policy", enable_network_policy)
        if fleet_workspace_name and not isinstance(fleet_workspace_name, str):
            raise TypeError("Expected argument 'fleet_workspace_name' to be a str")
        pulumi.set(__self__, "fleet_workspace_name", fleet_workspace_name)
        if gke_config and not isinstance(gke_config, dict):
            raise TypeError("Expected argument 'gke_config' to be a dict")
        pulumi.set(__self__, "gke_config", gke_config)
        if gke_config_v2 and not isinstance(gke_config_v2, dict):
            raise TypeError("Expected argument 'gke_config_v2' to be a dict")
        pulumi.set(__self__, "gke_config_v2", gke_config_v2)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if k3s_config and not isinstance(k3s_config, dict):
            raise TypeError("Expected argument 'k3s_config' to be a dict")
        pulumi.set(__self__, "k3s_config", k3s_config)
        if kube_config and not isinstance(kube_config, str):
            raise TypeError("Expected argument 'kube_config' to be a str")
        pulumi.set(__self__, "kube_config", kube_config)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if oke_config and not isinstance(oke_config, dict):
            raise TypeError("Expected argument 'oke_config' to be a dict")
        pulumi.set(__self__, "oke_config", oke_config)
        if rke2_config and not isinstance(rke2_config, dict):
            raise TypeError("Expected argument 'rke2_config' to be a dict")
        pulumi.set(__self__, "rke2_config", rke2_config)
        if rke_config and not isinstance(rke_config, dict):
            raise TypeError("Expected argument 'rke_config' to be a dict")
        pulumi.set(__self__, "rke_config", rke_config)
        if system_project_id and not isinstance(system_project_id, str):
            raise TypeError("Expected argument 'system_project_id' to be a str")
        pulumi.set(__self__, "system_project_id", system_project_id)

    @property
    @pulumi.getter(name="agentEnvVars")
    def agent_env_vars(self) -> Sequence[str]:
        """
        (Computed) Optional Agent Env Vars for Rancher agent. For Rancher v2.5.6 and above (list)
        """
        return pulumi.get(self, "agent_env_vars")

    @property
    @pulumi.getter(name="aksConfig")
    def aks_config(self) -> 'outputs.GetClusterAksConfigResult':
        """
        (Computed) The Azure aks configuration for `aks` Clusters. Conflicts with `aks_config_v2`, `eks_config`, `eks_config_v2`, `gke_config`, `gke_config_v2`, `oke_config`, `k3s_config` and `rke_config` (list maxitems:1)
        """
        return pulumi.get(self, "aks_config")

    @property
    @pulumi.getter(name="aksConfigV2")
    def aks_config_v2(self) -> 'outputs.GetClusterAksConfigV2Result':
        """
        (Optional) The Azure AKS v2 configuration for creating/import `aks` Clusters. Conflicts with `aks_config`, `eks_config`, `eks_config_v2`, `gke_config`, `gke_config_v2`, `oke_config` `k3s_config` and `rke_config` (list maxitems:1)
        """
        return pulumi.get(self, "aks_config_v2")

    @property
    @pulumi.getter
    def annotations(self) -> Mapping[str, Any]:
        """
        (Computed) Annotations for Node Pool object (map)
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="caCert")
    def ca_cert(self) -> str:
        """
        (Computed) K8s cluster ca cert (string)
        """
        return pulumi.get(self, "ca_cert")

    @property
    @pulumi.getter(name="clusterAuthEndpoint")
    def cluster_auth_endpoint(self) -> 'outputs.GetClusterClusterAuthEndpointResult':
        """
        (Computed) Enabling the [local cluster authorized endpoint](https://rancher.com/docs/rancher/v2.x/en/cluster-provisioning/rke-clusters/options/#local-cluster-auth-endpoint) allows direct communication with the cluster, bypassing the Rancher API proxy. (list maxitems:1)
        """
        return pulumi.get(self, "cluster_auth_endpoint")

    @property
    @pulumi.getter(name="clusterMonitoringInput")
    def cluster_monitoring_input(self) -> 'outputs.GetClusterClusterMonitoringInputResult':
        """
        (Computed) Cluster monitoring config (list maxitems:1)
        """
        return pulumi.get(self, "cluster_monitoring_input")

    @property
    @pulumi.getter(name="clusterRegistrationToken")
    def cluster_registration_token(self) -> 'outputs.GetClusterClusterRegistrationTokenResult':
        """
        (Computed) Cluster Registration Token generated for the cluster (list maxitems:1)
        """
        return pulumi.get(self, "cluster_registration_token")

    @property
    @pulumi.getter(name="clusterTemplateAnswers")
    def cluster_template_answers(self) -> 'outputs.GetClusterClusterTemplateAnswersResult':
        """
        (Computed) Cluster template answers (list maxitems:1)
        """
        return pulumi.get(self, "cluster_template_answers")

    @property
    @pulumi.getter(name="clusterTemplateId")
    def cluster_template_id(self) -> str:
        """
        (Computed) Cluster template ID (string)
        """
        return pulumi.get(self, "cluster_template_id")

    @property
    @pulumi.getter(name="clusterTemplateQuestions")
    def cluster_template_questions(self) -> Sequence['outputs.GetClusterClusterTemplateQuestionResult']:
        """
        (Computed) Cluster template questions (list)
        """
        return pulumi.get(self, "cluster_template_questions")

    @property
    @pulumi.getter(name="clusterTemplateRevisionId")
    def cluster_template_revision_id(self) -> str:
        """
        (Computed) Cluster template revision ID (string)
        """
        return pulumi.get(self, "cluster_template_revision_id")

    @property
    @pulumi.getter(name="defaultPodSecurityAdmissionConfigurationTemplateName")
    def default_pod_security_admission_configuration_template_name(self) -> str:
        return pulumi.get(self, "default_pod_security_admission_configuration_template_name")

    @property
    @pulumi.getter(name="defaultPodSecurityPolicyTemplateId")
    def default_pod_security_policy_template_id(self) -> str:
        """
        (Optional/Computed) [Default pod security policy template id](https://rancher.com/docs/rancher/v2.x/en/cluster-provisioning/rke-clusters/options/#pod-security-policy-support) (string)
        """
        return pulumi.get(self, "default_pod_security_policy_template_id")

    @property
    @pulumi.getter(name="defaultProjectId")
    def default_project_id(self) -> str:
        """
        (Computed) Default project ID for the cluster (string)
        """
        return pulumi.get(self, "default_project_id")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        (Computed) The description for Cluster (string)
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def driver(self) -> str:
        """
        (Computed) The driver used for the Cluster. `imported`, `azurekubernetesservice`, `amazonelasticcontainerservice`, `googlekubernetesengine` and `rancherKubernetesEngine` are supported (string)
        """
        return pulumi.get(self, "driver")

    @property
    @pulumi.getter(name="eksConfig")
    def eks_config(self) -> 'outputs.GetClusterEksConfigResult':
        """
        (Computed) The Amazon eks configuration for `eks` Conflicts with `aks_config`, `aks_config_v2`, `eks_config_v2`, `gke_config`, `gke_config_v2`, `oke_config`, `k3s_config` and `rke_config` (list maxitems:1)
        """
        return pulumi.get(self, "eks_config")

    @property
    @pulumi.getter(name="eksConfigV2")
    def eks_config_v2(self) -> 'outputs.GetClusterEksConfigV2Result':
        """
        (Computed) The Amazon EKS V2 configuration to create or import `eks` Clusters. Conflicts with `aks_config`, `aks_config_v2`, `eks_config`, `gke_config`, `gke_config_v2`, `oke_config`, `k3s_config` and `rke_config`. For Rancher v2.5.x and above (list maxitems:1)
        """
        return pulumi.get(self, "eks_config_v2")

    @property
    @pulumi.getter(name="enableClusterAlerting")
    def enable_cluster_alerting(self) -> bool:
        return pulumi.get(self, "enable_cluster_alerting")

    @property
    @pulumi.getter(name="enableClusterMonitoring")
    def enable_cluster_monitoring(self) -> bool:
        """
        (Computed) Enable built-in cluster monitoring. Default `false` (bool)
        """
        return pulumi.get(self, "enable_cluster_monitoring")

    @property
    @pulumi.getter(name="enableNetworkPolicy")
    def enable_network_policy(self) -> bool:
        """
        (Computed) Enable project network isolation. Default `false` (bool)
        """
        return pulumi.get(self, "enable_network_policy")

    @property
    @pulumi.getter(name="fleetWorkspaceName")
    def fleet_workspace_name(self) -> str:
        """
        (Computed) Fleet workspace name (string)
        """
        return pulumi.get(self, "fleet_workspace_name")

    @property
    @pulumi.getter(name="gkeConfig")
    def gke_config(self) -> 'outputs.GetClusterGkeConfigResult':
        """
        (Computed) The Google gke configuration for `gke` Clusters. Conflicts with `aks_config`, `aks_config_v2`, `eks_config`, `eks_config_v2`, `gke_config_v2`, `oke_config`, `k3s_config` and `rke_config` (list maxitems:1) (list maxitems:1)
        """
        return pulumi.get(self, "gke_config")

    @property
    @pulumi.getter(name="gkeConfigV2")
    def gke_config_v2(self) -> 'outputs.GetClusterGkeConfigV2Result':
        """
        (Computed) The Google GKE V2 configuration for `gke` Clusters. Conflicts with `aks_config`, `aks_config_v2`, `eks_config`, `eks_config_v2`, `gke_config`, `oke_config`, `k3s_config` and `rke_config`. For Rancher v2.5.8 and above (list maxitems:1)
        """
        return pulumi.get(self, "gke_config_v2")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="k3sConfig")
    def k3s_config(self) -> 'outputs.GetClusterK3sConfigResult':
        """
        (Computed) The K3S configuration for `k3s` imported Clusters. Conflicts with `aks_config`, `aks_config_v2`, `eks_config`, `eks_config_v2`, `gke_config`, `gke_config_v2`, `oke_config` and `rke_config` (list maxitems:1)
        """
        return pulumi.get(self, "k3s_config")

    @property
    @pulumi.getter(name="kubeConfig")
    def kube_config(self) -> str:
        """
        (Computed) Kube Config generated for the cluster (string)
        """
        return pulumi.get(self, "kube_config")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, Any]:
        """
        (Computed) Labels for Node Pool object (map)
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="okeConfig")
    def oke_config(self) -> 'outputs.GetClusterOkeConfigResult':
        """
        (Computed) The Oracle OKE configuration for `oke` Clusters. Conflicts with `aks_config`, `aks_config_v2`, `eks_config`, `eks_config_v2`, `gke_config`, `gke_config_v2`, `k3s_config` and `rke_config` (list maxitems:1)
        """
        return pulumi.get(self, "oke_config")

    @property
    @pulumi.getter(name="rke2Config")
    def rke2_config(self) -> 'outputs.GetClusterRke2ConfigResult':
        """
        (Computed) The RKE2 configuration for `rke2` Clusters. Conflicts with `aks_config`, `aks_config_v2`, `eks_config`, `gke_config`, `oke_config`, `k3s_config` and `rke_config` (list maxitems:1)
        """
        return pulumi.get(self, "rke2_config")

    @property
    @pulumi.getter(name="rkeConfig")
    def rke_config(self) -> 'outputs.GetClusterRkeConfigResult':
        """
        (Computed) The RKE configuration for `rke` Clusters. Conflicts with `aks_config`, `aks_config_v2`, `eks_config`, `eks_config_v2`, `gke_config`, `gke_config_v2`, `oke_config` and `k3s_config` (list maxitems:1)
        """
        return pulumi.get(self, "rke_config")

    @property
    @pulumi.getter(name="systemProjectId")
    def system_project_id(self) -> str:
        """
        (Computed) System project ID for the cluster (string)
        """
        return pulumi.get(self, "system_project_id")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            agent_env_vars=self.agent_env_vars,
            aks_config=self.aks_config,
            aks_config_v2=self.aks_config_v2,
            annotations=self.annotations,
            ca_cert=self.ca_cert,
            cluster_auth_endpoint=self.cluster_auth_endpoint,
            cluster_monitoring_input=self.cluster_monitoring_input,
            cluster_registration_token=self.cluster_registration_token,
            cluster_template_answers=self.cluster_template_answers,
            cluster_template_id=self.cluster_template_id,
            cluster_template_questions=self.cluster_template_questions,
            cluster_template_revision_id=self.cluster_template_revision_id,
            default_pod_security_admission_configuration_template_name=self.default_pod_security_admission_configuration_template_name,
            default_pod_security_policy_template_id=self.default_pod_security_policy_template_id,
            default_project_id=self.default_project_id,
            description=self.description,
            driver=self.driver,
            eks_config=self.eks_config,
            eks_config_v2=self.eks_config_v2,
            enable_cluster_alerting=self.enable_cluster_alerting,
            enable_cluster_monitoring=self.enable_cluster_monitoring,
            enable_network_policy=self.enable_network_policy,
            fleet_workspace_name=self.fleet_workspace_name,
            gke_config=self.gke_config,
            gke_config_v2=self.gke_config_v2,
            id=self.id,
            k3s_config=self.k3s_config,
            kube_config=self.kube_config,
            labels=self.labels,
            name=self.name,
            oke_config=self.oke_config,
            rke2_config=self.rke2_config,
            rke_config=self.rke_config,
            system_project_id=self.system_project_id)


def get_cluster(default_pod_security_admission_configuration_template_name: Optional[str] = None,
                name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    Use this data source to retrieve information about a Rancher v2 cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_rancher2 as rancher2

    foo_custom = rancher2.get_cluster(name="foo-custom")
    ```


    :param str name: The name of the Cluster (string)
    """
    __args__ = dict()
    __args__['defaultPodSecurityAdmissionConfigurationTemplateName'] = default_pod_security_admission_configuration_template_name
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('rancher2:index/getCluster:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        agent_env_vars=pulumi.get(__ret__, 'agent_env_vars'),
        aks_config=pulumi.get(__ret__, 'aks_config'),
        aks_config_v2=pulumi.get(__ret__, 'aks_config_v2'),
        annotations=pulumi.get(__ret__, 'annotations'),
        ca_cert=pulumi.get(__ret__, 'ca_cert'),
        cluster_auth_endpoint=pulumi.get(__ret__, 'cluster_auth_endpoint'),
        cluster_monitoring_input=pulumi.get(__ret__, 'cluster_monitoring_input'),
        cluster_registration_token=pulumi.get(__ret__, 'cluster_registration_token'),
        cluster_template_answers=pulumi.get(__ret__, 'cluster_template_answers'),
        cluster_template_id=pulumi.get(__ret__, 'cluster_template_id'),
        cluster_template_questions=pulumi.get(__ret__, 'cluster_template_questions'),
        cluster_template_revision_id=pulumi.get(__ret__, 'cluster_template_revision_id'),
        default_pod_security_admission_configuration_template_name=pulumi.get(__ret__, 'default_pod_security_admission_configuration_template_name'),
        default_pod_security_policy_template_id=pulumi.get(__ret__, 'default_pod_security_policy_template_id'),
        default_project_id=pulumi.get(__ret__, 'default_project_id'),
        description=pulumi.get(__ret__, 'description'),
        driver=pulumi.get(__ret__, 'driver'),
        eks_config=pulumi.get(__ret__, 'eks_config'),
        eks_config_v2=pulumi.get(__ret__, 'eks_config_v2'),
        enable_cluster_alerting=pulumi.get(__ret__, 'enable_cluster_alerting'),
        enable_cluster_monitoring=pulumi.get(__ret__, 'enable_cluster_monitoring'),
        enable_network_policy=pulumi.get(__ret__, 'enable_network_policy'),
        fleet_workspace_name=pulumi.get(__ret__, 'fleet_workspace_name'),
        gke_config=pulumi.get(__ret__, 'gke_config'),
        gke_config_v2=pulumi.get(__ret__, 'gke_config_v2'),
        id=pulumi.get(__ret__, 'id'),
        k3s_config=pulumi.get(__ret__, 'k3s_config'),
        kube_config=pulumi.get(__ret__, 'kube_config'),
        labels=pulumi.get(__ret__, 'labels'),
        name=pulumi.get(__ret__, 'name'),
        oke_config=pulumi.get(__ret__, 'oke_config'),
        rke2_config=pulumi.get(__ret__, 'rke2_config'),
        rke_config=pulumi.get(__ret__, 'rke_config'),
        system_project_id=pulumi.get(__ret__, 'system_project_id'))


@_utilities.lift_output_func(get_cluster)
def get_cluster_output(default_pod_security_admission_configuration_template_name: Optional[pulumi.Input[Optional[str]]] = None,
                       name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterResult]:
    """
    Use this data source to retrieve information about a Rancher v2 cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_rancher2 as rancher2

    foo_custom = rancher2.get_cluster(name="foo-custom")
    ```


    :param str name: The name of the Cluster (string)
    """
    ...
