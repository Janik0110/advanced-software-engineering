from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class RatingCreated:
    station_id: str
    rating_value: int
    comment: str
    timestamp: datetime
