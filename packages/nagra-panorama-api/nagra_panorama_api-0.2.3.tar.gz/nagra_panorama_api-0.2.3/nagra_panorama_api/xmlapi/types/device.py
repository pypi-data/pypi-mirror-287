from typing import Optional

from pydantic import BaseModel, ConfigDict

from nagra_panorama_api.utils import (
    first,
)
from nagra_panorama_api.xmlapi.types.utils import (
    Datetime,
    mksx,
)
from nagra_panorama_api.xmlapi.utils import (
    el2dict,
)


class Device(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    serial: str
    connected: bool
    unsupported_version: bool
    wildfire_rt: bool
    deactivated: Optional[str] = None
    hostname: Optional[str] = None
    ip_address: Optional[str] = None
    ipv6_address: Optional[str] = None
    mac_addr: Optional[str] = None
    uptime: Optional[str] = None
    family: Optional[str] = None
    model: Optional[str] = None
    sw_version: Optional[str] = None
    app_version: Optional[str] = None
    av_version: Optional[str] = None
    device_dictionary_version: Optional[str] = ""
    wildfire_version: Optional[str] = None
    threat_version: Optional[str] = None
    url_db: Optional[str] = None
    url_filtering_version: Optional[str] = None
    logdb_version: Optional[str] = None
    vpnclient_package_version: Optional[str] = None
    global_protect_client_package_version: Optional[str] = None
    prev_app_version: Optional[str] = None
    prev_av_version: Optional[str] = None
    prev_threat_version: Optional[str] = None
    prev_wildfire_version: Optional[str] = None
    prev_device_dictionary_version: Optional[str] = ""
    # domain/: str
    # slot_count: str
    # type/: str
    # tag/: str
    # plugin_versions
    # ha_cluster
    ha_peer_serial: Optional[str] = None
    vpn_disable_mode: bool
    operational_mode: str
    certificate_status: Optional[str] = None
    certificate_subject_name: Optional[str] = None
    certificate_expiry: Datetime
    connected_at: Datetime
    custom_certificate_usage: Optional[str] = None
    multi_vsys: bool
    # vsys
    last_masterkey_push_status: str
    last_masterkey_push_timestamp: Optional[str] = None
    express_mode: bool
    device_cert_present: Optional[str] = None
    device_cert_expiry_date: str

    @staticmethod
    def from_xml(xml) -> Optional["Device"]:
        if isinstance(xml, (list, tuple)):
            xml = first(xml)
        if xml is None:
            return None
        res = {k.replace("-", "_"): v for k, v in el2dict(xml)["entry"].items()}
        p = mksx(xml)
        res.update({"ha_peer_serial": p(".//ha/peer/serial/text()")})
        return Device(**res)
        # res = Device(**res)
        # if res.ip_address == "10.9.158.246":
        #     pprint(xml)
        # return res


class VPNFlow(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str
    id: int
    gwid: int
    inner_if: str
    outer_if: str
    localip: str
    peerip: str
    state: str
    mon: str
    owner: str

    @staticmethod
    def from_xml(xml):
        if isinstance(xml, (list, tuple)):
            xml = first(xml)
        if xml is None:
            return None
        res = {k.replace("-", "_"): v for k, v in el2dict(xml)["entry"].items()}
        return VPNFlow(**res)


class HAInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    enabled: bool
    preemptive: Optional[bool] = None
    mode: Optional[str] = None
    state: Optional[str] = None
    peer_state: Optional[str] = None
    priority: Optional[int] = None
    peer_priority: Optional[int] = None
    is_primary: Optional[bool] = None
    peer_conn_status: Optional[str] = None
    mgmt_ip: Optional[str] = None
    ha1_ipaddr: Optional[str] = None
    ha1_backup_ipaddr: Optional[str] = None
    ha2_ipaddr: Optional[str] = None
    ha1_macaddress: Optional[str] = None
    ha1_backup_macaddress: Optional[str] = None
    ha2_macaddress: Optional[str] = None

    @staticmethod
    def from_xml(xml):
        if isinstance(xml, (list, tuple)):
            xml = first(xml)
        if xml is None:
            return None
        p = mksx(xml)
        priority = p("./group/local-info/priority/text()", parser=int)
        peer_priority = p("./group/peer-info/priority/text()", parser=int)
        is_primary = None
        if priority is not None and peer_priority is not None:
            is_primary = priority < peer_priority
        return HAInfo(
            enabled=p("./enabled/text()"),
            preemptive=p("./group/local-info/preemptive/text()"),
            mode=p("./group/local-info/mode/text()"),
            state=p("./group/local-info/state/text()"),
            peer_state=p("./group/peer-info/state/text()"),
            priority=priority,
            peer_priority=peer_priority,
            is_primary=is_primary,
            peer_conn_status=p("./group/peer-info/conn-status/text()"),
            mgmt_ip=p("./group/local-info/mgmt-ip/text()"),
            ha1_ipaddr=p("./group/local-info/ha1-ipaddr/text()"),
            ha1_backup_ipaddr=p("./group/local-info/ha1-backup-ipaddr/text()"),
            ha2_ipaddr=p("./group/local-info/ha2-ipaddr/text()"),
            ha1_macaddress=p("./group/local-info/ha1-macaddr/text()"),
            ha1_backup_macaddress=p("./group/local-info/ha1-backup-macaddr/text()"),
            ha2_macaddress=p("./group/local-info/ha2-macaddr/text()"),
        )
