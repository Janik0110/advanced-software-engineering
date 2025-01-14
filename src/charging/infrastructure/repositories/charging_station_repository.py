from typing import List

from charging.domain.value_objects.postal_code import PostalCode
from charging.domain.aggregates.charging_station import ChargingStation


class ChargingStationRepository:
    def find_by_postal_code(self, postal_code: PostalCode) -> List[ChargingStation]:
        raise NotImplementedError
