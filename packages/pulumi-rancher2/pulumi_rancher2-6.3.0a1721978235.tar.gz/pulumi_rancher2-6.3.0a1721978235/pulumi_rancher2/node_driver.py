# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['NodeDriverArgs', 'NodeDriver']

@pulumi.input_type
class NodeDriverArgs:
    def __init__(__self__, *,
                 active: pulumi.Input[bool],
                 builtin: pulumi.Input[bool],
                 url: pulumi.Input[str],
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 checksum: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ui_url: Optional[pulumi.Input[str]] = None,
                 whitelist_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NodeDriver resource.
        :param pulumi.Input[bool] active: Specify if the node driver state (bool)
        :param pulumi.Input[bool] builtin: Specify wheter the node driver is an internal node driver or not (bool)
        :param pulumi.Input[str] url: The URL to download the machine driver binary for 64-bit Linux (string)
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations of the resource (map)
        :param pulumi.Input[str] checksum: Verify that the downloaded driver matches the expected checksum (string)
        :param pulumi.Input[str] description: Description of the node driver (string)
        :param pulumi.Input[str] external_id: External ID (string)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels of the resource (map)
        :param pulumi.Input[str] name: Name of the node driver (string)
        :param pulumi.Input[str] ui_url: The URL to load for customized Add Nodes screen for this driver (string)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] whitelist_domains: Domains to whitelist for the ui (list)
        """
        pulumi.set(__self__, "active", active)
        pulumi.set(__self__, "builtin", builtin)
        pulumi.set(__self__, "url", url)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if checksum is not None:
            pulumi.set(__self__, "checksum", checksum)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ui_url is not None:
            pulumi.set(__self__, "ui_url", ui_url)
        if whitelist_domains is not None:
            pulumi.set(__self__, "whitelist_domains", whitelist_domains)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Input[bool]:
        """
        Specify if the node driver state (bool)
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: pulumi.Input[bool]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter
    def builtin(self) -> pulumi.Input[bool]:
        """
        Specify wheter the node driver is an internal node driver or not (bool)
        """
        return pulumi.get(self, "builtin")

    @builtin.setter
    def builtin(self, value: pulumi.Input[bool]):
        pulumi.set(self, "builtin", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        The URL to download the machine driver binary for 64-bit Linux (string)
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Annotations of the resource (map)
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter
    def checksum(self) -> Optional[pulumi.Input[str]]:
        """
        Verify that the downloaded driver matches the expected checksum (string)
        """
        return pulumi.get(self, "checksum")

    @checksum.setter
    def checksum(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "checksum", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the node driver (string)
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[str]]:
        """
        External ID (string)
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Labels of the resource (map)
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the node driver (string)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="uiUrl")
    def ui_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL to load for customized Add Nodes screen for this driver (string)
        """
        return pulumi.get(self, "ui_url")

    @ui_url.setter
    def ui_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ui_url", value)

    @property
    @pulumi.getter(name="whitelistDomains")
    def whitelist_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Domains to whitelist for the ui (list)
        """
        return pulumi.get(self, "whitelist_domains")

    @whitelist_domains.setter
    def whitelist_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "whitelist_domains", value)


@pulumi.input_type
class _NodeDriverState:
    def __init__(__self__, *,
                 active: Optional[pulumi.Input[bool]] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 builtin: Optional[pulumi.Input[bool]] = None,
                 checksum: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ui_url: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 whitelist_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering NodeDriver resources.
        :param pulumi.Input[bool] active: Specify if the node driver state (bool)
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations of the resource (map)
        :param pulumi.Input[bool] builtin: Specify wheter the node driver is an internal node driver or not (bool)
        :param pulumi.Input[str] checksum: Verify that the downloaded driver matches the expected checksum (string)
        :param pulumi.Input[str] description: Description of the node driver (string)
        :param pulumi.Input[str] external_id: External ID (string)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels of the resource (map)
        :param pulumi.Input[str] name: Name of the node driver (string)
        :param pulumi.Input[str] ui_url: The URL to load for customized Add Nodes screen for this driver (string)
        :param pulumi.Input[str] url: The URL to download the machine driver binary for 64-bit Linux (string)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] whitelist_domains: Domains to whitelist for the ui (list)
        """
        if active is not None:
            pulumi.set(__self__, "active", active)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if builtin is not None:
            pulumi.set(__self__, "builtin", builtin)
        if checksum is not None:
            pulumi.set(__self__, "checksum", checksum)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ui_url is not None:
            pulumi.set(__self__, "ui_url", ui_url)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if whitelist_domains is not None:
            pulumi.set(__self__, "whitelist_domains", whitelist_domains)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        """
        Specify if the node driver state (bool)
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Annotations of the resource (map)
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter
    def builtin(self) -> Optional[pulumi.Input[bool]]:
        """
        Specify wheter the node driver is an internal node driver or not (bool)
        """
        return pulumi.get(self, "builtin")

    @builtin.setter
    def builtin(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "builtin", value)

    @property
    @pulumi.getter
    def checksum(self) -> Optional[pulumi.Input[str]]:
        """
        Verify that the downloaded driver matches the expected checksum (string)
        """
        return pulumi.get(self, "checksum")

    @checksum.setter
    def checksum(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "checksum", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the node driver (string)
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[str]]:
        """
        External ID (string)
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Labels of the resource (map)
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the node driver (string)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="uiUrl")
    def ui_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL to load for customized Add Nodes screen for this driver (string)
        """
        return pulumi.get(self, "ui_url")

    @ui_url.setter
    def ui_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ui_url", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL to download the machine driver binary for 64-bit Linux (string)
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="whitelistDomains")
    def whitelist_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Domains to whitelist for the ui (list)
        """
        return pulumi.get(self, "whitelist_domains")

    @whitelist_domains.setter
    def whitelist_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "whitelist_domains", value)


class NodeDriver(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 builtin: Optional[pulumi.Input[bool]] = None,
                 checksum: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ui_url: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 whitelist_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a Rancher v2 Node Driver resource. This can be used to create Node Driver for Rancher v2 RKE clusters and retrieve their information.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_rancher2 as rancher2

        # Create a new rancher2 Node Driver
        foo = rancher2.NodeDriver("foo",
            active=True,
            builtin=False,
            checksum="0x0",
            description="Foo description",
            external_id="foo_external",
            name="foo",
            ui_url="local://ui",
            url="local://",
            whitelist_domains=["*.foo.com"])
        ```

        ## Import

        Node Driver can be imported using the Rancher Node Driver ID

        ```sh
        $ pulumi import rancher2:index/nodeDriver:NodeDriver foo &lt;node_driver_id&gt;
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Specify if the node driver state (bool)
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations of the resource (map)
        :param pulumi.Input[bool] builtin: Specify wheter the node driver is an internal node driver or not (bool)
        :param pulumi.Input[str] checksum: Verify that the downloaded driver matches the expected checksum (string)
        :param pulumi.Input[str] description: Description of the node driver (string)
        :param pulumi.Input[str] external_id: External ID (string)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels of the resource (map)
        :param pulumi.Input[str] name: Name of the node driver (string)
        :param pulumi.Input[str] ui_url: The URL to load for customized Add Nodes screen for this driver (string)
        :param pulumi.Input[str] url: The URL to download the machine driver binary for 64-bit Linux (string)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] whitelist_domains: Domains to whitelist for the ui (list)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NodeDriverArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Rancher v2 Node Driver resource. This can be used to create Node Driver for Rancher v2 RKE clusters and retrieve their information.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_rancher2 as rancher2

        # Create a new rancher2 Node Driver
        foo = rancher2.NodeDriver("foo",
            active=True,
            builtin=False,
            checksum="0x0",
            description="Foo description",
            external_id="foo_external",
            name="foo",
            ui_url="local://ui",
            url="local://",
            whitelist_domains=["*.foo.com"])
        ```

        ## Import

        Node Driver can be imported using the Rancher Node Driver ID

        ```sh
        $ pulumi import rancher2:index/nodeDriver:NodeDriver foo &lt;node_driver_id&gt;
        ```

        :param str resource_name: The name of the resource.
        :param NodeDriverArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NodeDriverArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 builtin: Optional[pulumi.Input[bool]] = None,
                 checksum: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ui_url: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 whitelist_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NodeDriverArgs.__new__(NodeDriverArgs)

            if active is None and not opts.urn:
                raise TypeError("Missing required property 'active'")
            __props__.__dict__["active"] = active
            __props__.__dict__["annotations"] = annotations
            if builtin is None and not opts.urn:
                raise TypeError("Missing required property 'builtin'")
            __props__.__dict__["builtin"] = builtin
            __props__.__dict__["checksum"] = checksum
            __props__.__dict__["description"] = description
            __props__.__dict__["external_id"] = external_id
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            __props__.__dict__["ui_url"] = ui_url
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
            __props__.__dict__["whitelist_domains"] = whitelist_domains
        super(NodeDriver, __self__).__init__(
            'rancher2:index/nodeDriver:NodeDriver',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active: Optional[pulumi.Input[bool]] = None,
            annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            builtin: Optional[pulumi.Input[bool]] = None,
            checksum: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            external_id: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            ui_url: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None,
            whitelist_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'NodeDriver':
        """
        Get an existing NodeDriver resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Specify if the node driver state (bool)
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations of the resource (map)
        :param pulumi.Input[bool] builtin: Specify wheter the node driver is an internal node driver or not (bool)
        :param pulumi.Input[str] checksum: Verify that the downloaded driver matches the expected checksum (string)
        :param pulumi.Input[str] description: Description of the node driver (string)
        :param pulumi.Input[str] external_id: External ID (string)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels of the resource (map)
        :param pulumi.Input[str] name: Name of the node driver (string)
        :param pulumi.Input[str] ui_url: The URL to load for customized Add Nodes screen for this driver (string)
        :param pulumi.Input[str] url: The URL to download the machine driver binary for 64-bit Linux (string)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] whitelist_domains: Domains to whitelist for the ui (list)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NodeDriverState.__new__(_NodeDriverState)

        __props__.__dict__["active"] = active
        __props__.__dict__["annotations"] = annotations
        __props__.__dict__["builtin"] = builtin
        __props__.__dict__["checksum"] = checksum
        __props__.__dict__["description"] = description
        __props__.__dict__["external_id"] = external_id
        __props__.__dict__["labels"] = labels
        __props__.__dict__["name"] = name
        __props__.__dict__["ui_url"] = ui_url
        __props__.__dict__["url"] = url
        __props__.__dict__["whitelist_domains"] = whitelist_domains
        return NodeDriver(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Output[bool]:
        """
        Specify if the node driver state (bool)
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Annotations of the resource (map)
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter
    def builtin(self) -> pulumi.Output[bool]:
        """
        Specify wheter the node driver is an internal node driver or not (bool)
        """
        return pulumi.get(self, "builtin")

    @property
    @pulumi.getter
    def checksum(self) -> pulumi.Output[Optional[str]]:
        """
        Verify that the downloaded driver matches the expected checksum (string)
        """
        return pulumi.get(self, "checksum")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the node driver (string)
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[Optional[str]]:
        """
        External ID (string)
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Labels of the resource (map)
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the node driver (string)
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="uiUrl")
    def ui_url(self) -> pulumi.Output[Optional[str]]:
        """
        The URL to load for customized Add Nodes screen for this driver (string)
        """
        return pulumi.get(self, "ui_url")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The URL to download the machine driver binary for 64-bit Linux (string)
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter(name="whitelistDomains")
    def whitelist_domains(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Domains to whitelist for the ui (list)
        """
        return pulumi.get(self, "whitelist_domains")

