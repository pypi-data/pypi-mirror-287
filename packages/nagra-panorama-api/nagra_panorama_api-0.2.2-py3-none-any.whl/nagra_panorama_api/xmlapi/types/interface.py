# Given a list of subnets,
# Find all NAT rules related to an address in the subnet

from ipaddress import ip_network
from typing import Optional

from pydantic import AliasPath, BaseModel, ConfigDict, Field

from nagra_panorama_api.xmlapi.utils import el2dict

from .utils import List, String


def get_ip_network(ip_netmask):
    try:
        if ip_netmask:
            return ip_network(ip_netmask, strict=False)
    except Exception:
        return None


class Layer3(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: Optional[String] = Field(validation_alias="@name", default=None)
    description: Optional[String] = Field(validation_alias="#text", default=None)
    ip: List[str] = Field(
        validation_alias=AliasPath("ip", "entry", "@name"), default_factory=list
    )
    untagged_sub_interface: Optional[String] = Field(
        alias="untagged-sub-interface",
        default=None,
    )
    units: List["Layer3"] = Field(
        alias="units",
        validation_alias=AliasPath("units", "entry"),
        default_factory=list,
    )
    comment: Optional[String] = None
    tags: List[String] = Field(
        validation_alias=AliasPath("tag", "member"),
        default_factory=list,
    )


class Vlan(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: Optional[String] = Field(validation_alias="@name", default=None)
    description: Optional[String] = Field(validation_alias="#text", default=None)
    ip: List[str] = Field(
        validation_alias=AliasPath("ip", "entry", "@name"), default_factory=list
    )
    # untagged_sub_interface: Optional[String] = Field(
    #     alias="untagged-sub-interface",
    #     default=None,
    # )
    units: List["Vlan"] = Field(
        alias="units",
        validation_alias=AliasPath("units", "entry"),
        default_factory=list,
    )
    comment: Optional[String] = None
    tags: List[String] = Field(
        validation_alias=AliasPath("tag", "member"),
        default_factory=list,
    )


class Ethernet(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: str = Field(validation_alias="@name")
    description: Optional[String] = Field(validation_alias="#text", default=None)
    link_state: Optional[str] = Field(
        alias="link-state",
        validation_alias=AliasPath("link-state", "#text"),
        default=None,
    )
    link_speed: Optional[str] = Field(
        alias="link-speed",
        validation_alias=AliasPath("link-speed", "#text"),
        default=None,
    )
    link_duplex: Optional[str] = Field(
        alias="link-duplex",
        validation_alias=AliasPath("link-duplex", "#text"),
        default=None,
    )
    aggregate_group: Optional[String] = Field(
        alias="aggregate-group",
        default=None,
    )
    layer3: Optional[Layer3] = Field(alias="layer3", default=None)
    tags: List[String] = Field(
        validation_alias=AliasPath("tag", "member"),
        default_factory=list,
    )
    # @model_validator(mode="before")
    # @classmethod
    # def test(cls, data):
    #     print("\n" * 5)
    #     print("Ethernet:", data)
    #     return data


class AggregateEthernet(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: str = Field(validation_alias="@name")
    description: Optional[String] = Field(validation_alias="#text", default=None)
    comment: Optional[String] = None
    units: List["AggregateEthernet"] = Field(
        alias="units",
        validation_alias=AliasPath("units", "entry"),
        default_factory=list,
    )
    layer3: Optional[Layer3] = Field(alias="layer3", default=None)
    untagged_sub_interface: Optional[String] = Field(
        alias="untagged-sub-interface",
        default=None,
    )
    tags: List[String] = Field(
        validation_alias=AliasPath("tag", "member"),
        default_factory=list,
    )
    # @model_validator(mode="before")
    # @classmethod
    # def test(cls, data):
    #     print("\n" * 5)
    #     print("AggregateEthernet:", data)
    #     return data


class Loopback(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: str = Field(validation_alias="@name")
    description: Optional[String] = Field(validation_alias="#text", default=None)
    ip: List[str] = Field(
        validation_alias=AliasPath("ip", "entry", "@name"), default_factory=list
    )
    comment: Optional[str] = Field(
        alias="comment", validation_alias=AliasPath("comment", "#text"), default=None
    )
    tags: List[String] = Field(
        validation_alias=AliasPath("tag", "member"),
        default_factory=list,
    )


# https://docs.pydantic.dev/latest/concepts/alias/#aliaspath-and-aliaschoices
class Interface(BaseModel):
    model_config = ConfigDict(extra="allow")

    aggregate_ethernet: List[AggregateEthernet] = Field(
        alias="aggregate-ethernet",
        validation_alias=AliasPath("aggregate-ethernet", "entry"),
        default_factory=list,
    )
    # entry = Field(alias="entry")
    ethernet: List[Ethernet] = Field(
        alias="ethernet",
        validation_alias=AliasPath("ethernet", "entry"),
        default_factory=list,
    )
    loopback: List[Loopback] = Field(
        alias="loopback",
        validation_alias=AliasPath("loopback", "units", "entry"),
        default_factory=list,
    )
    vlan: List[Vlan] = Field(
        alias="vlan",
        validation_alias=AliasPath("vlan", "units", "entry"),
        default_factory=list,
    )
    # ha1 = Field(alias='ha1')
    # ha1_backup = Field(alias='ha1-backup')
    # ha2 = Field(alias='ha2')
    # ha2_backup = Field(alias='ha2-backup')
    # ha3 = Field(alias='ha3')
    # member = Field(alias='member')
    # tunnel = Field(alias='tunnel')

    @staticmethod
    def from_xml(xml):
        entry = el2dict(xml)["interface"]
        return Interface.model_validate(entry)
