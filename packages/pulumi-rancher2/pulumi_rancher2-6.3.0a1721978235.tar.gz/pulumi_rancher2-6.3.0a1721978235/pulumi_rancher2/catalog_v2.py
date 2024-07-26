# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CatalogV2Args', 'CatalogV2']

@pulumi.input_type
class CatalogV2Args:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 ca_bundle: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 git_branch: Optional[pulumi.Input[str]] = None,
                 git_repo: Optional[pulumi.Input[str]] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 secret_name: Optional[pulumi.Input[str]] = None,
                 secret_namespace: Optional[pulumi.Input[str]] = None,
                 service_account: Optional[pulumi.Input[str]] = None,
                 service_account_namespace: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CatalogV2 resource.
        :param pulumi.Input[str] cluster_id: The cluster id of the catalog V2 (string)
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations for the catalog v2 (map)
        :param pulumi.Input[str] ca_bundle: CA certificate in base64-encoded DER format which will be used to validate the repo's certificate (string)
        :param pulumi.Input[bool] enabled: If disabled the repo clone will not be updated or allowed to be installed from. Default: `true` (bool)
        :param pulumi.Input[str] git_branch: Git Repository branch containing Helm chart definitions. Default `master` (string)
        :param pulumi.Input[str] git_repo: The url of the catalog v2 repo. Conflicts with `url` (string)
        :param pulumi.Input[bool] insecure: Use insecure HTTPS to download the repo's index. Default: `false` (bool)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels for the catalog v2 (map)
        :param pulumi.Input[str] name: The name of the catalog v2 (string)
        :param pulumi.Input[str] secret_name: K8s secret name to be used to connect to the repo (string)
        :param pulumi.Input[str] secret_namespace: K8s secret namespace (string)
        :param pulumi.Input[str] service_account: K8s service account used to deploy charts instead of the end users credentials (string)
        :param pulumi.Input[str] service_account_namespace: The username to access the catalog if needed (string)
        :param pulumi.Input[str] url: URL to an index generated by Helm. Conflicts with `git_repo` (string)
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if ca_bundle is not None:
            pulumi.set(__self__, "ca_bundle", ca_bundle)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if git_branch is not None:
            pulumi.set(__self__, "git_branch", git_branch)
        if git_repo is not None:
            pulumi.set(__self__, "git_repo", git_repo)
        if insecure is not None:
            pulumi.set(__self__, "insecure", insecure)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if secret_name is not None:
            pulumi.set(__self__, "secret_name", secret_name)
        if secret_namespace is not None:
            pulumi.set(__self__, "secret_namespace", secret_namespace)
        if service_account is not None:
            pulumi.set(__self__, "service_account", service_account)
        if service_account_namespace is not None:
            pulumi.set(__self__, "service_account_namespace", service_account_namespace)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The cluster id of the catalog V2 (string)
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Annotations for the catalog v2 (map)
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter(name="caBundle")
    def ca_bundle(self) -> Optional[pulumi.Input[str]]:
        """
        CA certificate in base64-encoded DER format which will be used to validate the repo's certificate (string)
        """
        return pulumi.get(self, "ca_bundle")

    @ca_bundle.setter
    def ca_bundle(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ca_bundle", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If disabled the repo clone will not be updated or allowed to be installed from. Default: `true` (bool)
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="gitBranch")
    def git_branch(self) -> Optional[pulumi.Input[str]]:
        """
        Git Repository branch containing Helm chart definitions. Default `master` (string)
        """
        return pulumi.get(self, "git_branch")

    @git_branch.setter
    def git_branch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "git_branch", value)

    @property
    @pulumi.getter(name="gitRepo")
    def git_repo(self) -> Optional[pulumi.Input[str]]:
        """
        The url of the catalog v2 repo. Conflicts with `url` (string)
        """
        return pulumi.get(self, "git_repo")

    @git_repo.setter
    def git_repo(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "git_repo", value)

    @property
    @pulumi.getter
    def insecure(self) -> Optional[pulumi.Input[bool]]:
        """
        Use insecure HTTPS to download the repo's index. Default: `false` (bool)
        """
        return pulumi.get(self, "insecure")

    @insecure.setter
    def insecure(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "insecure", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Labels for the catalog v2 (map)
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the catalog v2 (string)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> Optional[pulumi.Input[str]]:
        """
        K8s secret name to be used to connect to the repo (string)
        """
        return pulumi.get(self, "secret_name")

    @secret_name.setter
    def secret_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_name", value)

    @property
    @pulumi.getter(name="secretNamespace")
    def secret_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        K8s secret namespace (string)
        """
        return pulumi.get(self, "secret_namespace")

    @secret_namespace.setter
    def secret_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_namespace", value)

    @property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[str]]:
        """
        K8s service account used to deploy charts instead of the end users credentials (string)
        """
        return pulumi.get(self, "service_account")

    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account", value)

    @property
    @pulumi.getter(name="serviceAccountNamespace")
    def service_account_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The username to access the catalog if needed (string)
        """
        return pulumi.get(self, "service_account_namespace")

    @service_account_namespace.setter
    def service_account_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account_namespace", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        URL to an index generated by Helm. Conflicts with `git_repo` (string)
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


@pulumi.input_type
class _CatalogV2State:
    def __init__(__self__, *,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 ca_bundle: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 git_branch: Optional[pulumi.Input[str]] = None,
                 git_repo: Optional[pulumi.Input[str]] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_version: Optional[pulumi.Input[str]] = None,
                 secret_name: Optional[pulumi.Input[str]] = None,
                 secret_namespace: Optional[pulumi.Input[str]] = None,
                 service_account: Optional[pulumi.Input[str]] = None,
                 service_account_namespace: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CatalogV2 resources.
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations for the catalog v2 (map)
        :param pulumi.Input[str] ca_bundle: CA certificate in base64-encoded DER format which will be used to validate the repo's certificate (string)
        :param pulumi.Input[str] cluster_id: The cluster id of the catalog V2 (string)
        :param pulumi.Input[bool] enabled: If disabled the repo clone will not be updated or allowed to be installed from. Default: `true` (bool)
        :param pulumi.Input[str] git_branch: Git Repository branch containing Helm chart definitions. Default `master` (string)
        :param pulumi.Input[str] git_repo: The url of the catalog v2 repo. Conflicts with `url` (string)
        :param pulumi.Input[bool] insecure: Use insecure HTTPS to download the repo's index. Default: `false` (bool)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels for the catalog v2 (map)
        :param pulumi.Input[str] name: The name of the catalog v2 (string)
        :param pulumi.Input[str] resource_version: (Computed) The k8s resource version (string)
        :param pulumi.Input[str] secret_name: K8s secret name to be used to connect to the repo (string)
        :param pulumi.Input[str] secret_namespace: K8s secret namespace (string)
        :param pulumi.Input[str] service_account: K8s service account used to deploy charts instead of the end users credentials (string)
        :param pulumi.Input[str] service_account_namespace: The username to access the catalog if needed (string)
        :param pulumi.Input[str] url: URL to an index generated by Helm. Conflicts with `git_repo` (string)
        """
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if ca_bundle is not None:
            pulumi.set(__self__, "ca_bundle", ca_bundle)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if git_branch is not None:
            pulumi.set(__self__, "git_branch", git_branch)
        if git_repo is not None:
            pulumi.set(__self__, "git_repo", git_repo)
        if insecure is not None:
            pulumi.set(__self__, "insecure", insecure)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_version is not None:
            pulumi.set(__self__, "resource_version", resource_version)
        if secret_name is not None:
            pulumi.set(__self__, "secret_name", secret_name)
        if secret_namespace is not None:
            pulumi.set(__self__, "secret_namespace", secret_namespace)
        if service_account is not None:
            pulumi.set(__self__, "service_account", service_account)
        if service_account_namespace is not None:
            pulumi.set(__self__, "service_account_namespace", service_account_namespace)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Annotations for the catalog v2 (map)
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter(name="caBundle")
    def ca_bundle(self) -> Optional[pulumi.Input[str]]:
        """
        CA certificate in base64-encoded DER format which will be used to validate the repo's certificate (string)
        """
        return pulumi.get(self, "ca_bundle")

    @ca_bundle.setter
    def ca_bundle(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ca_bundle", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The cluster id of the catalog V2 (string)
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If disabled the repo clone will not be updated or allowed to be installed from. Default: `true` (bool)
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="gitBranch")
    def git_branch(self) -> Optional[pulumi.Input[str]]:
        """
        Git Repository branch containing Helm chart definitions. Default `master` (string)
        """
        return pulumi.get(self, "git_branch")

    @git_branch.setter
    def git_branch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "git_branch", value)

    @property
    @pulumi.getter(name="gitRepo")
    def git_repo(self) -> Optional[pulumi.Input[str]]:
        """
        The url of the catalog v2 repo. Conflicts with `url` (string)
        """
        return pulumi.get(self, "git_repo")

    @git_repo.setter
    def git_repo(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "git_repo", value)

    @property
    @pulumi.getter
    def insecure(self) -> Optional[pulumi.Input[bool]]:
        """
        Use insecure HTTPS to download the repo's index. Default: `false` (bool)
        """
        return pulumi.get(self, "insecure")

    @insecure.setter
    def insecure(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "insecure", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Labels for the catalog v2 (map)
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the catalog v2 (string)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> Optional[pulumi.Input[str]]:
        """
        (Computed) The k8s resource version (string)
        """
        return pulumi.get(self, "resource_version")

    @resource_version.setter
    def resource_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_version", value)

    @property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> Optional[pulumi.Input[str]]:
        """
        K8s secret name to be used to connect to the repo (string)
        """
        return pulumi.get(self, "secret_name")

    @secret_name.setter
    def secret_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_name", value)

    @property
    @pulumi.getter(name="secretNamespace")
    def secret_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        K8s secret namespace (string)
        """
        return pulumi.get(self, "secret_namespace")

    @secret_namespace.setter
    def secret_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_namespace", value)

    @property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[str]]:
        """
        K8s service account used to deploy charts instead of the end users credentials (string)
        """
        return pulumi.get(self, "service_account")

    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account", value)

    @property
    @pulumi.getter(name="serviceAccountNamespace")
    def service_account_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The username to access the catalog if needed (string)
        """
        return pulumi.get(self, "service_account_namespace")

    @service_account_namespace.setter
    def service_account_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account_namespace", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        URL to an index generated by Helm. Conflicts with `git_repo` (string)
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class CatalogV2(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 ca_bundle: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 git_branch: Optional[pulumi.Input[str]] = None,
                 git_repo: Optional[pulumi.Input[str]] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 secret_name: Optional[pulumi.Input[str]] = None,
                 secret_namespace: Optional[pulumi.Input[str]] = None,
                 service_account: Optional[pulumi.Input[str]] = None,
                 service_account_namespace: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Rancher Catalog v2 resource. This can be used to create cluster helm catalogs for Rancher v2 environments and retrieve their information. Catalog v2 resource is available at Rancher v2.5.x and above.

        ## Import

        V2 catalogs can be imported using the Rancher cluster ID and Catalog V2 name.

        ```sh
        $ pulumi import rancher2:index/catalogV2:CatalogV2 foo &lt;CLUSTER_ID&gt;.&lt;CATALOG_V2_NAME&gt;
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations for the catalog v2 (map)
        :param pulumi.Input[str] ca_bundle: CA certificate in base64-encoded DER format which will be used to validate the repo's certificate (string)
        :param pulumi.Input[str] cluster_id: The cluster id of the catalog V2 (string)
        :param pulumi.Input[bool] enabled: If disabled the repo clone will not be updated or allowed to be installed from. Default: `true` (bool)
        :param pulumi.Input[str] git_branch: Git Repository branch containing Helm chart definitions. Default `master` (string)
        :param pulumi.Input[str] git_repo: The url of the catalog v2 repo. Conflicts with `url` (string)
        :param pulumi.Input[bool] insecure: Use insecure HTTPS to download the repo's index. Default: `false` (bool)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels for the catalog v2 (map)
        :param pulumi.Input[str] name: The name of the catalog v2 (string)
        :param pulumi.Input[str] secret_name: K8s secret name to be used to connect to the repo (string)
        :param pulumi.Input[str] secret_namespace: K8s secret namespace (string)
        :param pulumi.Input[str] service_account: K8s service account used to deploy charts instead of the end users credentials (string)
        :param pulumi.Input[str] service_account_namespace: The username to access the catalog if needed (string)
        :param pulumi.Input[str] url: URL to an index generated by Helm. Conflicts with `git_repo` (string)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CatalogV2Args,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Rancher Catalog v2 resource. This can be used to create cluster helm catalogs for Rancher v2 environments and retrieve their information. Catalog v2 resource is available at Rancher v2.5.x and above.

        ## Import

        V2 catalogs can be imported using the Rancher cluster ID and Catalog V2 name.

        ```sh
        $ pulumi import rancher2:index/catalogV2:CatalogV2 foo &lt;CLUSTER_ID&gt;.&lt;CATALOG_V2_NAME&gt;
        ```

        :param str resource_name: The name of the resource.
        :param CatalogV2Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CatalogV2Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 ca_bundle: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 git_branch: Optional[pulumi.Input[str]] = None,
                 git_repo: Optional[pulumi.Input[str]] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 secret_name: Optional[pulumi.Input[str]] = None,
                 secret_namespace: Optional[pulumi.Input[str]] = None,
                 service_account: Optional[pulumi.Input[str]] = None,
                 service_account_namespace: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CatalogV2Args.__new__(CatalogV2Args)

            __props__.__dict__["annotations"] = annotations
            __props__.__dict__["ca_bundle"] = ca_bundle
            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["git_branch"] = git_branch
            __props__.__dict__["git_repo"] = git_repo
            __props__.__dict__["insecure"] = insecure
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            __props__.__dict__["secret_name"] = secret_name
            __props__.__dict__["secret_namespace"] = secret_namespace
            __props__.__dict__["service_account"] = service_account
            __props__.__dict__["service_account_namespace"] = service_account_namespace
            __props__.__dict__["url"] = url
            __props__.__dict__["resource_version"] = None
        super(CatalogV2, __self__).__init__(
            'rancher2:index/catalogV2:CatalogV2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            ca_bundle: Optional[pulumi.Input[str]] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            git_branch: Optional[pulumi.Input[str]] = None,
            git_repo: Optional[pulumi.Input[str]] = None,
            insecure: Optional[pulumi.Input[bool]] = None,
            labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_version: Optional[pulumi.Input[str]] = None,
            secret_name: Optional[pulumi.Input[str]] = None,
            secret_namespace: Optional[pulumi.Input[str]] = None,
            service_account: Optional[pulumi.Input[str]] = None,
            service_account_namespace: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'CatalogV2':
        """
        Get an existing CatalogV2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations for the catalog v2 (map)
        :param pulumi.Input[str] ca_bundle: CA certificate in base64-encoded DER format which will be used to validate the repo's certificate (string)
        :param pulumi.Input[str] cluster_id: The cluster id of the catalog V2 (string)
        :param pulumi.Input[bool] enabled: If disabled the repo clone will not be updated or allowed to be installed from. Default: `true` (bool)
        :param pulumi.Input[str] git_branch: Git Repository branch containing Helm chart definitions. Default `master` (string)
        :param pulumi.Input[str] git_repo: The url of the catalog v2 repo. Conflicts with `url` (string)
        :param pulumi.Input[bool] insecure: Use insecure HTTPS to download the repo's index. Default: `false` (bool)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels for the catalog v2 (map)
        :param pulumi.Input[str] name: The name of the catalog v2 (string)
        :param pulumi.Input[str] resource_version: (Computed) The k8s resource version (string)
        :param pulumi.Input[str] secret_name: K8s secret name to be used to connect to the repo (string)
        :param pulumi.Input[str] secret_namespace: K8s secret namespace (string)
        :param pulumi.Input[str] service_account: K8s service account used to deploy charts instead of the end users credentials (string)
        :param pulumi.Input[str] service_account_namespace: The username to access the catalog if needed (string)
        :param pulumi.Input[str] url: URL to an index generated by Helm. Conflicts with `git_repo` (string)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CatalogV2State.__new__(_CatalogV2State)

        __props__.__dict__["annotations"] = annotations
        __props__.__dict__["ca_bundle"] = ca_bundle
        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["git_branch"] = git_branch
        __props__.__dict__["git_repo"] = git_repo
        __props__.__dict__["insecure"] = insecure
        __props__.__dict__["labels"] = labels
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_version"] = resource_version
        __props__.__dict__["secret_name"] = secret_name
        __props__.__dict__["secret_namespace"] = secret_namespace
        __props__.__dict__["service_account"] = service_account
        __props__.__dict__["service_account_namespace"] = service_account_namespace
        __props__.__dict__["url"] = url
        return CatalogV2(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Annotations for the catalog v2 (map)
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="caBundle")
    def ca_bundle(self) -> pulumi.Output[Optional[str]]:
        """
        CA certificate in base64-encoded DER format which will be used to validate the repo's certificate (string)
        """
        return pulumi.get(self, "ca_bundle")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The cluster id of the catalog V2 (string)
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        If disabled the repo clone will not be updated or allowed to be installed from. Default: `true` (bool)
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="gitBranch")
    def git_branch(self) -> pulumi.Output[str]:
        """
        Git Repository branch containing Helm chart definitions. Default `master` (string)
        """
        return pulumi.get(self, "git_branch")

    @property
    @pulumi.getter(name="gitRepo")
    def git_repo(self) -> pulumi.Output[Optional[str]]:
        """
        The url of the catalog v2 repo. Conflicts with `url` (string)
        """
        return pulumi.get(self, "git_repo")

    @property
    @pulumi.getter
    def insecure(self) -> pulumi.Output[Optional[bool]]:
        """
        Use insecure HTTPS to download the repo's index. Default: `false` (bool)
        """
        return pulumi.get(self, "insecure")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Labels for the catalog v2 (map)
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the catalog v2 (string)
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> pulumi.Output[str]:
        """
        (Computed) The k8s resource version (string)
        """
        return pulumi.get(self, "resource_version")

    @property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Output[Optional[str]]:
        """
        K8s secret name to be used to connect to the repo (string)
        """
        return pulumi.get(self, "secret_name")

    @property
    @pulumi.getter(name="secretNamespace")
    def secret_namespace(self) -> pulumi.Output[Optional[str]]:
        """
        K8s secret namespace (string)
        """
        return pulumi.get(self, "secret_namespace")

    @property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[Optional[str]]:
        """
        K8s service account used to deploy charts instead of the end users credentials (string)
        """
        return pulumi.get(self, "service_account")

    @property
    @pulumi.getter(name="serviceAccountNamespace")
    def service_account_namespace(self) -> pulumi.Output[Optional[str]]:
        """
        The username to access the catalog if needed (string)
        """
        return pulumi.get(self, "service_account_namespace")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[Optional[str]]:
        """
        URL to an index generated by Helm. Conflicts with `git_repo` (string)
        """
        return pulumi.get(self, "url")

