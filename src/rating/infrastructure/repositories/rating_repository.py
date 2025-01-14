from rating.domain.aggregates.rating import Rating


class RatingRepository:
    def save(self, rating: Rating):
        raise NotImplementedError
