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
    'GetAntiSpywareProfileResult',
    'AwaitableGetAntiSpywareProfileResult',
    'get_anti_spyware_profile',
    'get_anti_spyware_profile_output',
]

@pulumi.output_type
class GetAntiSpywareProfileResult:
    """
    A collection of values returned by getAntiSpywareProfile.
    """
    def __init__(__self__, cloud_inline_analysis=None, description=None, id=None, inline_exception_edl_urls=None, inline_exception_ip_addresses=None, mica_engine_spyware_enabled_lists=None, name=None, rules=None, tfid=None, threat_exceptions=None):
        if cloud_inline_analysis and not isinstance(cloud_inline_analysis, bool):
            raise TypeError("Expected argument 'cloud_inline_analysis' to be a bool")
        pulumi.set(__self__, "cloud_inline_analysis", cloud_inline_analysis)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if inline_exception_edl_urls and not isinstance(inline_exception_edl_urls, list):
            raise TypeError("Expected argument 'inline_exception_edl_urls' to be a list")
        pulumi.set(__self__, "inline_exception_edl_urls", inline_exception_edl_urls)
        if inline_exception_ip_addresses and not isinstance(inline_exception_ip_addresses, list):
            raise TypeError("Expected argument 'inline_exception_ip_addresses' to be a list")
        pulumi.set(__self__, "inline_exception_ip_addresses", inline_exception_ip_addresses)
        if mica_engine_spyware_enabled_lists and not isinstance(mica_engine_spyware_enabled_lists, list):
            raise TypeError("Expected argument 'mica_engine_spyware_enabled_lists' to be a list")
        pulumi.set(__self__, "mica_engine_spyware_enabled_lists", mica_engine_spyware_enabled_lists)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)
        if tfid and not isinstance(tfid, str):
            raise TypeError("Expected argument 'tfid' to be a str")
        pulumi.set(__self__, "tfid", tfid)
        if threat_exceptions and not isinstance(threat_exceptions, list):
            raise TypeError("Expected argument 'threat_exceptions' to be a list")
        pulumi.set(__self__, "threat_exceptions", threat_exceptions)

    @property
    @pulumi.getter(name="cloudInlineAnalysis")
    def cloud_inline_analysis(self) -> bool:
        """
        The CloudInlineAnalysis param. Default: `false`.
        """
        return pulumi.get(self, "cloud_inline_analysis")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The Description param.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The Id param.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inlineExceptionEdlUrls")
    def inline_exception_edl_urls(self) -> Sequence[str]:
        """
        The InlineExceptionEdlUrls param.
        """
        return pulumi.get(self, "inline_exception_edl_urls")

    @property
    @pulumi.getter(name="inlineExceptionIpAddresses")
    def inline_exception_ip_addresses(self) -> Sequence[str]:
        """
        The InlineExceptionIpAddresses param.
        """
        return pulumi.get(self, "inline_exception_ip_addresses")

    @property
    @pulumi.getter(name="micaEngineSpywareEnabledLists")
    def mica_engine_spyware_enabled_lists(self) -> Sequence['outputs.GetAntiSpywareProfileMicaEngineSpywareEnabledListResult']:
        """
        The MicaEngineSpywareEnabledList param.
        """
        return pulumi.get(self, "mica_engine_spyware_enabled_lists")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The Name param.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rules(self) -> Sequence['outputs.GetAntiSpywareProfileRuleResult']:
        """
        The Rules param.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def tfid(self) -> str:
        return pulumi.get(self, "tfid")

    @property
    @pulumi.getter(name="threatExceptions")
    def threat_exceptions(self) -> Sequence['outputs.GetAntiSpywareProfileThreatExceptionResult']:
        """
        The ThreatExceptions param.
        """
        return pulumi.get(self, "threat_exceptions")


class AwaitableGetAntiSpywareProfileResult(GetAntiSpywareProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAntiSpywareProfileResult(
            cloud_inline_analysis=self.cloud_inline_analysis,
            description=self.description,
            id=self.id,
            inline_exception_edl_urls=self.inline_exception_edl_urls,
            inline_exception_ip_addresses=self.inline_exception_ip_addresses,
            mica_engine_spyware_enabled_lists=self.mica_engine_spyware_enabled_lists,
            name=self.name,
            rules=self.rules,
            tfid=self.tfid,
            threat_exceptions=self.threat_exceptions)


def get_anti_spyware_profile(id: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAntiSpywareProfileResult:
    """
    Retrieves a config item.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scm as scm

    example = scm.get_anti_spyware_profile(id="1234-56-789")
    ```


    :param str id: The Id param.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('scm:index/getAntiSpywareProfile:getAntiSpywareProfile', __args__, opts=opts, typ=GetAntiSpywareProfileResult).value

    return AwaitableGetAntiSpywareProfileResult(
        cloud_inline_analysis=pulumi.get(__ret__, 'cloud_inline_analysis'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        inline_exception_edl_urls=pulumi.get(__ret__, 'inline_exception_edl_urls'),
        inline_exception_ip_addresses=pulumi.get(__ret__, 'inline_exception_ip_addresses'),
        mica_engine_spyware_enabled_lists=pulumi.get(__ret__, 'mica_engine_spyware_enabled_lists'),
        name=pulumi.get(__ret__, 'name'),
        rules=pulumi.get(__ret__, 'rules'),
        tfid=pulumi.get(__ret__, 'tfid'),
        threat_exceptions=pulumi.get(__ret__, 'threat_exceptions'))


@_utilities.lift_output_func(get_anti_spyware_profile)
def get_anti_spyware_profile_output(id: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAntiSpywareProfileResult]:
    """
    Retrieves a config item.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scm as scm

    example = scm.get_anti_spyware_profile(id="1234-56-789")
    ```


    :param str id: The Id param.
    """
    ...
