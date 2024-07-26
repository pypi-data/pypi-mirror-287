# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['EntityAliasArgs', 'EntityAlias']

@pulumi.input_type
class EntityAliasArgs:
    def __init__(__self__, *,
                 canonical_id: pulumi.Input[str],
                 mount_accessor: pulumi.Input[str],
                 custom_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EntityAlias resource.
        :param pulumi.Input[str] canonical_id: Entity ID to which this alias belongs to.
        :param pulumi.Input[str] mount_accessor: Accessor of the mount to which the alias should belong to.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_metadata: Custom metadata to be associated with this alias.
        :param pulumi.Input[str] name: Name of the alias. Name should be the identifier of the client in the authentication source. For example, if the alias belongs to userpass backend, the name should be a valid username within userpass backend. If alias belongs to GitHub, it should be the GitHub username.
        :param pulumi.Input[str] namespace: The namespace to provision the resource in.
               The value should not contain leading or trailing forward slashes.
               The `namespace` is always relative to the provider's configured [namespace](https://www.terraform.io/docs/providers/vault/index.html#namespace).
               *Available only for Vault Enterprise*.
        """
        pulumi.set(__self__, "canonical_id", canonical_id)
        pulumi.set(__self__, "mount_accessor", mount_accessor)
        if custom_metadata is not None:
            pulumi.set(__self__, "custom_metadata", custom_metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter(name="canonicalId")
    def canonical_id(self) -> pulumi.Input[str]:
        """
        Entity ID to which this alias belongs to.
        """
        return pulumi.get(self, "canonical_id")

    @canonical_id.setter
    def canonical_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "canonical_id", value)

    @property
    @pulumi.getter(name="mountAccessor")
    def mount_accessor(self) -> pulumi.Input[str]:
        """
        Accessor of the mount to which the alias should belong to.
        """
        return pulumi.get(self, "mount_accessor")

    @mount_accessor.setter
    def mount_accessor(self, value: pulumi.Input[str]):
        pulumi.set(self, "mount_accessor", value)

    @property
    @pulumi.getter(name="customMetadata")
    def custom_metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Custom metadata to be associated with this alias.
        """
        return pulumi.get(self, "custom_metadata")

    @custom_metadata.setter
    def custom_metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "custom_metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the alias. Name should be the identifier of the client in the authentication source. For example, if the alias belongs to userpass backend, the name should be a valid username within userpass backend. If alias belongs to GitHub, it should be the GitHub username.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace to provision the resource in.
        The value should not contain leading or trailing forward slashes.
        The `namespace` is always relative to the provider's configured [namespace](https://www.terraform.io/docs/providers/vault/index.html#namespace).
        *Available only for Vault Enterprise*.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)


@pulumi.input_type
class _EntityAliasState:
    def __init__(__self__, *,
                 canonical_id: Optional[pulumi.Input[str]] = None,
                 custom_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 mount_accessor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering EntityAlias resources.
        :param pulumi.Input[str] canonical_id: Entity ID to which this alias belongs to.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_metadata: Custom metadata to be associated with this alias.
        :param pulumi.Input[str] mount_accessor: Accessor of the mount to which the alias should belong to.
        :param pulumi.Input[str] name: Name of the alias. Name should be the identifier of the client in the authentication source. For example, if the alias belongs to userpass backend, the name should be a valid username within userpass backend. If alias belongs to GitHub, it should be the GitHub username.
        :param pulumi.Input[str] namespace: The namespace to provision the resource in.
               The value should not contain leading or trailing forward slashes.
               The `namespace` is always relative to the provider's configured [namespace](https://www.terraform.io/docs/providers/vault/index.html#namespace).
               *Available only for Vault Enterprise*.
        """
        if canonical_id is not None:
            pulumi.set(__self__, "canonical_id", canonical_id)
        if custom_metadata is not None:
            pulumi.set(__self__, "custom_metadata", custom_metadata)
        if mount_accessor is not None:
            pulumi.set(__self__, "mount_accessor", mount_accessor)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter(name="canonicalId")
    def canonical_id(self) -> Optional[pulumi.Input[str]]:
        """
        Entity ID to which this alias belongs to.
        """
        return pulumi.get(self, "canonical_id")

    @canonical_id.setter
    def canonical_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "canonical_id", value)

    @property
    @pulumi.getter(name="customMetadata")
    def custom_metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Custom metadata to be associated with this alias.
        """
        return pulumi.get(self, "custom_metadata")

    @custom_metadata.setter
    def custom_metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "custom_metadata", value)

    @property
    @pulumi.getter(name="mountAccessor")
    def mount_accessor(self) -> Optional[pulumi.Input[str]]:
        """
        Accessor of the mount to which the alias should belong to.
        """
        return pulumi.get(self, "mount_accessor")

    @mount_accessor.setter
    def mount_accessor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mount_accessor", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the alias. Name should be the identifier of the client in the authentication source. For example, if the alias belongs to userpass backend, the name should be a valid username within userpass backend. If alias belongs to GitHub, it should be the GitHub username.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace to provision the resource in.
        The value should not contain leading or trailing forward slashes.
        The `namespace` is always relative to the provider's configured [namespace](https://www.terraform.io/docs/providers/vault/index.html#namespace).
        *Available only for Vault Enterprise*.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)


class EntityAlias(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 canonical_id: Optional[pulumi.Input[str]] = None,
                 custom_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 mount_accessor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_vault as vault

        test = vault.identity.EntityAlias("test",
            name="user_1",
            mount_accessor="token_1f2bd5",
            canonical_id="49877D63-07AD-4B85-BDA8-B61626C477E8")
        ```

        ## Import

        Identity entity alias can be imported using the `id`, e.g.

        ```sh
        $ pulumi import vault:identity/entityAlias:EntityAlias test "3856fb4d-3c91-dcaf-2401-68f446796bfb"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] canonical_id: Entity ID to which this alias belongs to.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_metadata: Custom metadata to be associated with this alias.
        :param pulumi.Input[str] mount_accessor: Accessor of the mount to which the alias should belong to.
        :param pulumi.Input[str] name: Name of the alias. Name should be the identifier of the client in the authentication source. For example, if the alias belongs to userpass backend, the name should be a valid username within userpass backend. If alias belongs to GitHub, it should be the GitHub username.
        :param pulumi.Input[str] namespace: The namespace to provision the resource in.
               The value should not contain leading or trailing forward slashes.
               The `namespace` is always relative to the provider's configured [namespace](https://www.terraform.io/docs/providers/vault/index.html#namespace).
               *Available only for Vault Enterprise*.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EntityAliasArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_vault as vault

        test = vault.identity.EntityAlias("test",
            name="user_1",
            mount_accessor="token_1f2bd5",
            canonical_id="49877D63-07AD-4B85-BDA8-B61626C477E8")
        ```

        ## Import

        Identity entity alias can be imported using the `id`, e.g.

        ```sh
        $ pulumi import vault:identity/entityAlias:EntityAlias test "3856fb4d-3c91-dcaf-2401-68f446796bfb"
        ```

        :param str resource_name: The name of the resource.
        :param EntityAliasArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EntityAliasArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 canonical_id: Optional[pulumi.Input[str]] = None,
                 custom_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 mount_accessor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EntityAliasArgs.__new__(EntityAliasArgs)

            if canonical_id is None and not opts.urn:
                raise TypeError("Missing required property 'canonical_id'")
            __props__.__dict__["canonical_id"] = canonical_id
            __props__.__dict__["custom_metadata"] = custom_metadata
            if mount_accessor is None and not opts.urn:
                raise TypeError("Missing required property 'mount_accessor'")
            __props__.__dict__["mount_accessor"] = mount_accessor
            __props__.__dict__["name"] = name
            __props__.__dict__["namespace"] = namespace
        super(EntityAlias, __self__).__init__(
            'vault:identity/entityAlias:EntityAlias',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            canonical_id: Optional[pulumi.Input[str]] = None,
            custom_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            mount_accessor: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace: Optional[pulumi.Input[str]] = None) -> 'EntityAlias':
        """
        Get an existing EntityAlias resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] canonical_id: Entity ID to which this alias belongs to.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_metadata: Custom metadata to be associated with this alias.
        :param pulumi.Input[str] mount_accessor: Accessor of the mount to which the alias should belong to.
        :param pulumi.Input[str] name: Name of the alias. Name should be the identifier of the client in the authentication source. For example, if the alias belongs to userpass backend, the name should be a valid username within userpass backend. If alias belongs to GitHub, it should be the GitHub username.
        :param pulumi.Input[str] namespace: The namespace to provision the resource in.
               The value should not contain leading or trailing forward slashes.
               The `namespace` is always relative to the provider's configured [namespace](https://www.terraform.io/docs/providers/vault/index.html#namespace).
               *Available only for Vault Enterprise*.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EntityAliasState.__new__(_EntityAliasState)

        __props__.__dict__["canonical_id"] = canonical_id
        __props__.__dict__["custom_metadata"] = custom_metadata
        __props__.__dict__["mount_accessor"] = mount_accessor
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace"] = namespace
        return EntityAlias(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="canonicalId")
    def canonical_id(self) -> pulumi.Output[str]:
        """
        Entity ID to which this alias belongs to.
        """
        return pulumi.get(self, "canonical_id")

    @property
    @pulumi.getter(name="customMetadata")
    def custom_metadata(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Custom metadata to be associated with this alias.
        """
        return pulumi.get(self, "custom_metadata")

    @property
    @pulumi.getter(name="mountAccessor")
    def mount_accessor(self) -> pulumi.Output[str]:
        """
        Accessor of the mount to which the alias should belong to.
        """
        return pulumi.get(self, "mount_accessor")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the alias. Name should be the identifier of the client in the authentication source. For example, if the alias belongs to userpass backend, the name should be a valid username within userpass backend. If alias belongs to GitHub, it should be the GitHub username.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[str]]:
        """
        The namespace to provision the resource in.
        The value should not contain leading or trailing forward slashes.
        The `namespace` is always relative to the provider's configured [namespace](https://www.terraform.io/docs/providers/vault/index.html#namespace).
        *Available only for Vault Enterprise*.
        """
        return pulumi.get(self, "namespace")

