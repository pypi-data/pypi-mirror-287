from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

from mashumaro import field_options
from mashumaro.mixins.orjson import DataClassORJSONMixin

IpCheckLookupSource = Literal["MaxMind", "NEP"]
IpCheckAccessGroup = Literal["NO", "EEA", "WORLD"]
DisplayAspectRatioVideo = Literal["16:9", "4:3"]

@dataclass
class IpCheck(DataClassORJSONMixin):
    client_ip_address: str = field(metadata=field_options(alias="clientIpAddress"))
    country_code: str = field(metadata=field_options(alias="countryCode"))
    is_ip_norwegian: bool = field(metadata=field_options(alias="isIpNorwegian"))
    lookup_source: IpCheckLookupSource = field(metadata=field_options(alias="lookupSource"))
    access_group: IpCheckAccessGroup = field(metadata=field_options(alias="accessGroup"))
