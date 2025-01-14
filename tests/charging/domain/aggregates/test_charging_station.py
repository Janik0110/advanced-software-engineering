import uuid
import pytest

from src.charging.domain.aggregates.charging_station import ChargingStation
from src.charging.domain.value_objects.charging_station_status import (
    ChargingStationStatus,
)
from src.charging.domain.value_objects.charging_station_type import ChargingStationType
from src.charging.domain.value_objects.postal_code import PostalCode


@pytest.fixture
def charging_station():
    postal_code = PostalCode("12345")
    location = "Test Location"
    station_type = ChargingStationType.FAST_CHARGING

    return ChargingStation(uuid.uuid4(), postal_code, location, station_type)


def test_init(charging_station: ChargingStation):
    assert charging_station.id is not None
    assert charging_station.postal_code == PostalCode("12345")
    assert charging_station.location == "Test Location"
    assert charging_station.type == ChargingStationType.FAST_CHARGING
    assert charging_station.status == ChargingStationStatus.AVAILABLE


def test_is_in_postal_code(charging_station: ChargingStation):
    assert charging_station.is_in_postal_code(PostalCode("12345")) is True


def test_is_not_in_postal_code(charging_station: ChargingStation):
    assert charging_station.is_in_postal_code(PostalCode("54321")) is False


def test_update_status(charging_station: ChargingStation):
    charging_station.update_status(ChargingStationStatus.OCCUPIED)
    assert charging_station.status == ChargingStationStatus.OCCUPIED


def test_update_status_to_same_status(charging_station: ChargingStation):
    charging_station.update_status(ChargingStationStatus.AVAILABLE)
    assert charging_station.status == ChargingStationStatus.AVAILABLE
    charging_station.update_status(ChargingStationStatus.AVAILABLE)
    assert charging_station.status == ChargingStationStatus.AVAILABLE
