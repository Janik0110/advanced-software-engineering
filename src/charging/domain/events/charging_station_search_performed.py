from dataclasses import dataclass
from datetime import datetime

from charging.domain.value_objects.postal_code import PostalCode


@dataclass(frozen=True)
class ChargingStationSearchPerformed:
    postal_code: PostalCode
    timestamp: datetime
    station_count: int
