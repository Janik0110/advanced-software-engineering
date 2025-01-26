from uuid import uuid4

import pytest
from unittest.mock import MagicMock, patch

from src.charging.domain.value_objects.charging_station_type import ChargingStationType
from src.charging.domain.value_objects.postal_code import PostalCode
from src.charging.domain.aggregates.charging_station import ChargingStation
from src.charging.infrastructure.repositories.charging_station_repository import (
    ChargingStationRepository,
)


@pytest.fixture
@patch("sqlite3.connect")
def mock_repo(mock_connect):
    """Fixture to provide a mocked ChargingStationRepository."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor
    return ChargingStationRepository(), mock_conn, mock_cursor


def test_repository_should_open_connection_on_init(mock_repo):
    """Test that the repository initializes the connection and cursor."""
    repo, mock_conn, _ = mock_repo

    assert repo.conn is not None
    assert repo.cursor is not None
    mock_conn.cursor.assert_called_once()


def test_repository_should_find_charging_stations_by_postal_code(mock_repo):
    """Test finding charging stations by postal code."""
    repo, _, mock_cursor = mock_repo

    postal_code = PostalCode("10117")
    mock_cursor.fetchall.return_value = [
        ("10117", "FAST_CHARGING", uuid4(), "Hauptstraße", "1"),
        ("10117", "NORMAL", uuid4(), "Hauptstraße", "2"),
    ]

    stations = repo.find_by_postal_code(postal_code)

    # Verify SQL execution
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM charging_stations WHERE postal_code LIKE ?",
        (postal_code.value,),
    )

    # Verify returned stations
    assert len(stations) == 2
    assert all(isinstance(station, ChargingStation) for station in stations)
    assert stations[0].postal_code.value == "10117"
    assert stations[0].location == "Hauptstraße 1"
    assert stations[0].type == ChargingStationType.FAST_CHARGING


def test_repository_should_return_empty_list_when_no_charging_stations_found(mock_repo):
    """Test that the repository returns an empty list when no stations are found."""
    repo, _, mock_cursor = mock_repo

    postal_code = PostalCode("00000")
    mock_cursor.fetchall.return_value = []

    stations = repo.find_by_postal_code(postal_code)

    # Verify SQL execution
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM charging_stations WHERE postal_code LIKE ?",
        (postal_code.value,),
    )

    # Verify no stations found
    assert len(stations) == 0


def test_repository_should_handle_database_errors_gracefully(mock_repo):
    """Test that the repository raises an exception on database errors."""
    repo, _, mock_cursor = mock_repo

    postal_code = PostalCode("10117")
    mock_cursor.execute.side_effect = Exception("Database error")

    with pytest.raises(Exception, match="Database error"):
        repo.find_by_postal_code(postal_code)

    # Verify SQL execution attempted
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM charging_stations WHERE postal_code LIKE ?",
        (postal_code.value,),
    )
