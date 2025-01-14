from dataclasses import dataclass
from uuid import UUID

from src.charging.domain.value_objects.charging_station_status import (
    ChargingStationStatus,
)
from src.charging.domain.value_objects.charging_station_type import ChargingStationType
from src.charging.domain.value_objects.postal_code import PostalCode


@dataclass
class ChargingStation:

    id: UUID
    postal_code: PostalCode
    location: str
    type: ChargingStationType
    status: ChargingStationStatus = ChargingStationStatus.AVAILABLE

    def is_in_postal_code(self, postal_code: PostalCode) -> bool:
        return self.postal_code == postal_code

    def update_status(self, status: ChargingStationStatus) -> None:
        self.status = status
