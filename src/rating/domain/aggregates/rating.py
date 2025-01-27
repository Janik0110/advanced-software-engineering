from dataclasses import dataclass
from uuid import UUID

from rating.domain.exceptions.invalid_rating_exception import InvalidRatingException


@dataclass(frozen=True)
class Rating:
    id: UUID
    value: int
    comment: str

    charging_station_id: UUID

    def __post_init__(self):
        if not (1 <= self.value <= 5):
            raise InvalidRatingException("Rating value must be between 1 and 5")

        if len(self.comment) > 500:
            raise InvalidRatingException("Comment is too long")
