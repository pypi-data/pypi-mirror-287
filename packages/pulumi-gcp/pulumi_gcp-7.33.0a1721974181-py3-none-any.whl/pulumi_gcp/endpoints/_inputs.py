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

__all__ = [
    'ConsumersIamBindingConditionArgs',
    'ConsumersIamBindingConditionArgsDict',
    'ConsumersIamMemberConditionArgs',
    'ConsumersIamMemberConditionArgsDict',
    'ServiceApiArgs',
    'ServiceApiArgsDict',
    'ServiceApiMethodArgs',
    'ServiceApiMethodArgsDict',
    'ServiceEndpointArgs',
    'ServiceEndpointArgsDict',
    'ServiceIamBindingConditionArgs',
    'ServiceIamBindingConditionArgsDict',
    'ServiceIamMemberConditionArgs',
    'ServiceIamMemberConditionArgsDict',
]

MYPY = False

if not MYPY:
    class ConsumersIamBindingConditionArgsDict(TypedDict):
        expression: pulumi.Input[str]
        title: pulumi.Input[str]
        description: NotRequired[pulumi.Input[str]]
elif False:
    ConsumersIamBindingConditionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ConsumersIamBindingConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


if not MYPY:
    class ConsumersIamMemberConditionArgsDict(TypedDict):
        expression: pulumi.Input[str]
        title: pulumi.Input[str]
        description: NotRequired[pulumi.Input[str]]
elif False:
    ConsumersIamMemberConditionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ConsumersIamMemberConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


if not MYPY:
    class ServiceApiArgsDict(TypedDict):
        methods: NotRequired[pulumi.Input[Sequence[pulumi.Input['ServiceApiMethodArgsDict']]]]
        """
        A list of Method objects; structure is documented below.
        """
        name: NotRequired[pulumi.Input[str]]
        """
        The simple name of the endpoint as described in the config.
        """
        syntax: NotRequired[pulumi.Input[str]]
        """
        `SYNTAX_PROTO2` or `SYNTAX_PROTO3`.
        """
        version: NotRequired[pulumi.Input[str]]
        """
        A version string for this api. If specified, will have the form major-version.minor-version, e.g. `1.10`.
        """
elif False:
    ServiceApiArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServiceApiArgs:
    def __init__(__self__, *,
                 methods: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceApiMethodArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 syntax: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input['ServiceApiMethodArgs']]] methods: A list of Method objects; structure is documented below.
        :param pulumi.Input[str] name: The simple name of the endpoint as described in the config.
        :param pulumi.Input[str] syntax: `SYNTAX_PROTO2` or `SYNTAX_PROTO3`.
        :param pulumi.Input[str] version: A version string for this api. If specified, will have the form major-version.minor-version, e.g. `1.10`.
        """
        if methods is not None:
            pulumi.set(__self__, "methods", methods)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if syntax is not None:
            pulumi.set(__self__, "syntax", syntax)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceApiMethodArgs']]]]:
        """
        A list of Method objects; structure is documented below.
        """
        return pulumi.get(self, "methods")

    @methods.setter
    def methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceApiMethodArgs']]]]):
        pulumi.set(self, "methods", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The simple name of the endpoint as described in the config.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def syntax(self) -> Optional[pulumi.Input[str]]:
        """
        `SYNTAX_PROTO2` or `SYNTAX_PROTO3`.
        """
        return pulumi.get(self, "syntax")

    @syntax.setter
    def syntax(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "syntax", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        A version string for this api. If specified, will have the form major-version.minor-version, e.g. `1.10`.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


if not MYPY:
    class ServiceApiMethodArgsDict(TypedDict):
        name: NotRequired[pulumi.Input[str]]
        """
        The simple name of the endpoint as described in the config.
        """
        request_type: NotRequired[pulumi.Input[str]]
        """
        The type URL for the request to this API.
        """
        response_type: NotRequired[pulumi.Input[str]]
        """
        The type URL for the response from this API.
        """
        syntax: NotRequired[pulumi.Input[str]]
        """
        `SYNTAX_PROTO2` or `SYNTAX_PROTO3`.
        """
elif False:
    ServiceApiMethodArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServiceApiMethodArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 request_type: Optional[pulumi.Input[str]] = None,
                 response_type: Optional[pulumi.Input[str]] = None,
                 syntax: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name: The simple name of the endpoint as described in the config.
        :param pulumi.Input[str] request_type: The type URL for the request to this API.
        :param pulumi.Input[str] response_type: The type URL for the response from this API.
        :param pulumi.Input[str] syntax: `SYNTAX_PROTO2` or `SYNTAX_PROTO3`.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if request_type is not None:
            pulumi.set(__self__, "request_type", request_type)
        if response_type is not None:
            pulumi.set(__self__, "response_type", response_type)
        if syntax is not None:
            pulumi.set(__self__, "syntax", syntax)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The simple name of the endpoint as described in the config.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="requestType")
    def request_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type URL for the request to this API.
        """
        return pulumi.get(self, "request_type")

    @request_type.setter
    def request_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_type", value)

    @property
    @pulumi.getter(name="responseType")
    def response_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type URL for the response from this API.
        """
        return pulumi.get(self, "response_type")

    @response_type.setter
    def response_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "response_type", value)

    @property
    @pulumi.getter
    def syntax(self) -> Optional[pulumi.Input[str]]:
        """
        `SYNTAX_PROTO2` or `SYNTAX_PROTO3`.
        """
        return pulumi.get(self, "syntax")

    @syntax.setter
    def syntax(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "syntax", value)


if not MYPY:
    class ServiceEndpointArgsDict(TypedDict):
        address: NotRequired[pulumi.Input[str]]
        """
        The FQDN of the endpoint as described in the config.
        """
        name: NotRequired[pulumi.Input[str]]
        """
        The simple name of the endpoint as described in the config.
        """
elif False:
    ServiceEndpointArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServiceEndpointArgs:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] address: The FQDN of the endpoint as described in the config.
        :param pulumi.Input[str] name: The simple name of the endpoint as described in the config.
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[str]]:
        """
        The FQDN of the endpoint as described in the config.
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The simple name of the endpoint as described in the config.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


if not MYPY:
    class ServiceIamBindingConditionArgsDict(TypedDict):
        expression: pulumi.Input[str]
        title: pulumi.Input[str]
        description: NotRequired[pulumi.Input[str]]
elif False:
    ServiceIamBindingConditionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServiceIamBindingConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


if not MYPY:
    class ServiceIamMemberConditionArgsDict(TypedDict):
        expression: pulumi.Input[str]
        title: pulumi.Input[str]
        description: NotRequired[pulumi.Input[str]]
elif False:
    ServiceIamMemberConditionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServiceIamMemberConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


