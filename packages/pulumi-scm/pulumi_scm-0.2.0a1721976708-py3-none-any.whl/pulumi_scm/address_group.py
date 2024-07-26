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

__all__ = ['AddressGroupArgs', 'AddressGroup']

@pulumi.input_type
class AddressGroupArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 device: Optional[pulumi.Input[str]] = None,
                 dynamic_value: Optional[pulumi.Input['AddressGroupDynamicValueArgs']] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 snippet: Optional[pulumi.Input[str]] = None,
                 static_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AddressGroup resource.
        :param pulumi.Input[str] description: The Description param. String length must not exceed 1023 characters.
        :param pulumi.Input[str] device: The Device param.
        :param pulumi.Input['AddressGroupDynamicValueArgs'] dynamic_value: The DynamicValue param. Ensure that only one of the following is specified: `dynamic`, `static`
        :param pulumi.Input[str] folder: The Folder param.
        :param pulumi.Input[str] name: Alphanumeric string [ 0-9a-zA-Z._-]. String length must not exceed 63 characters.
        :param pulumi.Input[str] snippet: The Snippet param.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] static_lists: The StaticList param. Individual elements in this list are subject to additional validation. String length must not exceed 63 characters. Ensure that only one of the following is specified: `dynamic`, `static`
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags for address group object. List must contain at most 64 elements. Individual elements in this list are subject to additional validation. String length must not exceed 127 characters.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if device is not None:
            pulumi.set(__self__, "device", device)
        if dynamic_value is not None:
            pulumi.set(__self__, "dynamic_value", dynamic_value)
        if folder is not None:
            pulumi.set(__self__, "folder", folder)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if snippet is not None:
            pulumi.set(__self__, "snippet", snippet)
        if static_lists is not None:
            pulumi.set(__self__, "static_lists", static_lists)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The Description param. String length must not exceed 1023 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def device(self) -> Optional[pulumi.Input[str]]:
        """
        The Device param.
        """
        return pulumi.get(self, "device")

    @device.setter
    def device(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device", value)

    @property
    @pulumi.getter(name="dynamicValue")
    def dynamic_value(self) -> Optional[pulumi.Input['AddressGroupDynamicValueArgs']]:
        """
        The DynamicValue param. Ensure that only one of the following is specified: `dynamic`, `static`
        """
        return pulumi.get(self, "dynamic_value")

    @dynamic_value.setter
    def dynamic_value(self, value: Optional[pulumi.Input['AddressGroupDynamicValueArgs']]):
        pulumi.set(self, "dynamic_value", value)

    @property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[str]]:
        """
        The Folder param.
        """
        return pulumi.get(self, "folder")

    @folder.setter
    def folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Alphanumeric string [ 0-9a-zA-Z._-]. String length must not exceed 63 characters.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def snippet(self) -> Optional[pulumi.Input[str]]:
        """
        The Snippet param.
        """
        return pulumi.get(self, "snippet")

    @snippet.setter
    def snippet(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snippet", value)

    @property
    @pulumi.getter(name="staticLists")
    def static_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The StaticList param. Individual elements in this list are subject to additional validation. String length must not exceed 63 characters. Ensure that only one of the following is specified: `dynamic`, `static`
        """
        return pulumi.get(self, "static_lists")

    @static_lists.setter
    def static_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "static_lists", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Tags for address group object. List must contain at most 64 elements. Individual elements in this list are subject to additional validation. String length must not exceed 127 characters.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _AddressGroupState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 device: Optional[pulumi.Input[str]] = None,
                 dynamic_value: Optional[pulumi.Input['AddressGroupDynamicValueArgs']] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 snippet: Optional[pulumi.Input[str]] = None,
                 static_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tfid: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AddressGroup resources.
        :param pulumi.Input[str] description: The Description param. String length must not exceed 1023 characters.
        :param pulumi.Input[str] device: The Device param.
        :param pulumi.Input['AddressGroupDynamicValueArgs'] dynamic_value: The DynamicValue param. Ensure that only one of the following is specified: `dynamic`, `static`
        :param pulumi.Input[str] folder: The Folder param.
        :param pulumi.Input[str] name: Alphanumeric string [ 0-9a-zA-Z._-]. String length must not exceed 63 characters.
        :param pulumi.Input[str] snippet: The Snippet param.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] static_lists: The StaticList param. Individual elements in this list are subject to additional validation. String length must not exceed 63 characters. Ensure that only one of the following is specified: `dynamic`, `static`
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags for address group object. List must contain at most 64 elements. Individual elements in this list are subject to additional validation. String length must not exceed 127 characters.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if device is not None:
            pulumi.set(__self__, "device", device)
        if dynamic_value is not None:
            pulumi.set(__self__, "dynamic_value", dynamic_value)
        if folder is not None:
            pulumi.set(__self__, "folder", folder)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if snippet is not None:
            pulumi.set(__self__, "snippet", snippet)
        if static_lists is not None:
            pulumi.set(__self__, "static_lists", static_lists)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tfid is not None:
            pulumi.set(__self__, "tfid", tfid)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The Description param. String length must not exceed 1023 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def device(self) -> Optional[pulumi.Input[str]]:
        """
        The Device param.
        """
        return pulumi.get(self, "device")

    @device.setter
    def device(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device", value)

    @property
    @pulumi.getter(name="dynamicValue")
    def dynamic_value(self) -> Optional[pulumi.Input['AddressGroupDynamicValueArgs']]:
        """
        The DynamicValue param. Ensure that only one of the following is specified: `dynamic`, `static`
        """
        return pulumi.get(self, "dynamic_value")

    @dynamic_value.setter
    def dynamic_value(self, value: Optional[pulumi.Input['AddressGroupDynamicValueArgs']]):
        pulumi.set(self, "dynamic_value", value)

    @property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[str]]:
        """
        The Folder param.
        """
        return pulumi.get(self, "folder")

    @folder.setter
    def folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Alphanumeric string [ 0-9a-zA-Z._-]. String length must not exceed 63 characters.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def snippet(self) -> Optional[pulumi.Input[str]]:
        """
        The Snippet param.
        """
        return pulumi.get(self, "snippet")

    @snippet.setter
    def snippet(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snippet", value)

    @property
    @pulumi.getter(name="staticLists")
    def static_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The StaticList param. Individual elements in this list are subject to additional validation. String length must not exceed 63 characters. Ensure that only one of the following is specified: `dynamic`, `static`
        """
        return pulumi.get(self, "static_lists")

    @static_lists.setter
    def static_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "static_lists", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Tags for address group object. List must contain at most 64 elements. Individual elements in this list are subject to additional validation. String length must not exceed 127 characters.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def tfid(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "tfid")

    @tfid.setter
    def tfid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tfid", value)


class AddressGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device: Optional[pulumi.Input[str]] = None,
                 dynamic_value: Optional[pulumi.Input[pulumi.InputType['AddressGroupDynamicValueArgs']]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 snippet: Optional[pulumi.Input[str]] = None,
                 static_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Retrieves a config item.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_scm as scm

        x = scm.AddressObject("x",
            folder="Shared",
            name="foo",
            description="Made by Pulumi",
            fqdn="www.example.com")
        example = scm.AddressGroup("example",
            folder="Shared",
            name="example",
            static_lists=[x.name])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The Description param. String length must not exceed 1023 characters.
        :param pulumi.Input[str] device: The Device param.
        :param pulumi.Input[pulumi.InputType['AddressGroupDynamicValueArgs']] dynamic_value: The DynamicValue param. Ensure that only one of the following is specified: `dynamic`, `static`
        :param pulumi.Input[str] folder: The Folder param.
        :param pulumi.Input[str] name: Alphanumeric string [ 0-9a-zA-Z._-]. String length must not exceed 63 characters.
        :param pulumi.Input[str] snippet: The Snippet param.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] static_lists: The StaticList param. Individual elements in this list are subject to additional validation. String length must not exceed 63 characters. Ensure that only one of the following is specified: `dynamic`, `static`
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags for address group object. List must contain at most 64 elements. Individual elements in this list are subject to additional validation. String length must not exceed 127 characters.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AddressGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Retrieves a config item.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_scm as scm

        x = scm.AddressObject("x",
            folder="Shared",
            name="foo",
            description="Made by Pulumi",
            fqdn="www.example.com")
        example = scm.AddressGroup("example",
            folder="Shared",
            name="example",
            static_lists=[x.name])
        ```

        :param str resource_name: The name of the resource.
        :param AddressGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AddressGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device: Optional[pulumi.Input[str]] = None,
                 dynamic_value: Optional[pulumi.Input[pulumi.InputType['AddressGroupDynamicValueArgs']]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 snippet: Optional[pulumi.Input[str]] = None,
                 static_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AddressGroupArgs.__new__(AddressGroupArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["device"] = device
            __props__.__dict__["dynamic_value"] = dynamic_value
            __props__.__dict__["folder"] = folder
            __props__.__dict__["name"] = name
            __props__.__dict__["snippet"] = snippet
            __props__.__dict__["static_lists"] = static_lists
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tfid"] = None
        super(AddressGroup, __self__).__init__(
            'scm:index/addressGroup:AddressGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            device: Optional[pulumi.Input[str]] = None,
            dynamic_value: Optional[pulumi.Input[pulumi.InputType['AddressGroupDynamicValueArgs']]] = None,
            folder: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            snippet: Optional[pulumi.Input[str]] = None,
            static_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tfid: Optional[pulumi.Input[str]] = None) -> 'AddressGroup':
        """
        Get an existing AddressGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The Description param. String length must not exceed 1023 characters.
        :param pulumi.Input[str] device: The Device param.
        :param pulumi.Input[pulumi.InputType['AddressGroupDynamicValueArgs']] dynamic_value: The DynamicValue param. Ensure that only one of the following is specified: `dynamic`, `static`
        :param pulumi.Input[str] folder: The Folder param.
        :param pulumi.Input[str] name: Alphanumeric string [ 0-9a-zA-Z._-]. String length must not exceed 63 characters.
        :param pulumi.Input[str] snippet: The Snippet param.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] static_lists: The StaticList param. Individual elements in this list are subject to additional validation. String length must not exceed 63 characters. Ensure that only one of the following is specified: `dynamic`, `static`
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags for address group object. List must contain at most 64 elements. Individual elements in this list are subject to additional validation. String length must not exceed 127 characters.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AddressGroupState.__new__(_AddressGroupState)

        __props__.__dict__["description"] = description
        __props__.__dict__["device"] = device
        __props__.__dict__["dynamic_value"] = dynamic_value
        __props__.__dict__["folder"] = folder
        __props__.__dict__["name"] = name
        __props__.__dict__["snippet"] = snippet
        __props__.__dict__["static_lists"] = static_lists
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tfid"] = tfid
        return AddressGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The Description param. String length must not exceed 1023 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def device(self) -> pulumi.Output[Optional[str]]:
        """
        The Device param.
        """
        return pulumi.get(self, "device")

    @property
    @pulumi.getter(name="dynamicValue")
    def dynamic_value(self) -> pulumi.Output[Optional['outputs.AddressGroupDynamicValue']]:
        """
        The DynamicValue param. Ensure that only one of the following is specified: `dynamic`, `static`
        """
        return pulumi.get(self, "dynamic_value")

    @property
    @pulumi.getter
    def folder(self) -> pulumi.Output[Optional[str]]:
        """
        The Folder param.
        """
        return pulumi.get(self, "folder")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Alphanumeric string [ 0-9a-zA-Z._-]. String length must not exceed 63 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def snippet(self) -> pulumi.Output[Optional[str]]:
        """
        The Snippet param.
        """
        return pulumi.get(self, "snippet")

    @property
    @pulumi.getter(name="staticLists")
    def static_lists(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The StaticList param. Individual elements in this list are subject to additional validation. String length must not exceed 63 characters. Ensure that only one of the following is specified: `dynamic`, `static`
        """
        return pulumi.get(self, "static_lists")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Tags for address group object. List must contain at most 64 elements. Individual elements in this list are subject to additional validation. String length must not exceed 127 characters.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tfid(self) -> pulumi.Output[str]:
        return pulumi.get(self, "tfid")

