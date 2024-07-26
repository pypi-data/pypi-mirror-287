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
    'GetTriggerResult',
    'AwaitableGetTriggerResult',
    'get_trigger',
    'get_trigger_output',
]

@pulumi.output_type
class GetTriggerResult:
    """
    A collection of values returned by getTrigger.
    """
    def __init__(__self__, app_id=None, conditions=None, description=None, id=None, name=None):
        if app_id and not isinstance(app_id, str):
            raise TypeError("Expected argument 'app_id' to be a str")
        pulumi.set(__self__, "app_id", app_id)
        if conditions and not isinstance(conditions, list):
            raise TypeError("Expected argument 'conditions' to be a list")
        pulumi.set(__self__, "conditions", conditions)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[str]:
        """
        The id of the application.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter
    def conditions(self) -> Sequence['outputs.GetTriggerConditionResult']:
        """
        The condition that will execute the Trigger: On new artifact, On pipeline completion, On Cron schedule, On webhook, On New Manifest.
        """
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The trigger description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Unique identifier of the trigger.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the trigger.
        """
        return pulumi.get(self, "name")


class AwaitableGetTriggerResult(GetTriggerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTriggerResult(
            app_id=self.app_id,
            conditions=self.conditions,
            description=self.description,
            id=self.id,
            name=self.name)


def get_trigger(app_id: Optional[str] = None,
                description: Optional[str] = None,
                id: Optional[str] = None,
                name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTriggerResult:
    """
    Data source for retrieving a Harness trigger.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_harness as harness

    example_by_name = harness.get_trigger(app_id="app_id",
        name="name")
    example_by_id = harness.get_trigger(id="trigger_id")
    ```


    :param str app_id: The id of the application.
    :param str description: The trigger description.
    :param str id: Unique identifier of the trigger.
    :param str name: The name of the trigger.
    """
    __args__ = dict()
    __args__['appId'] = app_id
    __args__['description'] = description
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('harness:index/getTrigger:getTrigger', __args__, opts=opts, typ=GetTriggerResult).value

    return AwaitableGetTriggerResult(
        app_id=pulumi.get(__ret__, 'app_id'),
        conditions=pulumi.get(__ret__, 'conditions'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_trigger)
def get_trigger_output(app_id: Optional[pulumi.Input[Optional[str]]] = None,
                       description: Optional[pulumi.Input[Optional[str]]] = None,
                       id: Optional[pulumi.Input[Optional[str]]] = None,
                       name: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTriggerResult]:
    """
    Data source for retrieving a Harness trigger.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_harness as harness

    example_by_name = harness.get_trigger(app_id="app_id",
        name="name")
    example_by_id = harness.get_trigger(id="trigger_id")
    ```


    :param str app_id: The id of the application.
    :param str description: The trigger description.
    :param str id: Unique identifier of the trigger.
    :param str name: The name of the trigger.
    """
    ...
