# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetDeviceGroupResult',
    'AwaitableGetDeviceGroupResult',
    'get_device_group',
    'get_device_group_output',
]

@pulumi.output_type
class GetDeviceGroupResult:
    """
    A collection of values returned by getDeviceGroup.
    """
    def __init__(__self__, description=None, id=None, name=None, root_group=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if root_group and not isinstance(root_group, str):
            raise TypeError("Expected argument 'root_group' to be a str")
        pulumi.set(__self__, "root_group", root_group)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the object
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the network device group including its hierarchy, e.g. `Device Type#All Device Types#ACCESS`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="rootGroup")
    def root_group(self) -> str:
        """
        The name of the root device group.
        """
        return pulumi.get(self, "root_group")


class AwaitableGetDeviceGroupResult(GetDeviceGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeviceGroupResult(
            description=self.description,
            id=self.id,
            name=self.name,
            root_group=self.root_group)


def get_device_group(id: Optional[str] = None,
                     name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeviceGroupResult:
    """
    This data source can read the Network Device Group.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ise as ise

    example = ise.network.get_device_group(id="76d24097-41c4-4558-a4d0-a8c07ac08470")
    ```


    :param str id: The id of the object
    :param str name: The name of the network device group including its hierarchy, e.g. `Device Type#All Device Types#ACCESS`.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ise:network/getDeviceGroup:getDeviceGroup', __args__, opts=opts, typ=GetDeviceGroupResult).value

    return AwaitableGetDeviceGroupResult(
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        root_group=pulumi.get(__ret__, 'root_group'))


@_utilities.lift_output_func(get_device_group)
def get_device_group_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                            name: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeviceGroupResult]:
    """
    This data source can read the Network Device Group.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ise as ise

    example = ise.network.get_device_group(id="76d24097-41c4-4558-a4d0-a8c07ac08470")
    ```


    :param str id: The id of the object
    :param str name: The name of the network device group including its hierarchy, e.g. `Device Type#All Device Types#ACCESS`.
    """
    ...
