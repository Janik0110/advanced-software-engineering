from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class RatingCreated:
    station_id: UUID
    rating_value: int
    comment: str
    timestamp: datetime
