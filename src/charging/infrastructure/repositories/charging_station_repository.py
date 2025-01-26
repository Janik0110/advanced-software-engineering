from typing import List
import sqlite3

from src.charging.domain.value_objects.charging_station_type import ChargingStationType
from src.charging.domain.value_objects.postal_code import PostalCode
from src.charging.domain.aggregates.charging_station import ChargingStation


class ChargingStationRepository:
    def __init__(self):
        self.conn = sqlite3.connect("src/datasets/database.sqlite")
        self.cursor = self.conn.cursor()

    def find_by_postal_code(self, postal_code: PostalCode) -> List[ChargingStation]:
        self.cursor.execute(
            "SELECT * FROM charging_stations WHERE postal_code LIKE ?",
            (postal_code.value,),
        )
        rows = self.cursor.fetchall()

        return [
            ChargingStation(
                id=row[2],
                postal_code=PostalCode(row[0]),
                location=f"{row[3]} {row[4]}",
                type=ChargingStationType(row[1]),
            )
            for row in rows
        ]
