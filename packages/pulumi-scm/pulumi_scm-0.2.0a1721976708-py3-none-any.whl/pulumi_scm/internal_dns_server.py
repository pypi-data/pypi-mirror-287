# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['InternalDnsServerArgs', 'InternalDnsServer']

@pulumi.input_type
class InternalDnsServerArgs:
    def __init__(__self__, *,
                 domain_names: pulumi.Input[Sequence[pulumi.Input[str]]],
                 primary: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 secondary: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a InternalDnsServer resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain_names: The DomainNames param.
        :param pulumi.Input[str] primary: The Primary param.
        :param pulumi.Input[str] name: The Name param.
        :param pulumi.Input[str] secondary: The Secondary param.
        """
        pulumi.set(__self__, "domain_names", domain_names)
        pulumi.set(__self__, "primary", primary)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if secondary is not None:
            pulumi.set(__self__, "secondary", secondary)

    @property
    @pulumi.getter(name="domainNames")
    def domain_names(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The DomainNames param.
        """
        return pulumi.get(self, "domain_names")

    @domain_names.setter
    def domain_names(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "domain_names", value)

    @property
    @pulumi.getter
    def primary(self) -> pulumi.Input[str]:
        """
        The Primary param.
        """
        return pulumi.get(self, "primary")

    @primary.setter
    def primary(self, value: pulumi.Input[str]):
        pulumi.set(self, "primary", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The Name param.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def secondary(self) -> Optional[pulumi.Input[str]]:
        """
        The Secondary param.
        """
        return pulumi.get(self, "secondary")

    @secondary.setter
    def secondary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secondary", value)


@pulumi.input_type
class _InternalDnsServerState:
    def __init__(__self__, *,
                 domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 primary: Optional[pulumi.Input[str]] = None,
                 secondary: Optional[pulumi.Input[str]] = None,
                 tfid: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering InternalDnsServer resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain_names: The DomainNames param.
        :param pulumi.Input[str] name: The Name param.
        :param pulumi.Input[str] primary: The Primary param.
        :param pulumi.Input[str] secondary: The Secondary param.
        """
        if domain_names is not None:
            pulumi.set(__self__, "domain_names", domain_names)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if primary is not None:
            pulumi.set(__self__, "primary", primary)
        if secondary is not None:
            pulumi.set(__self__, "secondary", secondary)
        if tfid is not None:
            pulumi.set(__self__, "tfid", tfid)

    @property
    @pulumi.getter(name="domainNames")
    def domain_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The DomainNames param.
        """
        return pulumi.get(self, "domain_names")

    @domain_names.setter
    def domain_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "domain_names", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The Name param.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[str]]:
        """
        The Primary param.
        """
        return pulumi.get(self, "primary")

    @primary.setter
    def primary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "primary", value)

    @property
    @pulumi.getter
    def secondary(self) -> Optional[pulumi.Input[str]]:
        """
        The Secondary param.
        """
        return pulumi.get(self, "secondary")

    @secondary.setter
    def secondary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secondary", value)

    @property
    @pulumi.getter
    def tfid(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "tfid")

    @tfid.setter
    def tfid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tfid", value)


class InternalDnsServer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 primary: Optional[pulumi.Input[str]] = None,
                 secondary: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Retrieves a config item.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_scm as scm

        example = scm.InternalDnsServer("example")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain_names: The DomainNames param.
        :param pulumi.Input[str] name: The Name param.
        :param pulumi.Input[str] primary: The Primary param.
        :param pulumi.Input[str] secondary: The Secondary param.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InternalDnsServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Retrieves a config item.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_scm as scm

        example = scm.InternalDnsServer("example")
        ```

        :param str resource_name: The name of the resource.
        :param InternalDnsServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InternalDnsServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 primary: Optional[pulumi.Input[str]] = None,
                 secondary: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InternalDnsServerArgs.__new__(InternalDnsServerArgs)

            if domain_names is None and not opts.urn:
                raise TypeError("Missing required property 'domain_names'")
            __props__.__dict__["domain_names"] = domain_names
            __props__.__dict__["name"] = name
            if primary is None and not opts.urn:
                raise TypeError("Missing required property 'primary'")
            __props__.__dict__["primary"] = primary
            __props__.__dict__["secondary"] = secondary
            __props__.__dict__["tfid"] = None
        super(InternalDnsServer, __self__).__init__(
            'scm:index/internalDnsServer:InternalDnsServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            primary: Optional[pulumi.Input[str]] = None,
            secondary: Optional[pulumi.Input[str]] = None,
            tfid: Optional[pulumi.Input[str]] = None) -> 'InternalDnsServer':
        """
        Get an existing InternalDnsServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain_names: The DomainNames param.
        :param pulumi.Input[str] name: The Name param.
        :param pulumi.Input[str] primary: The Primary param.
        :param pulumi.Input[str] secondary: The Secondary param.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InternalDnsServerState.__new__(_InternalDnsServerState)

        __props__.__dict__["domain_names"] = domain_names
        __props__.__dict__["name"] = name
        __props__.__dict__["primary"] = primary
        __props__.__dict__["secondary"] = secondary
        __props__.__dict__["tfid"] = tfid
        return InternalDnsServer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainNames")
    def domain_names(self) -> pulumi.Output[Sequence[str]]:
        """
        The DomainNames param.
        """
        return pulumi.get(self, "domain_names")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The Name param.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def primary(self) -> pulumi.Output[str]:
        """
        The Primary param.
        """
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter
    def secondary(self) -> pulumi.Output[Optional[str]]:
        """
        The Secondary param.
        """
        return pulumi.get(self, "secondary")

    @property
    @pulumi.getter
    def tfid(self) -> pulumi.Output[str]:
        return pulumi.get(self, "tfid")

