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

__all__ = ['ServiceConnectionArgs', 'ServiceConnection']

@pulumi.input_type
class ServiceConnectionArgs:
    def __init__(__self__, *,
                 ipsec_tunnel: pulumi.Input[str],
                 region: pulumi.Input[str],
                 backup_sc: Optional[pulumi.Input[str]] = None,
                 bgp_peer: Optional[pulumi.Input['ServiceConnectionBgpPeerArgs']] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nat_pool: Optional[pulumi.Input[str]] = None,
                 no_export_community: Optional[pulumi.Input[str]] = None,
                 onboarding_type: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input['ServiceConnectionProtocolArgs']] = None,
                 qos: Optional[pulumi.Input['ServiceConnectionQosArgs']] = None,
                 secondary_ipsec_tunnel: Optional[pulumi.Input[str]] = None,
                 source_nat: Optional[pulumi.Input[bool]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ServiceConnection resource.
        :param pulumi.Input[str] ipsec_tunnel: The IpsecTunnel param.
        :param pulumi.Input[str] region: The Region param.
        :param pulumi.Input[str] backup_sc: The BackupSC param.
        :param pulumi.Input['ServiceConnectionBgpPeerArgs'] bgp_peer: The BgpPeer param.
        :param pulumi.Input[str] folder: The Folder param. String can either be a specific string(`"Service Connections"`) or match this regex: `^[0-9a-zA-Z._\\s-]{1,}$`. Default: `"Service Connections"`.
        :param pulumi.Input[str] name: The Name param.
        :param pulumi.Input[str] nat_pool: The NatPool param.
        :param pulumi.Input[str] no_export_community: The NoExportCommunity param. String must be one of these: `"Disabled"`, `"Enabled-In"`, `"Enabled-Out"`, `"Enabled-Both"`.
        :param pulumi.Input[str] onboarding_type: The OnboardingType param. String must be one of these: `"classic"`. Default: `"classic"`.
        :param pulumi.Input['ServiceConnectionProtocolArgs'] protocol: The Protocol param.
        :param pulumi.Input['ServiceConnectionQosArgs'] qos: The Qos param.
        :param pulumi.Input[str] secondary_ipsec_tunnel: The SecondaryIpsecTunnel param.
        :param pulumi.Input[bool] source_nat: The SourceNat param.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnets: The Subnets param.
        """
        pulumi.set(__self__, "ipsec_tunnel", ipsec_tunnel)
        pulumi.set(__self__, "region", region)
        if backup_sc is not None:
            pulumi.set(__self__, "backup_sc", backup_sc)
        if bgp_peer is not None:
            pulumi.set(__self__, "bgp_peer", bgp_peer)
        if folder is not None:
            pulumi.set(__self__, "folder", folder)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if nat_pool is not None:
            pulumi.set(__self__, "nat_pool", nat_pool)
        if no_export_community is not None:
            pulumi.set(__self__, "no_export_community", no_export_community)
        if onboarding_type is not None:
            pulumi.set(__self__, "onboarding_type", onboarding_type)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if qos is not None:
            pulumi.set(__self__, "qos", qos)
        if secondary_ipsec_tunnel is not None:
            pulumi.set(__self__, "secondary_ipsec_tunnel", secondary_ipsec_tunnel)
        if source_nat is not None:
            pulumi.set(__self__, "source_nat", source_nat)
        if subnets is not None:
            pulumi.set(__self__, "subnets", subnets)

    @property
    @pulumi.getter(name="ipsecTunnel")
    def ipsec_tunnel(self) -> pulumi.Input[str]:
        """
        The IpsecTunnel param.
        """
        return pulumi.get(self, "ipsec_tunnel")

    @ipsec_tunnel.setter
    def ipsec_tunnel(self, value: pulumi.Input[str]):
        pulumi.set(self, "ipsec_tunnel", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        The Region param.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="backupSC")
    def backup_sc(self) -> Optional[pulumi.Input[str]]:
        """
        The BackupSC param.
        """
        return pulumi.get(self, "backup_sc")

    @backup_sc.setter
    def backup_sc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backup_sc", value)

    @property
    @pulumi.getter(name="bgpPeer")
    def bgp_peer(self) -> Optional[pulumi.Input['ServiceConnectionBgpPeerArgs']]:
        """
        The BgpPeer param.
        """
        return pulumi.get(self, "bgp_peer")

    @bgp_peer.setter
    def bgp_peer(self, value: Optional[pulumi.Input['ServiceConnectionBgpPeerArgs']]):
        pulumi.set(self, "bgp_peer", value)

    @property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[str]]:
        """
        The Folder param. String can either be a specific string(`"Service Connections"`) or match this regex: `^[0-9a-zA-Z._\\s-]{1,}$`. Default: `"Service Connections"`.
        """
        return pulumi.get(self, "folder")

    @folder.setter
    def folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder", value)

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
    @pulumi.getter(name="natPool")
    def nat_pool(self) -> Optional[pulumi.Input[str]]:
        """
        The NatPool param.
        """
        return pulumi.get(self, "nat_pool")

    @nat_pool.setter
    def nat_pool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nat_pool", value)

    @property
    @pulumi.getter(name="noExportCommunity")
    def no_export_community(self) -> Optional[pulumi.Input[str]]:
        """
        The NoExportCommunity param. String must be one of these: `"Disabled"`, `"Enabled-In"`, `"Enabled-Out"`, `"Enabled-Both"`.
        """
        return pulumi.get(self, "no_export_community")

    @no_export_community.setter
    def no_export_community(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "no_export_community", value)

    @property
    @pulumi.getter(name="onboardingType")
    def onboarding_type(self) -> Optional[pulumi.Input[str]]:
        """
        The OnboardingType param. String must be one of these: `"classic"`. Default: `"classic"`.
        """
        return pulumi.get(self, "onboarding_type")

    @onboarding_type.setter
    def onboarding_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "onboarding_type", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input['ServiceConnectionProtocolArgs']]:
        """
        The Protocol param.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input['ServiceConnectionProtocolArgs']]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def qos(self) -> Optional[pulumi.Input['ServiceConnectionQosArgs']]:
        """
        The Qos param.
        """
        return pulumi.get(self, "qos")

    @qos.setter
    def qos(self, value: Optional[pulumi.Input['ServiceConnectionQosArgs']]):
        pulumi.set(self, "qos", value)

    @property
    @pulumi.getter(name="secondaryIpsecTunnel")
    def secondary_ipsec_tunnel(self) -> Optional[pulumi.Input[str]]:
        """
        The SecondaryIpsecTunnel param.
        """
        return pulumi.get(self, "secondary_ipsec_tunnel")

    @secondary_ipsec_tunnel.setter
    def secondary_ipsec_tunnel(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secondary_ipsec_tunnel", value)

    @property
    @pulumi.getter(name="sourceNat")
    def source_nat(self) -> Optional[pulumi.Input[bool]]:
        """
        The SourceNat param.
        """
        return pulumi.get(self, "source_nat")

    @source_nat.setter
    def source_nat(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "source_nat", value)

    @property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The Subnets param.
        """
        return pulumi.get(self, "subnets")

    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnets", value)


@pulumi.input_type
class _ServiceConnectionState:
    def __init__(__self__, *,
                 backup_sc: Optional[pulumi.Input[str]] = None,
                 bgp_peer: Optional[pulumi.Input['ServiceConnectionBgpPeerArgs']] = None,
                 encrypted_values: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 ipsec_tunnel: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nat_pool: Optional[pulumi.Input[str]] = None,
                 no_export_community: Optional[pulumi.Input[str]] = None,
                 onboarding_type: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input['ServiceConnectionProtocolArgs']] = None,
                 qos: Optional[pulumi.Input['ServiceConnectionQosArgs']] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secondary_ipsec_tunnel: Optional[pulumi.Input[str]] = None,
                 source_nat: Optional[pulumi.Input[bool]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tfid: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ServiceConnection resources.
        :param pulumi.Input[str] backup_sc: The BackupSC param.
        :param pulumi.Input['ServiceConnectionBgpPeerArgs'] bgp_peer: The BgpPeer param.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] encrypted_values: (Internal use) Encrypted values returned from the API.
        :param pulumi.Input[str] folder: The Folder param. String can either be a specific string(`"Service Connections"`) or match this regex: `^[0-9a-zA-Z._\\s-]{1,}$`. Default: `"Service Connections"`.
        :param pulumi.Input[str] ipsec_tunnel: The IpsecTunnel param.
        :param pulumi.Input[str] name: The Name param.
        :param pulumi.Input[str] nat_pool: The NatPool param.
        :param pulumi.Input[str] no_export_community: The NoExportCommunity param. String must be one of these: `"Disabled"`, `"Enabled-In"`, `"Enabled-Out"`, `"Enabled-Both"`.
        :param pulumi.Input[str] onboarding_type: The OnboardingType param. String must be one of these: `"classic"`. Default: `"classic"`.
        :param pulumi.Input['ServiceConnectionProtocolArgs'] protocol: The Protocol param.
        :param pulumi.Input['ServiceConnectionQosArgs'] qos: The Qos param.
        :param pulumi.Input[str] region: The Region param.
        :param pulumi.Input[str] secondary_ipsec_tunnel: The SecondaryIpsecTunnel param.
        :param pulumi.Input[bool] source_nat: The SourceNat param.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnets: The Subnets param.
        """
        if backup_sc is not None:
            pulumi.set(__self__, "backup_sc", backup_sc)
        if bgp_peer is not None:
            pulumi.set(__self__, "bgp_peer", bgp_peer)
        if encrypted_values is not None:
            pulumi.set(__self__, "encrypted_values", encrypted_values)
        if folder is not None:
            pulumi.set(__self__, "folder", folder)
        if ipsec_tunnel is not None:
            pulumi.set(__self__, "ipsec_tunnel", ipsec_tunnel)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if nat_pool is not None:
            pulumi.set(__self__, "nat_pool", nat_pool)
        if no_export_community is not None:
            pulumi.set(__self__, "no_export_community", no_export_community)
        if onboarding_type is not None:
            pulumi.set(__self__, "onboarding_type", onboarding_type)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if qos is not None:
            pulumi.set(__self__, "qos", qos)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if secondary_ipsec_tunnel is not None:
            pulumi.set(__self__, "secondary_ipsec_tunnel", secondary_ipsec_tunnel)
        if source_nat is not None:
            pulumi.set(__self__, "source_nat", source_nat)
        if subnets is not None:
            pulumi.set(__self__, "subnets", subnets)
        if tfid is not None:
            pulumi.set(__self__, "tfid", tfid)

    @property
    @pulumi.getter(name="backupSC")
    def backup_sc(self) -> Optional[pulumi.Input[str]]:
        """
        The BackupSC param.
        """
        return pulumi.get(self, "backup_sc")

    @backup_sc.setter
    def backup_sc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backup_sc", value)

    @property
    @pulumi.getter(name="bgpPeer")
    def bgp_peer(self) -> Optional[pulumi.Input['ServiceConnectionBgpPeerArgs']]:
        """
        The BgpPeer param.
        """
        return pulumi.get(self, "bgp_peer")

    @bgp_peer.setter
    def bgp_peer(self, value: Optional[pulumi.Input['ServiceConnectionBgpPeerArgs']]):
        pulumi.set(self, "bgp_peer", value)

    @property
    @pulumi.getter(name="encryptedValues")
    def encrypted_values(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        (Internal use) Encrypted values returned from the API.
        """
        return pulumi.get(self, "encrypted_values")

    @encrypted_values.setter
    def encrypted_values(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "encrypted_values", value)

    @property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[str]]:
        """
        The Folder param. String can either be a specific string(`"Service Connections"`) or match this regex: `^[0-9a-zA-Z._\\s-]{1,}$`. Default: `"Service Connections"`.
        """
        return pulumi.get(self, "folder")

    @folder.setter
    def folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder", value)

    @property
    @pulumi.getter(name="ipsecTunnel")
    def ipsec_tunnel(self) -> Optional[pulumi.Input[str]]:
        """
        The IpsecTunnel param.
        """
        return pulumi.get(self, "ipsec_tunnel")

    @ipsec_tunnel.setter
    def ipsec_tunnel(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipsec_tunnel", value)

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
    @pulumi.getter(name="natPool")
    def nat_pool(self) -> Optional[pulumi.Input[str]]:
        """
        The NatPool param.
        """
        return pulumi.get(self, "nat_pool")

    @nat_pool.setter
    def nat_pool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nat_pool", value)

    @property
    @pulumi.getter(name="noExportCommunity")
    def no_export_community(self) -> Optional[pulumi.Input[str]]:
        """
        The NoExportCommunity param. String must be one of these: `"Disabled"`, `"Enabled-In"`, `"Enabled-Out"`, `"Enabled-Both"`.
        """
        return pulumi.get(self, "no_export_community")

    @no_export_community.setter
    def no_export_community(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "no_export_community", value)

    @property
    @pulumi.getter(name="onboardingType")
    def onboarding_type(self) -> Optional[pulumi.Input[str]]:
        """
        The OnboardingType param. String must be one of these: `"classic"`. Default: `"classic"`.
        """
        return pulumi.get(self, "onboarding_type")

    @onboarding_type.setter
    def onboarding_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "onboarding_type", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input['ServiceConnectionProtocolArgs']]:
        """
        The Protocol param.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input['ServiceConnectionProtocolArgs']]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def qos(self) -> Optional[pulumi.Input['ServiceConnectionQosArgs']]:
        """
        The Qos param.
        """
        return pulumi.get(self, "qos")

    @qos.setter
    def qos(self, value: Optional[pulumi.Input['ServiceConnectionQosArgs']]):
        pulumi.set(self, "qos", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The Region param.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="secondaryIpsecTunnel")
    def secondary_ipsec_tunnel(self) -> Optional[pulumi.Input[str]]:
        """
        The SecondaryIpsecTunnel param.
        """
        return pulumi.get(self, "secondary_ipsec_tunnel")

    @secondary_ipsec_tunnel.setter
    def secondary_ipsec_tunnel(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secondary_ipsec_tunnel", value)

    @property
    @pulumi.getter(name="sourceNat")
    def source_nat(self) -> Optional[pulumi.Input[bool]]:
        """
        The SourceNat param.
        """
        return pulumi.get(self, "source_nat")

    @source_nat.setter
    def source_nat(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "source_nat", value)

    @property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The Subnets param.
        """
        return pulumi.get(self, "subnets")

    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnets", value)

    @property
    @pulumi.getter
    def tfid(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "tfid")

    @tfid.setter
    def tfid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tfid", value)


class ServiceConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_sc: Optional[pulumi.Input[str]] = None,
                 bgp_peer: Optional[pulumi.Input[pulumi.InputType['ServiceConnectionBgpPeerArgs']]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 ipsec_tunnel: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nat_pool: Optional[pulumi.Input[str]] = None,
                 no_export_community: Optional[pulumi.Input[str]] = None,
                 onboarding_type: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[pulumi.InputType['ServiceConnectionProtocolArgs']]] = None,
                 qos: Optional[pulumi.Input[pulumi.InputType['ServiceConnectionQosArgs']]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secondary_ipsec_tunnel: Optional[pulumi.Input[str]] = None,
                 source_nat: Optional[pulumi.Input[bool]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Retrieves a config item.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_scm as scm

        example = scm.ServiceConnection("example")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backup_sc: The BackupSC param.
        :param pulumi.Input[pulumi.InputType['ServiceConnectionBgpPeerArgs']] bgp_peer: The BgpPeer param.
        :param pulumi.Input[str] folder: The Folder param. String can either be a specific string(`"Service Connections"`) or match this regex: `^[0-9a-zA-Z._\\s-]{1,}$`. Default: `"Service Connections"`.
        :param pulumi.Input[str] ipsec_tunnel: The IpsecTunnel param.
        :param pulumi.Input[str] name: The Name param.
        :param pulumi.Input[str] nat_pool: The NatPool param.
        :param pulumi.Input[str] no_export_community: The NoExportCommunity param. String must be one of these: `"Disabled"`, `"Enabled-In"`, `"Enabled-Out"`, `"Enabled-Both"`.
        :param pulumi.Input[str] onboarding_type: The OnboardingType param. String must be one of these: `"classic"`. Default: `"classic"`.
        :param pulumi.Input[pulumi.InputType['ServiceConnectionProtocolArgs']] protocol: The Protocol param.
        :param pulumi.Input[pulumi.InputType['ServiceConnectionQosArgs']] qos: The Qos param.
        :param pulumi.Input[str] region: The Region param.
        :param pulumi.Input[str] secondary_ipsec_tunnel: The SecondaryIpsecTunnel param.
        :param pulumi.Input[bool] source_nat: The SourceNat param.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnets: The Subnets param.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Retrieves a config item.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_scm as scm

        example = scm.ServiceConnection("example")
        ```

        :param str resource_name: The name of the resource.
        :param ServiceConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_sc: Optional[pulumi.Input[str]] = None,
                 bgp_peer: Optional[pulumi.Input[pulumi.InputType['ServiceConnectionBgpPeerArgs']]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 ipsec_tunnel: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nat_pool: Optional[pulumi.Input[str]] = None,
                 no_export_community: Optional[pulumi.Input[str]] = None,
                 onboarding_type: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[pulumi.InputType['ServiceConnectionProtocolArgs']]] = None,
                 qos: Optional[pulumi.Input[pulumi.InputType['ServiceConnectionQosArgs']]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secondary_ipsec_tunnel: Optional[pulumi.Input[str]] = None,
                 source_nat: Optional[pulumi.Input[bool]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceConnectionArgs.__new__(ServiceConnectionArgs)

            __props__.__dict__["backup_sc"] = backup_sc
            __props__.__dict__["bgp_peer"] = bgp_peer
            __props__.__dict__["folder"] = folder
            if ipsec_tunnel is None and not opts.urn:
                raise TypeError("Missing required property 'ipsec_tunnel'")
            __props__.__dict__["ipsec_tunnel"] = ipsec_tunnel
            __props__.__dict__["name"] = name
            __props__.__dict__["nat_pool"] = nat_pool
            __props__.__dict__["no_export_community"] = no_export_community
            __props__.__dict__["onboarding_type"] = onboarding_type
            __props__.__dict__["protocol"] = protocol
            __props__.__dict__["qos"] = qos
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["secondary_ipsec_tunnel"] = secondary_ipsec_tunnel
            __props__.__dict__["source_nat"] = source_nat
            __props__.__dict__["subnets"] = subnets
            __props__.__dict__["encrypted_values"] = None
            __props__.__dict__["tfid"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["encryptedValues"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(ServiceConnection, __self__).__init__(
            'scm:index/serviceConnection:ServiceConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            backup_sc: Optional[pulumi.Input[str]] = None,
            bgp_peer: Optional[pulumi.Input[pulumi.InputType['ServiceConnectionBgpPeerArgs']]] = None,
            encrypted_values: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            folder: Optional[pulumi.Input[str]] = None,
            ipsec_tunnel: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            nat_pool: Optional[pulumi.Input[str]] = None,
            no_export_community: Optional[pulumi.Input[str]] = None,
            onboarding_type: Optional[pulumi.Input[str]] = None,
            protocol: Optional[pulumi.Input[pulumi.InputType['ServiceConnectionProtocolArgs']]] = None,
            qos: Optional[pulumi.Input[pulumi.InputType['ServiceConnectionQosArgs']]] = None,
            region: Optional[pulumi.Input[str]] = None,
            secondary_ipsec_tunnel: Optional[pulumi.Input[str]] = None,
            source_nat: Optional[pulumi.Input[bool]] = None,
            subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tfid: Optional[pulumi.Input[str]] = None) -> 'ServiceConnection':
        """
        Get an existing ServiceConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backup_sc: The BackupSC param.
        :param pulumi.Input[pulumi.InputType['ServiceConnectionBgpPeerArgs']] bgp_peer: The BgpPeer param.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] encrypted_values: (Internal use) Encrypted values returned from the API.
        :param pulumi.Input[str] folder: The Folder param. String can either be a specific string(`"Service Connections"`) or match this regex: `^[0-9a-zA-Z._\\s-]{1,}$`. Default: `"Service Connections"`.
        :param pulumi.Input[str] ipsec_tunnel: The IpsecTunnel param.
        :param pulumi.Input[str] name: The Name param.
        :param pulumi.Input[str] nat_pool: The NatPool param.
        :param pulumi.Input[str] no_export_community: The NoExportCommunity param. String must be one of these: `"Disabled"`, `"Enabled-In"`, `"Enabled-Out"`, `"Enabled-Both"`.
        :param pulumi.Input[str] onboarding_type: The OnboardingType param. String must be one of these: `"classic"`. Default: `"classic"`.
        :param pulumi.Input[pulumi.InputType['ServiceConnectionProtocolArgs']] protocol: The Protocol param.
        :param pulumi.Input[pulumi.InputType['ServiceConnectionQosArgs']] qos: The Qos param.
        :param pulumi.Input[str] region: The Region param.
        :param pulumi.Input[str] secondary_ipsec_tunnel: The SecondaryIpsecTunnel param.
        :param pulumi.Input[bool] source_nat: The SourceNat param.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnets: The Subnets param.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServiceConnectionState.__new__(_ServiceConnectionState)

        __props__.__dict__["backup_sc"] = backup_sc
        __props__.__dict__["bgp_peer"] = bgp_peer
        __props__.__dict__["encrypted_values"] = encrypted_values
        __props__.__dict__["folder"] = folder
        __props__.__dict__["ipsec_tunnel"] = ipsec_tunnel
        __props__.__dict__["name"] = name
        __props__.__dict__["nat_pool"] = nat_pool
        __props__.__dict__["no_export_community"] = no_export_community
        __props__.__dict__["onboarding_type"] = onboarding_type
        __props__.__dict__["protocol"] = protocol
        __props__.__dict__["qos"] = qos
        __props__.__dict__["region"] = region
        __props__.__dict__["secondary_ipsec_tunnel"] = secondary_ipsec_tunnel
        __props__.__dict__["source_nat"] = source_nat
        __props__.__dict__["subnets"] = subnets
        __props__.__dict__["tfid"] = tfid
        return ServiceConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backupSC")
    def backup_sc(self) -> pulumi.Output[Optional[str]]:
        """
        The BackupSC param.
        """
        return pulumi.get(self, "backup_sc")

    @property
    @pulumi.getter(name="bgpPeer")
    def bgp_peer(self) -> pulumi.Output[Optional['outputs.ServiceConnectionBgpPeer']]:
        """
        The BgpPeer param.
        """
        return pulumi.get(self, "bgp_peer")

    @property
    @pulumi.getter(name="encryptedValues")
    def encrypted_values(self) -> pulumi.Output[Mapping[str, str]]:
        """
        (Internal use) Encrypted values returned from the API.
        """
        return pulumi.get(self, "encrypted_values")

    @property
    @pulumi.getter
    def folder(self) -> pulumi.Output[str]:
        """
        The Folder param. String can either be a specific string(`"Service Connections"`) or match this regex: `^[0-9a-zA-Z._\\s-]{1,}$`. Default: `"Service Connections"`.
        """
        return pulumi.get(self, "folder")

    @property
    @pulumi.getter(name="ipsecTunnel")
    def ipsec_tunnel(self) -> pulumi.Output[str]:
        """
        The IpsecTunnel param.
        """
        return pulumi.get(self, "ipsec_tunnel")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The Name param.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="natPool")
    def nat_pool(self) -> pulumi.Output[Optional[str]]:
        """
        The NatPool param.
        """
        return pulumi.get(self, "nat_pool")

    @property
    @pulumi.getter(name="noExportCommunity")
    def no_export_community(self) -> pulumi.Output[Optional[str]]:
        """
        The NoExportCommunity param. String must be one of these: `"Disabled"`, `"Enabled-In"`, `"Enabled-Out"`, `"Enabled-Both"`.
        """
        return pulumi.get(self, "no_export_community")

    @property
    @pulumi.getter(name="onboardingType")
    def onboarding_type(self) -> pulumi.Output[str]:
        """
        The OnboardingType param. String must be one of these: `"classic"`. Default: `"classic"`.
        """
        return pulumi.get(self, "onboarding_type")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional['outputs.ServiceConnectionProtocol']]:
        """
        The Protocol param.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def qos(self) -> pulumi.Output[Optional['outputs.ServiceConnectionQos']]:
        """
        The Qos param.
        """
        return pulumi.get(self, "qos")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The Region param.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="secondaryIpsecTunnel")
    def secondary_ipsec_tunnel(self) -> pulumi.Output[Optional[str]]:
        """
        The SecondaryIpsecTunnel param.
        """
        return pulumi.get(self, "secondary_ipsec_tunnel")

    @property
    @pulumi.getter(name="sourceNat")
    def source_nat(self) -> pulumi.Output[Optional[bool]]:
        """
        The SourceNat param.
        """
        return pulumi.get(self, "source_nat")

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The Subnets param.
        """
        return pulumi.get(self, "subnets")

    @property
    @pulumi.getter
    def tfid(self) -> pulumi.Output[str]:
        return pulumi.get(self, "tfid")

