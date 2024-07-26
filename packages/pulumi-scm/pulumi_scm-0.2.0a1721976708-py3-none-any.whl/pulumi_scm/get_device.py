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
    'GetDeviceResult',
    'AwaitableGetDeviceResult',
    'get_device',
    'get_device_output',
]

@pulumi.output_type
class GetDeviceResult:
    """
    A collection of values returned by getDevice.
    """
    def __init__(__self__, anti_virus_version=None, app_release_date=None, app_version=None, av_release_date=None, available_licensesses=None, connected_since=None, dev_cert_detail=None, dev_cert_expiry_date=None, family=None, gp_client_verion=None, gp_data_version=None, ha_peer_serial=None, ha_peer_state=None, ha_state=None, hostname=None, id=None, installed_licenses=None, iot_release_date=None, iot_version=None, ip_address=None, ip_v6_address=None, is_connected=None, license_match=None, log_db_version=None, mac_address=None, model=None, serial=None, software_version=None, tfid=None, threat_release_date=None, threat_version=None, uptime=None, url_db_type=None, url_db_ver=None, vm_state=None, wf_release_date=None, wf_ver=None):
        if anti_virus_version and not isinstance(anti_virus_version, str):
            raise TypeError("Expected argument 'anti_virus_version' to be a str")
        pulumi.set(__self__, "anti_virus_version", anti_virus_version)
        if app_release_date and not isinstance(app_release_date, str):
            raise TypeError("Expected argument 'app_release_date' to be a str")
        pulumi.set(__self__, "app_release_date", app_release_date)
        if app_version and not isinstance(app_version, str):
            raise TypeError("Expected argument 'app_version' to be a str")
        pulumi.set(__self__, "app_version", app_version)
        if av_release_date and not isinstance(av_release_date, str):
            raise TypeError("Expected argument 'av_release_date' to be a str")
        pulumi.set(__self__, "av_release_date", av_release_date)
        if available_licensesses and not isinstance(available_licensesses, list):
            raise TypeError("Expected argument 'available_licensesses' to be a list")
        pulumi.set(__self__, "available_licensesses", available_licensesses)
        if connected_since and not isinstance(connected_since, str):
            raise TypeError("Expected argument 'connected_since' to be a str")
        pulumi.set(__self__, "connected_since", connected_since)
        if dev_cert_detail and not isinstance(dev_cert_detail, str):
            raise TypeError("Expected argument 'dev_cert_detail' to be a str")
        pulumi.set(__self__, "dev_cert_detail", dev_cert_detail)
        if dev_cert_expiry_date and not isinstance(dev_cert_expiry_date, str):
            raise TypeError("Expected argument 'dev_cert_expiry_date' to be a str")
        pulumi.set(__self__, "dev_cert_expiry_date", dev_cert_expiry_date)
        if family and not isinstance(family, str):
            raise TypeError("Expected argument 'family' to be a str")
        pulumi.set(__self__, "family", family)
        if gp_client_verion and not isinstance(gp_client_verion, str):
            raise TypeError("Expected argument 'gp_client_verion' to be a str")
        pulumi.set(__self__, "gp_client_verion", gp_client_verion)
        if gp_data_version and not isinstance(gp_data_version, str):
            raise TypeError("Expected argument 'gp_data_version' to be a str")
        pulumi.set(__self__, "gp_data_version", gp_data_version)
        if ha_peer_serial and not isinstance(ha_peer_serial, str):
            raise TypeError("Expected argument 'ha_peer_serial' to be a str")
        pulumi.set(__self__, "ha_peer_serial", ha_peer_serial)
        if ha_peer_state and not isinstance(ha_peer_state, str):
            raise TypeError("Expected argument 'ha_peer_state' to be a str")
        pulumi.set(__self__, "ha_peer_state", ha_peer_state)
        if ha_state and not isinstance(ha_state, str):
            raise TypeError("Expected argument 'ha_state' to be a str")
        pulumi.set(__self__, "ha_state", ha_state)
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if installed_licenses and not isinstance(installed_licenses, list):
            raise TypeError("Expected argument 'installed_licenses' to be a list")
        pulumi.set(__self__, "installed_licenses", installed_licenses)
        if iot_release_date and not isinstance(iot_release_date, str):
            raise TypeError("Expected argument 'iot_release_date' to be a str")
        pulumi.set(__self__, "iot_release_date", iot_release_date)
        if iot_version and not isinstance(iot_version, str):
            raise TypeError("Expected argument 'iot_version' to be a str")
        pulumi.set(__self__, "iot_version", iot_version)
        if ip_address and not isinstance(ip_address, str):
            raise TypeError("Expected argument 'ip_address' to be a str")
        pulumi.set(__self__, "ip_address", ip_address)
        if ip_v6_address and not isinstance(ip_v6_address, str):
            raise TypeError("Expected argument 'ip_v6_address' to be a str")
        pulumi.set(__self__, "ip_v6_address", ip_v6_address)
        if is_connected and not isinstance(is_connected, bool):
            raise TypeError("Expected argument 'is_connected' to be a bool")
        pulumi.set(__self__, "is_connected", is_connected)
        if license_match and not isinstance(license_match, bool):
            raise TypeError("Expected argument 'license_match' to be a bool")
        pulumi.set(__self__, "license_match", license_match)
        if log_db_version and not isinstance(log_db_version, str):
            raise TypeError("Expected argument 'log_db_version' to be a str")
        pulumi.set(__self__, "log_db_version", log_db_version)
        if mac_address and not isinstance(mac_address, str):
            raise TypeError("Expected argument 'mac_address' to be a str")
        pulumi.set(__self__, "mac_address", mac_address)
        if model and not isinstance(model, str):
            raise TypeError("Expected argument 'model' to be a str")
        pulumi.set(__self__, "model", model)
        if serial and not isinstance(serial, str):
            raise TypeError("Expected argument 'serial' to be a str")
        pulumi.set(__self__, "serial", serial)
        if software_version and not isinstance(software_version, str):
            raise TypeError("Expected argument 'software_version' to be a str")
        pulumi.set(__self__, "software_version", software_version)
        if tfid and not isinstance(tfid, str):
            raise TypeError("Expected argument 'tfid' to be a str")
        pulumi.set(__self__, "tfid", tfid)
        if threat_release_date and not isinstance(threat_release_date, str):
            raise TypeError("Expected argument 'threat_release_date' to be a str")
        pulumi.set(__self__, "threat_release_date", threat_release_date)
        if threat_version and not isinstance(threat_version, str):
            raise TypeError("Expected argument 'threat_version' to be a str")
        pulumi.set(__self__, "threat_version", threat_version)
        if uptime and not isinstance(uptime, str):
            raise TypeError("Expected argument 'uptime' to be a str")
        pulumi.set(__self__, "uptime", uptime)
        if url_db_type and not isinstance(url_db_type, str):
            raise TypeError("Expected argument 'url_db_type' to be a str")
        pulumi.set(__self__, "url_db_type", url_db_type)
        if url_db_ver and not isinstance(url_db_ver, str):
            raise TypeError("Expected argument 'url_db_ver' to be a str")
        pulumi.set(__self__, "url_db_ver", url_db_ver)
        if vm_state and not isinstance(vm_state, str):
            raise TypeError("Expected argument 'vm_state' to be a str")
        pulumi.set(__self__, "vm_state", vm_state)
        if wf_release_date and not isinstance(wf_release_date, str):
            raise TypeError("Expected argument 'wf_release_date' to be a str")
        pulumi.set(__self__, "wf_release_date", wf_release_date)
        if wf_ver and not isinstance(wf_ver, str):
            raise TypeError("Expected argument 'wf_ver' to be a str")
        pulumi.set(__self__, "wf_ver", wf_ver)

    @property
    @pulumi.getter(name="antiVirusVersion")
    def anti_virus_version(self) -> str:
        """
        The AntiVirusVersion param.
        """
        return pulumi.get(self, "anti_virus_version")

    @property
    @pulumi.getter(name="appReleaseDate")
    def app_release_date(self) -> str:
        """
        The AppReleaseDate param.
        """
        return pulumi.get(self, "app_release_date")

    @property
    @pulumi.getter(name="appVersion")
    def app_version(self) -> str:
        """
        The AppVersion param.
        """
        return pulumi.get(self, "app_version")

    @property
    @pulumi.getter(name="avReleaseDate")
    def av_release_date(self) -> str:
        """
        The AvReleaseDate param.
        """
        return pulumi.get(self, "av_release_date")

    @property
    @pulumi.getter(name="availableLicensesses")
    def available_licensesses(self) -> Sequence['outputs.GetDeviceAvailableLicensessResult']:
        """
        The AvailableLicensess param.
        """
        return pulumi.get(self, "available_licensesses")

    @property
    @pulumi.getter(name="connectedSince")
    def connected_since(self) -> str:
        """
        The ConnectedSince param.
        """
        return pulumi.get(self, "connected_since")

    @property
    @pulumi.getter(name="devCertDetail")
    def dev_cert_detail(self) -> str:
        """
        The DevCertDetail param.
        """
        return pulumi.get(self, "dev_cert_detail")

    @property
    @pulumi.getter(name="devCertExpiryDate")
    def dev_cert_expiry_date(self) -> str:
        """
        The DevCertExpiryDate param.
        """
        return pulumi.get(self, "dev_cert_expiry_date")

    @property
    @pulumi.getter
    def family(self) -> str:
        """
        The Family param.
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter(name="gpClientVerion")
    def gp_client_verion(self) -> str:
        """
        The GpClientVerion param.
        """
        return pulumi.get(self, "gp_client_verion")

    @property
    @pulumi.getter(name="gpDataVersion")
    def gp_data_version(self) -> str:
        """
        The GpDataVersion param.
        """
        return pulumi.get(self, "gp_data_version")

    @property
    @pulumi.getter(name="haPeerSerial")
    def ha_peer_serial(self) -> str:
        """
        The HaPeerSerial param.
        """
        return pulumi.get(self, "ha_peer_serial")

    @property
    @pulumi.getter(name="haPeerState")
    def ha_peer_state(self) -> str:
        """
        The HaPeerState param.
        """
        return pulumi.get(self, "ha_peer_state")

    @property
    @pulumi.getter(name="haState")
    def ha_state(self) -> str:
        """
        The HaState param.
        """
        return pulumi.get(self, "ha_state")

    @property
    @pulumi.getter
    def hostname(self) -> str:
        """
        The Hostname param.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The Id param.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="installedLicenses")
    def installed_licenses(self) -> Sequence['outputs.GetDeviceInstalledLicenseResult']:
        """
        The InstalledLicenses param.
        """
        return pulumi.get(self, "installed_licenses")

    @property
    @pulumi.getter(name="iotReleaseDate")
    def iot_release_date(self) -> str:
        """
        The IotReleaseDate param.
        """
        return pulumi.get(self, "iot_release_date")

    @property
    @pulumi.getter(name="iotVersion")
    def iot_version(self) -> str:
        """
        The IotVersion param.
        """
        return pulumi.get(self, "iot_version")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        """
        The IpAddress param.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="ipV6Address")
    def ip_v6_address(self) -> str:
        """
        The IpV6Address param.
        """
        return pulumi.get(self, "ip_v6_address")

    @property
    @pulumi.getter(name="isConnected")
    def is_connected(self) -> bool:
        """
        The IsConnected param.
        """
        return pulumi.get(self, "is_connected")

    @property
    @pulumi.getter(name="licenseMatch")
    def license_match(self) -> bool:
        """
        The LicenseMatch param.
        """
        return pulumi.get(self, "license_match")

    @property
    @pulumi.getter(name="logDbVersion")
    def log_db_version(self) -> str:
        """
        The LogDbVersion param.
        """
        return pulumi.get(self, "log_db_version")

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> str:
        """
        The MacAddress param.
        """
        return pulumi.get(self, "mac_address")

    @property
    @pulumi.getter
    def model(self) -> str:
        """
        The Model param.
        """
        return pulumi.get(self, "model")

    @property
    @pulumi.getter
    def serial(self) -> str:
        """
        The Serial param.
        """
        return pulumi.get(self, "serial")

    @property
    @pulumi.getter(name="softwareVersion")
    def software_version(self) -> str:
        """
        The SoftwareVersion param.
        """
        return pulumi.get(self, "software_version")

    @property
    @pulumi.getter
    def tfid(self) -> str:
        return pulumi.get(self, "tfid")

    @property
    @pulumi.getter(name="threatReleaseDate")
    def threat_release_date(self) -> str:
        """
        The ThreatReleaseDate param.
        """
        return pulumi.get(self, "threat_release_date")

    @property
    @pulumi.getter(name="threatVersion")
    def threat_version(self) -> str:
        """
        The ThreatVersion param.
        """
        return pulumi.get(self, "threat_version")

    @property
    @pulumi.getter
    def uptime(self) -> str:
        """
        The Uptime param.
        """
        return pulumi.get(self, "uptime")

    @property
    @pulumi.getter(name="urlDbType")
    def url_db_type(self) -> str:
        """
        The UrlDbType param.
        """
        return pulumi.get(self, "url_db_type")

    @property
    @pulumi.getter(name="urlDbVer")
    def url_db_ver(self) -> str:
        """
        The UrlDbVer param.
        """
        return pulumi.get(self, "url_db_ver")

    @property
    @pulumi.getter(name="vmState")
    def vm_state(self) -> str:
        """
        The VmState param.
        """
        return pulumi.get(self, "vm_state")

    @property
    @pulumi.getter(name="wfReleaseDate")
    def wf_release_date(self) -> str:
        """
        The WfReleaseDate param.
        """
        return pulumi.get(self, "wf_release_date")

    @property
    @pulumi.getter(name="wfVer")
    def wf_ver(self) -> str:
        """
        The WfVer param.
        """
        return pulumi.get(self, "wf_ver")


class AwaitableGetDeviceResult(GetDeviceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeviceResult(
            anti_virus_version=self.anti_virus_version,
            app_release_date=self.app_release_date,
            app_version=self.app_version,
            av_release_date=self.av_release_date,
            available_licensesses=self.available_licensesses,
            connected_since=self.connected_since,
            dev_cert_detail=self.dev_cert_detail,
            dev_cert_expiry_date=self.dev_cert_expiry_date,
            family=self.family,
            gp_client_verion=self.gp_client_verion,
            gp_data_version=self.gp_data_version,
            ha_peer_serial=self.ha_peer_serial,
            ha_peer_state=self.ha_peer_state,
            ha_state=self.ha_state,
            hostname=self.hostname,
            id=self.id,
            installed_licenses=self.installed_licenses,
            iot_release_date=self.iot_release_date,
            iot_version=self.iot_version,
            ip_address=self.ip_address,
            ip_v6_address=self.ip_v6_address,
            is_connected=self.is_connected,
            license_match=self.license_match,
            log_db_version=self.log_db_version,
            mac_address=self.mac_address,
            model=self.model,
            serial=self.serial,
            software_version=self.software_version,
            tfid=self.tfid,
            threat_release_date=self.threat_release_date,
            threat_version=self.threat_version,
            uptime=self.uptime,
            url_db_type=self.url_db_type,
            url_db_ver=self.url_db_ver,
            vm_state=self.vm_state,
            wf_release_date=self.wf_release_date,
            wf_ver=self.wf_ver)


def get_device(serial: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeviceResult:
    """
    Retrieves a config item.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scm as scm

    example = scm.get_device(serial="12345")
    ```


    :param str serial: The Serial param.
    """
    __args__ = dict()
    __args__['serial'] = serial
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('scm:index/getDevice:getDevice', __args__, opts=opts, typ=GetDeviceResult).value

    return AwaitableGetDeviceResult(
        anti_virus_version=pulumi.get(__ret__, 'anti_virus_version'),
        app_release_date=pulumi.get(__ret__, 'app_release_date'),
        app_version=pulumi.get(__ret__, 'app_version'),
        av_release_date=pulumi.get(__ret__, 'av_release_date'),
        available_licensesses=pulumi.get(__ret__, 'available_licensesses'),
        connected_since=pulumi.get(__ret__, 'connected_since'),
        dev_cert_detail=pulumi.get(__ret__, 'dev_cert_detail'),
        dev_cert_expiry_date=pulumi.get(__ret__, 'dev_cert_expiry_date'),
        family=pulumi.get(__ret__, 'family'),
        gp_client_verion=pulumi.get(__ret__, 'gp_client_verion'),
        gp_data_version=pulumi.get(__ret__, 'gp_data_version'),
        ha_peer_serial=pulumi.get(__ret__, 'ha_peer_serial'),
        ha_peer_state=pulumi.get(__ret__, 'ha_peer_state'),
        ha_state=pulumi.get(__ret__, 'ha_state'),
        hostname=pulumi.get(__ret__, 'hostname'),
        id=pulumi.get(__ret__, 'id'),
        installed_licenses=pulumi.get(__ret__, 'installed_licenses'),
        iot_release_date=pulumi.get(__ret__, 'iot_release_date'),
        iot_version=pulumi.get(__ret__, 'iot_version'),
        ip_address=pulumi.get(__ret__, 'ip_address'),
        ip_v6_address=pulumi.get(__ret__, 'ip_v6_address'),
        is_connected=pulumi.get(__ret__, 'is_connected'),
        license_match=pulumi.get(__ret__, 'license_match'),
        log_db_version=pulumi.get(__ret__, 'log_db_version'),
        mac_address=pulumi.get(__ret__, 'mac_address'),
        model=pulumi.get(__ret__, 'model'),
        serial=pulumi.get(__ret__, 'serial'),
        software_version=pulumi.get(__ret__, 'software_version'),
        tfid=pulumi.get(__ret__, 'tfid'),
        threat_release_date=pulumi.get(__ret__, 'threat_release_date'),
        threat_version=pulumi.get(__ret__, 'threat_version'),
        uptime=pulumi.get(__ret__, 'uptime'),
        url_db_type=pulumi.get(__ret__, 'url_db_type'),
        url_db_ver=pulumi.get(__ret__, 'url_db_ver'),
        vm_state=pulumi.get(__ret__, 'vm_state'),
        wf_release_date=pulumi.get(__ret__, 'wf_release_date'),
        wf_ver=pulumi.get(__ret__, 'wf_ver'))


@_utilities.lift_output_func(get_device)
def get_device_output(serial: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeviceResult]:
    """
    Retrieves a config item.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scm as scm

    example = scm.get_device(serial="12345")
    ```


    :param str serial: The Serial param.
    """
    ...
