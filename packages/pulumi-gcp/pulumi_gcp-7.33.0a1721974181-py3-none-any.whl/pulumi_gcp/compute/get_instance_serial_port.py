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
    'GetInstanceSerialPortResult',
    'AwaitableGetInstanceSerialPortResult',
    'get_instance_serial_port',
    'get_instance_serial_port_output',
]

@pulumi.output_type
class GetInstanceSerialPortResult:
    """
    A collection of values returned by getInstanceSerialPort.
    """
    def __init__(__self__, contents=None, id=None, instance=None, port=None, project=None, zone=None):
        if contents and not isinstance(contents, str):
            raise TypeError("Expected argument 'contents' to be a str")
        pulumi.set(__self__, "contents", contents)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance and not isinstance(instance, str):
            raise TypeError("Expected argument 'instance' to be a str")
        pulumi.set(__self__, "instance", instance)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def contents(self) -> str:
        """
        The output of the serial port. Serial port output is available only when the VM instance is running, and logs are limited to the most recent 1 MB of output per port.
        """
        return pulumi.get(self, "contents")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def instance(self) -> str:
        return pulumi.get(self, "instance")

    @property
    @pulumi.getter
    def port(self) -> int:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def zone(self) -> str:
        return pulumi.get(self, "zone")


class AwaitableGetInstanceSerialPortResult(GetInstanceSerialPortResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceSerialPortResult(
            contents=self.contents,
            id=self.id,
            instance=self.instance,
            port=self.port,
            project=self.project,
            zone=self.zone)


def get_instance_serial_port(instance: Optional[str] = None,
                             port: Optional[int] = None,
                             project: Optional[str] = None,
                             zone: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceSerialPortResult:
    """
    Get the serial port output from a Compute Instance. For more information see
    the official [API](https://cloud.google.com/compute/docs/instances/viewing-serial-port-output) documentation.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    serial = gcp.compute.get_instance_serial_port(instance="my-instance",
        zone="us-central1-a",
        port=1)
    pulumi.export("serialOut", serial.contents)
    ```

    Using the serial port output to generate a windows password, derived from the [official guide](https://cloud.google.com/compute/docs/instances/windows/automate-pw-generation):

    ```python
    import pulumi
    import json
    import pulumi_gcp as gcp

    windows = gcp.compute.Instance("windows",
        network_interfaces=[{
            "access_configs": [{}],
            "network": "default",
        }],
        name="windows-instance",
        machine_type="e2-medium",
        zone="us-central1-a",
        boot_disk={
            "initialize_params": {
                "image": "windows-cloud/windows-2019",
            },
        },
        metadata={
            "serial-port-logging-enable": "TRUE",
            "windows-keys": json.dumps({
                "email": "example.user@example.com",
                "expireOn": "2020-04-14T01:37:19Z",
                "exponent": "AQAB",
                "modulus": "wgsquN4IBNPqIUnu+h/5Za1kujb2YRhX1vCQVQAkBwnWigcCqOBVfRa5JoZfx6KIvEXjWqa77jPvlsxM4WPqnDIM2qiK36up3SKkYwFjff6F2ni/ry8vrwXCX3sGZ1hbIHlK0O012HpA3ISeEswVZmX2X67naOvJXfY5v0hGPWqCADao+xVxrmxsZD4IWnKl1UaZzI5lhAzr8fw6utHwx1EZ/MSgsEki6tujcZfN+GUDRnmJGQSnPTXmsf7Q4DKreTZk49cuyB3prV91S0x3DYjCUpSXrkVy1Ha5XicGD/q+ystuFsJnrrhbNXJbpSjM6sjo/aduAkZJl4FmOt0R7Q==",
                "userName": "example-user",
            }),
        },
        service_account={
            "scopes": [
                "userinfo-email",
                "compute-ro",
                "storage-ro",
            ],
        })
    serial = pulumi.Output.all(windows.name, windows.zone).apply(lambda name, zone: gcp.compute.get_instance_serial_port_output(instance=name,
        zone=zone,
        port=4))
    pulumi.export("serialOut", serial.contents)
    ```


    :param str instance: The name of the Compute Instance to read output from.
    :param int port: The number of the serial port to read output from. Possible values are 1-4.
           
           - - -
    :param str project: The project in which the Compute Instance exists. If it
           is not provided, the provider project is used.
    :param str zone: The zone in which the Compute Instance exists.
           If it is not provided, the provider zone is used.
    """
    __args__ = dict()
    __args__['instance'] = instance
    __args__['port'] = port
    __args__['project'] = project
    __args__['zone'] = zone
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:compute/getInstanceSerialPort:getInstanceSerialPort', __args__, opts=opts, typ=GetInstanceSerialPortResult).value

    return AwaitableGetInstanceSerialPortResult(
        contents=pulumi.get(__ret__, 'contents'),
        id=pulumi.get(__ret__, 'id'),
        instance=pulumi.get(__ret__, 'instance'),
        port=pulumi.get(__ret__, 'port'),
        project=pulumi.get(__ret__, 'project'),
        zone=pulumi.get(__ret__, 'zone'))


@_utilities.lift_output_func(get_instance_serial_port)
def get_instance_serial_port_output(instance: Optional[pulumi.Input[str]] = None,
                                    port: Optional[pulumi.Input[int]] = None,
                                    project: Optional[pulumi.Input[Optional[str]]] = None,
                                    zone: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceSerialPortResult]:
    """
    Get the serial port output from a Compute Instance. For more information see
    the official [API](https://cloud.google.com/compute/docs/instances/viewing-serial-port-output) documentation.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    serial = gcp.compute.get_instance_serial_port(instance="my-instance",
        zone="us-central1-a",
        port=1)
    pulumi.export("serialOut", serial.contents)
    ```

    Using the serial port output to generate a windows password, derived from the [official guide](https://cloud.google.com/compute/docs/instances/windows/automate-pw-generation):

    ```python
    import pulumi
    import json
    import pulumi_gcp as gcp

    windows = gcp.compute.Instance("windows",
        network_interfaces=[{
            "access_configs": [{}],
            "network": "default",
        }],
        name="windows-instance",
        machine_type="e2-medium",
        zone="us-central1-a",
        boot_disk={
            "initialize_params": {
                "image": "windows-cloud/windows-2019",
            },
        },
        metadata={
            "serial-port-logging-enable": "TRUE",
            "windows-keys": json.dumps({
                "email": "example.user@example.com",
                "expireOn": "2020-04-14T01:37:19Z",
                "exponent": "AQAB",
                "modulus": "wgsquN4IBNPqIUnu+h/5Za1kujb2YRhX1vCQVQAkBwnWigcCqOBVfRa5JoZfx6KIvEXjWqa77jPvlsxM4WPqnDIM2qiK36up3SKkYwFjff6F2ni/ry8vrwXCX3sGZ1hbIHlK0O012HpA3ISeEswVZmX2X67naOvJXfY5v0hGPWqCADao+xVxrmxsZD4IWnKl1UaZzI5lhAzr8fw6utHwx1EZ/MSgsEki6tujcZfN+GUDRnmJGQSnPTXmsf7Q4DKreTZk49cuyB3prV91S0x3DYjCUpSXrkVy1Ha5XicGD/q+ystuFsJnrrhbNXJbpSjM6sjo/aduAkZJl4FmOt0R7Q==",
                "userName": "example-user",
            }),
        },
        service_account={
            "scopes": [
                "userinfo-email",
                "compute-ro",
                "storage-ro",
            ],
        })
    serial = pulumi.Output.all(windows.name, windows.zone).apply(lambda name, zone: gcp.compute.get_instance_serial_port_output(instance=name,
        zone=zone,
        port=4))
    pulumi.export("serialOut", serial.contents)
    ```


    :param str instance: The name of the Compute Instance to read output from.
    :param int port: The number of the serial port to read output from. Possible values are 1-4.
           
           - - -
    :param str project: The project in which the Compute Instance exists. If it
           is not provided, the provider project is used.
    :param str zone: The zone in which the Compute Instance exists.
           If it is not provided, the provider zone is used.
    """
    ...
