import sqlite3

from src.rating.domain.aggregates.rating import Rating


class RatingRepository:
    def __init__(self):
        self.conn = sqlite3.connect("src/datasets/database.sqlite")
        self.cursor = self.conn.cursor()

    def save(self, rating: Rating):
        self.cursor.execute(
            "INSERT INTO ratings (id, value, comment, charging_station_id) VALUES (?, ?, ?, ?)",
            (rating.id, rating.value, rating.comment, rating.charging_station_id),
        )
        self.conn.commit()
