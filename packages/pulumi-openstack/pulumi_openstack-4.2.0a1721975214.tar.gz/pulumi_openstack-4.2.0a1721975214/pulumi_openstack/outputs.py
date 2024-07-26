# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'BgpvpnPortAssociateV2Route',
]

@pulumi.output_type
class BgpvpnPortAssociateV2Route(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bgpvpnId":
            suggest = "bgpvpn_id"
        elif key == "localPref":
            suggest = "local_pref"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BgpvpnPortAssociateV2Route. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BgpvpnPortAssociateV2Route.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BgpvpnPortAssociateV2Route.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: str,
                 bgpvpn_id: Optional[str] = None,
                 local_pref: Optional[int] = None,
                 prefix: Optional[str] = None):
        """
        :param str type: Can be `prefix` or `bgpvpn`. For the `prefix` type, the
               CIDR prefix (v4 or v6) must be specified in the `prefix` key. For the
               `bgpvpn` type, the BGP VPN ID must be specified in the `bgpvpn_id` key.
        :param str bgpvpn_id: The ID of the BGP VPN to be advertised. Required
               if `type` is `bgpvpn`. Conflicts with `prefix`.
        :param int local_pref: The BGP LOCAL\\_PREF value of the routes that will
               be advertised.
        :param str prefix: The CIDR prefix (v4 or v6) to be advertised. Required
               if `type` is `prefix`. Conflicts with `bgpvpn_id`.
        """
        pulumi.set(__self__, "type", type)
        if bgpvpn_id is not None:
            pulumi.set(__self__, "bgpvpn_id", bgpvpn_id)
        if local_pref is not None:
            pulumi.set(__self__, "local_pref", local_pref)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Can be `prefix` or `bgpvpn`. For the `prefix` type, the
        CIDR prefix (v4 or v6) must be specified in the `prefix` key. For the
        `bgpvpn` type, the BGP VPN ID must be specified in the `bgpvpn_id` key.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="bgpvpnId")
    def bgpvpn_id(self) -> Optional[str]:
        """
        The ID of the BGP VPN to be advertised. Required
        if `type` is `bgpvpn`. Conflicts with `prefix`.
        """
        return pulumi.get(self, "bgpvpn_id")

    @property
    @pulumi.getter(name="localPref")
    def local_pref(self) -> Optional[int]:
        """
        The BGP LOCAL\\_PREF value of the routes that will
        be advertised.
        """
        return pulumi.get(self, "local_pref")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        """
        The CIDR prefix (v4 or v6) to be advertised. Required
        if `type` is `prefix`. Conflicts with `bgpvpn_id`.
        """
        return pulumi.get(self, "prefix")


