import pytest

from src.rating.domain.exceptions.invalid_rating_exception import InvalidRatingException
from src.rating.domain.aggregates.rating import Rating


def is_valid_rating(value: int, comment: str):
    assert Rating(value, comment).value == value
    assert Rating(value, comment).comment == comment


def is_invalid_rating(value: int, comment: str):
    with pytest.raises(InvalidRatingException):
        Rating(value, comment)


@pytest.mark.parametrize("value, comment", [(1, "Good"), (5, "Bad")])
def test_valid_rating(value: int, comment: str):
    """Test valid rating"""
    is_valid_rating(value, comment)


@pytest.mark.parametrize("value, comment", [(0, "Good"), (6, "Bad"), (1, "a" * 501)])
def test_invalid_rating(value: int, comment: str):
    """Test invalid rating"""
    is_invalid_rating(value, comment)
