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
    'GetCollectorResult',
    'AwaitableGetCollectorResult',
    'get_collector',
    'get_collector_output',
]

@pulumi.output_type
class GetCollectorResult:
    """
    A collection of values returned by getCollector.
    """
    def __init__(__self__, category=None, description=None, fields=None, id=None, name=None, timezone=None):
        if category and not isinstance(category, str):
            raise TypeError("Expected argument 'category' to be a str")
        pulumi.set(__self__, "category", category)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if fields and not isinstance(fields, dict):
            raise TypeError("Expected argument 'fields' to be a dict")
        pulumi.set(__self__, "fields", fields)
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if timezone and not isinstance(timezone, str):
            raise TypeError("Expected argument 'timezone' to be a str")
        pulumi.set(__self__, "timezone", timezone)

    @property
    @pulumi.getter
    def category(self) -> str:
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def fields(self) -> Mapping[str, str]:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def id(self) -> int:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def timezone(self) -> str:
        return pulumi.get(self, "timezone")


class AwaitableGetCollectorResult(GetCollectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCollectorResult(
            category=self.category,
            description=self.description,
            fields=self.fields,
            id=self.id,
            name=self.name,
            timezone=self.timezone)


def get_collector(id: Optional[int] = None,
                  name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCollectorResult:
    """
    Provides a way to retrieve Sumo Logic collector details (id, names, etc) for a collector.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sumologic as sumologic

    this = sumologic.get_collector(name="MyCollector")
    ```

    ```python
    import pulumi
    import pulumi_sumologic as sumologic

    that = sumologic.get_collector(id=1234567890)
    ```

    A collector can be looked up by either `id` or `name`. One of those attributes needs to be specified.

    If both `id` and `name` have been specified, `id` takes precedence.

    ## Attributes reference

    The following attributes are exported:

    - `id` - The internal ID of the collector. This can be used to attach sources to the collector.
    - `name` - The name of the collector.
    - `description` - The description of the collector.
    - `category` - The default source category for any source attached to this collector.
    - `timezone` - The time zone to use for this collector. The value follows the [tzdata][2] naming convention.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sumologic:index/getCollector:getCollector', __args__, opts=opts, typ=GetCollectorResult).value

    return AwaitableGetCollectorResult(
        category=pulumi.get(__ret__, 'category'),
        description=pulumi.get(__ret__, 'description'),
        fields=pulumi.get(__ret__, 'fields'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        timezone=pulumi.get(__ret__, 'timezone'))


@_utilities.lift_output_func(get_collector)
def get_collector_output(id: Optional[pulumi.Input[Optional[int]]] = None,
                         name: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCollectorResult]:
    """
    Provides a way to retrieve Sumo Logic collector details (id, names, etc) for a collector.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sumologic as sumologic

    this = sumologic.get_collector(name="MyCollector")
    ```

    ```python
    import pulumi
    import pulumi_sumologic as sumologic

    that = sumologic.get_collector(id=1234567890)
    ```

    A collector can be looked up by either `id` or `name`. One of those attributes needs to be specified.

    If both `id` and `name` have been specified, `id` takes precedence.

    ## Attributes reference

    The following attributes are exported:

    - `id` - The internal ID of the collector. This can be used to attach sources to the collector.
    - `name` - The name of the collector.
    - `description` - The description of the collector.
    - `category` - The default source category for any source attached to this collector.
    - `timezone` - The time zone to use for this collector. The value follows the [tzdata][2] naming convention.
    """
    ...
