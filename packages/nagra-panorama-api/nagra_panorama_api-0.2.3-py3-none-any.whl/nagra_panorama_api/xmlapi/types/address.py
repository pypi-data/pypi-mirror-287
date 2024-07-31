# Given a list of subnets,
# Find all NAT rules related to an address in the subnet

from dataclasses import dataclass
from ipaddress import IPv4Network, IPv6Network, ip_network
from itertools import chain
from typing import Optional, Union

from pydantic import AliasChoices, AliasPath, BaseModel, Field
from pydantic.functional_validators import field_validator, model_validator
from typing_extensions import Self

from nagra_panorama_api.xmlapi.utils import el2dict

from .utils import List, String

IPNetwork = Union[IPv4Network, IPv6Network]


@dataclass
class NATRule:
    device_group: str
    name: str
    uuid: str
    ttype: str
    to_members: List[str]
    from_members: List[str]
    src_members: List[str]
    dst_members: List[str]
    src_translations: List[str]
    dst_translations: List[str]

    @property
    def members(self):
        return set(
            chain(
                self.to_members,
                self.from_members,
                self.src_members,
                self.dst_members,
                self.src_translations,
                self.dst_translations,
            )
        )


def _parse_trans_addr(xml):
    static = xml.xpath(".//translated-address/text()")  # for static-ip
    dynamic = xml.xpath(".//translated-address/member/text()")  # for dynamic-ip
    dynamic_and_port = xml.xpath(".//interface-address/ip/text()")
    return static, dynamic, dynamic_and_port


def parse_trans_addr(xml):
    static = []
    dynamic = []
    dynamic_and_port = []
    if not xml:
        return static, dynamic, dynamic_and_port
    if not isinstance(xml, (list, tuple)):
        xml = [xml]
    for e in xml:
        a, b, c = _parse_trans_addr(e)
        static.extend(a)
        dynamic.extend(b)
        dynamic_and_port.extend(c)
    return static, dynamic, dynamic_and_port


def get_trans_addr(xml):
    static, dynamic, dynamic_and_port = parse_trans_addr(xml)
    return [*static, *dynamic]


def xml2nat(xml):
    post_pre = xml.getparent().getparent().getparent()
    device_group = post_pre.getparent().attrib["name"]
    name = xml.attrib["name"]
    uuid = xml.attrib["uuid"]
    ttype = post_pre.tag
    to_members = xml.xpath("./to/member/text()")
    from_members = xml.xpath("./from/member/text()")
    src_members = xml.xpath("./source/member/text()")
    dst_members = xml.xpath("./destination/member/text()")
    src_translations = get_trans_addr(xml.xpath("./source-translation"))
    dst_translations = get_trans_addr(xml.xpath("./destination-translation"))
    return NATRule(
        device_group,
        name,
        uuid,
        ttype,
        to_members,
        from_members,
        src_members,
        dst_members,
        src_translations,
        dst_translations,
    )


def get_ip_network(ip_netmask):
    try:
        if ip_netmask:
            return ip_network(ip_netmask, strict=False)
    except Exception:
        return None


# https://docs.pydantic.dev/latest/concepts/alias/#aliaspath-and-aliaschoices
class Address(BaseModel):
    name: str = Field(validation_alias="@name")
    type: Optional[str] = None
    prefix: Optional[str] = None
    ip_netmask: Optional[str] = Field(
        alias="ip-netmask",
        validation_alias=AliasChoices(
            AliasPath("ip-netmask", "#text"),
            "ip-netmask",
        ),
        default=None,
    )
    ip_network: Optional[IPNetwork] = None
    ip_range: Optional[str] = Field(alias="ip-range", default=None)
    fqdn: Optional[String] = None
    tags: List[String] = Field(
        validation_alias=AliasPath("tag", "member"), default=None
    )

    @field_validator("tags", mode="before")
    @classmethod
    def validate_tags(cls, v) -> List[str]:
        if not v:
            return []
        if not isinstance(v, list):
            return [v]
        return v

    @model_validator(mode="after")
    def validate_ip_network(self) -> Self:
        if self.ip_network is None:
            self.ip_network = get_ip_network(self.ip_netmask)
        if not isinstance(self.ip_network, (IPv4Network, IPv6Network)):
            self.ip_network = None
        return self

    @model_validator(mode="after")
    def validate_type(self) -> Self:
        address_type = None
        if self.prefix:
            address_type = "prefix"
        elif self.ip_netmask:
            address_type = "ip-netmask"
        elif self.ip_range:
            address_type = "ip-range"
        elif self.fqdn:
            address_type = "fqdn"
        self.type = address_type
        return self

    @staticmethod
    def from_xml(xml):
        entry = el2dict(xml)["entry"]
        return Address.model_validate(entry)


def get_nat_membership(tree):
    # nat_rules_xml = tree.xpath(".//nat/rules/entry")
    nat_rules_xml = tree.xpath("./devices/entry/device-group//nat/rules/entry")
    nat_rules = [xml2nat(n) for n in nat_rules_xml]

    # Create a dict member -> associated nat rules
    nat_membership = {}
    for n in nat_rules:
        for m in n.members:
            member_nat_rules = nat_membership.setdefault(m, [])
            member_nat_rules.append(n)
    return nat_membership


def find_addresses(tree):
    # addresses_xml = tree.xpath(".//address/entry")
    addresses_xml = tree.xpath("./devices/entry/device-group//address/entry")
    address_objects = [Address.from_xml(n) for n in addresses_xml]

    addresses = []
    subnets = []
    for a in address_objects:
        network = a.ip_network
        # We do not consider ip ranges for now
        if not network:
            continue
        if network.prefixlen == network.max_prefixlen:
            addresses.append(a)
        else:
            subnets.append(a)
    return addresses, subnets
