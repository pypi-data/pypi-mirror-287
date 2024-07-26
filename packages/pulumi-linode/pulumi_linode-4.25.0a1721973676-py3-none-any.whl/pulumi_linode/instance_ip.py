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

__all__ = ['InstanceIpArgs', 'InstanceIp']

@pulumi.input_type
class InstanceIpArgs:
    def __init__(__self__, *,
                 linode_id: pulumi.Input[int],
                 apply_immediately: Optional[pulumi.Input[bool]] = None,
                 public: Optional[pulumi.Input[bool]] = None,
                 rdns: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a InstanceIp resource.
        :param pulumi.Input[int] linode_id: The ID of the Linode to allocate an IPv4 address for.
        :param pulumi.Input[bool] apply_immediately: If true, the instance will be rebooted to update network interfaces.
        :param pulumi.Input[bool] public: Whether the IPv4 address is public or private. Defaults to true.
        :param pulumi.Input[str] rdns: The reverse DNS assigned to this address.
        """
        pulumi.set(__self__, "linode_id", linode_id)
        if apply_immediately is not None:
            pulumi.set(__self__, "apply_immediately", apply_immediately)
        if public is not None:
            pulumi.set(__self__, "public", public)
        if rdns is not None:
            pulumi.set(__self__, "rdns", rdns)

    @property
    @pulumi.getter(name="linodeId")
    def linode_id(self) -> pulumi.Input[int]:
        """
        The ID of the Linode to allocate an IPv4 address for.
        """
        return pulumi.get(self, "linode_id")

    @linode_id.setter
    def linode_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "linode_id", value)

    @property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, the instance will be rebooted to update network interfaces.
        """
        return pulumi.get(self, "apply_immediately")

    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "apply_immediately", value)

    @property
    @pulumi.getter
    def public(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the IPv4 address is public or private. Defaults to true.
        """
        return pulumi.get(self, "public")

    @public.setter
    def public(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public", value)

    @property
    @pulumi.getter
    def rdns(self) -> Optional[pulumi.Input[str]]:
        """
        The reverse DNS assigned to this address.
        """
        return pulumi.get(self, "rdns")

    @rdns.setter
    def rdns(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rdns", value)


@pulumi.input_type
class _InstanceIpState:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[str]] = None,
                 apply_immediately: Optional[pulumi.Input[bool]] = None,
                 gateway: Optional[pulumi.Input[str]] = None,
                 linode_id: Optional[pulumi.Input[int]] = None,
                 prefix: Optional[pulumi.Input[int]] = None,
                 public: Optional[pulumi.Input[bool]] = None,
                 rdns: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 subnet_mask: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vpc_nat11s: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceIpVpcNat11Args']]]] = None):
        """
        Input properties used for looking up and filtering InstanceIp resources.
        :param pulumi.Input[str] address: The resulting IPv4 address.
        :param pulumi.Input[bool] apply_immediately: If true, the instance will be rebooted to update network interfaces.
        :param pulumi.Input[str] gateway: The default gateway for this address
        :param pulumi.Input[int] linode_id: The ID of the Linode to allocate an IPv4 address for.
        :param pulumi.Input[int] prefix: The number of bits set in the subnet mask.
        :param pulumi.Input[bool] public: Whether the IPv4 address is public or private. Defaults to true.
        :param pulumi.Input[str] rdns: The reverse DNS assigned to this address.
        :param pulumi.Input[str] region: The region this IP resides in.
        :param pulumi.Input[str] subnet_mask: The mask that separates host bits from network bits for this address.
        :param pulumi.Input[str] type: The type of IP address. (`ipv4`, `ipv6`, `ipv6/pool`, `ipv6/range`)
        :param pulumi.Input[Sequence[pulumi.Input['InstanceIpVpcNat11Args']]] vpc_nat11s: Contains information about the NAT 1:1 mapping of a public IP address to a VPC subnet.
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if apply_immediately is not None:
            pulumi.set(__self__, "apply_immediately", apply_immediately)
        if gateway is not None:
            pulumi.set(__self__, "gateway", gateway)
        if linode_id is not None:
            pulumi.set(__self__, "linode_id", linode_id)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)
        if public is not None:
            pulumi.set(__self__, "public", public)
        if rdns is not None:
            pulumi.set(__self__, "rdns", rdns)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if subnet_mask is not None:
            pulumi.set(__self__, "subnet_mask", subnet_mask)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if vpc_nat11s is not None:
            pulumi.set(__self__, "vpc_nat11s", vpc_nat11s)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[str]]:
        """
        The resulting IPv4 address.
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, the instance will be rebooted to update network interfaces.
        """
        return pulumi.get(self, "apply_immediately")

    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "apply_immediately", value)

    @property
    @pulumi.getter
    def gateway(self) -> Optional[pulumi.Input[str]]:
        """
        The default gateway for this address
        """
        return pulumi.get(self, "gateway")

    @gateway.setter
    def gateway(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway", value)

    @property
    @pulumi.getter(name="linodeId")
    def linode_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the Linode to allocate an IPv4 address for.
        """
        return pulumi.get(self, "linode_id")

    @linode_id.setter
    def linode_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "linode_id", value)

    @property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[int]]:
        """
        The number of bits set in the subnet mask.
        """
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "prefix", value)

    @property
    @pulumi.getter
    def public(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the IPv4 address is public or private. Defaults to true.
        """
        return pulumi.get(self, "public")

    @public.setter
    def public(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public", value)

    @property
    @pulumi.getter
    def rdns(self) -> Optional[pulumi.Input[str]]:
        """
        The reverse DNS assigned to this address.
        """
        return pulumi.get(self, "rdns")

    @rdns.setter
    def rdns(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rdns", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region this IP resides in.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="subnetMask")
    def subnet_mask(self) -> Optional[pulumi.Input[str]]:
        """
        The mask that separates host bits from network bits for this address.
        """
        return pulumi.get(self, "subnet_mask")

    @subnet_mask.setter
    def subnet_mask(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_mask", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of IP address. (`ipv4`, `ipv6`, `ipv6/pool`, `ipv6/range`)
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="vpcNat11s")
    def vpc_nat11s(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstanceIpVpcNat11Args']]]]:
        """
        Contains information about the NAT 1:1 mapping of a public IP address to a VPC subnet.
        """
        return pulumi.get(self, "vpc_nat11s")

    @vpc_nat11s.setter
    def vpc_nat11s(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceIpVpcNat11Args']]]]):
        pulumi.set(self, "vpc_nat11s", value)


class InstanceIp(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apply_immediately: Optional[pulumi.Input[bool]] = None,
                 linode_id: Optional[pulumi.Input[int]] = None,
                 public: Optional[pulumi.Input[bool]] = None,
                 rdns: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Linode instance IP.
        For more information, see the [Linode APIv4 docs](https://techdocs.akamai.com/linode-api/reference/post-add-linode-ip).

        > **NOTICE:** You may need to contact support to increase your instance IP limit before you can allocate additional IPs.

        > **NOTICE:** This resource will reboot the specified instance following IP allocation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_linode as linode

        foo = linode.Instance("foo",
            image="linode/alpine3.19",
            label="foobar-test",
            type="g6-nanode-1",
            region="us-east")
        foo_instance_ip = linode.InstanceIp("foo",
            linode_id=foo.id,
            public=True)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] apply_immediately: If true, the instance will be rebooted to update network interfaces.
        :param pulumi.Input[int] linode_id: The ID of the Linode to allocate an IPv4 address for.
        :param pulumi.Input[bool] public: Whether the IPv4 address is public or private. Defaults to true.
        :param pulumi.Input[str] rdns: The reverse DNS assigned to this address.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceIpArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Linode instance IP.
        For more information, see the [Linode APIv4 docs](https://techdocs.akamai.com/linode-api/reference/post-add-linode-ip).

        > **NOTICE:** You may need to contact support to increase your instance IP limit before you can allocate additional IPs.

        > **NOTICE:** This resource will reboot the specified instance following IP allocation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_linode as linode

        foo = linode.Instance("foo",
            image="linode/alpine3.19",
            label="foobar-test",
            type="g6-nanode-1",
            region="us-east")
        foo_instance_ip = linode.InstanceIp("foo",
            linode_id=foo.id,
            public=True)
        ```

        :param str resource_name: The name of the resource.
        :param InstanceIpArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceIpArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apply_immediately: Optional[pulumi.Input[bool]] = None,
                 linode_id: Optional[pulumi.Input[int]] = None,
                 public: Optional[pulumi.Input[bool]] = None,
                 rdns: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstanceIpArgs.__new__(InstanceIpArgs)

            __props__.__dict__["apply_immediately"] = apply_immediately
            if linode_id is None and not opts.urn:
                raise TypeError("Missing required property 'linode_id'")
            __props__.__dict__["linode_id"] = linode_id
            __props__.__dict__["public"] = public
            __props__.__dict__["rdns"] = rdns
            __props__.__dict__["address"] = None
            __props__.__dict__["gateway"] = None
            __props__.__dict__["prefix"] = None
            __props__.__dict__["region"] = None
            __props__.__dict__["subnet_mask"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["vpc_nat11s"] = None
        super(InstanceIp, __self__).__init__(
            'linode:index/instanceIp:InstanceIp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address: Optional[pulumi.Input[str]] = None,
            apply_immediately: Optional[pulumi.Input[bool]] = None,
            gateway: Optional[pulumi.Input[str]] = None,
            linode_id: Optional[pulumi.Input[int]] = None,
            prefix: Optional[pulumi.Input[int]] = None,
            public: Optional[pulumi.Input[bool]] = None,
            rdns: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            subnet_mask: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            vpc_nat11s: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceIpVpcNat11Args']]]]] = None) -> 'InstanceIp':
        """
        Get an existing InstanceIp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: The resulting IPv4 address.
        :param pulumi.Input[bool] apply_immediately: If true, the instance will be rebooted to update network interfaces.
        :param pulumi.Input[str] gateway: The default gateway for this address
        :param pulumi.Input[int] linode_id: The ID of the Linode to allocate an IPv4 address for.
        :param pulumi.Input[int] prefix: The number of bits set in the subnet mask.
        :param pulumi.Input[bool] public: Whether the IPv4 address is public or private. Defaults to true.
        :param pulumi.Input[str] rdns: The reverse DNS assigned to this address.
        :param pulumi.Input[str] region: The region this IP resides in.
        :param pulumi.Input[str] subnet_mask: The mask that separates host bits from network bits for this address.
        :param pulumi.Input[str] type: The type of IP address. (`ipv4`, `ipv6`, `ipv6/pool`, `ipv6/range`)
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceIpVpcNat11Args']]]] vpc_nat11s: Contains information about the NAT 1:1 mapping of a public IP address to a VPC subnet.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstanceIpState.__new__(_InstanceIpState)

        __props__.__dict__["address"] = address
        __props__.__dict__["apply_immediately"] = apply_immediately
        __props__.__dict__["gateway"] = gateway
        __props__.__dict__["linode_id"] = linode_id
        __props__.__dict__["prefix"] = prefix
        __props__.__dict__["public"] = public
        __props__.__dict__["rdns"] = rdns
        __props__.__dict__["region"] = region
        __props__.__dict__["subnet_mask"] = subnet_mask
        __props__.__dict__["type"] = type
        __props__.__dict__["vpc_nat11s"] = vpc_nat11s
        return InstanceIp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Output[str]:
        """
        The resulting IPv4 address.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> pulumi.Output[bool]:
        """
        If true, the instance will be rebooted to update network interfaces.
        """
        return pulumi.get(self, "apply_immediately")

    @property
    @pulumi.getter
    def gateway(self) -> pulumi.Output[str]:
        """
        The default gateway for this address
        """
        return pulumi.get(self, "gateway")

    @property
    @pulumi.getter(name="linodeId")
    def linode_id(self) -> pulumi.Output[int]:
        """
        The ID of the Linode to allocate an IPv4 address for.
        """
        return pulumi.get(self, "linode_id")

    @property
    @pulumi.getter
    def prefix(self) -> pulumi.Output[int]:
        """
        The number of bits set in the subnet mask.
        """
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter
    def public(self) -> pulumi.Output[bool]:
        """
        Whether the IPv4 address is public or private. Defaults to true.
        """
        return pulumi.get(self, "public")

    @property
    @pulumi.getter
    def rdns(self) -> pulumi.Output[str]:
        """
        The reverse DNS assigned to this address.
        """
        return pulumi.get(self, "rdns")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region this IP resides in.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="subnetMask")
    def subnet_mask(self) -> pulumi.Output[str]:
        """
        The mask that separates host bits from network bits for this address.
        """
        return pulumi.get(self, "subnet_mask")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of IP address. (`ipv4`, `ipv6`, `ipv6/pool`, `ipv6/range`)
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vpcNat11s")
    def vpc_nat11s(self) -> pulumi.Output[Sequence['outputs.InstanceIpVpcNat11']]:
        """
        Contains information about the NAT 1:1 mapping of a public IP address to a VPC subnet.
        """
        return pulumi.get(self, "vpc_nat11s")

