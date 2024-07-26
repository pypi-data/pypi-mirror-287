# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetLocalUserResult',
    'AwaitableGetLocalUserResult',
    'get_local_user',
    'get_local_user_output',
]

@pulumi.output_type
class GetLocalUserResult:
    """
    A collection of values returned by getLocalUser.
    """
    def __init__(__self__, disabled=None, id=None, name=None, password=None, tfid=None):
        if disabled and not isinstance(disabled, bool):
            raise TypeError("Expected argument 'disabled' to be a bool")
        pulumi.set(__self__, "disabled", disabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if password and not isinstance(password, str):
            raise TypeError("Expected argument 'password' to be a str")
        pulumi.set(__self__, "password", password)
        if tfid and not isinstance(tfid, str):
            raise TypeError("Expected argument 'tfid' to be a str")
        pulumi.set(__self__, "tfid", tfid)

    @property
    @pulumi.getter
    def disabled(self) -> bool:
        """
        The Disabled param.
        """
        return pulumi.get(self, "disabled")

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
        The Name param. String length must not exceed 31 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        The Password param. String length must not exceed 63 characters.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def tfid(self) -> str:
        return pulumi.get(self, "tfid")


class AwaitableGetLocalUserResult(GetLocalUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocalUserResult(
            disabled=self.disabled,
            id=self.id,
            name=self.name,
            password=self.password,
            tfid=self.tfid)


def get_local_user(id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocalUserResult:
    """
    Retrieves a config item.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scm as scm

    example = scm.get_local_user(id="1234-56-789")
    ```


    :param str id: The Id param.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('scm:index/getLocalUser:getLocalUser', __args__, opts=opts, typ=GetLocalUserResult).value

    return AwaitableGetLocalUserResult(
        disabled=pulumi.get(__ret__, 'disabled'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        password=pulumi.get(__ret__, 'password'),
        tfid=pulumi.get(__ret__, 'tfid'))


@_utilities.lift_output_func(get_local_user)
def get_local_user_output(id: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLocalUserResult]:
    """
    Retrieves a config item.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scm as scm

    example = scm.get_local_user(id="1234-56-789")
    ```


    :param str id: The Id param.
    """
    ...
