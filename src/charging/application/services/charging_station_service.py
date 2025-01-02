from dataclasses import dataclass
from datetime import datetime
from typing import List

from charging.domain.events.charging_station_search_performed import (
    ChargingStationSearchPerformed,
)
from charging.domain.value_objects.postal_code import PostalCode
from charging.domain.aggregates.charging_station import ChargingStation
from charging.infrastructure.repositories.charging_station_repository import (
    ChargingStationRepository,
)


@dataclass(frozen=True)
class SearchResult:
    stations: List[ChargingStation]
    event: ChargingStationSearchPerformed


class ChargingStationService:
    repository: ChargingStationRepository

    def __init__(self, repository: ChargingStationRepository):
        self.repository = repository

    def find_charging_station_by_postal_code(self, postal_code: str) -> SearchResult:
        postal_code = PostalCode(postal_code)
        stations = self.repository.find_by_postal_code(postal_code)

        event = ChargingStationSearchPerformed(
            postal_code=postal_code,
            timestamp=datetime.now(),
            station_count=len(stations),
        )

        return SearchResult(stations, event)
