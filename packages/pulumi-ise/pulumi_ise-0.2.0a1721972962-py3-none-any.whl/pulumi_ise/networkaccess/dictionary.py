# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DictionaryArgs', 'Dictionary']

@pulumi.input_type
class DictionaryArgs:
    def __init__(__self__, *,
                 dictionary_attr_type: pulumi.Input[str],
                 version: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Dictionary resource.
        :param pulumi.Input[str] dictionary_attr_type: The dictionary attribute type - Choices: `ENTITY_ATTR`, `MSG_ATTR`, `PIP_ATTR`
        :param pulumi.Input[str] version: The version of the dictionary
        :param pulumi.Input[str] description: The description of the dictionary
        :param pulumi.Input[str] name: The dictionary name
        """
        pulumi.set(__self__, "dictionary_attr_type", dictionary_attr_type)
        pulumi.set(__self__, "version", version)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="dictionaryAttrType")
    def dictionary_attr_type(self) -> pulumi.Input[str]:
        """
        The dictionary attribute type - Choices: `ENTITY_ATTR`, `MSG_ATTR`, `PIP_ATTR`
        """
        return pulumi.get(self, "dictionary_attr_type")

    @dictionary_attr_type.setter
    def dictionary_attr_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "dictionary_attr_type", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[str]:
        """
        The version of the dictionary
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the dictionary
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The dictionary name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _DictionaryState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 dictionary_attr_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Dictionary resources.
        :param pulumi.Input[str] description: The description of the dictionary
        :param pulumi.Input[str] dictionary_attr_type: The dictionary attribute type - Choices: `ENTITY_ATTR`, `MSG_ATTR`, `PIP_ATTR`
        :param pulumi.Input[str] name: The dictionary name
        :param pulumi.Input[str] version: The version of the dictionary
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if dictionary_attr_type is not None:
            pulumi.set(__self__, "dictionary_attr_type", dictionary_attr_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the dictionary
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="dictionaryAttrType")
    def dictionary_attr_type(self) -> Optional[pulumi.Input[str]]:
        """
        The dictionary attribute type - Choices: `ENTITY_ATTR`, `MSG_ATTR`, `PIP_ATTR`
        """
        return pulumi.get(self, "dictionary_attr_type")

    @dictionary_attr_type.setter
    def dictionary_attr_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dictionary_attr_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The dictionary name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the dictionary
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class Dictionary(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dictionary_attr_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource can manage a Network Access Dictionary.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ise as ise

        example = ise.networkaccess.Dictionary("example",
            name="Dict1",
            description="My description",
            version="1.1",
            dictionary_attr_type="ENTITY_ATTR")
        ```

        ## Import

        ```sh
        $ pulumi import ise:networkaccess/dictionary:Dictionary example "Dict1"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the dictionary
        :param pulumi.Input[str] dictionary_attr_type: The dictionary attribute type - Choices: `ENTITY_ATTR`, `MSG_ATTR`, `PIP_ATTR`
        :param pulumi.Input[str] name: The dictionary name
        :param pulumi.Input[str] version: The version of the dictionary
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DictionaryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource can manage a Network Access Dictionary.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ise as ise

        example = ise.networkaccess.Dictionary("example",
            name="Dict1",
            description="My description",
            version="1.1",
            dictionary_attr_type="ENTITY_ATTR")
        ```

        ## Import

        ```sh
        $ pulumi import ise:networkaccess/dictionary:Dictionary example "Dict1"
        ```

        :param str resource_name: The name of the resource.
        :param DictionaryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DictionaryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dictionary_attr_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DictionaryArgs.__new__(DictionaryArgs)

            __props__.__dict__["description"] = description
            if dictionary_attr_type is None and not opts.urn:
                raise TypeError("Missing required property 'dictionary_attr_type'")
            __props__.__dict__["dictionary_attr_type"] = dictionary_attr_type
            __props__.__dict__["name"] = name
            if version is None and not opts.urn:
                raise TypeError("Missing required property 'version'")
            __props__.__dict__["version"] = version
        super(Dictionary, __self__).__init__(
            'ise:networkaccess/dictionary:Dictionary',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            dictionary_attr_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'Dictionary':
        """
        Get an existing Dictionary resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the dictionary
        :param pulumi.Input[str] dictionary_attr_type: The dictionary attribute type - Choices: `ENTITY_ATTR`, `MSG_ATTR`, `PIP_ATTR`
        :param pulumi.Input[str] name: The dictionary name
        :param pulumi.Input[str] version: The version of the dictionary
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DictionaryState.__new__(_DictionaryState)

        __props__.__dict__["description"] = description
        __props__.__dict__["dictionary_attr_type"] = dictionary_attr_type
        __props__.__dict__["name"] = name
        __props__.__dict__["version"] = version
        return Dictionary(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the dictionary
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dictionaryAttrType")
    def dictionary_attr_type(self) -> pulumi.Output[str]:
        """
        The dictionary attribute type - Choices: `ENTITY_ATTR`, `MSG_ATTR`, `PIP_ATTR`
        """
        return pulumi.get(self, "dictionary_attr_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The dictionary name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        The version of the dictionary
        """
        return pulumi.get(self, "version")

