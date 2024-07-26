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
    'ClientAuthenticationFlowBindingOverridesArgs',
]

@pulumi.input_type
class ClientAuthenticationFlowBindingOverridesArgs:
    def __init__(__self__, *,
                 browser_id: Optional[pulumi.Input[str]] = None,
                 direct_grant_id: Optional[pulumi.Input[str]] = None):
        if browser_id is not None:
            pulumi.set(__self__, "browser_id", browser_id)
        if direct_grant_id is not None:
            pulumi.set(__self__, "direct_grant_id", direct_grant_id)

    @property
    @pulumi.getter(name="browserId")
    def browser_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "browser_id")

    @browser_id.setter
    def browser_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "browser_id", value)

    @property
    @pulumi.getter(name="directGrantId")
    def direct_grant_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "direct_grant_id")

    @direct_grant_id.setter
    def direct_grant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "direct_grant_id", value)


