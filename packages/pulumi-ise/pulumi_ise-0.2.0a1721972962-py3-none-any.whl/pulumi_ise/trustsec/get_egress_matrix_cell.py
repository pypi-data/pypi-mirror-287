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
    'GetEgressMatrixCellResult',
    'AwaitableGetEgressMatrixCellResult',
    'get_egress_matrix_cell',
    'get_egress_matrix_cell_output',
]

@pulumi.output_type
class GetEgressMatrixCellResult:
    """
    A collection of values returned by getEgressMatrixCell.
    """
    def __init__(__self__, default_rule=None, description=None, destination_sgt_id=None, id=None, matrix_cell_status=None, sgacls=None, source_sgt_id=None):
        if default_rule and not isinstance(default_rule, str):
            raise TypeError("Expected argument 'default_rule' to be a str")
        pulumi.set(__self__, "default_rule", default_rule)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if destination_sgt_id and not isinstance(destination_sgt_id, str):
            raise TypeError("Expected argument 'destination_sgt_id' to be a str")
        pulumi.set(__self__, "destination_sgt_id", destination_sgt_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if matrix_cell_status and not isinstance(matrix_cell_status, str):
            raise TypeError("Expected argument 'matrix_cell_status' to be a str")
        pulumi.set(__self__, "matrix_cell_status", matrix_cell_status)
        if sgacls and not isinstance(sgacls, list):
            raise TypeError("Expected argument 'sgacls' to be a list")
        pulumi.set(__self__, "sgacls", sgacls)
        if source_sgt_id and not isinstance(source_sgt_id, str):
            raise TypeError("Expected argument 'source_sgt_id' to be a str")
        pulumi.set(__self__, "source_sgt_id", source_sgt_id)

    @property
    @pulumi.getter(name="defaultRule")
    def default_rule(self) -> str:
        """
        Can be used only if sgacls not specified.
        """
        return pulumi.get(self, "default_rule")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationSgtId")
    def destination_sgt_id(self) -> str:
        """
        Destination Trustsec Security Group ID
        """
        return pulumi.get(self, "destination_sgt_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the object
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="matrixCellStatus")
    def matrix_cell_status(self) -> str:
        """
        Matrix Cell Status
        """
        return pulumi.get(self, "matrix_cell_status")

    @property
    @pulumi.getter
    def sgacls(self) -> Sequence[str]:
        """
        List of TrustSec Security Groups ACLs
        """
        return pulumi.get(self, "sgacls")

    @property
    @pulumi.getter(name="sourceSgtId")
    def source_sgt_id(self) -> str:
        """
        Source Trustsec Security Group ID
        """
        return pulumi.get(self, "source_sgt_id")


class AwaitableGetEgressMatrixCellResult(GetEgressMatrixCellResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEgressMatrixCellResult(
            default_rule=self.default_rule,
            description=self.description,
            destination_sgt_id=self.destination_sgt_id,
            id=self.id,
            matrix_cell_status=self.matrix_cell_status,
            sgacls=self.sgacls,
            source_sgt_id=self.source_sgt_id)


def get_egress_matrix_cell(id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEgressMatrixCellResult:
    """
    This data source can read the TrustSec Egress Matrix Cell.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ise as ise

    example = ise.trustsec.get_egress_matrix_cell(id="76d24097-41c4-4558-a4d0-a8c07ac08470")
    ```


    :param str id: The id of the object
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ise:trustsec/getEgressMatrixCell:getEgressMatrixCell', __args__, opts=opts, typ=GetEgressMatrixCellResult).value

    return AwaitableGetEgressMatrixCellResult(
        default_rule=pulumi.get(__ret__, 'default_rule'),
        description=pulumi.get(__ret__, 'description'),
        destination_sgt_id=pulumi.get(__ret__, 'destination_sgt_id'),
        id=pulumi.get(__ret__, 'id'),
        matrix_cell_status=pulumi.get(__ret__, 'matrix_cell_status'),
        sgacls=pulumi.get(__ret__, 'sgacls'),
        source_sgt_id=pulumi.get(__ret__, 'source_sgt_id'))


@_utilities.lift_output_func(get_egress_matrix_cell)
def get_egress_matrix_cell_output(id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEgressMatrixCellResult]:
    """
    This data source can read the TrustSec Egress Matrix Cell.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ise as ise

    example = ise.trustsec.get_egress_matrix_cell(id="76d24097-41c4-4558-a4d0-a8c07ac08470")
    ```


    :param str id: The id of the object
    """
    ...
