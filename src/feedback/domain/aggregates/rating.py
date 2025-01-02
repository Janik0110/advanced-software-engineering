from dataclasses import dataclass

from feedback.domain.exceptions.invalid_rating_exception import InvalidRatingException


@dataclass(frozen=True)
class Rating:
    value: int
    comment: str

    def __post_init__(self):
        if not (1 <= self.value <= 5):
            raise InvalidRatingException("Rating value must be between 1 and 5")

        if len(self.comment) > 500:
            raise InvalidRatingException("Comment is too long")
