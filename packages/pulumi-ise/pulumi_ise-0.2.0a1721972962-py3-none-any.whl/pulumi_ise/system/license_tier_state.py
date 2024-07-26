# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['LicenseTierStateArgs', 'LicenseTierState']

@pulumi.input_type
class LicenseTierStateArgs:
    def __init__(__self__, *,
                 licenses: pulumi.Input[Sequence[pulumi.Input['LicenseTierStateLicenseArgs']]]):
        """
        The set of arguments for constructing a LicenseTierState resource.
        :param pulumi.Input[Sequence[pulumi.Input['LicenseTierStateLicenseArgs']]] licenses: List of licenses
        """
        pulumi.set(__self__, "licenses", licenses)

    @property
    @pulumi.getter
    def licenses(self) -> pulumi.Input[Sequence[pulumi.Input['LicenseTierStateLicenseArgs']]]:
        """
        List of licenses
        """
        return pulumi.get(self, "licenses")

    @licenses.setter
    def licenses(self, value: pulumi.Input[Sequence[pulumi.Input['LicenseTierStateLicenseArgs']]]):
        pulumi.set(self, "licenses", value)


@pulumi.input_type
class _LicenseTierStateState:
    def __init__(__self__, *,
                 licenses: Optional[pulumi.Input[Sequence[pulumi.Input['LicenseTierStateLicenseArgs']]]] = None):
        """
        Input properties used for looking up and filtering LicenseTierState resources.
        :param pulumi.Input[Sequence[pulumi.Input['LicenseTierStateLicenseArgs']]] licenses: List of licenses
        """
        if licenses is not None:
            pulumi.set(__self__, "licenses", licenses)

    @property
    @pulumi.getter
    def licenses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LicenseTierStateLicenseArgs']]]]:
        """
        List of licenses
        """
        return pulumi.get(self, "licenses")

    @licenses.setter
    def licenses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LicenseTierStateLicenseArgs']]]]):
        pulumi.set(self, "licenses", value)


class LicenseTierState(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 licenses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LicenseTierStateLicenseArgs']]]]] = None,
                 __props__=None):
        """
        This resource can manage a License Tier State.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ise as ise

        example = ise.system.LicenseTierState("example", licenses=[ise.system.LicenseTierStateLicenseArgs(
            name="ESSENTIAL",
            status="ENABLED",
        )])
        ```

        ## Import

        ```sh
        $ pulumi import ise:system/licenseTierState:LicenseTierState example "76d24097-41c4-4558-a4d0-a8c07ac08470"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LicenseTierStateLicenseArgs']]]] licenses: List of licenses
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LicenseTierStateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource can manage a License Tier State.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ise as ise

        example = ise.system.LicenseTierState("example", licenses=[ise.system.LicenseTierStateLicenseArgs(
            name="ESSENTIAL",
            status="ENABLED",
        )])
        ```

        ## Import

        ```sh
        $ pulumi import ise:system/licenseTierState:LicenseTierState example "76d24097-41c4-4558-a4d0-a8c07ac08470"
        ```

        :param str resource_name: The name of the resource.
        :param LicenseTierStateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LicenseTierStateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 licenses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LicenseTierStateLicenseArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LicenseTierStateArgs.__new__(LicenseTierStateArgs)

            if licenses is None and not opts.urn:
                raise TypeError("Missing required property 'licenses'")
            __props__.__dict__["licenses"] = licenses
        super(LicenseTierState, __self__).__init__(
            'ise:system/licenseTierState:LicenseTierState',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            licenses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LicenseTierStateLicenseArgs']]]]] = None) -> 'LicenseTierState':
        """
        Get an existing LicenseTierState resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LicenseTierStateLicenseArgs']]]] licenses: List of licenses
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LicenseTierStateState.__new__(_LicenseTierStateState)

        __props__.__dict__["licenses"] = licenses
        return LicenseTierState(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def licenses(self) -> pulumi.Output[Sequence['outputs.LicenseTierStateLicense']]:
        """
        List of licenses
        """
        return pulumi.get(self, "licenses")

