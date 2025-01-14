from dataclasses import dataclass
from datetime import datetime

from rating.domain.aggregates.rating import Rating
from rating.domain.events.rating_created import RatingCreated


@dataclass(frozen=True)
class RatingCreatedResult:
    rating: Rating
    event: RatingCreated


class RatingService:
    def __init__(self, repository: RatingRepository):
        self.repository = repository

    def create_rating(self, station_id: str, value: int, comment: str):
        rating = Rating(value, comment)
        self.repository.save(rating)

        event = RatingCreated(
            station_id=station_id,
            rating_value=value,
            comment=comment,
            timestamp=datetime.now(),
        )

        return RatingCreatedResult(rating, event)
