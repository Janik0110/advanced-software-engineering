from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4

from rating.domain.aggregates.rating import Rating
from rating.domain.events.rating_created import RatingCreated
from rating.infrastructure.repositories.rating_repository import RatingRepository


@dataclass(frozen=True)
class RatingCreatedResult:
    rating: Rating
    event: RatingCreated


class RatingService:
    def __init__(self, repository: RatingRepository):
        self.repository = repository

    def create_rating(self, station_id: UUID, value: int, comment: str):
        rating = Rating(uuid4(), value, comment, station_id)
        self.repository.save(rating)

        event = RatingCreated(
            station_id=station_id,
            rating_value=value,
            comment=comment,
            timestamp=datetime.now(),
        )

        return RatingCreatedResult(rating, event)
