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
from ._inputs import *

__all__ = ['RegistryArgs', 'Registry']

@pulumi.input_type
class RegistryArgs:
    def __init__(__self__, *,
                 project_id: pulumi.Input[str],
                 registries: pulumi.Input[Sequence[pulumi.Input['RegistryRegistryArgs']]],
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Registry resource.
        :param pulumi.Input[str] project_id: The project id where to assign the registry (string)
        :param pulumi.Input[Sequence[pulumi.Input['RegistryRegistryArgs']]] registries: Registries data for registry (list)
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations for Registry object (map)
        :param pulumi.Input[str] description: A registry description (string)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels for Registry object (map)
        :param pulumi.Input[str] name: The name of the registry (string)
        :param pulumi.Input[str] namespace_id: The namespace id where to assign the namespaced registry (string)
        """
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "registries", registries)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace_id is not None:
            pulumi.set(__self__, "namespace_id", namespace_id)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        The project id where to assign the registry (string)
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def registries(self) -> pulumi.Input[Sequence[pulumi.Input['RegistryRegistryArgs']]]:
        """
        Registries data for registry (list)
        """
        return pulumi.get(self, "registries")

    @registries.setter
    def registries(self, value: pulumi.Input[Sequence[pulumi.Input['RegistryRegistryArgs']]]):
        pulumi.set(self, "registries", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Annotations for Registry object (map)
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A registry description (string)
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Labels for Registry object (map)
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the registry (string)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace id where to assign the namespaced registry (string)
        """
        return pulumi.get(self, "namespace_id")

    @namespace_id.setter
    def namespace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_id", value)


@pulumi.input_type
class _RegistryState:
    def __init__(__self__, *,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 registries: Optional[pulumi.Input[Sequence[pulumi.Input['RegistryRegistryArgs']]]] = None):
        """
        Input properties used for looking up and filtering Registry resources.
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations for Registry object (map)
        :param pulumi.Input[str] description: A registry description (string)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels for Registry object (map)
        :param pulumi.Input[str] name: The name of the registry (string)
        :param pulumi.Input[str] namespace_id: The namespace id where to assign the namespaced registry (string)
        :param pulumi.Input[str] project_id: The project id where to assign the registry (string)
        :param pulumi.Input[Sequence[pulumi.Input['RegistryRegistryArgs']]] registries: Registries data for registry (list)
        """
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace_id is not None:
            pulumi.set(__self__, "namespace_id", namespace_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if registries is not None:
            pulumi.set(__self__, "registries", registries)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Annotations for Registry object (map)
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A registry description (string)
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Labels for Registry object (map)
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the registry (string)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace id where to assign the namespaced registry (string)
        """
        return pulumi.get(self, "namespace_id")

    @namespace_id.setter
    def namespace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The project id where to assign the registry (string)
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def registries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RegistryRegistryArgs']]]]:
        """
        Registries data for registry (list)
        """
        return pulumi.get(self, "registries")

    @registries.setter
    def registries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RegistryRegistryArgs']]]]):
        pulumi.set(self, "registries", value)


class Registry(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 registries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegistryRegistryArgs']]]]] = None,
                 __props__=None):
        """
        Provides a Rancher v2 Registry resource. This resource creates Kubernetes secrets with the type `kubernetes.io/dockerconfigjson` for authenticating against Docker registries for Rancher v2 environments and retrieving their information.

        Depending on the availability, there are 2 types of Rancher v2 Docker registry resources:
        - Project registry resource: Available to all namespaces in the `project_id`.
        - Namespaced registry resource: Available to `namespace_id` in the `project_id`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_rancher2 as rancher2

        # Create a new rancher2 Project Registry
        foo = rancher2.Registry("foo",
            name="foo",
            description="Terraform registry foo",
            project_id="<project_id>",
            registries=[rancher2.RegistryRegistryArgs(
                address="test.io",
                username="user",
                password="pass",
            )])
        ```

        ```python
        import pulumi
        import pulumi_rancher2 as rancher2

        # Create a new rancher2 Namespaced Registry
        foo = rancher2.Registry("foo",
            name="foo",
            description="Terraform registry foo",
            project_id="<project_id>",
            namespace_id="<namespace_id>",
            registries=[rancher2.RegistryRegistryArgs(
                address="test.io",
                username="user2",
                password="pass",
            )])
        ```

        ## Import

        Registries can be imported using the registry ID in the format `<namespace_id>.<project_id>.<registry_id>`

        ```sh
        $ pulumi import rancher2:index/registry:Registry foo &lt;namespace_id&gt;.&lt;project_id&gt;.&lt;registry_id&gt;
        ```
        `<namespace_id>` is optional, just needed for namespaced registry.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations for Registry object (map)
        :param pulumi.Input[str] description: A registry description (string)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels for Registry object (map)
        :param pulumi.Input[str] name: The name of the registry (string)
        :param pulumi.Input[str] namespace_id: The namespace id where to assign the namespaced registry (string)
        :param pulumi.Input[str] project_id: The project id where to assign the registry (string)
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegistryRegistryArgs']]]] registries: Registries data for registry (list)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegistryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Rancher v2 Registry resource. This resource creates Kubernetes secrets with the type `kubernetes.io/dockerconfigjson` for authenticating against Docker registries for Rancher v2 environments and retrieving their information.

        Depending on the availability, there are 2 types of Rancher v2 Docker registry resources:
        - Project registry resource: Available to all namespaces in the `project_id`.
        - Namespaced registry resource: Available to `namespace_id` in the `project_id`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_rancher2 as rancher2

        # Create a new rancher2 Project Registry
        foo = rancher2.Registry("foo",
            name="foo",
            description="Terraform registry foo",
            project_id="<project_id>",
            registries=[rancher2.RegistryRegistryArgs(
                address="test.io",
                username="user",
                password="pass",
            )])
        ```

        ```python
        import pulumi
        import pulumi_rancher2 as rancher2

        # Create a new rancher2 Namespaced Registry
        foo = rancher2.Registry("foo",
            name="foo",
            description="Terraform registry foo",
            project_id="<project_id>",
            namespace_id="<namespace_id>",
            registries=[rancher2.RegistryRegistryArgs(
                address="test.io",
                username="user2",
                password="pass",
            )])
        ```

        ## Import

        Registries can be imported using the registry ID in the format `<namespace_id>.<project_id>.<registry_id>`

        ```sh
        $ pulumi import rancher2:index/registry:Registry foo &lt;namespace_id&gt;.&lt;project_id&gt;.&lt;registry_id&gt;
        ```
        `<namespace_id>` is optional, just needed for namespaced registry.

        :param str resource_name: The name of the resource.
        :param RegistryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegistryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 registries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegistryRegistryArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegistryArgs.__new__(RegistryArgs)

            __props__.__dict__["annotations"] = annotations
            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            __props__.__dict__["namespace_id"] = namespace_id
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            if registries is None and not opts.urn:
                raise TypeError("Missing required property 'registries'")
            __props__.__dict__["registries"] = registries
        super(Registry, __self__).__init__(
            'rancher2:index/registry:Registry',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            registries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegistryRegistryArgs']]]]] = None) -> 'Registry':
        """
        Get an existing Registry resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations for Registry object (map)
        :param pulumi.Input[str] description: A registry description (string)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels for Registry object (map)
        :param pulumi.Input[str] name: The name of the registry (string)
        :param pulumi.Input[str] namespace_id: The namespace id where to assign the namespaced registry (string)
        :param pulumi.Input[str] project_id: The project id where to assign the registry (string)
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegistryRegistryArgs']]]] registries: Registries data for registry (list)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RegistryState.__new__(_RegistryState)

        __props__.__dict__["annotations"] = annotations
        __props__.__dict__["description"] = description
        __props__.__dict__["labels"] = labels
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace_id"] = namespace_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["registries"] = registries
        return Registry(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Annotations for Registry object (map)
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A registry description (string)
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Labels for Registry object (map)
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the registry (string)
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> pulumi.Output[Optional[str]]:
        """
        The namespace id where to assign the namespaced registry (string)
        """
        return pulumi.get(self, "namespace_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The project id where to assign the registry (string)
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def registries(self) -> pulumi.Output[Sequence['outputs.RegistryRegistry']]:
        """
        Registries data for registry (list)
        """
        return pulumi.get(self, "registries")

