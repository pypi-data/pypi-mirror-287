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
    'GetPodSecurityAdmissionConfigurationTemplateResult',
    'AwaitableGetPodSecurityAdmissionConfigurationTemplateResult',
    'get_pod_security_admission_configuration_template',
    'get_pod_security_admission_configuration_template_output',
]

@pulumi.output_type
class GetPodSecurityAdmissionConfigurationTemplateResult:
    """
    A collection of values returned by getPodSecurityAdmissionConfigurationTemplate.
    """
    def __init__(__self__, annotations=None, defaults=None, description=None, exemptions=None, id=None, labels=None, name=None):
        if annotations and not isinstance(annotations, dict):
            raise TypeError("Expected argument 'annotations' to be a dict")
        pulumi.set(__self__, "annotations", annotations)
        if defaults and not isinstance(defaults, dict):
            raise TypeError("Expected argument 'defaults' to be a dict")
        pulumi.set(__self__, "defaults", defaults)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if exemptions and not isinstance(exemptions, dict):
            raise TypeError("Expected argument 'exemptions' to be a dict")
        pulumi.set(__self__, "exemptions", exemptions)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def annotations(self) -> Mapping[str, Any]:
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter
    def defaults(self) -> 'outputs.GetPodSecurityAdmissionConfigurationTemplateDefaultsResult':
        return pulumi.get(self, "defaults")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def exemptions(self) -> 'outputs.GetPodSecurityAdmissionConfigurationTemplateExemptionsResult':
        return pulumi.get(self, "exemptions")

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
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


class AwaitableGetPodSecurityAdmissionConfigurationTemplateResult(GetPodSecurityAdmissionConfigurationTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPodSecurityAdmissionConfigurationTemplateResult(
            annotations=self.annotations,
            defaults=self.defaults,
            description=self.description,
            exemptions=self.exemptions,
            id=self.id,
            labels=self.labels,
            name=self.name)


def get_pod_security_admission_configuration_template(annotations: Optional[Mapping[str, Any]] = None,
                                                      labels: Optional[Mapping[str, Any]] = None,
                                                      name: Optional[str] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPodSecurityAdmissionConfigurationTemplateResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['annotations'] = annotations
    __args__['labels'] = labels
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('rancher2:index/getPodSecurityAdmissionConfigurationTemplate:getPodSecurityAdmissionConfigurationTemplate', __args__, opts=opts, typ=GetPodSecurityAdmissionConfigurationTemplateResult).value

    return AwaitableGetPodSecurityAdmissionConfigurationTemplateResult(
        annotations=pulumi.get(__ret__, 'annotations'),
        defaults=pulumi.get(__ret__, 'defaults'),
        description=pulumi.get(__ret__, 'description'),
        exemptions=pulumi.get(__ret__, 'exemptions'),
        id=pulumi.get(__ret__, 'id'),
        labels=pulumi.get(__ret__, 'labels'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_pod_security_admission_configuration_template)
def get_pod_security_admission_configuration_template_output(annotations: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                                                             labels: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                                                             name: Optional[pulumi.Input[str]] = None,
                                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPodSecurityAdmissionConfigurationTemplateResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
