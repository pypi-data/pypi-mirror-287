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
    'GetNodeTemplateResult',
    'AwaitableGetNodeTemplateResult',
    'get_node_template',
    'get_node_template_output',
]

@pulumi.output_type
class GetNodeTemplateResult:
    """
    A collection of values returned by getNodeTemplate.
    """
    def __init__(__self__, annotations=None, cloud_credential_id=None, description=None, driver=None, engine_env=None, engine_insecure_registries=None, engine_install_url=None, engine_label=None, engine_opt=None, engine_registry_mirrors=None, engine_storage_driver=None, id=None, labels=None, name=None, node_taints=None, use_internal_ip_address=None):
        if annotations and not isinstance(annotations, dict):
            raise TypeError("Expected argument 'annotations' to be a dict")
        pulumi.set(__self__, "annotations", annotations)
        if cloud_credential_id and not isinstance(cloud_credential_id, str):
            raise TypeError("Expected argument 'cloud_credential_id' to be a str")
        pulumi.set(__self__, "cloud_credential_id", cloud_credential_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if driver and not isinstance(driver, str):
            raise TypeError("Expected argument 'driver' to be a str")
        pulumi.set(__self__, "driver", driver)
        if engine_env and not isinstance(engine_env, dict):
            raise TypeError("Expected argument 'engine_env' to be a dict")
        pulumi.set(__self__, "engine_env", engine_env)
        if engine_insecure_registries and not isinstance(engine_insecure_registries, list):
            raise TypeError("Expected argument 'engine_insecure_registries' to be a list")
        pulumi.set(__self__, "engine_insecure_registries", engine_insecure_registries)
        if engine_install_url and not isinstance(engine_install_url, str):
            raise TypeError("Expected argument 'engine_install_url' to be a str")
        pulumi.set(__self__, "engine_install_url", engine_install_url)
        if engine_label and not isinstance(engine_label, dict):
            raise TypeError("Expected argument 'engine_label' to be a dict")
        pulumi.set(__self__, "engine_label", engine_label)
        if engine_opt and not isinstance(engine_opt, dict):
            raise TypeError("Expected argument 'engine_opt' to be a dict")
        pulumi.set(__self__, "engine_opt", engine_opt)
        if engine_registry_mirrors and not isinstance(engine_registry_mirrors, list):
            raise TypeError("Expected argument 'engine_registry_mirrors' to be a list")
        pulumi.set(__self__, "engine_registry_mirrors", engine_registry_mirrors)
        if engine_storage_driver and not isinstance(engine_storage_driver, str):
            raise TypeError("Expected argument 'engine_storage_driver' to be a str")
        pulumi.set(__self__, "engine_storage_driver", engine_storage_driver)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if node_taints and not isinstance(node_taints, list):
            raise TypeError("Expected argument 'node_taints' to be a list")
        pulumi.set(__self__, "node_taints", node_taints)
        if use_internal_ip_address and not isinstance(use_internal_ip_address, bool):
            raise TypeError("Expected argument 'use_internal_ip_address' to be a bool")
        pulumi.set(__self__, "use_internal_ip_address", use_internal_ip_address)

    @property
    @pulumi.getter
    def annotations(self) -> Mapping[str, Any]:
        """
        (Computed) Annotations for Node Template object (map)
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="cloudCredentialId")
    def cloud_credential_id(self) -> str:
        """
        (Computed) Cloud credential ID for the Node Template. Required from Rancher v2.2.x (string)
        """
        return pulumi.get(self, "cloud_credential_id")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        (Computed) Description for the Node Template (string)
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def driver(self) -> str:
        """
        (Computed) The driver of the node template (string)
        """
        return pulumi.get(self, "driver")

    @property
    @pulumi.getter(name="engineEnv")
    def engine_env(self) -> Mapping[str, Any]:
        """
        (Computed) Engine environment for the node template (string)
        """
        return pulumi.get(self, "engine_env")

    @property
    @pulumi.getter(name="engineInsecureRegistries")
    def engine_insecure_registries(self) -> Sequence[str]:
        """
        (Computed) Insecure registry for the node template (list)
        """
        return pulumi.get(self, "engine_insecure_registries")

    @property
    @pulumi.getter(name="engineInstallUrl")
    def engine_install_url(self) -> str:
        """
        (Computed) Docker engine install URL for the node template (string)
        """
        return pulumi.get(self, "engine_install_url")

    @property
    @pulumi.getter(name="engineLabel")
    def engine_label(self) -> Mapping[str, Any]:
        """
        (Computed) Engine label for the node template (string)
        """
        return pulumi.get(self, "engine_label")

    @property
    @pulumi.getter(name="engineOpt")
    def engine_opt(self) -> Mapping[str, Any]:
        """
        (Computed) Engine options for the node template (map)
        """
        return pulumi.get(self, "engine_opt")

    @property
    @pulumi.getter(name="engineRegistryMirrors")
    def engine_registry_mirrors(self) -> Sequence[str]:
        """
        (Computed) Engine registry mirror for the node template (list)
        """
        return pulumi.get(self, "engine_registry_mirrors")

    @property
    @pulumi.getter(name="engineStorageDriver")
    def engine_storage_driver(self) -> str:
        """
        (Computed) Engine storage driver for the node template (string)
        """
        return pulumi.get(self, "engine_storage_driver")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, Any]:
        """
        (Computed) Labels for Node Template object (map)
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeTaints")
    def node_taints(self) -> Sequence['outputs.GetNodeTemplateNodeTaintResult']:
        """
        (Computed) Node taints (List)
        """
        return pulumi.get(self, "node_taints")

    @property
    @pulumi.getter(name="useInternalIpAddress")
    def use_internal_ip_address(self) -> Optional[bool]:
        """
        (Computed) Engine storage driver for the node template (bool)
        """
        return pulumi.get(self, "use_internal_ip_address")


class AwaitableGetNodeTemplateResult(GetNodeTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNodeTemplateResult(
            annotations=self.annotations,
            cloud_credential_id=self.cloud_credential_id,
            description=self.description,
            driver=self.driver,
            engine_env=self.engine_env,
            engine_insecure_registries=self.engine_insecure_registries,
            engine_install_url=self.engine_install_url,
            engine_label=self.engine_label,
            engine_opt=self.engine_opt,
            engine_registry_mirrors=self.engine_registry_mirrors,
            engine_storage_driver=self.engine_storage_driver,
            id=self.id,
            labels=self.labels,
            name=self.name,
            node_taints=self.node_taints,
            use_internal_ip_address=self.use_internal_ip_address)


def get_node_template(name: Optional[str] = None,
                      use_internal_ip_address: Optional[bool] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNodeTemplateResult:
    """
    Use this data source to retrieve information about a Rancher v2 Node Template resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_rancher2 as rancher2

    foo = rancher2.get_node_template(name="foo")
    ```


    :param str name: The name of the Node Template (string)
    :param bool use_internal_ip_address: (Computed) Engine storage driver for the node template (bool)
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['useInternalIpAddress'] = use_internal_ip_address
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('rancher2:index/getNodeTemplate:getNodeTemplate', __args__, opts=opts, typ=GetNodeTemplateResult).value

    return AwaitableGetNodeTemplateResult(
        annotations=pulumi.get(__ret__, 'annotations'),
        cloud_credential_id=pulumi.get(__ret__, 'cloud_credential_id'),
        description=pulumi.get(__ret__, 'description'),
        driver=pulumi.get(__ret__, 'driver'),
        engine_env=pulumi.get(__ret__, 'engine_env'),
        engine_insecure_registries=pulumi.get(__ret__, 'engine_insecure_registries'),
        engine_install_url=pulumi.get(__ret__, 'engine_install_url'),
        engine_label=pulumi.get(__ret__, 'engine_label'),
        engine_opt=pulumi.get(__ret__, 'engine_opt'),
        engine_registry_mirrors=pulumi.get(__ret__, 'engine_registry_mirrors'),
        engine_storage_driver=pulumi.get(__ret__, 'engine_storage_driver'),
        id=pulumi.get(__ret__, 'id'),
        labels=pulumi.get(__ret__, 'labels'),
        name=pulumi.get(__ret__, 'name'),
        node_taints=pulumi.get(__ret__, 'node_taints'),
        use_internal_ip_address=pulumi.get(__ret__, 'use_internal_ip_address'))


@_utilities.lift_output_func(get_node_template)
def get_node_template_output(name: Optional[pulumi.Input[str]] = None,
                             use_internal_ip_address: Optional[pulumi.Input[Optional[bool]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNodeTemplateResult]:
    """
    Use this data source to retrieve information about a Rancher v2 Node Template resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_rancher2 as rancher2

    foo = rancher2.get_node_template(name="foo")
    ```


    :param str name: The name of the Node Template (string)
    :param bool use_internal_ip_address: (Computed) Engine storage driver for the node template (bool)
    """
    ...
