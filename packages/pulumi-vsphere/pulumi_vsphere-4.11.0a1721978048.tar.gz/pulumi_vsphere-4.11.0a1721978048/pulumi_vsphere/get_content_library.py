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
    'GetContentLibraryResult',
    'AwaitableGetContentLibraryResult',
    'get_content_library',
    'get_content_library_output',
]

@pulumi.output_type
class GetContentLibraryResult:
    """
    A collection of values returned by getContentLibrary.
    """
    def __init__(__self__, id=None, name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


class AwaitableGetContentLibraryResult(GetContentLibraryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContentLibraryResult(
            id=self.id,
            name=self.name)


def get_content_library(name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContentLibraryResult:
    """
    The `ContentLibrary` data source can be used to discover the ID of a
    content library.

    > **NOTE:** This resource requires vCenter and is not available on direct ESXi
    host connections.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_vsphere as vsphere

    content_library = vsphere.get_content_library(name="Content Library")
    ```


    :param str name: The name of the content library.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('vsphere:index/getContentLibrary:getContentLibrary', __args__, opts=opts, typ=GetContentLibraryResult).value

    return AwaitableGetContentLibraryResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_content_library)
def get_content_library_output(name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContentLibraryResult]:
    """
    The `ContentLibrary` data source can be used to discover the ID of a
    content library.

    > **NOTE:** This resource requires vCenter and is not available on direct ESXi
    host connections.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_vsphere as vsphere

    content_library = vsphere.get_content_library(name="Content Library")
    ```


    :param str name: The name of the content library.
    """
    ...
