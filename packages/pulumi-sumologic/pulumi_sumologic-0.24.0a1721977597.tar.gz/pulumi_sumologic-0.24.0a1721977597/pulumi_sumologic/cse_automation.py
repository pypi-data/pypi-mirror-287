# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CseAutomationArgs', 'CseAutomation']

@pulumi.input_type
class CseAutomationArgs:
    def __init__(__self__, *,
                 cse_resource_type: pulumi.Input[str],
                 enabled: pulumi.Input[bool],
                 execution_types: pulumi.Input[Sequence[pulumi.Input[str]]],
                 playbook_id: pulumi.Input[str],
                 cse_resource_sub_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a CseAutomation resource.
        :param pulumi.Input[str] cse_resource_type: CSE Resource type for automation. Valid values: "INSIGHT", "ENTITY".
        :param pulumi.Input[Sequence[pulumi.Input[str]]] execution_types: Automation execution type. Valid values: "NEW_INSIGHT", "INSIGHT_CLOSED", "ON_DEMAND".
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cse_resource_sub_types: CSE Resource sub-type when cse_resource_type is specified as "ENTITY". Examples: "_ip", "_mac".
               
               The following attributes are exported:
        """
        pulumi.set(__self__, "cse_resource_type", cse_resource_type)
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "execution_types", execution_types)
        pulumi.set(__self__, "playbook_id", playbook_id)
        if cse_resource_sub_types is not None:
            pulumi.set(__self__, "cse_resource_sub_types", cse_resource_sub_types)

    @property
    @pulumi.getter(name="cseResourceType")
    def cse_resource_type(self) -> pulumi.Input[str]:
        """
        CSE Resource type for automation. Valid values: "INSIGHT", "ENTITY".
        """
        return pulumi.get(self, "cse_resource_type")

    @cse_resource_type.setter
    def cse_resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "cse_resource_type", value)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="executionTypes")
    def execution_types(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Automation execution type. Valid values: "NEW_INSIGHT", "INSIGHT_CLOSED", "ON_DEMAND".
        """
        return pulumi.get(self, "execution_types")

    @execution_types.setter
    def execution_types(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "execution_types", value)

    @property
    @pulumi.getter(name="playbookId")
    def playbook_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "playbook_id")

    @playbook_id.setter
    def playbook_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "playbook_id", value)

    @property
    @pulumi.getter(name="cseResourceSubTypes")
    def cse_resource_sub_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        CSE Resource sub-type when cse_resource_type is specified as "ENTITY". Examples: "_ip", "_mac".

        The following attributes are exported:
        """
        return pulumi.get(self, "cse_resource_sub_types")

    @cse_resource_sub_types.setter
    def cse_resource_sub_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "cse_resource_sub_types", value)


@pulumi.input_type
class _CseAutomationState:
    def __init__(__self__, *,
                 cse_resource_sub_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cse_resource_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 execution_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 playbook_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CseAutomation resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cse_resource_sub_types: CSE Resource sub-type when cse_resource_type is specified as "ENTITY". Examples: "_ip", "_mac".
               
               The following attributes are exported:
        :param pulumi.Input[str] cse_resource_type: CSE Resource type for automation. Valid values: "INSIGHT", "ENTITY".
        :param pulumi.Input[str] description: Automation description.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] execution_types: Automation execution type. Valid values: "NEW_INSIGHT", "INSIGHT_CLOSED", "ON_DEMAND".
        :param pulumi.Input[str] name: Automation name.
        """
        if cse_resource_sub_types is not None:
            pulumi.set(__self__, "cse_resource_sub_types", cse_resource_sub_types)
        if cse_resource_type is not None:
            pulumi.set(__self__, "cse_resource_type", cse_resource_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if execution_types is not None:
            pulumi.set(__self__, "execution_types", execution_types)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if playbook_id is not None:
            pulumi.set(__self__, "playbook_id", playbook_id)

    @property
    @pulumi.getter(name="cseResourceSubTypes")
    def cse_resource_sub_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        CSE Resource sub-type when cse_resource_type is specified as "ENTITY". Examples: "_ip", "_mac".

        The following attributes are exported:
        """
        return pulumi.get(self, "cse_resource_sub_types")

    @cse_resource_sub_types.setter
    def cse_resource_sub_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "cse_resource_sub_types", value)

    @property
    @pulumi.getter(name="cseResourceType")
    def cse_resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        CSE Resource type for automation. Valid values: "INSIGHT", "ENTITY".
        """
        return pulumi.get(self, "cse_resource_type")

    @cse_resource_type.setter
    def cse_resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cse_resource_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Automation description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="executionTypes")
    def execution_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Automation execution type. Valid values: "NEW_INSIGHT", "INSIGHT_CLOSED", "ON_DEMAND".
        """
        return pulumi.get(self, "execution_types")

    @execution_types.setter
    def execution_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "execution_types", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Automation name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="playbookId")
    def playbook_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "playbook_id")

    @playbook_id.setter
    def playbook_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "playbook_id", value)


class CseAutomation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cse_resource_sub_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cse_resource_type: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 execution_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 playbook_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Sumologic CSE Automation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        insight_automation = sumologic.CseAutomation("insight_automation",
            playbook_id="638079aedb99cafada1e80a0",
            cse_resource_type="INSIGHT",
            execution_types=[
                "NEW_INSIGHT",
                "INSIGHT_CLOSED",
            ])
        entity_automation = sumologic.CseAutomation("entity_automation",
            playbook_id="638079aedb99cafada1e80a0",
            cse_resource_type="ENTITY",
            cse_resource_sub_types=["_ip"],
            execution_types=["ON_DEMAND"])
        ```

        ## Import

        Automation can be imported using the field id, e.g.:

        hcl

        ```sh
        $ pulumi import sumologic:index/cseAutomation:CseAutomation automation id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cse_resource_sub_types: CSE Resource sub-type when cse_resource_type is specified as "ENTITY". Examples: "_ip", "_mac".
               
               The following attributes are exported:
        :param pulumi.Input[str] cse_resource_type: CSE Resource type for automation. Valid values: "INSIGHT", "ENTITY".
        :param pulumi.Input[Sequence[pulumi.Input[str]]] execution_types: Automation execution type. Valid values: "NEW_INSIGHT", "INSIGHT_CLOSED", "ON_DEMAND".
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CseAutomationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Sumologic CSE Automation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        insight_automation = sumologic.CseAutomation("insight_automation",
            playbook_id="638079aedb99cafada1e80a0",
            cse_resource_type="INSIGHT",
            execution_types=[
                "NEW_INSIGHT",
                "INSIGHT_CLOSED",
            ])
        entity_automation = sumologic.CseAutomation("entity_automation",
            playbook_id="638079aedb99cafada1e80a0",
            cse_resource_type="ENTITY",
            cse_resource_sub_types=["_ip"],
            execution_types=["ON_DEMAND"])
        ```

        ## Import

        Automation can be imported using the field id, e.g.:

        hcl

        ```sh
        $ pulumi import sumologic:index/cseAutomation:CseAutomation automation id
        ```

        :param str resource_name: The name of the resource.
        :param CseAutomationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CseAutomationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cse_resource_sub_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cse_resource_type: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 execution_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 playbook_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CseAutomationArgs.__new__(CseAutomationArgs)

            __props__.__dict__["cse_resource_sub_types"] = cse_resource_sub_types
            if cse_resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'cse_resource_type'")
            __props__.__dict__["cse_resource_type"] = cse_resource_type
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            if execution_types is None and not opts.urn:
                raise TypeError("Missing required property 'execution_types'")
            __props__.__dict__["execution_types"] = execution_types
            if playbook_id is None and not opts.urn:
                raise TypeError("Missing required property 'playbook_id'")
            __props__.__dict__["playbook_id"] = playbook_id
            __props__.__dict__["description"] = None
            __props__.__dict__["name"] = None
        super(CseAutomation, __self__).__init__(
            'sumologic:index/cseAutomation:CseAutomation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cse_resource_sub_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            cse_resource_type: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            execution_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            playbook_id: Optional[pulumi.Input[str]] = None) -> 'CseAutomation':
        """
        Get an existing CseAutomation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cse_resource_sub_types: CSE Resource sub-type when cse_resource_type is specified as "ENTITY". Examples: "_ip", "_mac".
               
               The following attributes are exported:
        :param pulumi.Input[str] cse_resource_type: CSE Resource type for automation. Valid values: "INSIGHT", "ENTITY".
        :param pulumi.Input[str] description: Automation description.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] execution_types: Automation execution type. Valid values: "NEW_INSIGHT", "INSIGHT_CLOSED", "ON_DEMAND".
        :param pulumi.Input[str] name: Automation name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CseAutomationState.__new__(_CseAutomationState)

        __props__.__dict__["cse_resource_sub_types"] = cse_resource_sub_types
        __props__.__dict__["cse_resource_type"] = cse_resource_type
        __props__.__dict__["description"] = description
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["execution_types"] = execution_types
        __props__.__dict__["name"] = name
        __props__.__dict__["playbook_id"] = playbook_id
        return CseAutomation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cseResourceSubTypes")
    def cse_resource_sub_types(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        CSE Resource sub-type when cse_resource_type is specified as "ENTITY". Examples: "_ip", "_mac".

        The following attributes are exported:
        """
        return pulumi.get(self, "cse_resource_sub_types")

    @property
    @pulumi.getter(name="cseResourceType")
    def cse_resource_type(self) -> pulumi.Output[str]:
        """
        CSE Resource type for automation. Valid values: "INSIGHT", "ENTITY".
        """
        return pulumi.get(self, "cse_resource_type")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Automation description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="executionTypes")
    def execution_types(self) -> pulumi.Output[Sequence[str]]:
        """
        Automation execution type. Valid values: "NEW_INSIGHT", "INSIGHT_CLOSED", "ON_DEMAND".
        """
        return pulumi.get(self, "execution_types")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Automation name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="playbookId")
    def playbook_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "playbook_id")

