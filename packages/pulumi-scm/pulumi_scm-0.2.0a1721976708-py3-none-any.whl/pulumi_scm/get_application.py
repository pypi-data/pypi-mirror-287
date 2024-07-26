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
    'GetApplicationResult',
    'AwaitableGetApplicationResult',
    'get_application',
    'get_application_output',
]

@pulumi.output_type
class GetApplicationResult:
    """
    A collection of values returned by getApplication.
    """
    def __init__(__self__, able_to_transfer_file=None, alg_disable_capability=None, category=None, consume_big_bandwidth=None, data_ident=None, default=None, description=None, evasive_behavior=None, file_type_ident=None, has_known_vulnerability=None, id=None, name=None, no_appid_caching=None, parent_app=None, pervasive_use=None, prone_to_misuse=None, risk=None, signatures=None, subcategory=None, tcp_half_closed_timeout=None, tcp_time_wait_timeout=None, tcp_timeout=None, technology=None, tfid=None, timeout=None, tunnel_applications=None, tunnel_other_application=None, udp_timeout=None, used_by_malware=None, virus_ident=None):
        if able_to_transfer_file and not isinstance(able_to_transfer_file, bool):
            raise TypeError("Expected argument 'able_to_transfer_file' to be a bool")
        pulumi.set(__self__, "able_to_transfer_file", able_to_transfer_file)
        if alg_disable_capability and not isinstance(alg_disable_capability, str):
            raise TypeError("Expected argument 'alg_disable_capability' to be a str")
        pulumi.set(__self__, "alg_disable_capability", alg_disable_capability)
        if category and not isinstance(category, str):
            raise TypeError("Expected argument 'category' to be a str")
        pulumi.set(__self__, "category", category)
        if consume_big_bandwidth and not isinstance(consume_big_bandwidth, bool):
            raise TypeError("Expected argument 'consume_big_bandwidth' to be a bool")
        pulumi.set(__self__, "consume_big_bandwidth", consume_big_bandwidth)
        if data_ident and not isinstance(data_ident, bool):
            raise TypeError("Expected argument 'data_ident' to be a bool")
        pulumi.set(__self__, "data_ident", data_ident)
        if default and not isinstance(default, dict):
            raise TypeError("Expected argument 'default' to be a dict")
        pulumi.set(__self__, "default", default)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if evasive_behavior and not isinstance(evasive_behavior, bool):
            raise TypeError("Expected argument 'evasive_behavior' to be a bool")
        pulumi.set(__self__, "evasive_behavior", evasive_behavior)
        if file_type_ident and not isinstance(file_type_ident, bool):
            raise TypeError("Expected argument 'file_type_ident' to be a bool")
        pulumi.set(__self__, "file_type_ident", file_type_ident)
        if has_known_vulnerability and not isinstance(has_known_vulnerability, bool):
            raise TypeError("Expected argument 'has_known_vulnerability' to be a bool")
        pulumi.set(__self__, "has_known_vulnerability", has_known_vulnerability)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if no_appid_caching and not isinstance(no_appid_caching, bool):
            raise TypeError("Expected argument 'no_appid_caching' to be a bool")
        pulumi.set(__self__, "no_appid_caching", no_appid_caching)
        if parent_app and not isinstance(parent_app, str):
            raise TypeError("Expected argument 'parent_app' to be a str")
        pulumi.set(__self__, "parent_app", parent_app)
        if pervasive_use and not isinstance(pervasive_use, bool):
            raise TypeError("Expected argument 'pervasive_use' to be a bool")
        pulumi.set(__self__, "pervasive_use", pervasive_use)
        if prone_to_misuse and not isinstance(prone_to_misuse, bool):
            raise TypeError("Expected argument 'prone_to_misuse' to be a bool")
        pulumi.set(__self__, "prone_to_misuse", prone_to_misuse)
        if risk and not isinstance(risk, int):
            raise TypeError("Expected argument 'risk' to be a int")
        pulumi.set(__self__, "risk", risk)
        if signatures and not isinstance(signatures, list):
            raise TypeError("Expected argument 'signatures' to be a list")
        pulumi.set(__self__, "signatures", signatures)
        if subcategory and not isinstance(subcategory, str):
            raise TypeError("Expected argument 'subcategory' to be a str")
        pulumi.set(__self__, "subcategory", subcategory)
        if tcp_half_closed_timeout and not isinstance(tcp_half_closed_timeout, int):
            raise TypeError("Expected argument 'tcp_half_closed_timeout' to be a int")
        pulumi.set(__self__, "tcp_half_closed_timeout", tcp_half_closed_timeout)
        if tcp_time_wait_timeout and not isinstance(tcp_time_wait_timeout, int):
            raise TypeError("Expected argument 'tcp_time_wait_timeout' to be a int")
        pulumi.set(__self__, "tcp_time_wait_timeout", tcp_time_wait_timeout)
        if tcp_timeout and not isinstance(tcp_timeout, int):
            raise TypeError("Expected argument 'tcp_timeout' to be a int")
        pulumi.set(__self__, "tcp_timeout", tcp_timeout)
        if technology and not isinstance(technology, str):
            raise TypeError("Expected argument 'technology' to be a str")
        pulumi.set(__self__, "technology", technology)
        if tfid and not isinstance(tfid, str):
            raise TypeError("Expected argument 'tfid' to be a str")
        pulumi.set(__self__, "tfid", tfid)
        if timeout and not isinstance(timeout, int):
            raise TypeError("Expected argument 'timeout' to be a int")
        pulumi.set(__self__, "timeout", timeout)
        if tunnel_applications and not isinstance(tunnel_applications, bool):
            raise TypeError("Expected argument 'tunnel_applications' to be a bool")
        pulumi.set(__self__, "tunnel_applications", tunnel_applications)
        if tunnel_other_application and not isinstance(tunnel_other_application, bool):
            raise TypeError("Expected argument 'tunnel_other_application' to be a bool")
        pulumi.set(__self__, "tunnel_other_application", tunnel_other_application)
        if udp_timeout and not isinstance(udp_timeout, int):
            raise TypeError("Expected argument 'udp_timeout' to be a int")
        pulumi.set(__self__, "udp_timeout", udp_timeout)
        if used_by_malware and not isinstance(used_by_malware, bool):
            raise TypeError("Expected argument 'used_by_malware' to be a bool")
        pulumi.set(__self__, "used_by_malware", used_by_malware)
        if virus_ident and not isinstance(virus_ident, bool):
            raise TypeError("Expected argument 'virus_ident' to be a bool")
        pulumi.set(__self__, "virus_ident", virus_ident)

    @property
    @pulumi.getter(name="ableToTransferFile")
    def able_to_transfer_file(self) -> bool:
        """
        The AbleToTransferFile param.
        """
        return pulumi.get(self, "able_to_transfer_file")

    @property
    @pulumi.getter(name="algDisableCapability")
    def alg_disable_capability(self) -> str:
        """
        The AlgDisableCapability param. String length must not exceed 127 characters.
        """
        return pulumi.get(self, "alg_disable_capability")

    @property
    @pulumi.getter
    def category(self) -> str:
        """
        The Category param.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="consumeBigBandwidth")
    def consume_big_bandwidth(self) -> bool:
        """
        The ConsumeBigBandwidth param.
        """
        return pulumi.get(self, "consume_big_bandwidth")

    @property
    @pulumi.getter(name="dataIdent")
    def data_ident(self) -> bool:
        """
        The DataIdent param.
        """
        return pulumi.get(self, "data_ident")

    @property
    @pulumi.getter
    def default(self) -> 'outputs.GetApplicationDefaultResult':
        """
        The Default param.
        """
        return pulumi.get(self, "default")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The Description param. String length must not exceed 1023 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="evasiveBehavior")
    def evasive_behavior(self) -> bool:
        """
        The EvasiveBehavior param.
        """
        return pulumi.get(self, "evasive_behavior")

    @property
    @pulumi.getter(name="fileTypeIdent")
    def file_type_ident(self) -> bool:
        """
        The FileTypeIdent param.
        """
        return pulumi.get(self, "file_type_ident")

    @property
    @pulumi.getter(name="hasKnownVulnerability")
    def has_known_vulnerability(self) -> bool:
        """
        The HasKnownVulnerability param.
        """
        return pulumi.get(self, "has_known_vulnerability")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The Id param.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Alphanumeric string [ 0-9a-zA-Z._-]. String length must not exceed 31 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="noAppidCaching")
    def no_appid_caching(self) -> bool:
        """
        The NoAppidCaching param.
        """
        return pulumi.get(self, "no_appid_caching")

    @property
    @pulumi.getter(name="parentApp")
    def parent_app(self) -> str:
        """
        The ParentApp param. String length must not exceed 127 characters.
        """
        return pulumi.get(self, "parent_app")

    @property
    @pulumi.getter(name="pervasiveUse")
    def pervasive_use(self) -> bool:
        """
        The PervasiveUse param.
        """
        return pulumi.get(self, "pervasive_use")

    @property
    @pulumi.getter(name="proneToMisuse")
    def prone_to_misuse(self) -> bool:
        """
        The ProneToMisuse param.
        """
        return pulumi.get(self, "prone_to_misuse")

    @property
    @pulumi.getter
    def risk(self) -> int:
        """
        The Risk param. Value must be between 1 and 5.
        """
        return pulumi.get(self, "risk")

    @property
    @pulumi.getter
    def signatures(self) -> Sequence['outputs.GetApplicationSignatureResult']:
        """
        The Signatures param.
        """
        return pulumi.get(self, "signatures")

    @property
    @pulumi.getter
    def subcategory(self) -> str:
        """
        The Subcategory param. String length must not exceed 63 characters.
        """
        return pulumi.get(self, "subcategory")

    @property
    @pulumi.getter(name="tcpHalfClosedTimeout")
    def tcp_half_closed_timeout(self) -> int:
        """
        timeout for half-close session in seconds. Value must be between 1 and 604800.
        """
        return pulumi.get(self, "tcp_half_closed_timeout")

    @property
    @pulumi.getter(name="tcpTimeWaitTimeout")
    def tcp_time_wait_timeout(self) -> int:
        """
        timeout for session in time_wait state in seconds. Value must be between 1 and 600.
        """
        return pulumi.get(self, "tcp_time_wait_timeout")

    @property
    @pulumi.getter(name="tcpTimeout")
    def tcp_timeout(self) -> int:
        """
        timeout in seconds. Value must be between 0 and 604800.
        """
        return pulumi.get(self, "tcp_timeout")

    @property
    @pulumi.getter
    def technology(self) -> str:
        """
        The Technology param. String length must not exceed 63 characters.
        """
        return pulumi.get(self, "technology")

    @property
    @pulumi.getter
    def tfid(self) -> str:
        return pulumi.get(self, "tfid")

    @property
    @pulumi.getter
    def timeout(self) -> int:
        """
        timeout in seconds. Value must be between 0 and 604800.
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter(name="tunnelApplications")
    def tunnel_applications(self) -> bool:
        """
        The TunnelApplications param.
        """
        return pulumi.get(self, "tunnel_applications")

    @property
    @pulumi.getter(name="tunnelOtherApplication")
    def tunnel_other_application(self) -> bool:
        """
        The TunnelOtherApplication param.
        """
        return pulumi.get(self, "tunnel_other_application")

    @property
    @pulumi.getter(name="udpTimeout")
    def udp_timeout(self) -> int:
        """
        timeout in seconds. Value must be between 0 and 604800.
        """
        return pulumi.get(self, "udp_timeout")

    @property
    @pulumi.getter(name="usedByMalware")
    def used_by_malware(self) -> bool:
        """
        The UsedByMalware param.
        """
        return pulumi.get(self, "used_by_malware")

    @property
    @pulumi.getter(name="virusIdent")
    def virus_ident(self) -> bool:
        """
        The VirusIdent param.
        """
        return pulumi.get(self, "virus_ident")


class AwaitableGetApplicationResult(GetApplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationResult(
            able_to_transfer_file=self.able_to_transfer_file,
            alg_disable_capability=self.alg_disable_capability,
            category=self.category,
            consume_big_bandwidth=self.consume_big_bandwidth,
            data_ident=self.data_ident,
            default=self.default,
            description=self.description,
            evasive_behavior=self.evasive_behavior,
            file_type_ident=self.file_type_ident,
            has_known_vulnerability=self.has_known_vulnerability,
            id=self.id,
            name=self.name,
            no_appid_caching=self.no_appid_caching,
            parent_app=self.parent_app,
            pervasive_use=self.pervasive_use,
            prone_to_misuse=self.prone_to_misuse,
            risk=self.risk,
            signatures=self.signatures,
            subcategory=self.subcategory,
            tcp_half_closed_timeout=self.tcp_half_closed_timeout,
            tcp_time_wait_timeout=self.tcp_time_wait_timeout,
            tcp_timeout=self.tcp_timeout,
            technology=self.technology,
            tfid=self.tfid,
            timeout=self.timeout,
            tunnel_applications=self.tunnel_applications,
            tunnel_other_application=self.tunnel_other_application,
            udp_timeout=self.udp_timeout,
            used_by_malware=self.used_by_malware,
            virus_ident=self.virus_ident)


def get_application(id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationResult:
    """
    Retrieves a config item.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scm as scm

    example = scm.get_application(id="1234-56-789")
    ```


    :param str id: The Id param.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('scm:index/getApplication:getApplication', __args__, opts=opts, typ=GetApplicationResult).value

    return AwaitableGetApplicationResult(
        able_to_transfer_file=pulumi.get(__ret__, 'able_to_transfer_file'),
        alg_disable_capability=pulumi.get(__ret__, 'alg_disable_capability'),
        category=pulumi.get(__ret__, 'category'),
        consume_big_bandwidth=pulumi.get(__ret__, 'consume_big_bandwidth'),
        data_ident=pulumi.get(__ret__, 'data_ident'),
        default=pulumi.get(__ret__, 'default'),
        description=pulumi.get(__ret__, 'description'),
        evasive_behavior=pulumi.get(__ret__, 'evasive_behavior'),
        file_type_ident=pulumi.get(__ret__, 'file_type_ident'),
        has_known_vulnerability=pulumi.get(__ret__, 'has_known_vulnerability'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        no_appid_caching=pulumi.get(__ret__, 'no_appid_caching'),
        parent_app=pulumi.get(__ret__, 'parent_app'),
        pervasive_use=pulumi.get(__ret__, 'pervasive_use'),
        prone_to_misuse=pulumi.get(__ret__, 'prone_to_misuse'),
        risk=pulumi.get(__ret__, 'risk'),
        signatures=pulumi.get(__ret__, 'signatures'),
        subcategory=pulumi.get(__ret__, 'subcategory'),
        tcp_half_closed_timeout=pulumi.get(__ret__, 'tcp_half_closed_timeout'),
        tcp_time_wait_timeout=pulumi.get(__ret__, 'tcp_time_wait_timeout'),
        tcp_timeout=pulumi.get(__ret__, 'tcp_timeout'),
        technology=pulumi.get(__ret__, 'technology'),
        tfid=pulumi.get(__ret__, 'tfid'),
        timeout=pulumi.get(__ret__, 'timeout'),
        tunnel_applications=pulumi.get(__ret__, 'tunnel_applications'),
        tunnel_other_application=pulumi.get(__ret__, 'tunnel_other_application'),
        udp_timeout=pulumi.get(__ret__, 'udp_timeout'),
        used_by_malware=pulumi.get(__ret__, 'used_by_malware'),
        virus_ident=pulumi.get(__ret__, 'virus_ident'))


@_utilities.lift_output_func(get_application)
def get_application_output(id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationResult]:
    """
    Retrieves a config item.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scm as scm

    example = scm.get_application(id="1234-56-789")
    ```


    :param str id: The Id param.
    """
    ...
