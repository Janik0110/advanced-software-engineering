from typing import List
from charging.domain.value_objects.postal_code import PostalCode
from charging.domain.aggregates.charging_station import ChargingStation


class ChargingStationRepository:
    def __init__(self):
        self._stations = [
            ChargingStation(id="1", name="Station A", postal_code="12345"),
            ChargingStation(id="2", name="Station B", postal_code="12345"),
            ChargingStation(id="3", name="Station C", postal_code="67890"),
        ]

    def find_by_postal_code(self, postal_code: PostalCode) -> List[ChargingStation]:
        return [
            station
            for station in self._stations
            if station.postal_code == str(postal_code)
        ]
