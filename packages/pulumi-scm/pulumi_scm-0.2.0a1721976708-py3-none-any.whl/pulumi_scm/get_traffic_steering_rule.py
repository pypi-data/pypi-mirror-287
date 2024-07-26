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
    'GetTrafficSteeringRuleResult',
    'AwaitableGetTrafficSteeringRuleResult',
    'get_traffic_steering_rule',
    'get_traffic_steering_rule_output',
]

@pulumi.output_type
class GetTrafficSteeringRuleResult:
    """
    A collection of values returned by getTrafficSteeringRule.
    """
    def __init__(__self__, action=None, categories=None, destinations=None, id=None, name=None, services=None, source_users=None, sources=None, tfid=None):
        if action and not isinstance(action, dict):
            raise TypeError("Expected argument 'action' to be a dict")
        pulumi.set(__self__, "action", action)
        if categories and not isinstance(categories, list):
            raise TypeError("Expected argument 'categories' to be a list")
        pulumi.set(__self__, "categories", categories)
        if destinations and not isinstance(destinations, list):
            raise TypeError("Expected argument 'destinations' to be a list")
        pulumi.set(__self__, "destinations", destinations)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if services and not isinstance(services, list):
            raise TypeError("Expected argument 'services' to be a list")
        pulumi.set(__self__, "services", services)
        if source_users and not isinstance(source_users, list):
            raise TypeError("Expected argument 'source_users' to be a list")
        pulumi.set(__self__, "source_users", source_users)
        if sources and not isinstance(sources, list):
            raise TypeError("Expected argument 'sources' to be a list")
        pulumi.set(__self__, "sources", sources)
        if tfid and not isinstance(tfid, str):
            raise TypeError("Expected argument 'tfid' to be a str")
        pulumi.set(__self__, "tfid", tfid)

    @property
    @pulumi.getter
    def action(self) -> 'outputs.GetTrafficSteeringRuleActionResult':
        """
        The Action param.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def categories(self) -> Sequence[str]:
        """
        The Category param.
        """
        return pulumi.get(self, "categories")

    @property
    @pulumi.getter
    def destinations(self) -> Sequence[str]:
        """
        The Destination param.
        """
        return pulumi.get(self, "destinations")

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
        The Name param.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def services(self) -> Sequence[str]:
        """
        The Service param.
        """
        return pulumi.get(self, "services")

    @property
    @pulumi.getter(name="sourceUsers")
    def source_users(self) -> Sequence[str]:
        """
        The SourceUser param.
        """
        return pulumi.get(self, "source_users")

    @property
    @pulumi.getter
    def sources(self) -> Sequence[str]:
        """
        The Source param.
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter
    def tfid(self) -> str:
        return pulumi.get(self, "tfid")


class AwaitableGetTrafficSteeringRuleResult(GetTrafficSteeringRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTrafficSteeringRuleResult(
            action=self.action,
            categories=self.categories,
            destinations=self.destinations,
            id=self.id,
            name=self.name,
            services=self.services,
            source_users=self.source_users,
            sources=self.sources,
            tfid=self.tfid)


def get_traffic_steering_rule(id: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTrafficSteeringRuleResult:
    """
    Retrieves a config item.


    :param str id: The Id param.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('scm:index/getTrafficSteeringRule:getTrafficSteeringRule', __args__, opts=opts, typ=GetTrafficSteeringRuleResult).value

    return AwaitableGetTrafficSteeringRuleResult(
        action=pulumi.get(__ret__, 'action'),
        categories=pulumi.get(__ret__, 'categories'),
        destinations=pulumi.get(__ret__, 'destinations'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        services=pulumi.get(__ret__, 'services'),
        source_users=pulumi.get(__ret__, 'source_users'),
        sources=pulumi.get(__ret__, 'sources'),
        tfid=pulumi.get(__ret__, 'tfid'))


@_utilities.lift_output_func(get_traffic_steering_rule)
def get_traffic_steering_rule_output(id: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTrafficSteeringRuleResult]:
    """
    Retrieves a config item.


    :param str id: The Id param.
    """
    ...
