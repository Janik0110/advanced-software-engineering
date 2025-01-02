from dataclasses import dataclass

from charging.domain.exceptions.InvalidPostalCodeException import (
    InvalidPostalCodeException,
)


@dataclass(frozen=True)
class PostalCode:
    value: str

    def __post_init__(self):
        if not self._is_valid():
            raise InvalidPostalCodeException(self.value)

    def _is_valid(self) -> bool:
        return len(self.value) == 5 and self.value.isdigit()
