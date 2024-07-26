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

__all__ = ['VolumeArgs', 'Volume']

@pulumi.input_type
class VolumeArgs:
    def __init__(__self__, *,
                 driver: Optional[pulumi.Input[str]] = None,
                 driver_opts: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input['VolumeLabelArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Volume resource.
        :param pulumi.Input[str] driver: Driver type for the volume. Defaults to `local`.
        :param pulumi.Input[Mapping[str, Any]] driver_opts: Options specific to the driver.
        :param pulumi.Input[Sequence[pulumi.Input['VolumeLabelArgs']]] labels: User-defined key/value metadata
        :param pulumi.Input[str] name: The name of the Docker volume (will be generated if not provided).
        """
        if driver is not None:
            pulumi.set(__self__, "driver", driver)
        if driver_opts is not None:
            pulumi.set(__self__, "driver_opts", driver_opts)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def driver(self) -> Optional[pulumi.Input[str]]:
        """
        Driver type for the volume. Defaults to `local`.
        """
        return pulumi.get(self, "driver")

    @driver.setter
    def driver(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "driver", value)

    @property
    @pulumi.getter(name="driverOpts")
    def driver_opts(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Options specific to the driver.
        """
        return pulumi.get(self, "driver_opts")

    @driver_opts.setter
    def driver_opts(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "driver_opts", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VolumeLabelArgs']]]]:
        """
        User-defined key/value metadata
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VolumeLabelArgs']]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Docker volume (will be generated if not provided).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _VolumeState:
    def __init__(__self__, *,
                 driver: Optional[pulumi.Input[str]] = None,
                 driver_opts: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input['VolumeLabelArgs']]]] = None,
                 mountpoint: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Volume resources.
        :param pulumi.Input[str] driver: Driver type for the volume. Defaults to `local`.
        :param pulumi.Input[Mapping[str, Any]] driver_opts: Options specific to the driver.
        :param pulumi.Input[Sequence[pulumi.Input['VolumeLabelArgs']]] labels: User-defined key/value metadata
        :param pulumi.Input[str] mountpoint: The mountpoint of the volume.
        :param pulumi.Input[str] name: The name of the Docker volume (will be generated if not provided).
        """
        if driver is not None:
            pulumi.set(__self__, "driver", driver)
        if driver_opts is not None:
            pulumi.set(__self__, "driver_opts", driver_opts)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if mountpoint is not None:
            pulumi.set(__self__, "mountpoint", mountpoint)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def driver(self) -> Optional[pulumi.Input[str]]:
        """
        Driver type for the volume. Defaults to `local`.
        """
        return pulumi.get(self, "driver")

    @driver.setter
    def driver(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "driver", value)

    @property
    @pulumi.getter(name="driverOpts")
    def driver_opts(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Options specific to the driver.
        """
        return pulumi.get(self, "driver_opts")

    @driver_opts.setter
    def driver_opts(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "driver_opts", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VolumeLabelArgs']]]]:
        """
        User-defined key/value metadata
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VolumeLabelArgs']]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def mountpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The mountpoint of the volume.
        """
        return pulumi.get(self, "mountpoint")

    @mountpoint.setter
    def mountpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mountpoint", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Docker volume (will be generated if not provided).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class Volume(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 driver: Optional[pulumi.Input[str]] = None,
                 driver_opts: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VolumeLabelArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        <!-- Bug: Type and Name are switched -->
        Creates and destroys a volume in Docker. This can be used alongside Container to prepare volumes that can be shared across containers.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_docker as docker

        shared_volume = docker.Volume("shared_volume", name="shared_volume")
        ```

        ## Import

        ### Example

        Assuming you created a `volume` as follows

        #!/bin/bash

        docker volume create

        prints the long ID

        524b0457aa2a87dd2b75c74c3e4e53f406974249e63ab3ed9bf21e5644f9dc7d

        you provide the definition for the resource as follows

        terraform

        resource "docker_volume" "foo" {

          name = "524b0457aa2a87dd2b75c74c3e4e53f406974249e63ab3ed9bf21e5644f9dc7d"

        }

        then the import command is as follows

        #!/bin/bash

        ```sh
        $ pulumi import docker:index/volume:Volume foo 524b0457aa2a87dd2b75c74c3e4e53f406974249e63ab3ed9bf21e5644f9dc7d
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] driver: Driver type for the volume. Defaults to `local`.
        :param pulumi.Input[Mapping[str, Any]] driver_opts: Options specific to the driver.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VolumeLabelArgs']]]] labels: User-defined key/value metadata
        :param pulumi.Input[str] name: The name of the Docker volume (will be generated if not provided).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[VolumeArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- Bug: Type and Name are switched -->
        Creates and destroys a volume in Docker. This can be used alongside Container to prepare volumes that can be shared across containers.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_docker as docker

        shared_volume = docker.Volume("shared_volume", name="shared_volume")
        ```

        ## Import

        ### Example

        Assuming you created a `volume` as follows

        #!/bin/bash

        docker volume create

        prints the long ID

        524b0457aa2a87dd2b75c74c3e4e53f406974249e63ab3ed9bf21e5644f9dc7d

        you provide the definition for the resource as follows

        terraform

        resource "docker_volume" "foo" {

          name = "524b0457aa2a87dd2b75c74c3e4e53f406974249e63ab3ed9bf21e5644f9dc7d"

        }

        then the import command is as follows

        #!/bin/bash

        ```sh
        $ pulumi import docker:index/volume:Volume foo 524b0457aa2a87dd2b75c74c3e4e53f406974249e63ab3ed9bf21e5644f9dc7d
        ```

        :param str resource_name: The name of the resource.
        :param VolumeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 driver: Optional[pulumi.Input[str]] = None,
                 driver_opts: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VolumeLabelArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeArgs.__new__(VolumeArgs)

            __props__.__dict__["driver"] = driver
            __props__.__dict__["driver_opts"] = driver_opts
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            __props__.__dict__["mountpoint"] = None
        super(Volume, __self__).__init__(
            'docker:index/volume:Volume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            driver: Optional[pulumi.Input[str]] = None,
            driver_opts: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            labels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VolumeLabelArgs']]]]] = None,
            mountpoint: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'Volume':
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] driver: Driver type for the volume. Defaults to `local`.
        :param pulumi.Input[Mapping[str, Any]] driver_opts: Options specific to the driver.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VolumeLabelArgs']]]] labels: User-defined key/value metadata
        :param pulumi.Input[str] mountpoint: The mountpoint of the volume.
        :param pulumi.Input[str] name: The name of the Docker volume (will be generated if not provided).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VolumeState.__new__(_VolumeState)

        __props__.__dict__["driver"] = driver
        __props__.__dict__["driver_opts"] = driver_opts
        __props__.__dict__["labels"] = labels
        __props__.__dict__["mountpoint"] = mountpoint
        __props__.__dict__["name"] = name
        return Volume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def driver(self) -> pulumi.Output[str]:
        """
        Driver type for the volume. Defaults to `local`.
        """
        return pulumi.get(self, "driver")

    @property
    @pulumi.getter(name="driverOpts")
    def driver_opts(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Options specific to the driver.
        """
        return pulumi.get(self, "driver_opts")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence['outputs.VolumeLabel']]]:
        """
        User-defined key/value metadata
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def mountpoint(self) -> pulumi.Output[str]:
        """
        The mountpoint of the volume.
        """
        return pulumi.get(self, "mountpoint")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Docker volume (will be generated if not provided).
        """
        return pulumi.get(self, "name")

