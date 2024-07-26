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

__all__ = ['CseChainRuleArgs', 'CseChainRule']

@pulumi.input_type
class CseChainRuleArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 enabled: pulumi.Input[bool],
                 entity_selectors: pulumi.Input[Sequence[pulumi.Input['CseChainRuleEntitySelectorArgs']]],
                 expressions_and_limits: pulumi.Input[Sequence[pulumi.Input['CseChainRuleExpressionsAndLimitArgs']]],
                 severity: pulumi.Input[int],
                 window_size: pulumi.Input[str],
                 group_by_fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 is_prototype: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ordered: Optional[pulumi.Input[bool]] = None,
                 summary_expression: Optional[pulumi.Input[str]] = None,
                 suppression_window_size: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 window_size_millis: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CseChainRule resource.
        :param pulumi.Input[str] description: The description of the generated Signals
        :param pulumi.Input[bool] enabled: Whether the rule should generate Signals
        :param pulumi.Input[Sequence[pulumi.Input['CseChainRuleEntitySelectorArgs']]] entity_selectors: The entities to generate Signals on
               + `entityType` - (Required) The type of the entity to generate the Signal on.
        :param pulumi.Input[Sequence[pulumi.Input['CseChainRuleExpressionsAndLimitArgs']]] expressions_and_limits: The list of expressions and associated limits to make up the conditions of the chain rule
        :param pulumi.Input[int] severity: The severity of the generated Signals
        :param pulumi.Input[str] window_size: How long of a window to aggregate records for. Current acceptable values are T05M, T10M, T30M, T60M, T24H, T12H, T05D or CUSTOM
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_by_fields: A list of fields to group records by
        :param pulumi.Input[bool] is_prototype: Whether the generated Signals should be prototype Signals
        :param pulumi.Input[str] name: The name of the Rule and the generated SignalS
        :param pulumi.Input[bool] ordered: Whether the records matching the expressions must be in the same chronological order as the expressions are listed in the rule
        :param pulumi.Input[str] summary_expression: The summary of the generated Signals
        :param pulumi.Input[int] suppression_window_size: For how long to suppress Signal generation, in milliseconds. Must be greater than `window_size` and less than the global limit of 7 days.
               
               The following attributes are exported:
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the generated Signals
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "entity_selectors", entity_selectors)
        pulumi.set(__self__, "expressions_and_limits", expressions_and_limits)
        pulumi.set(__self__, "severity", severity)
        pulumi.set(__self__, "window_size", window_size)
        if group_by_fields is not None:
            pulumi.set(__self__, "group_by_fields", group_by_fields)
        if is_prototype is not None:
            pulumi.set(__self__, "is_prototype", is_prototype)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ordered is not None:
            pulumi.set(__self__, "ordered", ordered)
        if summary_expression is not None:
            pulumi.set(__self__, "summary_expression", summary_expression)
        if suppression_window_size is not None:
            pulumi.set(__self__, "suppression_window_size", suppression_window_size)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if window_size_millis is not None:
            pulumi.set(__self__, "window_size_millis", window_size_millis)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The description of the generated Signals
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Whether the rule should generate Signals
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="entitySelectors")
    def entity_selectors(self) -> pulumi.Input[Sequence[pulumi.Input['CseChainRuleEntitySelectorArgs']]]:
        """
        The entities to generate Signals on
        + `entityType` - (Required) The type of the entity to generate the Signal on.
        """
        return pulumi.get(self, "entity_selectors")

    @entity_selectors.setter
    def entity_selectors(self, value: pulumi.Input[Sequence[pulumi.Input['CseChainRuleEntitySelectorArgs']]]):
        pulumi.set(self, "entity_selectors", value)

    @property
    @pulumi.getter(name="expressionsAndLimits")
    def expressions_and_limits(self) -> pulumi.Input[Sequence[pulumi.Input['CseChainRuleExpressionsAndLimitArgs']]]:
        """
        The list of expressions and associated limits to make up the conditions of the chain rule
        """
        return pulumi.get(self, "expressions_and_limits")

    @expressions_and_limits.setter
    def expressions_and_limits(self, value: pulumi.Input[Sequence[pulumi.Input['CseChainRuleExpressionsAndLimitArgs']]]):
        pulumi.set(self, "expressions_and_limits", value)

    @property
    @pulumi.getter
    def severity(self) -> pulumi.Input[int]:
        """
        The severity of the generated Signals
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: pulumi.Input[int]):
        pulumi.set(self, "severity", value)

    @property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> pulumi.Input[str]:
        """
        How long of a window to aggregate records for. Current acceptable values are T05M, T10M, T30M, T60M, T24H, T12H, T05D or CUSTOM
        """
        return pulumi.get(self, "window_size")

    @window_size.setter
    def window_size(self, value: pulumi.Input[str]):
        pulumi.set(self, "window_size", value)

    @property
    @pulumi.getter(name="groupByFields")
    def group_by_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of fields to group records by
        """
        return pulumi.get(self, "group_by_fields")

    @group_by_fields.setter
    def group_by_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "group_by_fields", value)

    @property
    @pulumi.getter(name="isPrototype")
    def is_prototype(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the generated Signals should be prototype Signals
        """
        return pulumi.get(self, "is_prototype")

    @is_prototype.setter
    def is_prototype(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_prototype", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Rule and the generated SignalS
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def ordered(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the records matching the expressions must be in the same chronological order as the expressions are listed in the rule
        """
        return pulumi.get(self, "ordered")

    @ordered.setter
    def ordered(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ordered", value)

    @property
    @pulumi.getter(name="summaryExpression")
    def summary_expression(self) -> Optional[pulumi.Input[str]]:
        """
        The summary of the generated Signals
        """
        return pulumi.get(self, "summary_expression")

    @summary_expression.setter
    def summary_expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "summary_expression", value)

    @property
    @pulumi.getter(name="suppressionWindowSize")
    def suppression_window_size(self) -> Optional[pulumi.Input[int]]:
        """
        For how long to suppress Signal generation, in milliseconds. Must be greater than `window_size` and less than the global limit of 7 days.

        The following attributes are exported:
        """
        return pulumi.get(self, "suppression_window_size")

    @suppression_window_size.setter
    def suppression_window_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "suppression_window_size", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The tags of the generated Signals
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="windowSizeMillis")
    def window_size_millis(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "window_size_millis")

    @window_size_millis.setter
    def window_size_millis(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "window_size_millis", value)


@pulumi.input_type
class _CseChainRuleState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 entity_selectors: Optional[pulumi.Input[Sequence[pulumi.Input['CseChainRuleEntitySelectorArgs']]]] = None,
                 expressions_and_limits: Optional[pulumi.Input[Sequence[pulumi.Input['CseChainRuleExpressionsAndLimitArgs']]]] = None,
                 group_by_fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 is_prototype: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ordered: Optional[pulumi.Input[bool]] = None,
                 severity: Optional[pulumi.Input[int]] = None,
                 summary_expression: Optional[pulumi.Input[str]] = None,
                 suppression_window_size: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 window_size: Optional[pulumi.Input[str]] = None,
                 window_size_millis: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CseChainRule resources.
        :param pulumi.Input[str] description: The description of the generated Signals
        :param pulumi.Input[bool] enabled: Whether the rule should generate Signals
        :param pulumi.Input[Sequence[pulumi.Input['CseChainRuleEntitySelectorArgs']]] entity_selectors: The entities to generate Signals on
               + `entityType` - (Required) The type of the entity to generate the Signal on.
        :param pulumi.Input[Sequence[pulumi.Input['CseChainRuleExpressionsAndLimitArgs']]] expressions_and_limits: The list of expressions and associated limits to make up the conditions of the chain rule
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_by_fields: A list of fields to group records by
        :param pulumi.Input[bool] is_prototype: Whether the generated Signals should be prototype Signals
        :param pulumi.Input[str] name: The name of the Rule and the generated SignalS
        :param pulumi.Input[bool] ordered: Whether the records matching the expressions must be in the same chronological order as the expressions are listed in the rule
        :param pulumi.Input[int] severity: The severity of the generated Signals
        :param pulumi.Input[str] summary_expression: The summary of the generated Signals
        :param pulumi.Input[int] suppression_window_size: For how long to suppress Signal generation, in milliseconds. Must be greater than `window_size` and less than the global limit of 7 days.
               
               The following attributes are exported:
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the generated Signals
        :param pulumi.Input[str] window_size: How long of a window to aggregate records for. Current acceptable values are T05M, T10M, T30M, T60M, T24H, T12H, T05D or CUSTOM
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if entity_selectors is not None:
            pulumi.set(__self__, "entity_selectors", entity_selectors)
        if expressions_and_limits is not None:
            pulumi.set(__self__, "expressions_and_limits", expressions_and_limits)
        if group_by_fields is not None:
            pulumi.set(__self__, "group_by_fields", group_by_fields)
        if is_prototype is not None:
            pulumi.set(__self__, "is_prototype", is_prototype)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ordered is not None:
            pulumi.set(__self__, "ordered", ordered)
        if severity is not None:
            pulumi.set(__self__, "severity", severity)
        if summary_expression is not None:
            pulumi.set(__self__, "summary_expression", summary_expression)
        if suppression_window_size is not None:
            pulumi.set(__self__, "suppression_window_size", suppression_window_size)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if window_size is not None:
            pulumi.set(__self__, "window_size", window_size)
        if window_size_millis is not None:
            pulumi.set(__self__, "window_size_millis", window_size_millis)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the generated Signals
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the rule should generate Signals
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="entitySelectors")
    def entity_selectors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CseChainRuleEntitySelectorArgs']]]]:
        """
        The entities to generate Signals on
        + `entityType` - (Required) The type of the entity to generate the Signal on.
        """
        return pulumi.get(self, "entity_selectors")

    @entity_selectors.setter
    def entity_selectors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CseChainRuleEntitySelectorArgs']]]]):
        pulumi.set(self, "entity_selectors", value)

    @property
    @pulumi.getter(name="expressionsAndLimits")
    def expressions_and_limits(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CseChainRuleExpressionsAndLimitArgs']]]]:
        """
        The list of expressions and associated limits to make up the conditions of the chain rule
        """
        return pulumi.get(self, "expressions_and_limits")

    @expressions_and_limits.setter
    def expressions_and_limits(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CseChainRuleExpressionsAndLimitArgs']]]]):
        pulumi.set(self, "expressions_and_limits", value)

    @property
    @pulumi.getter(name="groupByFields")
    def group_by_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of fields to group records by
        """
        return pulumi.get(self, "group_by_fields")

    @group_by_fields.setter
    def group_by_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "group_by_fields", value)

    @property
    @pulumi.getter(name="isPrototype")
    def is_prototype(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the generated Signals should be prototype Signals
        """
        return pulumi.get(self, "is_prototype")

    @is_prototype.setter
    def is_prototype(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_prototype", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Rule and the generated SignalS
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def ordered(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the records matching the expressions must be in the same chronological order as the expressions are listed in the rule
        """
        return pulumi.get(self, "ordered")

    @ordered.setter
    def ordered(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ordered", value)

    @property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[int]]:
        """
        The severity of the generated Signals
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "severity", value)

    @property
    @pulumi.getter(name="summaryExpression")
    def summary_expression(self) -> Optional[pulumi.Input[str]]:
        """
        The summary of the generated Signals
        """
        return pulumi.get(self, "summary_expression")

    @summary_expression.setter
    def summary_expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "summary_expression", value)

    @property
    @pulumi.getter(name="suppressionWindowSize")
    def suppression_window_size(self) -> Optional[pulumi.Input[int]]:
        """
        For how long to suppress Signal generation, in milliseconds. Must be greater than `window_size` and less than the global limit of 7 days.

        The following attributes are exported:
        """
        return pulumi.get(self, "suppression_window_size")

    @suppression_window_size.setter
    def suppression_window_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "suppression_window_size", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The tags of the generated Signals
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> Optional[pulumi.Input[str]]:
        """
        How long of a window to aggregate records for. Current acceptable values are T05M, T10M, T30M, T60M, T24H, T12H, T05D or CUSTOM
        """
        return pulumi.get(self, "window_size")

    @window_size.setter
    def window_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "window_size", value)

    @property
    @pulumi.getter(name="windowSizeMillis")
    def window_size_millis(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "window_size_millis")

    @window_size_millis.setter
    def window_size_millis(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "window_size_millis", value)


class CseChainRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 entity_selectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CseChainRuleEntitySelectorArgs']]]]] = None,
                 expressions_and_limits: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CseChainRuleExpressionsAndLimitArgs']]]]] = None,
                 group_by_fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 is_prototype: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ordered: Optional[pulumi.Input[bool]] = None,
                 severity: Optional[pulumi.Input[int]] = None,
                 summary_expression: Optional[pulumi.Input[str]] = None,
                 suppression_window_size: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 window_size: Optional[pulumi.Input[str]] = None,
                 window_size_millis: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Sumo Logic CSE [Chain Rule](https://help.sumologic.com/Cloud_SIEM_Enterprise/CSE_Rules/07_Write_a_Chain_Rule).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        chain_rule = sumologic.CseChainRule("chain_rule",
            description="Signal description",
            enabled=True,
            entity_selectors=[sumologic.CseChainRuleEntitySelectorArgs(
                entity_type="_username",
                expression="user_username",
            )],
            expressions_and_limits=[
                sumologic.CseChainRuleExpressionsAndLimitArgs(
                    expression="success = false",
                    limit=5,
                ),
                sumologic.CseChainRuleExpressionsAndLimitArgs(
                    expression="success = true",
                    limit=1,
                ),
            ],
            group_by_fields=[],
            is_prototype=False,
            ordered=True,
            name="Chain Rule Example",
            severity=5,
            summary_expression="Signal summary",
            tags=["_mitreAttackTactic:TA0009"],
            window_size="T30M",
            suppression_window_size=2100000)
        ```

        ## Import

        Chain Rules can be imported using the field id, e.g.:

        hcl

        ```sh
        $ pulumi import sumologic:index/cseChainRule:CseChainRule chain_rule id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the generated Signals
        :param pulumi.Input[bool] enabled: Whether the rule should generate Signals
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CseChainRuleEntitySelectorArgs']]]] entity_selectors: The entities to generate Signals on
               + `entityType` - (Required) The type of the entity to generate the Signal on.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CseChainRuleExpressionsAndLimitArgs']]]] expressions_and_limits: The list of expressions and associated limits to make up the conditions of the chain rule
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_by_fields: A list of fields to group records by
        :param pulumi.Input[bool] is_prototype: Whether the generated Signals should be prototype Signals
        :param pulumi.Input[str] name: The name of the Rule and the generated SignalS
        :param pulumi.Input[bool] ordered: Whether the records matching the expressions must be in the same chronological order as the expressions are listed in the rule
        :param pulumi.Input[int] severity: The severity of the generated Signals
        :param pulumi.Input[str] summary_expression: The summary of the generated Signals
        :param pulumi.Input[int] suppression_window_size: For how long to suppress Signal generation, in milliseconds. Must be greater than `window_size` and less than the global limit of 7 days.
               
               The following attributes are exported:
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the generated Signals
        :param pulumi.Input[str] window_size: How long of a window to aggregate records for. Current acceptable values are T05M, T10M, T30M, T60M, T24H, T12H, T05D or CUSTOM
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CseChainRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Sumo Logic CSE [Chain Rule](https://help.sumologic.com/Cloud_SIEM_Enterprise/CSE_Rules/07_Write_a_Chain_Rule).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        chain_rule = sumologic.CseChainRule("chain_rule",
            description="Signal description",
            enabled=True,
            entity_selectors=[sumologic.CseChainRuleEntitySelectorArgs(
                entity_type="_username",
                expression="user_username",
            )],
            expressions_and_limits=[
                sumologic.CseChainRuleExpressionsAndLimitArgs(
                    expression="success = false",
                    limit=5,
                ),
                sumologic.CseChainRuleExpressionsAndLimitArgs(
                    expression="success = true",
                    limit=1,
                ),
            ],
            group_by_fields=[],
            is_prototype=False,
            ordered=True,
            name="Chain Rule Example",
            severity=5,
            summary_expression="Signal summary",
            tags=["_mitreAttackTactic:TA0009"],
            window_size="T30M",
            suppression_window_size=2100000)
        ```

        ## Import

        Chain Rules can be imported using the field id, e.g.:

        hcl

        ```sh
        $ pulumi import sumologic:index/cseChainRule:CseChainRule chain_rule id
        ```

        :param str resource_name: The name of the resource.
        :param CseChainRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CseChainRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 entity_selectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CseChainRuleEntitySelectorArgs']]]]] = None,
                 expressions_and_limits: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CseChainRuleExpressionsAndLimitArgs']]]]] = None,
                 group_by_fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 is_prototype: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ordered: Optional[pulumi.Input[bool]] = None,
                 severity: Optional[pulumi.Input[int]] = None,
                 summary_expression: Optional[pulumi.Input[str]] = None,
                 suppression_window_size: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 window_size: Optional[pulumi.Input[str]] = None,
                 window_size_millis: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CseChainRuleArgs.__new__(CseChainRuleArgs)

            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            if entity_selectors is None and not opts.urn:
                raise TypeError("Missing required property 'entity_selectors'")
            __props__.__dict__["entity_selectors"] = entity_selectors
            if expressions_and_limits is None and not opts.urn:
                raise TypeError("Missing required property 'expressions_and_limits'")
            __props__.__dict__["expressions_and_limits"] = expressions_and_limits
            __props__.__dict__["group_by_fields"] = group_by_fields
            __props__.__dict__["is_prototype"] = is_prototype
            __props__.__dict__["name"] = name
            __props__.__dict__["ordered"] = ordered
            if severity is None and not opts.urn:
                raise TypeError("Missing required property 'severity'")
            __props__.__dict__["severity"] = severity
            __props__.__dict__["summary_expression"] = summary_expression
            __props__.__dict__["suppression_window_size"] = suppression_window_size
            __props__.__dict__["tags"] = tags
            if window_size is None and not opts.urn:
                raise TypeError("Missing required property 'window_size'")
            __props__.__dict__["window_size"] = window_size
            __props__.__dict__["window_size_millis"] = window_size_millis
        super(CseChainRule, __self__).__init__(
            'sumologic:index/cseChainRule:CseChainRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            entity_selectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CseChainRuleEntitySelectorArgs']]]]] = None,
            expressions_and_limits: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CseChainRuleExpressionsAndLimitArgs']]]]] = None,
            group_by_fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            is_prototype: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            ordered: Optional[pulumi.Input[bool]] = None,
            severity: Optional[pulumi.Input[int]] = None,
            summary_expression: Optional[pulumi.Input[str]] = None,
            suppression_window_size: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            window_size: Optional[pulumi.Input[str]] = None,
            window_size_millis: Optional[pulumi.Input[str]] = None) -> 'CseChainRule':
        """
        Get an existing CseChainRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the generated Signals
        :param pulumi.Input[bool] enabled: Whether the rule should generate Signals
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CseChainRuleEntitySelectorArgs']]]] entity_selectors: The entities to generate Signals on
               + `entityType` - (Required) The type of the entity to generate the Signal on.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CseChainRuleExpressionsAndLimitArgs']]]] expressions_and_limits: The list of expressions and associated limits to make up the conditions of the chain rule
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_by_fields: A list of fields to group records by
        :param pulumi.Input[bool] is_prototype: Whether the generated Signals should be prototype Signals
        :param pulumi.Input[str] name: The name of the Rule and the generated SignalS
        :param pulumi.Input[bool] ordered: Whether the records matching the expressions must be in the same chronological order as the expressions are listed in the rule
        :param pulumi.Input[int] severity: The severity of the generated Signals
        :param pulumi.Input[str] summary_expression: The summary of the generated Signals
        :param pulumi.Input[int] suppression_window_size: For how long to suppress Signal generation, in milliseconds. Must be greater than `window_size` and less than the global limit of 7 days.
               
               The following attributes are exported:
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the generated Signals
        :param pulumi.Input[str] window_size: How long of a window to aggregate records for. Current acceptable values are T05M, T10M, T30M, T60M, T24H, T12H, T05D or CUSTOM
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CseChainRuleState.__new__(_CseChainRuleState)

        __props__.__dict__["description"] = description
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["entity_selectors"] = entity_selectors
        __props__.__dict__["expressions_and_limits"] = expressions_and_limits
        __props__.__dict__["group_by_fields"] = group_by_fields
        __props__.__dict__["is_prototype"] = is_prototype
        __props__.__dict__["name"] = name
        __props__.__dict__["ordered"] = ordered
        __props__.__dict__["severity"] = severity
        __props__.__dict__["summary_expression"] = summary_expression
        __props__.__dict__["suppression_window_size"] = suppression_window_size
        __props__.__dict__["tags"] = tags
        __props__.__dict__["window_size"] = window_size
        __props__.__dict__["window_size_millis"] = window_size_millis
        return CseChainRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the generated Signals
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Whether the rule should generate Signals
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="entitySelectors")
    def entity_selectors(self) -> pulumi.Output[Sequence['outputs.CseChainRuleEntitySelector']]:
        """
        The entities to generate Signals on
        + `entityType` - (Required) The type of the entity to generate the Signal on.
        """
        return pulumi.get(self, "entity_selectors")

    @property
    @pulumi.getter(name="expressionsAndLimits")
    def expressions_and_limits(self) -> pulumi.Output[Sequence['outputs.CseChainRuleExpressionsAndLimit']]:
        """
        The list of expressions and associated limits to make up the conditions of the chain rule
        """
        return pulumi.get(self, "expressions_and_limits")

    @property
    @pulumi.getter(name="groupByFields")
    def group_by_fields(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of fields to group records by
        """
        return pulumi.get(self, "group_by_fields")

    @property
    @pulumi.getter(name="isPrototype")
    def is_prototype(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the generated Signals should be prototype Signals
        """
        return pulumi.get(self, "is_prototype")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Rule and the generated SignalS
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def ordered(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the records matching the expressions must be in the same chronological order as the expressions are listed in the rule
        """
        return pulumi.get(self, "ordered")

    @property
    @pulumi.getter
    def severity(self) -> pulumi.Output[int]:
        """
        The severity of the generated Signals
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter(name="summaryExpression")
    def summary_expression(self) -> pulumi.Output[Optional[str]]:
        """
        The summary of the generated Signals
        """
        return pulumi.get(self, "summary_expression")

    @property
    @pulumi.getter(name="suppressionWindowSize")
    def suppression_window_size(self) -> pulumi.Output[Optional[int]]:
        """
        For how long to suppress Signal generation, in milliseconds. Must be greater than `window_size` and less than the global limit of 7 days.

        The following attributes are exported:
        """
        return pulumi.get(self, "suppression_window_size")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The tags of the generated Signals
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> pulumi.Output[str]:
        """
        How long of a window to aggregate records for. Current acceptable values are T05M, T10M, T30M, T60M, T24H, T12H, T05D or CUSTOM
        """
        return pulumi.get(self, "window_size")

    @property
    @pulumi.getter(name="windowSizeMillis")
    def window_size_millis(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "window_size_millis")

