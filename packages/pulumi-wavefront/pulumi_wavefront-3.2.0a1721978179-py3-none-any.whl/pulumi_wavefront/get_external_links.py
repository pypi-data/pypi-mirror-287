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
    'GetExternalLinksResult',
    'AwaitableGetExternalLinksResult',
    'get_external_links',
    'get_external_links_output',
]

@pulumi.output_type
class GetExternalLinksResult:
    """
    A collection of values returned by getExternalLinks.
    """
    def __init__(__self__, external_links=None, id=None, limit=None, offset=None):
        if external_links and not isinstance(external_links, list):
            raise TypeError("Expected argument 'external_links' to be a list")
        pulumi.set(__self__, "external_links", external_links)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if limit and not isinstance(limit, int):
            raise TypeError("Expected argument 'limit' to be a int")
        pulumi.set(__self__, "limit", limit)
        if offset and not isinstance(offset, int):
            raise TypeError("Expected argument 'offset' to be a int")
        pulumi.set(__self__, "offset", offset)

    @property
    @pulumi.getter(name="externalLinks")
    def external_links(self) -> Sequence['outputs.GetExternalLinksExternalLinkResult']:
        """
        List of all external links in Wavefront. For each external link you will see a list of attributes.
        """
        return pulumi.get(self, "external_links")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def limit(self) -> Optional[int]:
        return pulumi.get(self, "limit")

    @property
    @pulumi.getter
    def offset(self) -> Optional[int]:
        return pulumi.get(self, "offset")


class AwaitableGetExternalLinksResult(GetExternalLinksResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExternalLinksResult(
            external_links=self.external_links,
            id=self.id,
            limit=self.limit,
            offset=self.offset)


def get_external_links(limit: Optional[int] = None,
                       offset: Optional[int] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExternalLinksResult:
    """
    Use this data source to get information about all Wavefront external links.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_wavefront as wavefront

    # Get the information about all external links.
    example = wavefront.get_external_links(limit=10,
        offset=0)
    ```


    :param int limit: Limit is the maximum number of results to be returned. Defaults to 100.
    :param int offset: Offset is the offset from the first result to be returned. Defaults to 0.
    """
    __args__ = dict()
    __args__['limit'] = limit
    __args__['offset'] = offset
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('wavefront:index/getExternalLinks:getExternalLinks', __args__, opts=opts, typ=GetExternalLinksResult).value

    return AwaitableGetExternalLinksResult(
        external_links=pulumi.get(__ret__, 'external_links'),
        id=pulumi.get(__ret__, 'id'),
        limit=pulumi.get(__ret__, 'limit'),
        offset=pulumi.get(__ret__, 'offset'))


@_utilities.lift_output_func(get_external_links)
def get_external_links_output(limit: Optional[pulumi.Input[Optional[int]]] = None,
                              offset: Optional[pulumi.Input[Optional[int]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExternalLinksResult]:
    """
    Use this data source to get information about all Wavefront external links.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_wavefront as wavefront

    # Get the information about all external links.
    example = wavefront.get_external_links(limit=10,
        offset=0)
    ```


    :param int limit: Limit is the maximum number of results to be returned. Defaults to 100.
    :param int offset: Offset is the offset from the first result to be returned. Defaults to 0.
    """
    ...
