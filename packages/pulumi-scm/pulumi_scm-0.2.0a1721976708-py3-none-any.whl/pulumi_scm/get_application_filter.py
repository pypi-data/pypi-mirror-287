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
    'GetApplicationFilterResult',
    'AwaitableGetApplicationFilterResult',
    'get_application_filter',
    'get_application_filter_output',
]

@pulumi.output_type
class GetApplicationFilterResult:
    """
    A collection of values returned by getApplicationFilter.
    """
    def __init__(__self__, categories=None, evasive=None, excessive_bandwidth_use=None, excludes=None, has_known_vulnerabilities=None, id=None, is_saas=None, name=None, new_appid=None, pervasive=None, prone_to_misuse=None, risks=None, saas_certifications=None, saas_risks=None, subcategories=None, tagging=None, technologies=None, tfid=None, transfers_files=None, tunnels_other_apps=None, used_by_malware=None):
        if categories and not isinstance(categories, list):
            raise TypeError("Expected argument 'categories' to be a list")
        pulumi.set(__self__, "categories", categories)
        if evasive and not isinstance(evasive, bool):
            raise TypeError("Expected argument 'evasive' to be a bool")
        pulumi.set(__self__, "evasive", evasive)
        if excessive_bandwidth_use and not isinstance(excessive_bandwidth_use, bool):
            raise TypeError("Expected argument 'excessive_bandwidth_use' to be a bool")
        pulumi.set(__self__, "excessive_bandwidth_use", excessive_bandwidth_use)
        if excludes and not isinstance(excludes, list):
            raise TypeError("Expected argument 'excludes' to be a list")
        pulumi.set(__self__, "excludes", excludes)
        if has_known_vulnerabilities and not isinstance(has_known_vulnerabilities, bool):
            raise TypeError("Expected argument 'has_known_vulnerabilities' to be a bool")
        pulumi.set(__self__, "has_known_vulnerabilities", has_known_vulnerabilities)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_saas and not isinstance(is_saas, bool):
            raise TypeError("Expected argument 'is_saas' to be a bool")
        pulumi.set(__self__, "is_saas", is_saas)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if new_appid and not isinstance(new_appid, bool):
            raise TypeError("Expected argument 'new_appid' to be a bool")
        pulumi.set(__self__, "new_appid", new_appid)
        if pervasive and not isinstance(pervasive, bool):
            raise TypeError("Expected argument 'pervasive' to be a bool")
        pulumi.set(__self__, "pervasive", pervasive)
        if prone_to_misuse and not isinstance(prone_to_misuse, bool):
            raise TypeError("Expected argument 'prone_to_misuse' to be a bool")
        pulumi.set(__self__, "prone_to_misuse", prone_to_misuse)
        if risks and not isinstance(risks, list):
            raise TypeError("Expected argument 'risks' to be a list")
        pulumi.set(__self__, "risks", risks)
        if saas_certifications and not isinstance(saas_certifications, list):
            raise TypeError("Expected argument 'saas_certifications' to be a list")
        pulumi.set(__self__, "saas_certifications", saas_certifications)
        if saas_risks and not isinstance(saas_risks, list):
            raise TypeError("Expected argument 'saas_risks' to be a list")
        pulumi.set(__self__, "saas_risks", saas_risks)
        if subcategories and not isinstance(subcategories, list):
            raise TypeError("Expected argument 'subcategories' to be a list")
        pulumi.set(__self__, "subcategories", subcategories)
        if tagging and not isinstance(tagging, dict):
            raise TypeError("Expected argument 'tagging' to be a dict")
        pulumi.set(__self__, "tagging", tagging)
        if technologies and not isinstance(technologies, list):
            raise TypeError("Expected argument 'technologies' to be a list")
        pulumi.set(__self__, "technologies", technologies)
        if tfid and not isinstance(tfid, str):
            raise TypeError("Expected argument 'tfid' to be a str")
        pulumi.set(__self__, "tfid", tfid)
        if transfers_files and not isinstance(transfers_files, bool):
            raise TypeError("Expected argument 'transfers_files' to be a bool")
        pulumi.set(__self__, "transfers_files", transfers_files)
        if tunnels_other_apps and not isinstance(tunnels_other_apps, bool):
            raise TypeError("Expected argument 'tunnels_other_apps' to be a bool")
        pulumi.set(__self__, "tunnels_other_apps", tunnels_other_apps)
        if used_by_malware and not isinstance(used_by_malware, bool):
            raise TypeError("Expected argument 'used_by_malware' to be a bool")
        pulumi.set(__self__, "used_by_malware", used_by_malware)

    @property
    @pulumi.getter
    def categories(self) -> Sequence[str]:
        """
        The Categories param. Individual elements in this list are subject to additional validation. String length must not exceed 128 characters.
        """
        return pulumi.get(self, "categories")

    @property
    @pulumi.getter
    def evasive(self) -> bool:
        """
        only True is a valid value.
        """
        return pulumi.get(self, "evasive")

    @property
    @pulumi.getter(name="excessiveBandwidthUse")
    def excessive_bandwidth_use(self) -> bool:
        """
        only True is a valid value.
        """
        return pulumi.get(self, "excessive_bandwidth_use")

    @property
    @pulumi.getter
    def excludes(self) -> Sequence[str]:
        """
        The Excludes param. Individual elements in this list are subject to additional validation. String length must not exceed 63 characters.
        """
        return pulumi.get(self, "excludes")

    @property
    @pulumi.getter(name="hasKnownVulnerabilities")
    def has_known_vulnerabilities(self) -> bool:
        """
        only True is a valid value.
        """
        return pulumi.get(self, "has_known_vulnerabilities")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The Id param.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isSaas")
    def is_saas(self) -> bool:
        """
        only True is a valid value.
        """
        return pulumi.get(self, "is_saas")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Alphanumeric string [ 0-9a-zA-Z._-]. String length must not exceed 31 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="newAppid")
    def new_appid(self) -> bool:
        """
        only True is a valid value.
        """
        return pulumi.get(self, "new_appid")

    @property
    @pulumi.getter
    def pervasive(self) -> bool:
        """
        only True is a valid value.
        """
        return pulumi.get(self, "pervasive")

    @property
    @pulumi.getter(name="proneToMisuse")
    def prone_to_misuse(self) -> bool:
        """
        only True is a valid value.
        """
        return pulumi.get(self, "prone_to_misuse")

    @property
    @pulumi.getter
    def risks(self) -> Sequence[int]:
        """
        The Risks param. Individual elements in this list are subject to additional validation. Value must be between 1 and 5.
        """
        return pulumi.get(self, "risks")

    @property
    @pulumi.getter(name="saasCertifications")
    def saas_certifications(self) -> Sequence[str]:
        """
        The SaasCertifications param. Individual elements in this list are subject to additional validation. String length must not exceed 32 characters.
        """
        return pulumi.get(self, "saas_certifications")

    @property
    @pulumi.getter(name="saasRisks")
    def saas_risks(self) -> Sequence[str]:
        """
        The SaasRisks param. Individual elements in this list are subject to additional validation. String length must not exceed 32 characters.
        """
        return pulumi.get(self, "saas_risks")

    @property
    @pulumi.getter
    def subcategories(self) -> Sequence[str]:
        """
        The Subcategories param. Individual elements in this list are subject to additional validation. String length must not exceed 128 characters.
        """
        return pulumi.get(self, "subcategories")

    @property
    @pulumi.getter
    def tagging(self) -> 'outputs.GetApplicationFilterTaggingResult':
        """
        The Tagging param.
        """
        return pulumi.get(self, "tagging")

    @property
    @pulumi.getter
    def technologies(self) -> Sequence[str]:
        """
        The Technologies param. Individual elements in this list are subject to additional validation. String length must not exceed 128 characters.
        """
        return pulumi.get(self, "technologies")

    @property
    @pulumi.getter
    def tfid(self) -> str:
        return pulumi.get(self, "tfid")

    @property
    @pulumi.getter(name="transfersFiles")
    def transfers_files(self) -> bool:
        """
        only True is a valid value.
        """
        return pulumi.get(self, "transfers_files")

    @property
    @pulumi.getter(name="tunnelsOtherApps")
    def tunnels_other_apps(self) -> bool:
        """
        only True is a valid value.
        """
        return pulumi.get(self, "tunnels_other_apps")

    @property
    @pulumi.getter(name="usedByMalware")
    def used_by_malware(self) -> bool:
        """
        only True is a valid value.
        """
        return pulumi.get(self, "used_by_malware")


class AwaitableGetApplicationFilterResult(GetApplicationFilterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationFilterResult(
            categories=self.categories,
            evasive=self.evasive,
            excessive_bandwidth_use=self.excessive_bandwidth_use,
            excludes=self.excludes,
            has_known_vulnerabilities=self.has_known_vulnerabilities,
            id=self.id,
            is_saas=self.is_saas,
            name=self.name,
            new_appid=self.new_appid,
            pervasive=self.pervasive,
            prone_to_misuse=self.prone_to_misuse,
            risks=self.risks,
            saas_certifications=self.saas_certifications,
            saas_risks=self.saas_risks,
            subcategories=self.subcategories,
            tagging=self.tagging,
            technologies=self.technologies,
            tfid=self.tfid,
            transfers_files=self.transfers_files,
            tunnels_other_apps=self.tunnels_other_apps,
            used_by_malware=self.used_by_malware)


def get_application_filter(id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationFilterResult:
    """
    Retrieves a config item.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scm as scm

    example = scm.get_application_filter(id="1234-56-789")
    ```


    :param str id: The Id param.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('scm:index/getApplicationFilter:getApplicationFilter', __args__, opts=opts, typ=GetApplicationFilterResult).value

    return AwaitableGetApplicationFilterResult(
        categories=pulumi.get(__ret__, 'categories'),
        evasive=pulumi.get(__ret__, 'evasive'),
        excessive_bandwidth_use=pulumi.get(__ret__, 'excessive_bandwidth_use'),
        excludes=pulumi.get(__ret__, 'excludes'),
        has_known_vulnerabilities=pulumi.get(__ret__, 'has_known_vulnerabilities'),
        id=pulumi.get(__ret__, 'id'),
        is_saas=pulumi.get(__ret__, 'is_saas'),
        name=pulumi.get(__ret__, 'name'),
        new_appid=pulumi.get(__ret__, 'new_appid'),
        pervasive=pulumi.get(__ret__, 'pervasive'),
        prone_to_misuse=pulumi.get(__ret__, 'prone_to_misuse'),
        risks=pulumi.get(__ret__, 'risks'),
        saas_certifications=pulumi.get(__ret__, 'saas_certifications'),
        saas_risks=pulumi.get(__ret__, 'saas_risks'),
        subcategories=pulumi.get(__ret__, 'subcategories'),
        tagging=pulumi.get(__ret__, 'tagging'),
        technologies=pulumi.get(__ret__, 'technologies'),
        tfid=pulumi.get(__ret__, 'tfid'),
        transfers_files=pulumi.get(__ret__, 'transfers_files'),
        tunnels_other_apps=pulumi.get(__ret__, 'tunnels_other_apps'),
        used_by_malware=pulumi.get(__ret__, 'used_by_malware'))


@_utilities.lift_output_func(get_application_filter)
def get_application_filter_output(id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationFilterResult]:
    """
    Retrieves a config item.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scm as scm

    example = scm.get_application_filter(id="1234-56-789")
    ```


    :param str id: The Id param.
    """
    ...
