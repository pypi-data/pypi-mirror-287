# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DownloadableAclArgs', 'DownloadableAcl']

@pulumi.input_type
class DownloadableAclArgs:
    def __init__(__self__, *,
                 dacl: pulumi.Input[str],
                 dacl_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DownloadableAcl resource.
        :param pulumi.Input[str] dacl: The DACL content
        :param pulumi.Input[str] dacl_type: The type of ACL - Choices: `IPV4`, `IPV6`, `IP_AGNOSTIC` - Default value: `IPV4`
        :param pulumi.Input[str] description: Description
        :param pulumi.Input[str] name: The name of the downloadable ACL
        """
        pulumi.set(__self__, "dacl", dacl)
        if dacl_type is not None:
            pulumi.set(__self__, "dacl_type", dacl_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def dacl(self) -> pulumi.Input[str]:
        """
        The DACL content
        """
        return pulumi.get(self, "dacl")

    @dacl.setter
    def dacl(self, value: pulumi.Input[str]):
        pulumi.set(self, "dacl", value)

    @property
    @pulumi.getter(name="daclType")
    def dacl_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of ACL - Choices: `IPV4`, `IPV6`, `IP_AGNOSTIC` - Default value: `IPV4`
        """
        return pulumi.get(self, "dacl_type")

    @dacl_type.setter
    def dacl_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dacl_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the downloadable ACL
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _DownloadableAclState:
    def __init__(__self__, *,
                 dacl: Optional[pulumi.Input[str]] = None,
                 dacl_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DownloadableAcl resources.
        :param pulumi.Input[str] dacl: The DACL content
        :param pulumi.Input[str] dacl_type: The type of ACL - Choices: `IPV4`, `IPV6`, `IP_AGNOSTIC` - Default value: `IPV4`
        :param pulumi.Input[str] description: Description
        :param pulumi.Input[str] name: The name of the downloadable ACL
        """
        if dacl is not None:
            pulumi.set(__self__, "dacl", dacl)
        if dacl_type is not None:
            pulumi.set(__self__, "dacl_type", dacl_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def dacl(self) -> Optional[pulumi.Input[str]]:
        """
        The DACL content
        """
        return pulumi.get(self, "dacl")

    @dacl.setter
    def dacl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dacl", value)

    @property
    @pulumi.getter(name="daclType")
    def dacl_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of ACL - Choices: `IPV4`, `IPV6`, `IP_AGNOSTIC` - Default value: `IPV4`
        """
        return pulumi.get(self, "dacl_type")

    @dacl_type.setter
    def dacl_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dacl_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the downloadable ACL
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class DownloadableAcl(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dacl: Optional[pulumi.Input[str]] = None,
                 dacl_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource can manage a Downloadable ACL.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ise as ise

        example = ise.networkaccess.DownloadableAcl("example",
            name="MyACL",
            description="My first downloadable ACL",
            dacl="permit ip any any",
            dacl_type="IPV4")
        ```

        ## Import

        ```sh
        $ pulumi import ise:networkaccess/downloadableAcl:DownloadableAcl example "76d24097-41c4-4558-a4d0-a8c07ac08470"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dacl: The DACL content
        :param pulumi.Input[str] dacl_type: The type of ACL - Choices: `IPV4`, `IPV6`, `IP_AGNOSTIC` - Default value: `IPV4`
        :param pulumi.Input[str] description: Description
        :param pulumi.Input[str] name: The name of the downloadable ACL
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DownloadableAclArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource can manage a Downloadable ACL.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ise as ise

        example = ise.networkaccess.DownloadableAcl("example",
            name="MyACL",
            description="My first downloadable ACL",
            dacl="permit ip any any",
            dacl_type="IPV4")
        ```

        ## Import

        ```sh
        $ pulumi import ise:networkaccess/downloadableAcl:DownloadableAcl example "76d24097-41c4-4558-a4d0-a8c07ac08470"
        ```

        :param str resource_name: The name of the resource.
        :param DownloadableAclArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DownloadableAclArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dacl: Optional[pulumi.Input[str]] = None,
                 dacl_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DownloadableAclArgs.__new__(DownloadableAclArgs)

            if dacl is None and not opts.urn:
                raise TypeError("Missing required property 'dacl'")
            __props__.__dict__["dacl"] = dacl
            __props__.__dict__["dacl_type"] = dacl_type
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
        super(DownloadableAcl, __self__).__init__(
            'ise:networkaccess/downloadableAcl:DownloadableAcl',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dacl: Optional[pulumi.Input[str]] = None,
            dacl_type: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'DownloadableAcl':
        """
        Get an existing DownloadableAcl resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dacl: The DACL content
        :param pulumi.Input[str] dacl_type: The type of ACL - Choices: `IPV4`, `IPV6`, `IP_AGNOSTIC` - Default value: `IPV4`
        :param pulumi.Input[str] description: Description
        :param pulumi.Input[str] name: The name of the downloadable ACL
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DownloadableAclState.__new__(_DownloadableAclState)

        __props__.__dict__["dacl"] = dacl
        __props__.__dict__["dacl_type"] = dacl_type
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        return DownloadableAcl(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def dacl(self) -> pulumi.Output[str]:
        """
        The DACL content
        """
        return pulumi.get(self, "dacl")

    @property
    @pulumi.getter(name="daclType")
    def dacl_type(self) -> pulumi.Output[str]:
        """
        The type of ACL - Choices: `IPV4`, `IPV6`, `IP_AGNOSTIC` - Default value: `IPV4`
        """
        return pulumi.get(self, "dacl_type")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the downloadable ACL
        """
        return pulumi.get(self, "name")

