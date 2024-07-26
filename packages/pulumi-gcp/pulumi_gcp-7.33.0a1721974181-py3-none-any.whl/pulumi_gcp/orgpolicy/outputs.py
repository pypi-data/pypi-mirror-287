# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities
from . import outputs

__all__ = [
    'PolicyDryRunSpec',
    'PolicyDryRunSpecRule',
    'PolicyDryRunSpecRuleCondition',
    'PolicyDryRunSpecRuleValues',
    'PolicySpec',
    'PolicySpecRule',
    'PolicySpecRuleCondition',
    'PolicySpecRuleValues',
]

@pulumi.output_type
class PolicyDryRunSpec(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "inheritFromParent":
            suggest = "inherit_from_parent"
        elif key == "updateTime":
            suggest = "update_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PolicyDryRunSpec. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PolicyDryRunSpec.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PolicyDryRunSpec.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 etag: Optional[str] = None,
                 inherit_from_parent: Optional[bool] = None,
                 reset: Optional[bool] = None,
                 rules: Optional[Sequence['outputs.PolicyDryRunSpecRule']] = None,
                 update_time: Optional[str] = None):
        """
        :param str etag: (Output)
               An opaque tag indicating the current version of the policy, used for concurrency control. This field is ignored if used in a `CreatePolicy` request. When the policy` is returned from either a `GetPolicy` or a `ListPolicies` request, this `etag` indicates the version of the current policy to use when executing a read-modify-write loop. When the policy is returned from a `GetEffectivePolicy` request, the `etag` will be unset.
        :param bool inherit_from_parent: Determines the inheritance behavior for this policy. If `inherit_from_parent` is true, policy rules set higher up in the hierarchy (up to the closest root) are inherited and present in the effective policy. If it is false, then no rules are inherited, and this policy becomes the new root for evaluation. This field can be set only for policies which configure list constraints.
        :param bool reset: Ignores policies set above this resource and restores the `constraint_default` enforcement behavior of the specific constraint at this resource. This field can be set in policies for either list or boolean constraints. If set, `rules` must be empty and `inherit_from_parent` must be set to false.
        :param Sequence['PolicyDryRunSpecRuleArgs'] rules: In policies for boolean constraints, the following requirements apply: - There must be one and only one policy rule where condition is unset. - Boolean policy rules with conditions must set `enforced` to the opposite of the policy rule without a condition. - During policy evaluation, policy rules with conditions that are true for a target resource take precedence.
               Structure is documented below.
        :param str update_time: (Output)
               Output only. The time stamp this was previously updated. This represents the last time a call to `CreatePolicy` or `UpdatePolicy` was made for that policy.
        """
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if inherit_from_parent is not None:
            pulumi.set(__self__, "inherit_from_parent", inherit_from_parent)
        if reset is not None:
            pulumi.set(__self__, "reset", reset)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        (Output)
        An opaque tag indicating the current version of the policy, used for concurrency control. This field is ignored if used in a `CreatePolicy` request. When the policy` is returned from either a `GetPolicy` or a `ListPolicies` request, this `etag` indicates the version of the current policy to use when executing a read-modify-write loop. When the policy is returned from a `GetEffectivePolicy` request, the `etag` will be unset.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="inheritFromParent")
    def inherit_from_parent(self) -> Optional[bool]:
        """
        Determines the inheritance behavior for this policy. If `inherit_from_parent` is true, policy rules set higher up in the hierarchy (up to the closest root) are inherited and present in the effective policy. If it is false, then no rules are inherited, and this policy becomes the new root for evaluation. This field can be set only for policies which configure list constraints.
        """
        return pulumi.get(self, "inherit_from_parent")

    @property
    @pulumi.getter
    def reset(self) -> Optional[bool]:
        """
        Ignores policies set above this resource and restores the `constraint_default` enforcement behavior of the specific constraint at this resource. This field can be set in policies for either list or boolean constraints. If set, `rules` must be empty and `inherit_from_parent` must be set to false.
        """
        return pulumi.get(self, "reset")

    @property
    @pulumi.getter
    def rules(self) -> Optional[Sequence['outputs.PolicyDryRunSpecRule']]:
        """
        In policies for boolean constraints, the following requirements apply: - There must be one and only one policy rule where condition is unset. - Boolean policy rules with conditions must set `enforced` to the opposite of the policy rule without a condition. - During policy evaluation, policy rules with conditions that are true for a target resource take precedence.
        Structure is documented below.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[str]:
        """
        (Output)
        Output only. The time stamp this was previously updated. This represents the last time a call to `CreatePolicy` or `UpdatePolicy` was made for that policy.
        """
        return pulumi.get(self, "update_time")


@pulumi.output_type
class PolicyDryRunSpecRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowAll":
            suggest = "allow_all"
        elif key == "denyAll":
            suggest = "deny_all"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PolicyDryRunSpecRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PolicyDryRunSpecRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PolicyDryRunSpecRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allow_all: Optional[str] = None,
                 condition: Optional['outputs.PolicyDryRunSpecRuleCondition'] = None,
                 deny_all: Optional[str] = None,
                 enforce: Optional[str] = None,
                 values: Optional['outputs.PolicyDryRunSpecRuleValues'] = None):
        """
        :param str allow_all: Setting this to `"TRUE"` means that all values are allowed. This field can be set only in Policies for list constraints.
        :param 'PolicyDryRunSpecRuleConditionArgs' condition: A condition which determines whether this rule is used in the evaluation of the policy. When set, the `expression` field in the `Expr' must include from 1 to 10 subexpressions, joined by the "||" or "&&" operators. Each subexpression must be of the form "resource.matchTag('/tag_key_short_name, 'tag_value_short_name')". or "resource.matchTagId('tagKeys/key_id', 'tagValues/value_id')". where key_name and value_name are the resource names for Label Keys and Values. These names are available from the Tag Manager Service. An example expression is: "resource.matchTag('123456789/environment, 'prod')". or "resource.matchTagId('tagKeys/123', 'tagValues/456')".
               Structure is documented below.
        :param str deny_all: Setting this to `"TRUE"` means that all values are denied. This field can be set only in Policies for list constraints.
        :param str enforce: If `"TRUE"`, then the `Policy` is enforced. If `"FALSE"`, then any configuration is acceptable. This field can be set only in Policies for boolean constraints.
        :param 'PolicyDryRunSpecRuleValuesArgs' values: List of values to be used for this policy rule. This field can be set only in policies for list constraints.
               Structure is documented below.
        """
        if allow_all is not None:
            pulumi.set(__self__, "allow_all", allow_all)
        if condition is not None:
            pulumi.set(__self__, "condition", condition)
        if deny_all is not None:
            pulumi.set(__self__, "deny_all", deny_all)
        if enforce is not None:
            pulumi.set(__self__, "enforce", enforce)
        if values is not None:
            pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter(name="allowAll")
    def allow_all(self) -> Optional[str]:
        """
        Setting this to `"TRUE"` means that all values are allowed. This field can be set only in Policies for list constraints.
        """
        return pulumi.get(self, "allow_all")

    @property
    @pulumi.getter
    def condition(self) -> Optional['outputs.PolicyDryRunSpecRuleCondition']:
        """
        A condition which determines whether this rule is used in the evaluation of the policy. When set, the `expression` field in the `Expr' must include from 1 to 10 subexpressions, joined by the "||" or "&&" operators. Each subexpression must be of the form "resource.matchTag('/tag_key_short_name, 'tag_value_short_name')". or "resource.matchTagId('tagKeys/key_id', 'tagValues/value_id')". where key_name and value_name are the resource names for Label Keys and Values. These names are available from the Tag Manager Service. An example expression is: "resource.matchTag('123456789/environment, 'prod')". or "resource.matchTagId('tagKeys/123', 'tagValues/456')".
        Structure is documented below.
        """
        return pulumi.get(self, "condition")

    @property
    @pulumi.getter(name="denyAll")
    def deny_all(self) -> Optional[str]:
        """
        Setting this to `"TRUE"` means that all values are denied. This field can be set only in Policies for list constraints.
        """
        return pulumi.get(self, "deny_all")

    @property
    @pulumi.getter
    def enforce(self) -> Optional[str]:
        """
        If `"TRUE"`, then the `Policy` is enforced. If `"FALSE"`, then any configuration is acceptable. This field can be set only in Policies for boolean constraints.
        """
        return pulumi.get(self, "enforce")

    @property
    @pulumi.getter
    def values(self) -> Optional['outputs.PolicyDryRunSpecRuleValues']:
        """
        List of values to be used for this policy rule. This field can be set only in policies for list constraints.
        Structure is documented below.
        """
        return pulumi.get(self, "values")


@pulumi.output_type
class PolicyDryRunSpecRuleCondition(dict):
    def __init__(__self__, *,
                 description: Optional[str] = None,
                 expression: Optional[str] = None,
                 location: Optional[str] = None,
                 title: Optional[str] = None):
        """
        :param str description: Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
        :param str expression: Textual representation of an expression in Common Expression Language syntax.
        :param str location: Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.
        :param str title: Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expression is not None:
            pulumi.set(__self__, "expression", expression)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def expression(self) -> Optional[str]:
        """
        Textual representation of an expression in Common Expression Language syntax.
        """
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def title(self) -> Optional[str]:
        """
        Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.
        """
        return pulumi.get(self, "title")


@pulumi.output_type
class PolicyDryRunSpecRuleValues(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowedValues":
            suggest = "allowed_values"
        elif key == "deniedValues":
            suggest = "denied_values"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PolicyDryRunSpecRuleValues. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PolicyDryRunSpecRuleValues.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PolicyDryRunSpecRuleValues.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allowed_values: Optional[Sequence[str]] = None,
                 denied_values: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] allowed_values: List of values allowed at this resource.
        :param Sequence[str] denied_values: List of values denied at this resource.
        """
        if allowed_values is not None:
            pulumi.set(__self__, "allowed_values", allowed_values)
        if denied_values is not None:
            pulumi.set(__self__, "denied_values", denied_values)

    @property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Optional[Sequence[str]]:
        """
        List of values allowed at this resource.
        """
        return pulumi.get(self, "allowed_values")

    @property
    @pulumi.getter(name="deniedValues")
    def denied_values(self) -> Optional[Sequence[str]]:
        """
        List of values denied at this resource.
        """
        return pulumi.get(self, "denied_values")


@pulumi.output_type
class PolicySpec(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "inheritFromParent":
            suggest = "inherit_from_parent"
        elif key == "updateTime":
            suggest = "update_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PolicySpec. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PolicySpec.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PolicySpec.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 etag: Optional[str] = None,
                 inherit_from_parent: Optional[bool] = None,
                 reset: Optional[bool] = None,
                 rules: Optional[Sequence['outputs.PolicySpecRule']] = None,
                 update_time: Optional[str] = None):
        """
        :param str etag: (Output)
               An opaque tag indicating the current version of the `Policy`, used for concurrency control. This field is ignored if used in a `CreatePolicy` request. When the `Policy` is returned from either a `GetPolicy` or a `ListPolicies` request, this `etag` indicates the version of the current `Policy` to use when executing a read-modify-write loop. When the `Policy` is returned from a `GetEffectivePolicy` request, the `etag` will be unset.
        :param bool inherit_from_parent: Determines the inheritance behavior for this `Policy`. If `inherit_from_parent` is true, PolicyRules set higher up in the hierarchy (up to the closest root) are inherited and present in the effective policy. If it is false, then no rules are inherited, and this Policy becomes the new root for evaluation. This field can be set only for Policies which configure list constraints.
        :param bool reset: Ignores policies set above this resource and restores the `constraint_default` enforcement behavior of the specific `Constraint` at this resource. This field can be set in policies for either list or boolean constraints. If set, `rules` must be empty and `inherit_from_parent` must be set to false.
        :param Sequence['PolicySpecRuleArgs'] rules: Up to 10 PolicyRules are allowed. In Policies for boolean constraints, the following requirements apply: - There must be one and only one PolicyRule where condition is unset. - BooleanPolicyRules with conditions must set `enforced` to the opposite of the PolicyRule without a condition. - During policy evaluation, PolicyRules with conditions that are true for a target resource take precedence.
               Structure is documented below.
        :param str update_time: (Output)
               Output only. The time stamp this was previously updated. This represents the last time a call to `CreatePolicy` or `UpdatePolicy` was made for that `Policy`.
        """
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if inherit_from_parent is not None:
            pulumi.set(__self__, "inherit_from_parent", inherit_from_parent)
        if reset is not None:
            pulumi.set(__self__, "reset", reset)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        (Output)
        An opaque tag indicating the current version of the `Policy`, used for concurrency control. This field is ignored if used in a `CreatePolicy` request. When the `Policy` is returned from either a `GetPolicy` or a `ListPolicies` request, this `etag` indicates the version of the current `Policy` to use when executing a read-modify-write loop. When the `Policy` is returned from a `GetEffectivePolicy` request, the `etag` will be unset.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="inheritFromParent")
    def inherit_from_parent(self) -> Optional[bool]:
        """
        Determines the inheritance behavior for this `Policy`. If `inherit_from_parent` is true, PolicyRules set higher up in the hierarchy (up to the closest root) are inherited and present in the effective policy. If it is false, then no rules are inherited, and this Policy becomes the new root for evaluation. This field can be set only for Policies which configure list constraints.
        """
        return pulumi.get(self, "inherit_from_parent")

    @property
    @pulumi.getter
    def reset(self) -> Optional[bool]:
        """
        Ignores policies set above this resource and restores the `constraint_default` enforcement behavior of the specific `Constraint` at this resource. This field can be set in policies for either list or boolean constraints. If set, `rules` must be empty and `inherit_from_parent` must be set to false.
        """
        return pulumi.get(self, "reset")

    @property
    @pulumi.getter
    def rules(self) -> Optional[Sequence['outputs.PolicySpecRule']]:
        """
        Up to 10 PolicyRules are allowed. In Policies for boolean constraints, the following requirements apply: - There must be one and only one PolicyRule where condition is unset. - BooleanPolicyRules with conditions must set `enforced` to the opposite of the PolicyRule without a condition. - During policy evaluation, PolicyRules with conditions that are true for a target resource take precedence.
        Structure is documented below.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[str]:
        """
        (Output)
        Output only. The time stamp this was previously updated. This represents the last time a call to `CreatePolicy` or `UpdatePolicy` was made for that `Policy`.
        """
        return pulumi.get(self, "update_time")


@pulumi.output_type
class PolicySpecRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowAll":
            suggest = "allow_all"
        elif key == "denyAll":
            suggest = "deny_all"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PolicySpecRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PolicySpecRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PolicySpecRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allow_all: Optional[str] = None,
                 condition: Optional['outputs.PolicySpecRuleCondition'] = None,
                 deny_all: Optional[str] = None,
                 enforce: Optional[str] = None,
                 values: Optional['outputs.PolicySpecRuleValues'] = None):
        """
        :param str allow_all: Setting this to `"TRUE"` means that all values are allowed. This field can be set only in Policies for list constraints.
        :param 'PolicySpecRuleConditionArgs' condition: A condition which determines whether this rule is used in the evaluation of the policy. When set, the `expression` field in the `Expr' must include from 1 to 10 subexpressions, joined by the "||" or "&&" operators. Each subexpression must be of the form "resource.matchTag('/tag_key_short_name, 'tag_value_short_name')". or "resource.matchTagId('tagKeys/key_id', 'tagValues/value_id')". where key_name and value_name are the resource names for Label Keys and Values. These names are available from the Tag Manager Service. An example expression is: "resource.matchTag('123456789/environment, 'prod')". or "resource.matchTagId('tagKeys/123', 'tagValues/456')".
               Structure is documented below.
        :param str deny_all: Setting this to `"TRUE"` means that all values are denied. This field can be set only in Policies for list constraints.
        :param str enforce: If `"TRUE"`, then the `Policy` is enforced. If `"FALSE"`, then any configuration is acceptable. This field can be set only in Policies for boolean constraints.
        :param 'PolicySpecRuleValuesArgs' values: List of values to be used for this policy rule. This field can be set only in policies for list constraints.
               Structure is documented below.
        """
        if allow_all is not None:
            pulumi.set(__self__, "allow_all", allow_all)
        if condition is not None:
            pulumi.set(__self__, "condition", condition)
        if deny_all is not None:
            pulumi.set(__self__, "deny_all", deny_all)
        if enforce is not None:
            pulumi.set(__self__, "enforce", enforce)
        if values is not None:
            pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter(name="allowAll")
    def allow_all(self) -> Optional[str]:
        """
        Setting this to `"TRUE"` means that all values are allowed. This field can be set only in Policies for list constraints.
        """
        return pulumi.get(self, "allow_all")

    @property
    @pulumi.getter
    def condition(self) -> Optional['outputs.PolicySpecRuleCondition']:
        """
        A condition which determines whether this rule is used in the evaluation of the policy. When set, the `expression` field in the `Expr' must include from 1 to 10 subexpressions, joined by the "||" or "&&" operators. Each subexpression must be of the form "resource.matchTag('/tag_key_short_name, 'tag_value_short_name')". or "resource.matchTagId('tagKeys/key_id', 'tagValues/value_id')". where key_name and value_name are the resource names for Label Keys and Values. These names are available from the Tag Manager Service. An example expression is: "resource.matchTag('123456789/environment, 'prod')". or "resource.matchTagId('tagKeys/123', 'tagValues/456')".
        Structure is documented below.
        """
        return pulumi.get(self, "condition")

    @property
    @pulumi.getter(name="denyAll")
    def deny_all(self) -> Optional[str]:
        """
        Setting this to `"TRUE"` means that all values are denied. This field can be set only in Policies for list constraints.
        """
        return pulumi.get(self, "deny_all")

    @property
    @pulumi.getter
    def enforce(self) -> Optional[str]:
        """
        If `"TRUE"`, then the `Policy` is enforced. If `"FALSE"`, then any configuration is acceptable. This field can be set only in Policies for boolean constraints.
        """
        return pulumi.get(self, "enforce")

    @property
    @pulumi.getter
    def values(self) -> Optional['outputs.PolicySpecRuleValues']:
        """
        List of values to be used for this policy rule. This field can be set only in policies for list constraints.
        Structure is documented below.
        """
        return pulumi.get(self, "values")


@pulumi.output_type
class PolicySpecRuleCondition(dict):
    def __init__(__self__, *,
                 description: Optional[str] = None,
                 expression: Optional[str] = None,
                 location: Optional[str] = None,
                 title: Optional[str] = None):
        """
        :param str description: Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
        :param str expression: Textual representation of an expression in Common Expression Language syntax.
        :param str location: Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.
        :param str title: Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expression is not None:
            pulumi.set(__self__, "expression", expression)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def expression(self) -> Optional[str]:
        """
        Textual representation of an expression in Common Expression Language syntax.
        """
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def title(self) -> Optional[str]:
        """
        Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.
        """
        return pulumi.get(self, "title")


@pulumi.output_type
class PolicySpecRuleValues(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowedValues":
            suggest = "allowed_values"
        elif key == "deniedValues":
            suggest = "denied_values"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PolicySpecRuleValues. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PolicySpecRuleValues.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PolicySpecRuleValues.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allowed_values: Optional[Sequence[str]] = None,
                 denied_values: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] allowed_values: List of values allowed at this resource.
        :param Sequence[str] denied_values: List of values denied at this resource.
        """
        if allowed_values is not None:
            pulumi.set(__self__, "allowed_values", allowed_values)
        if denied_values is not None:
            pulumi.set(__self__, "denied_values", denied_values)

    @property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Optional[Sequence[str]]:
        """
        List of values allowed at this resource.
        """
        return pulumi.get(self, "allowed_values")

    @property
    @pulumi.getter(name="deniedValues")
    def denied_values(self) -> Optional[Sequence[str]]:
        """
        List of values denied at this resource.
        """
        return pulumi.get(self, "denied_values")


