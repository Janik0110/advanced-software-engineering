import pytest

from src.charging.domain.exceptions.InvalidPostalCodeException import (
    InvalidPostalCodeException,
)
from src.charging.domain.value_objects.postal_code import PostalCode


def is_valid_postal_code(value: str):
    assert PostalCode(value).value == value


def is_invalid_postal_code(value: str):
    with pytest.raises(InvalidPostalCodeException):
        PostalCode(value)


@pytest.mark.parametrize("value", ["12345", "54321", "00000", "99999"])
def test_valid_postal_code(value: str):
    """Test valid postal code"""
    is_valid_postal_code(value)


@pytest.mark.parametrize("value", ["12A45", "5432", "0000", "999999"])
def test_invalid_postal_code(value: str):
    """Test invalid postal code"""
    is_invalid_postal_code(value)
