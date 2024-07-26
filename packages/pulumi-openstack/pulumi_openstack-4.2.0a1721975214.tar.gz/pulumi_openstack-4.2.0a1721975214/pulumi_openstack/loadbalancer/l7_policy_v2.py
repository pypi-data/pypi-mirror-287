# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['L7PolicyV2Args', 'L7PolicyV2']

@pulumi.input_type
class L7PolicyV2Args:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 listener_id: pulumi.Input[str],
                 admin_state_up: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 position: Optional[pulumi.Input[int]] = None,
                 redirect_http_code: Optional[pulumi.Input[int]] = None,
                 redirect_pool_id: Optional[pulumi.Input[str]] = None,
                 redirect_prefix: Optional[pulumi.Input[str]] = None,
                 redirect_url: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a L7PolicyV2 resource.
        :param pulumi.Input[str] action: The L7 Policy action - can either be REDIRECT\\_TO\\_POOL,
               REDIRECT\\_TO\\_URL or REJECT.
        :param pulumi.Input[str] listener_id: The Listener on which the L7 Policy will be associated with.
               Changing this creates a new L7 Policy.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the L7 Policy.
               A valid value is true (UP) or false (DOWN).
        :param pulumi.Input[str] description: Human-readable description for the L7 Policy.
        :param pulumi.Input[str] name: Human-readable name for the L7 Policy. Does not have
               to be unique.
        :param pulumi.Input[int] position: The position of this policy on the listener. Positions start at 1.
        :param pulumi.Input[int] redirect_http_code: Integer. Requests matching this policy will be  
               redirected to the specified URL or Prefix URL with the HTTP response code.
               Valid if action is REDIRECT\\_TO\\_URL or REDIRECT\\_PREFIX. Valid options are:
               301, 302, 303, 307, or 308. Default is 302. New in octavia version 2.9
        :param pulumi.Input[str] redirect_pool_id: Requests matching this policy will be redirected to the
               pool with this ID. Only valid if action is REDIRECT\\_TO\\_POOL.
        :param pulumi.Input[str] redirect_prefix: Requests matching this policy will be redirected to 
               this Prefix URL. Only valid if action is REDIRECT\\_PREFIX.
        :param pulumi.Input[str] redirect_url: Requests matching this policy will be redirected to this URL.
               Only valid if action is REDIRECT\\_TO\\_URL.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an . If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               L7 Policy.
        :param pulumi.Input[str] tenant_id: Required for admins. The UUID of the tenant who owns
               the L7 Policy.  Only administrative users can specify a tenant UUID
               other than their own. Changing this creates a new L7 Policy.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "listener_id", listener_id)
        if admin_state_up is not None:
            pulumi.set(__self__, "admin_state_up", admin_state_up)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if position is not None:
            pulumi.set(__self__, "position", position)
        if redirect_http_code is not None:
            pulumi.set(__self__, "redirect_http_code", redirect_http_code)
        if redirect_pool_id is not None:
            pulumi.set(__self__, "redirect_pool_id", redirect_pool_id)
        if redirect_prefix is not None:
            pulumi.set(__self__, "redirect_prefix", redirect_prefix)
        if redirect_url is not None:
            pulumi.set(__self__, "redirect_url", redirect_url)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        """
        The L7 Policy action - can either be REDIRECT\\_TO\\_POOL,
        REDIRECT\\_TO\\_URL or REJECT.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Input[str]:
        """
        The Listener on which the L7 Policy will be associated with.
        Changing this creates a new L7 Policy.
        """
        return pulumi.get(self, "listener_id")

    @listener_id.setter
    def listener_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "listener_id", value)

    @property
    @pulumi.getter(name="adminStateUp")
    def admin_state_up(self) -> Optional[pulumi.Input[bool]]:
        """
        The administrative state of the L7 Policy.
        A valid value is true (UP) or false (DOWN).
        """
        return pulumi.get(self, "admin_state_up")

    @admin_state_up.setter
    def admin_state_up(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "admin_state_up", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Human-readable description for the L7 Policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Human-readable name for the L7 Policy. Does not have
        to be unique.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def position(self) -> Optional[pulumi.Input[int]]:
        """
        The position of this policy on the listener. Positions start at 1.
        """
        return pulumi.get(self, "position")

    @position.setter
    def position(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "position", value)

    @property
    @pulumi.getter(name="redirectHttpCode")
    def redirect_http_code(self) -> Optional[pulumi.Input[int]]:
        """
        Integer. Requests matching this policy will be  
        redirected to the specified URL or Prefix URL with the HTTP response code.
        Valid if action is REDIRECT\\_TO\\_URL or REDIRECT\\_PREFIX. Valid options are:
        301, 302, 303, 307, or 308. Default is 302. New in octavia version 2.9
        """
        return pulumi.get(self, "redirect_http_code")

    @redirect_http_code.setter
    def redirect_http_code(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "redirect_http_code", value)

    @property
    @pulumi.getter(name="redirectPoolId")
    def redirect_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        Requests matching this policy will be redirected to the
        pool with this ID. Only valid if action is REDIRECT\\_TO\\_POOL.
        """
        return pulumi.get(self, "redirect_pool_id")

    @redirect_pool_id.setter
    def redirect_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "redirect_pool_id", value)

    @property
    @pulumi.getter(name="redirectPrefix")
    def redirect_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Requests matching this policy will be redirected to 
        this Prefix URL. Only valid if action is REDIRECT\\_PREFIX.
        """
        return pulumi.get(self, "redirect_prefix")

    @redirect_prefix.setter
    def redirect_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "redirect_prefix", value)

    @property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> Optional[pulumi.Input[str]]:
        """
        Requests matching this policy will be redirected to this URL.
        Only valid if action is REDIRECT\\_TO\\_URL.
        """
        return pulumi.get(self, "redirect_url")

    @redirect_url.setter
    def redirect_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "redirect_url", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create an . If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        L7 Policy.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        Required for admins. The UUID of the tenant who owns
        the L7 Policy.  Only administrative users can specify a tenant UUID
        other than their own. Changing this creates a new L7 Policy.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


@pulumi.input_type
class _L7PolicyV2State:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input[str]] = None,
                 admin_state_up: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 position: Optional[pulumi.Input[int]] = None,
                 redirect_http_code: Optional[pulumi.Input[int]] = None,
                 redirect_pool_id: Optional[pulumi.Input[str]] = None,
                 redirect_prefix: Optional[pulumi.Input[str]] = None,
                 redirect_url: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering L7PolicyV2 resources.
        :param pulumi.Input[str] action: The L7 Policy action - can either be REDIRECT\\_TO\\_POOL,
               REDIRECT\\_TO\\_URL or REJECT.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the L7 Policy.
               A valid value is true (UP) or false (DOWN).
        :param pulumi.Input[str] description: Human-readable description for the L7 Policy.
        :param pulumi.Input[str] listener_id: The Listener on which the L7 Policy will be associated with.
               Changing this creates a new L7 Policy.
        :param pulumi.Input[str] name: Human-readable name for the L7 Policy. Does not have
               to be unique.
        :param pulumi.Input[int] position: The position of this policy on the listener. Positions start at 1.
        :param pulumi.Input[int] redirect_http_code: Integer. Requests matching this policy will be  
               redirected to the specified URL or Prefix URL with the HTTP response code.
               Valid if action is REDIRECT\\_TO\\_URL or REDIRECT\\_PREFIX. Valid options are:
               301, 302, 303, 307, or 308. Default is 302. New in octavia version 2.9
        :param pulumi.Input[str] redirect_pool_id: Requests matching this policy will be redirected to the
               pool with this ID. Only valid if action is REDIRECT\\_TO\\_POOL.
        :param pulumi.Input[str] redirect_prefix: Requests matching this policy will be redirected to 
               this Prefix URL. Only valid if action is REDIRECT\\_PREFIX.
        :param pulumi.Input[str] redirect_url: Requests matching this policy will be redirected to this URL.
               Only valid if action is REDIRECT\\_TO\\_URL.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an . If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               L7 Policy.
        :param pulumi.Input[str] tenant_id: Required for admins. The UUID of the tenant who owns
               the L7 Policy.  Only administrative users can specify a tenant UUID
               other than their own. Changing this creates a new L7 Policy.
        """
        if action is not None:
            pulumi.set(__self__, "action", action)
        if admin_state_up is not None:
            pulumi.set(__self__, "admin_state_up", admin_state_up)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if listener_id is not None:
            pulumi.set(__self__, "listener_id", listener_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if position is not None:
            pulumi.set(__self__, "position", position)
        if redirect_http_code is not None:
            pulumi.set(__self__, "redirect_http_code", redirect_http_code)
        if redirect_pool_id is not None:
            pulumi.set(__self__, "redirect_pool_id", redirect_pool_id)
        if redirect_prefix is not None:
            pulumi.set(__self__, "redirect_prefix", redirect_prefix)
        if redirect_url is not None:
            pulumi.set(__self__, "redirect_url", redirect_url)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        """
        The L7 Policy action - can either be REDIRECT\\_TO\\_POOL,
        REDIRECT\\_TO\\_URL or REJECT.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="adminStateUp")
    def admin_state_up(self) -> Optional[pulumi.Input[bool]]:
        """
        The administrative state of the L7 Policy.
        A valid value is true (UP) or false (DOWN).
        """
        return pulumi.get(self, "admin_state_up")

    @admin_state_up.setter
    def admin_state_up(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "admin_state_up", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Human-readable description for the L7 Policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Listener on which the L7 Policy will be associated with.
        Changing this creates a new L7 Policy.
        """
        return pulumi.get(self, "listener_id")

    @listener_id.setter
    def listener_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "listener_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Human-readable name for the L7 Policy. Does not have
        to be unique.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def position(self) -> Optional[pulumi.Input[int]]:
        """
        The position of this policy on the listener. Positions start at 1.
        """
        return pulumi.get(self, "position")

    @position.setter
    def position(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "position", value)

    @property
    @pulumi.getter(name="redirectHttpCode")
    def redirect_http_code(self) -> Optional[pulumi.Input[int]]:
        """
        Integer. Requests matching this policy will be  
        redirected to the specified URL or Prefix URL with the HTTP response code.
        Valid if action is REDIRECT\\_TO\\_URL or REDIRECT\\_PREFIX. Valid options are:
        301, 302, 303, 307, or 308. Default is 302. New in octavia version 2.9
        """
        return pulumi.get(self, "redirect_http_code")

    @redirect_http_code.setter
    def redirect_http_code(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "redirect_http_code", value)

    @property
    @pulumi.getter(name="redirectPoolId")
    def redirect_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        Requests matching this policy will be redirected to the
        pool with this ID. Only valid if action is REDIRECT\\_TO\\_POOL.
        """
        return pulumi.get(self, "redirect_pool_id")

    @redirect_pool_id.setter
    def redirect_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "redirect_pool_id", value)

    @property
    @pulumi.getter(name="redirectPrefix")
    def redirect_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Requests matching this policy will be redirected to 
        this Prefix URL. Only valid if action is REDIRECT\\_PREFIX.
        """
        return pulumi.get(self, "redirect_prefix")

    @redirect_prefix.setter
    def redirect_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "redirect_prefix", value)

    @property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> Optional[pulumi.Input[str]]:
        """
        Requests matching this policy will be redirected to this URL.
        Only valid if action is REDIRECT\\_TO\\_URL.
        """
        return pulumi.get(self, "redirect_url")

    @redirect_url.setter
    def redirect_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "redirect_url", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create an . If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        L7 Policy.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        Required for admins. The UUID of the tenant who owns
        the L7 Policy.  Only administrative users can specify a tenant UUID
        other than their own. Changing this creates a new L7 Policy.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


class L7PolicyV2(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 admin_state_up: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 position: Optional[pulumi.Input[int]] = None,
                 redirect_http_code: Optional[pulumi.Input[int]] = None,
                 redirect_pool_id: Optional[pulumi.Input[str]] = None,
                 redirect_prefix: Optional[pulumi.Input[str]] = None,
                 redirect_url: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Load Balancer L7 Policy resource within OpenStack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        network1 = openstack.networking.Network("network_1",
            name="network_1",
            admin_state_up=True)
        subnet1 = openstack.networking.Subnet("subnet_1",
            name="subnet_1",
            cidr="192.168.199.0/24",
            ip_version=4,
            network_id=network1.id)
        loadbalancer1 = openstack.LbLoadbalancerV2("loadbalancer_1",
            name="loadbalancer_1",
            vip_subnet_id=subnet1.id)
        listener1 = openstack.loadbalancer.Listener("listener_1",
            name="listener_1",
            protocol="HTTP",
            protocol_port=8080,
            loadbalancer_id=loadbalancer1.id)
        pool1 = openstack.loadbalancer.Pool("pool_1",
            name="pool_1",
            protocol="HTTP",
            lb_method="ROUND_ROBIN",
            loadbalancer_id=loadbalancer1.id)
        l7policy1 = openstack.loadbalancer.L7PolicyV2("l7policy_1",
            name="test",
            action="REDIRECT_TO_POOL",
            description="test l7 policy",
            position=1,
            listener_id=listener1.id,
            redirect_pool_id=pool1.id)
        ```

        ## Import

        Load Balancer L7 Policy can be imported using the L7 Policy ID, e.g.:

        ```sh
        $ pulumi import openstack:loadbalancer/l7PolicyV2:L7PolicyV2 l7policy_1 8a7a79c2-cf17-4e65-b2ae-ddc8bfcf6c74
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: The L7 Policy action - can either be REDIRECT\\_TO\\_POOL,
               REDIRECT\\_TO\\_URL or REJECT.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the L7 Policy.
               A valid value is true (UP) or false (DOWN).
        :param pulumi.Input[str] description: Human-readable description for the L7 Policy.
        :param pulumi.Input[str] listener_id: The Listener on which the L7 Policy will be associated with.
               Changing this creates a new L7 Policy.
        :param pulumi.Input[str] name: Human-readable name for the L7 Policy. Does not have
               to be unique.
        :param pulumi.Input[int] position: The position of this policy on the listener. Positions start at 1.
        :param pulumi.Input[int] redirect_http_code: Integer. Requests matching this policy will be  
               redirected to the specified URL or Prefix URL with the HTTP response code.
               Valid if action is REDIRECT\\_TO\\_URL or REDIRECT\\_PREFIX. Valid options are:
               301, 302, 303, 307, or 308. Default is 302. New in octavia version 2.9
        :param pulumi.Input[str] redirect_pool_id: Requests matching this policy will be redirected to the
               pool with this ID. Only valid if action is REDIRECT\\_TO\\_POOL.
        :param pulumi.Input[str] redirect_prefix: Requests matching this policy will be redirected to 
               this Prefix URL. Only valid if action is REDIRECT\\_PREFIX.
        :param pulumi.Input[str] redirect_url: Requests matching this policy will be redirected to this URL.
               Only valid if action is REDIRECT\\_TO\\_URL.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an . If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               L7 Policy.
        :param pulumi.Input[str] tenant_id: Required for admins. The UUID of the tenant who owns
               the L7 Policy.  Only administrative users can specify a tenant UUID
               other than their own. Changing this creates a new L7 Policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: L7PolicyV2Args,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Load Balancer L7 Policy resource within OpenStack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        network1 = openstack.networking.Network("network_1",
            name="network_1",
            admin_state_up=True)
        subnet1 = openstack.networking.Subnet("subnet_1",
            name="subnet_1",
            cidr="192.168.199.0/24",
            ip_version=4,
            network_id=network1.id)
        loadbalancer1 = openstack.LbLoadbalancerV2("loadbalancer_1",
            name="loadbalancer_1",
            vip_subnet_id=subnet1.id)
        listener1 = openstack.loadbalancer.Listener("listener_1",
            name="listener_1",
            protocol="HTTP",
            protocol_port=8080,
            loadbalancer_id=loadbalancer1.id)
        pool1 = openstack.loadbalancer.Pool("pool_1",
            name="pool_1",
            protocol="HTTP",
            lb_method="ROUND_ROBIN",
            loadbalancer_id=loadbalancer1.id)
        l7policy1 = openstack.loadbalancer.L7PolicyV2("l7policy_1",
            name="test",
            action="REDIRECT_TO_POOL",
            description="test l7 policy",
            position=1,
            listener_id=listener1.id,
            redirect_pool_id=pool1.id)
        ```

        ## Import

        Load Balancer L7 Policy can be imported using the L7 Policy ID, e.g.:

        ```sh
        $ pulumi import openstack:loadbalancer/l7PolicyV2:L7PolicyV2 l7policy_1 8a7a79c2-cf17-4e65-b2ae-ddc8bfcf6c74
        ```

        :param str resource_name: The name of the resource.
        :param L7PolicyV2Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(L7PolicyV2Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 admin_state_up: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 position: Optional[pulumi.Input[int]] = None,
                 redirect_http_code: Optional[pulumi.Input[int]] = None,
                 redirect_pool_id: Optional[pulumi.Input[str]] = None,
                 redirect_prefix: Optional[pulumi.Input[str]] = None,
                 redirect_url: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = L7PolicyV2Args.__new__(L7PolicyV2Args)

            if action is None and not opts.urn:
                raise TypeError("Missing required property 'action'")
            __props__.__dict__["action"] = action
            __props__.__dict__["admin_state_up"] = admin_state_up
            __props__.__dict__["description"] = description
            if listener_id is None and not opts.urn:
                raise TypeError("Missing required property 'listener_id'")
            __props__.__dict__["listener_id"] = listener_id
            __props__.__dict__["name"] = name
            __props__.__dict__["position"] = position
            __props__.__dict__["redirect_http_code"] = redirect_http_code
            __props__.__dict__["redirect_pool_id"] = redirect_pool_id
            __props__.__dict__["redirect_prefix"] = redirect_prefix
            __props__.__dict__["redirect_url"] = redirect_url
            __props__.__dict__["region"] = region
            __props__.__dict__["tenant_id"] = tenant_id
        super(L7PolicyV2, __self__).__init__(
            'openstack:loadbalancer/l7PolicyV2:L7PolicyV2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action: Optional[pulumi.Input[str]] = None,
            admin_state_up: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            listener_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            position: Optional[pulumi.Input[int]] = None,
            redirect_http_code: Optional[pulumi.Input[int]] = None,
            redirect_pool_id: Optional[pulumi.Input[str]] = None,
            redirect_prefix: Optional[pulumi.Input[str]] = None,
            redirect_url: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None) -> 'L7PolicyV2':
        """
        Get an existing L7PolicyV2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: The L7 Policy action - can either be REDIRECT\\_TO\\_POOL,
               REDIRECT\\_TO\\_URL or REJECT.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the L7 Policy.
               A valid value is true (UP) or false (DOWN).
        :param pulumi.Input[str] description: Human-readable description for the L7 Policy.
        :param pulumi.Input[str] listener_id: The Listener on which the L7 Policy will be associated with.
               Changing this creates a new L7 Policy.
        :param pulumi.Input[str] name: Human-readable name for the L7 Policy. Does not have
               to be unique.
        :param pulumi.Input[int] position: The position of this policy on the listener. Positions start at 1.
        :param pulumi.Input[int] redirect_http_code: Integer. Requests matching this policy will be  
               redirected to the specified URL or Prefix URL with the HTTP response code.
               Valid if action is REDIRECT\\_TO\\_URL or REDIRECT\\_PREFIX. Valid options are:
               301, 302, 303, 307, or 308. Default is 302. New in octavia version 2.9
        :param pulumi.Input[str] redirect_pool_id: Requests matching this policy will be redirected to the
               pool with this ID. Only valid if action is REDIRECT\\_TO\\_POOL.
        :param pulumi.Input[str] redirect_prefix: Requests matching this policy will be redirected to 
               this Prefix URL. Only valid if action is REDIRECT\\_PREFIX.
        :param pulumi.Input[str] redirect_url: Requests matching this policy will be redirected to this URL.
               Only valid if action is REDIRECT\\_TO\\_URL.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an . If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               L7 Policy.
        :param pulumi.Input[str] tenant_id: Required for admins. The UUID of the tenant who owns
               the L7 Policy.  Only administrative users can specify a tenant UUID
               other than their own. Changing this creates a new L7 Policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _L7PolicyV2State.__new__(_L7PolicyV2State)

        __props__.__dict__["action"] = action
        __props__.__dict__["admin_state_up"] = admin_state_up
        __props__.__dict__["description"] = description
        __props__.__dict__["listener_id"] = listener_id
        __props__.__dict__["name"] = name
        __props__.__dict__["position"] = position
        __props__.__dict__["redirect_http_code"] = redirect_http_code
        __props__.__dict__["redirect_pool_id"] = redirect_pool_id
        __props__.__dict__["redirect_prefix"] = redirect_prefix
        __props__.__dict__["redirect_url"] = redirect_url
        __props__.__dict__["region"] = region
        __props__.__dict__["tenant_id"] = tenant_id
        return L7PolicyV2(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[str]:
        """
        The L7 Policy action - can either be REDIRECT\\_TO\\_POOL,
        REDIRECT\\_TO\\_URL or REJECT.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="adminStateUp")
    def admin_state_up(self) -> pulumi.Output[Optional[bool]]:
        """
        The administrative state of the L7 Policy.
        A valid value is true (UP) or false (DOWN).
        """
        return pulumi.get(self, "admin_state_up")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Human-readable description for the L7 Policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Output[str]:
        """
        The Listener on which the L7 Policy will be associated with.
        Changing this creates a new L7 Policy.
        """
        return pulumi.get(self, "listener_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Human-readable name for the L7 Policy. Does not have
        to be unique.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def position(self) -> pulumi.Output[int]:
        """
        The position of this policy on the listener. Positions start at 1.
        """
        return pulumi.get(self, "position")

    @property
    @pulumi.getter(name="redirectHttpCode")
    def redirect_http_code(self) -> pulumi.Output[int]:
        """
        Integer. Requests matching this policy will be  
        redirected to the specified URL or Prefix URL with the HTTP response code.
        Valid if action is REDIRECT\\_TO\\_URL or REDIRECT\\_PREFIX. Valid options are:
        301, 302, 303, 307, or 308. Default is 302. New in octavia version 2.9
        """
        return pulumi.get(self, "redirect_http_code")

    @property
    @pulumi.getter(name="redirectPoolId")
    def redirect_pool_id(self) -> pulumi.Output[Optional[str]]:
        """
        Requests matching this policy will be redirected to the
        pool with this ID. Only valid if action is REDIRECT\\_TO\\_POOL.
        """
        return pulumi.get(self, "redirect_pool_id")

    @property
    @pulumi.getter(name="redirectPrefix")
    def redirect_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        Requests matching this policy will be redirected to 
        this Prefix URL. Only valid if action is REDIRECT\\_PREFIX.
        """
        return pulumi.get(self, "redirect_prefix")

    @property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> pulumi.Output[Optional[str]]:
        """
        Requests matching this policy will be redirected to this URL.
        Only valid if action is REDIRECT\\_TO\\_URL.
        """
        return pulumi.get(self, "redirect_url")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create an . If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        L7 Policy.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        Required for admins. The UUID of the tenant who owns
        the L7 Policy.  Only administrative users can specify a tenant UUID
        other than their own. Changing this creates a new L7 Policy.
        """
        return pulumi.get(self, "tenant_id")

