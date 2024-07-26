# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['EndpointIdentityGroupArgs', 'EndpointIdentityGroup']

@pulumi.input_type
class EndpointIdentityGroupArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_endpoint_identity_group_id: Optional[pulumi.Input[str]] = None,
                 system_defined: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a EndpointIdentityGroup resource.
        :param pulumi.Input[str] description: Description
        :param pulumi.Input[str] name: The name of the endpoint identity group
        :param pulumi.Input[str] parent_endpoint_identity_group_id: Parent endpoint identity group ID
        :param pulumi.Input[bool] system_defined: System defined endpoint identity group - Default value: `false`
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent_endpoint_identity_group_id is not None:
            pulumi.set(__self__, "parent_endpoint_identity_group_id", parent_endpoint_identity_group_id)
        if system_defined is not None:
            pulumi.set(__self__, "system_defined", system_defined)

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
        The name of the endpoint identity group
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parentEndpointIdentityGroupId")
    def parent_endpoint_identity_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Parent endpoint identity group ID
        """
        return pulumi.get(self, "parent_endpoint_identity_group_id")

    @parent_endpoint_identity_group_id.setter
    def parent_endpoint_identity_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_endpoint_identity_group_id", value)

    @property
    @pulumi.getter(name="systemDefined")
    def system_defined(self) -> Optional[pulumi.Input[bool]]:
        """
        System defined endpoint identity group - Default value: `false`
        """
        return pulumi.get(self, "system_defined")

    @system_defined.setter
    def system_defined(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "system_defined", value)


@pulumi.input_type
class _EndpointIdentityGroupState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_endpoint_identity_group_id: Optional[pulumi.Input[str]] = None,
                 system_defined: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering EndpointIdentityGroup resources.
        :param pulumi.Input[str] description: Description
        :param pulumi.Input[str] name: The name of the endpoint identity group
        :param pulumi.Input[str] parent_endpoint_identity_group_id: Parent endpoint identity group ID
        :param pulumi.Input[bool] system_defined: System defined endpoint identity group - Default value: `false`
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent_endpoint_identity_group_id is not None:
            pulumi.set(__self__, "parent_endpoint_identity_group_id", parent_endpoint_identity_group_id)
        if system_defined is not None:
            pulumi.set(__self__, "system_defined", system_defined)

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
        The name of the endpoint identity group
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parentEndpointIdentityGroupId")
    def parent_endpoint_identity_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Parent endpoint identity group ID
        """
        return pulumi.get(self, "parent_endpoint_identity_group_id")

    @parent_endpoint_identity_group_id.setter
    def parent_endpoint_identity_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_endpoint_identity_group_id", value)

    @property
    @pulumi.getter(name="systemDefined")
    def system_defined(self) -> Optional[pulumi.Input[bool]]:
        """
        System defined endpoint identity group - Default value: `false`
        """
        return pulumi.get(self, "system_defined")

    @system_defined.setter
    def system_defined(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "system_defined", value)


class EndpointIdentityGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_endpoint_identity_group_id: Optional[pulumi.Input[str]] = None,
                 system_defined: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        This resource can manage an Endpoint Identity Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ise as ise

        example = ise.identitymanagement.EndpointIdentityGroup("example",
            name="Group1",
            description="My endpoint identity group",
            system_defined=False)
        ```

        ## Import

        ```sh
        $ pulumi import ise:identitymanagement/endpointIdentityGroup:EndpointIdentityGroup example "76d24097-41c4-4558-a4d0-a8c07ac08470"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description
        :param pulumi.Input[str] name: The name of the endpoint identity group
        :param pulumi.Input[str] parent_endpoint_identity_group_id: Parent endpoint identity group ID
        :param pulumi.Input[bool] system_defined: System defined endpoint identity group - Default value: `false`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[EndpointIdentityGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource can manage an Endpoint Identity Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ise as ise

        example = ise.identitymanagement.EndpointIdentityGroup("example",
            name="Group1",
            description="My endpoint identity group",
            system_defined=False)
        ```

        ## Import

        ```sh
        $ pulumi import ise:identitymanagement/endpointIdentityGroup:EndpointIdentityGroup example "76d24097-41c4-4558-a4d0-a8c07ac08470"
        ```

        :param str resource_name: The name of the resource.
        :param EndpointIdentityGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EndpointIdentityGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_endpoint_identity_group_id: Optional[pulumi.Input[str]] = None,
                 system_defined: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EndpointIdentityGroupArgs.__new__(EndpointIdentityGroupArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["parent_endpoint_identity_group_id"] = parent_endpoint_identity_group_id
            __props__.__dict__["system_defined"] = system_defined
        super(EndpointIdentityGroup, __self__).__init__(
            'ise:identitymanagement/endpointIdentityGroup:EndpointIdentityGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent_endpoint_identity_group_id: Optional[pulumi.Input[str]] = None,
            system_defined: Optional[pulumi.Input[bool]] = None) -> 'EndpointIdentityGroup':
        """
        Get an existing EndpointIdentityGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description
        :param pulumi.Input[str] name: The name of the endpoint identity group
        :param pulumi.Input[str] parent_endpoint_identity_group_id: Parent endpoint identity group ID
        :param pulumi.Input[bool] system_defined: System defined endpoint identity group - Default value: `false`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EndpointIdentityGroupState.__new__(_EndpointIdentityGroupState)

        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["parent_endpoint_identity_group_id"] = parent_endpoint_identity_group_id
        __props__.__dict__["system_defined"] = system_defined
        return EndpointIdentityGroup(resource_name, opts=opts, __props__=__props__)

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
        The name of the endpoint identity group
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentEndpointIdentityGroupId")
    def parent_endpoint_identity_group_id(self) -> pulumi.Output[Optional[str]]:
        """
        Parent endpoint identity group ID
        """
        return pulumi.get(self, "parent_endpoint_identity_group_id")

    @property
    @pulumi.getter(name="systemDefined")
    def system_defined(self) -> pulumi.Output[bool]:
        """
        System defined endpoint identity group - Default value: `false`
        """
        return pulumi.get(self, "system_defined")

