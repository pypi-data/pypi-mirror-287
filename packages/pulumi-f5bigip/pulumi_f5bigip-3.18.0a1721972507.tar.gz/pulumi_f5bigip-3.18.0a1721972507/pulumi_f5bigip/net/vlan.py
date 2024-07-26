# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['VlanArgs', 'Vlan']

@pulumi.input_type
class VlanArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 cmp_hash: Optional[pulumi.Input[str]] = None,
                 interfaces: Optional[pulumi.Input[Sequence[pulumi.Input['VlanInterfaceArgs']]]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 tag: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Vlan resource.
        :param pulumi.Input[str] name: Name of the vlan
        :param pulumi.Input[str] cmp_hash: Specifies how the traffic on the VLAN will be disaggregated. The value selected determines the traffic disaggregation method. possible options: [`default`, `src-ip`, `dst-ip`]
        :param pulumi.Input[Sequence[pulumi.Input['VlanInterfaceArgs']]] interfaces: Specifies which interfaces you want this VLAN to use for traffic management.
        :param pulumi.Input[int] mtu: Specifies the maximum transmission unit (MTU) for traffic on this VLAN. The default value is `1500`.
        :param pulumi.Input[int] tag: Specifies a number that the system adds into the header of any frame passing through the VLAN.
        """
        pulumi.set(__self__, "name", name)
        if cmp_hash is not None:
            pulumi.set(__self__, "cmp_hash", cmp_hash)
        if interfaces is not None:
            pulumi.set(__self__, "interfaces", interfaces)
        if mtu is not None:
            pulumi.set(__self__, "mtu", mtu)
        if tag is not None:
            pulumi.set(__self__, "tag", tag)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the vlan
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="cmpHash")
    def cmp_hash(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies how the traffic on the VLAN will be disaggregated. The value selected determines the traffic disaggregation method. possible options: [`default`, `src-ip`, `dst-ip`]
        """
        return pulumi.get(self, "cmp_hash")

    @cmp_hash.setter
    def cmp_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cmp_hash", value)

    @property
    @pulumi.getter
    def interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VlanInterfaceArgs']]]]:
        """
        Specifies which interfaces you want this VLAN to use for traffic management.
        """
        return pulumi.get(self, "interfaces")

    @interfaces.setter
    def interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VlanInterfaceArgs']]]]):
        pulumi.set(self, "interfaces", value)

    @property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the maximum transmission unit (MTU) for traffic on this VLAN. The default value is `1500`.
        """
        return pulumi.get(self, "mtu")

    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mtu", value)

    @property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies a number that the system adds into the header of any frame passing through the VLAN.
        """
        return pulumi.get(self, "tag")

    @tag.setter
    def tag(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "tag", value)


@pulumi.input_type
class _VlanState:
    def __init__(__self__, *,
                 cmp_hash: Optional[pulumi.Input[str]] = None,
                 interfaces: Optional[pulumi.Input[Sequence[pulumi.Input['VlanInterfaceArgs']]]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tag: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Vlan resources.
        :param pulumi.Input[str] cmp_hash: Specifies how the traffic on the VLAN will be disaggregated. The value selected determines the traffic disaggregation method. possible options: [`default`, `src-ip`, `dst-ip`]
        :param pulumi.Input[Sequence[pulumi.Input['VlanInterfaceArgs']]] interfaces: Specifies which interfaces you want this VLAN to use for traffic management.
        :param pulumi.Input[int] mtu: Specifies the maximum transmission unit (MTU) for traffic on this VLAN. The default value is `1500`.
        :param pulumi.Input[str] name: Name of the vlan
        :param pulumi.Input[int] tag: Specifies a number that the system adds into the header of any frame passing through the VLAN.
        """
        if cmp_hash is not None:
            pulumi.set(__self__, "cmp_hash", cmp_hash)
        if interfaces is not None:
            pulumi.set(__self__, "interfaces", interfaces)
        if mtu is not None:
            pulumi.set(__self__, "mtu", mtu)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tag is not None:
            pulumi.set(__self__, "tag", tag)

    @property
    @pulumi.getter(name="cmpHash")
    def cmp_hash(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies how the traffic on the VLAN will be disaggregated. The value selected determines the traffic disaggregation method. possible options: [`default`, `src-ip`, `dst-ip`]
        """
        return pulumi.get(self, "cmp_hash")

    @cmp_hash.setter
    def cmp_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cmp_hash", value)

    @property
    @pulumi.getter
    def interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VlanInterfaceArgs']]]]:
        """
        Specifies which interfaces you want this VLAN to use for traffic management.
        """
        return pulumi.get(self, "interfaces")

    @interfaces.setter
    def interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VlanInterfaceArgs']]]]):
        pulumi.set(self, "interfaces", value)

    @property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the maximum transmission unit (MTU) for traffic on this VLAN. The default value is `1500`.
        """
        return pulumi.get(self, "mtu")

    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mtu", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the vlan
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies a number that the system adds into the header of any frame passing through the VLAN.
        """
        return pulumi.get(self, "tag")

    @tag.setter
    def tag(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "tag", value)


class Vlan(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cmp_hash: Optional[pulumi.Input[str]] = None,
                 interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VlanInterfaceArgs']]]]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tag: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        `net.Vlan` Manages a vlan configuration

        For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_f5bigip as f5bigip

        vlan1 = f5bigip.net.Vlan("vlan1",
            name="/Common/Internal",
            tag=101,
            interfaces=[f5bigip.net.VlanInterfaceArgs(
                vlanport="1.2",
                tagged=False,
            )])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cmp_hash: Specifies how the traffic on the VLAN will be disaggregated. The value selected determines the traffic disaggregation method. possible options: [`default`, `src-ip`, `dst-ip`]
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VlanInterfaceArgs']]]] interfaces: Specifies which interfaces you want this VLAN to use for traffic management.
        :param pulumi.Input[int] mtu: Specifies the maximum transmission unit (MTU) for traffic on this VLAN. The default value is `1500`.
        :param pulumi.Input[str] name: Name of the vlan
        :param pulumi.Input[int] tag: Specifies a number that the system adds into the header of any frame passing through the VLAN.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VlanArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        `net.Vlan` Manages a vlan configuration

        For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_f5bigip as f5bigip

        vlan1 = f5bigip.net.Vlan("vlan1",
            name="/Common/Internal",
            tag=101,
            interfaces=[f5bigip.net.VlanInterfaceArgs(
                vlanport="1.2",
                tagged=False,
            )])
        ```

        :param str resource_name: The name of the resource.
        :param VlanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VlanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cmp_hash: Optional[pulumi.Input[str]] = None,
                 interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VlanInterfaceArgs']]]]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tag: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VlanArgs.__new__(VlanArgs)

            __props__.__dict__["cmp_hash"] = cmp_hash
            __props__.__dict__["interfaces"] = interfaces
            __props__.__dict__["mtu"] = mtu
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["tag"] = tag
        super(Vlan, __self__).__init__(
            'f5bigip:net/vlan:Vlan',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cmp_hash: Optional[pulumi.Input[str]] = None,
            interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VlanInterfaceArgs']]]]] = None,
            mtu: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tag: Optional[pulumi.Input[int]] = None) -> 'Vlan':
        """
        Get an existing Vlan resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cmp_hash: Specifies how the traffic on the VLAN will be disaggregated. The value selected determines the traffic disaggregation method. possible options: [`default`, `src-ip`, `dst-ip`]
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VlanInterfaceArgs']]]] interfaces: Specifies which interfaces you want this VLAN to use for traffic management.
        :param pulumi.Input[int] mtu: Specifies the maximum transmission unit (MTU) for traffic on this VLAN. The default value is `1500`.
        :param pulumi.Input[str] name: Name of the vlan
        :param pulumi.Input[int] tag: Specifies a number that the system adds into the header of any frame passing through the VLAN.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VlanState.__new__(_VlanState)

        __props__.__dict__["cmp_hash"] = cmp_hash
        __props__.__dict__["interfaces"] = interfaces
        __props__.__dict__["mtu"] = mtu
        __props__.__dict__["name"] = name
        __props__.__dict__["tag"] = tag
        return Vlan(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cmpHash")
    def cmp_hash(self) -> pulumi.Output[str]:
        """
        Specifies how the traffic on the VLAN will be disaggregated. The value selected determines the traffic disaggregation method. possible options: [`default`, `src-ip`, `dst-ip`]
        """
        return pulumi.get(self, "cmp_hash")

    @property
    @pulumi.getter
    def interfaces(self) -> pulumi.Output[Optional[Sequence['outputs.VlanInterface']]]:
        """
        Specifies which interfaces you want this VLAN to use for traffic management.
        """
        return pulumi.get(self, "interfaces")

    @property
    @pulumi.getter
    def mtu(self) -> pulumi.Output[Optional[int]]:
        """
        Specifies the maximum transmission unit (MTU) for traffic on this VLAN. The default value is `1500`.
        """
        return pulumi.get(self, "mtu")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the vlan
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tag(self) -> pulumi.Output[Optional[int]]:
        """
        Specifies a number that the system adds into the header of any frame passing through the VLAN.
        """
        return pulumi.get(self, "tag")

