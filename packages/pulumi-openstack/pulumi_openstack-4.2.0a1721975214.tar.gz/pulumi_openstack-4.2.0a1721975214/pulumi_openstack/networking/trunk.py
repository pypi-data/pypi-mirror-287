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

__all__ = ['TrunkArgs', 'Trunk']

@pulumi.input_type
class TrunkArgs:
    def __init__(__self__, *,
                 port_id: pulumi.Input[str],
                 admin_state_up: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 sub_ports: Optional[pulumi.Input[Sequence[pulumi.Input['TrunkSubPortArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Trunk resource.
        :param pulumi.Input[str] port_id: The ID of the port to be used as the parent port of the
               trunk. This is the port that should be used as the compute instance network
               port. Changing this creates a new trunk.
        :param pulumi.Input[bool] admin_state_up: Administrative up/down status for the trunk
               (must be "true" or "false" if provided). Changing this updates the
               `admin_state_up` of an existing trunk.
        :param pulumi.Input[str] description: Human-readable description of the trunk. Changing this
               updates the name of the existing trunk.
        :param pulumi.Input[str] name: A unique name for the trunk. Changing this
               updates the `name` of an existing trunk.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to create a trunk. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               trunk.
        :param pulumi.Input[Sequence[pulumi.Input['TrunkSubPortArgs']]] sub_ports: The set of ports that will be made subports of the trunk.
               The structure of each subport is described below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A set of string tags for the port.
        :param pulumi.Input[str] tenant_id: The owner of the Trunk. Required if admin wants
               to create a trunk on behalf of another tenant. Changing this creates a new trunk.
        """
        pulumi.set(__self__, "port_id", port_id)
        if admin_state_up is not None:
            pulumi.set(__self__, "admin_state_up", admin_state_up)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if sub_ports is not None:
            pulumi.set(__self__, "sub_ports", sub_ports)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="portId")
    def port_id(self) -> pulumi.Input[str]:
        """
        The ID of the port to be used as the parent port of the
        trunk. This is the port that should be used as the compute instance network
        port. Changing this creates a new trunk.
        """
        return pulumi.get(self, "port_id")

    @port_id.setter
    def port_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "port_id", value)

    @property
    @pulumi.getter(name="adminStateUp")
    def admin_state_up(self) -> Optional[pulumi.Input[bool]]:
        """
        Administrative up/down status for the trunk
        (must be "true" or "false" if provided). Changing this updates the
        `admin_state_up` of an existing trunk.
        """
        return pulumi.get(self, "admin_state_up")

    @admin_state_up.setter
    def admin_state_up(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "admin_state_up", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Human-readable description of the trunk. Changing this
        updates the name of the existing trunk.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique name for the trunk. Changing this
        updates the `name` of an existing trunk.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 networking client.
        A networking client is needed to create a trunk. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        trunk.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="subPorts")
    def sub_ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TrunkSubPortArgs']]]]:
        """
        The set of ports that will be made subports of the trunk.
        The structure of each subport is described below.
        """
        return pulumi.get(self, "sub_ports")

    @sub_ports.setter
    def sub_ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TrunkSubPortArgs']]]]):
        pulumi.set(self, "sub_ports", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of string tags for the port.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The owner of the Trunk. Required if admin wants
        to create a trunk on behalf of another tenant. Changing this creates a new trunk.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


@pulumi.input_type
class _TrunkState:
    def __init__(__self__, *,
                 admin_state_up: Optional[pulumi.Input[bool]] = None,
                 all_tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 sub_ports: Optional[pulumi.Input[Sequence[pulumi.Input['TrunkSubPortArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Trunk resources.
        :param pulumi.Input[bool] admin_state_up: Administrative up/down status for the trunk
               (must be "true" or "false" if provided). Changing this updates the
               `admin_state_up` of an existing trunk.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] all_tags: The collection of tags assigned on the trunk, which have been
               explicitly and implicitly added.
        :param pulumi.Input[str] description: Human-readable description of the trunk. Changing this
               updates the name of the existing trunk.
        :param pulumi.Input[str] name: A unique name for the trunk. Changing this
               updates the `name` of an existing trunk.
        :param pulumi.Input[str] port_id: The ID of the port to be used as the parent port of the
               trunk. This is the port that should be used as the compute instance network
               port. Changing this creates a new trunk.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to create a trunk. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               trunk.
        :param pulumi.Input[Sequence[pulumi.Input['TrunkSubPortArgs']]] sub_ports: The set of ports that will be made subports of the trunk.
               The structure of each subport is described below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A set of string tags for the port.
        :param pulumi.Input[str] tenant_id: The owner of the Trunk. Required if admin wants
               to create a trunk on behalf of another tenant. Changing this creates a new trunk.
        """
        if admin_state_up is not None:
            pulumi.set(__self__, "admin_state_up", admin_state_up)
        if all_tags is not None:
            pulumi.set(__self__, "all_tags", all_tags)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port_id is not None:
            pulumi.set(__self__, "port_id", port_id)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if sub_ports is not None:
            pulumi.set(__self__, "sub_ports", sub_ports)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="adminStateUp")
    def admin_state_up(self) -> Optional[pulumi.Input[bool]]:
        """
        Administrative up/down status for the trunk
        (must be "true" or "false" if provided). Changing this updates the
        `admin_state_up` of an existing trunk.
        """
        return pulumi.get(self, "admin_state_up")

    @admin_state_up.setter
    def admin_state_up(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "admin_state_up", value)

    @property
    @pulumi.getter(name="allTags")
    def all_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The collection of tags assigned on the trunk, which have been
        explicitly and implicitly added.
        """
        return pulumi.get(self, "all_tags")

    @all_tags.setter
    def all_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "all_tags", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Human-readable description of the trunk. Changing this
        updates the name of the existing trunk.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique name for the trunk. Changing this
        updates the `name` of an existing trunk.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="portId")
    def port_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the port to be used as the parent port of the
        trunk. This is the port that should be used as the compute instance network
        port. Changing this creates a new trunk.
        """
        return pulumi.get(self, "port_id")

    @port_id.setter
    def port_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 networking client.
        A networking client is needed to create a trunk. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        trunk.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="subPorts")
    def sub_ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TrunkSubPortArgs']]]]:
        """
        The set of ports that will be made subports of the trunk.
        The structure of each subport is described below.
        """
        return pulumi.get(self, "sub_ports")

    @sub_ports.setter
    def sub_ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TrunkSubPortArgs']]]]):
        pulumi.set(self, "sub_ports", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of string tags for the port.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The owner of the Trunk. Required if admin wants
        to create a trunk on behalf of another tenant. Changing this creates a new trunk.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


class Trunk(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_state_up: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 sub_ports: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TrunkSubPortArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a networking V2 trunk resource within OpenStack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        network1 = openstack.networking.Network("network_1",
            name="network_1",
            admin_state_up=True)
        subnet1 = openstack.networking.Subnet("subnet_1",
            name="subnet_1",
            network_id=network1.id,
            cidr="192.168.1.0/24",
            ip_version=4,
            enable_dhcp=True,
            no_gateway=True)
        parent_port1 = openstack.networking.Port("parent_port_1",
            name="parent_port_1",
            network_id=network1.id,
            admin_state_up=True,
            opts = pulumi.ResourceOptions(depends_on=[subnet1]))
        subport1 = openstack.networking.Port("subport_1",
            name="subport_1",
            network_id=network1.id,
            admin_state_up=True,
            opts = pulumi.ResourceOptions(depends_on=[subnet1]))
        trunk1 = openstack.networking.Trunk("trunk_1",
            name="trunk_1",
            admin_state_up=True,
            port_id=parent_port1.id,
            sub_ports=[openstack.networking.TrunkSubPortArgs(
                port_id=subport1.id,
                segmentation_id=1,
                segmentation_type="vlan",
            )])
        instance1 = openstack.compute.Instance("instance_1",
            name="instance_1",
            security_groups=["default"],
            networks=[openstack.compute.InstanceNetworkArgs(
                port=trunk1.port_id,
            )])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: Administrative up/down status for the trunk
               (must be "true" or "false" if provided). Changing this updates the
               `admin_state_up` of an existing trunk.
        :param pulumi.Input[str] description: Human-readable description of the trunk. Changing this
               updates the name of the existing trunk.
        :param pulumi.Input[str] name: A unique name for the trunk. Changing this
               updates the `name` of an existing trunk.
        :param pulumi.Input[str] port_id: The ID of the port to be used as the parent port of the
               trunk. This is the port that should be used as the compute instance network
               port. Changing this creates a new trunk.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to create a trunk. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               trunk.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TrunkSubPortArgs']]]] sub_ports: The set of ports that will be made subports of the trunk.
               The structure of each subport is described below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A set of string tags for the port.
        :param pulumi.Input[str] tenant_id: The owner of the Trunk. Required if admin wants
               to create a trunk on behalf of another tenant. Changing this creates a new trunk.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TrunkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a networking V2 trunk resource within OpenStack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        network1 = openstack.networking.Network("network_1",
            name="network_1",
            admin_state_up=True)
        subnet1 = openstack.networking.Subnet("subnet_1",
            name="subnet_1",
            network_id=network1.id,
            cidr="192.168.1.0/24",
            ip_version=4,
            enable_dhcp=True,
            no_gateway=True)
        parent_port1 = openstack.networking.Port("parent_port_1",
            name="parent_port_1",
            network_id=network1.id,
            admin_state_up=True,
            opts = pulumi.ResourceOptions(depends_on=[subnet1]))
        subport1 = openstack.networking.Port("subport_1",
            name="subport_1",
            network_id=network1.id,
            admin_state_up=True,
            opts = pulumi.ResourceOptions(depends_on=[subnet1]))
        trunk1 = openstack.networking.Trunk("trunk_1",
            name="trunk_1",
            admin_state_up=True,
            port_id=parent_port1.id,
            sub_ports=[openstack.networking.TrunkSubPortArgs(
                port_id=subport1.id,
                segmentation_id=1,
                segmentation_type="vlan",
            )])
        instance1 = openstack.compute.Instance("instance_1",
            name="instance_1",
            security_groups=["default"],
            networks=[openstack.compute.InstanceNetworkArgs(
                port=trunk1.port_id,
            )])
        ```

        :param str resource_name: The name of the resource.
        :param TrunkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TrunkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_state_up: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 sub_ports: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TrunkSubPortArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TrunkArgs.__new__(TrunkArgs)

            __props__.__dict__["admin_state_up"] = admin_state_up
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if port_id is None and not opts.urn:
                raise TypeError("Missing required property 'port_id'")
            __props__.__dict__["port_id"] = port_id
            __props__.__dict__["region"] = region
            __props__.__dict__["sub_ports"] = sub_ports
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tenant_id"] = tenant_id
            __props__.__dict__["all_tags"] = None
        super(Trunk, __self__).__init__(
            'openstack:networking/trunk:Trunk',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            admin_state_up: Optional[pulumi.Input[bool]] = None,
            all_tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            port_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            sub_ports: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TrunkSubPortArgs']]]]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None) -> 'Trunk':
        """
        Get an existing Trunk resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: Administrative up/down status for the trunk
               (must be "true" or "false" if provided). Changing this updates the
               `admin_state_up` of an existing trunk.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] all_tags: The collection of tags assigned on the trunk, which have been
               explicitly and implicitly added.
        :param pulumi.Input[str] description: Human-readable description of the trunk. Changing this
               updates the name of the existing trunk.
        :param pulumi.Input[str] name: A unique name for the trunk. Changing this
               updates the `name` of an existing trunk.
        :param pulumi.Input[str] port_id: The ID of the port to be used as the parent port of the
               trunk. This is the port that should be used as the compute instance network
               port. Changing this creates a new trunk.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to create a trunk. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               trunk.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TrunkSubPortArgs']]]] sub_ports: The set of ports that will be made subports of the trunk.
               The structure of each subport is described below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A set of string tags for the port.
        :param pulumi.Input[str] tenant_id: The owner of the Trunk. Required if admin wants
               to create a trunk on behalf of another tenant. Changing this creates a new trunk.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TrunkState.__new__(_TrunkState)

        __props__.__dict__["admin_state_up"] = admin_state_up
        __props__.__dict__["all_tags"] = all_tags
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["port_id"] = port_id
        __props__.__dict__["region"] = region
        __props__.__dict__["sub_ports"] = sub_ports
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tenant_id"] = tenant_id
        return Trunk(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminStateUp")
    def admin_state_up(self) -> pulumi.Output[Optional[bool]]:
        """
        Administrative up/down status for the trunk
        (must be "true" or "false" if provided). Changing this updates the
        `admin_state_up` of an existing trunk.
        """
        return pulumi.get(self, "admin_state_up")

    @property
    @pulumi.getter(name="allTags")
    def all_tags(self) -> pulumi.Output[Sequence[str]]:
        """
        The collection of tags assigned on the trunk, which have been
        explicitly and implicitly added.
        """
        return pulumi.get(self, "all_tags")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Human-readable description of the trunk. Changing this
        updates the name of the existing trunk.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique name for the trunk. Changing this
        updates the `name` of an existing trunk.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="portId")
    def port_id(self) -> pulumi.Output[str]:
        """
        The ID of the port to be used as the parent port of the
        trunk. This is the port that should be used as the compute instance network
        port. Changing this creates a new trunk.
        """
        return pulumi.get(self, "port_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 networking client.
        A networking client is needed to create a trunk. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        trunk.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="subPorts")
    def sub_ports(self) -> pulumi.Output[Optional[Sequence['outputs.TrunkSubPort']]]:
        """
        The set of ports that will be made subports of the trunk.
        The structure of each subport is described below.
        """
        return pulumi.get(self, "sub_ports")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A set of string tags for the port.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The owner of the Trunk. Required if admin wants
        to create a trunk on behalf of another tenant. Changing this creates a new trunk.
        """
        return pulumi.get(self, "tenant_id")

