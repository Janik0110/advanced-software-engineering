from uuid import uuid4

import pytest
from unittest.mock import MagicMock, patch
from src.rating.domain.aggregates.rating import Rating
from src.rating.infrastructure.repositories.rating_repository import RatingRepository


@pytest.fixture
@patch("sqlite3.connect")
def mock_repo(mock_connect):
    """Fixture to provide a mocked RatingRepository instance."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor
    return RatingRepository(), mock_conn, mock_cursor


def test_repository_should_open_connection_on_init(mock_repo):
    """Test that the repository initializes the connection and cursor."""
    repo, mock_conn, _ = mock_repo

    assert repo.conn is not None
    assert repo.cursor is not None
    mock_conn.cursor.assert_called_once()


def test_save_rating(mock_repo):
    """Test the save method of RatingRepository."""
    repo, mock_conn, mock_cursor = mock_repo

    # Create a sample Rating object
    rating = Rating(id=uuid4(), value=5, comment="Great!", charging_station_id=uuid4())

    # Call the save method
    repo.save(rating)

    # Assert the cursor's execute method was called with the correct query and parameters
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO ratings (id, value, comment, charging_station_id) VALUES (?, ?, ?, ?)",
        (rating.id, rating.value, rating.comment, rating.charging_station_id),
    )

    # Assert the commit method was called on the connection
    mock_conn.commit.assert_called_once()


def test_repository_initialization(mock_repo):
    """Test that the RatingRepository initializes correctly."""
    repo, mock_conn, _ = mock_repo

    # Assert the connection is established
    mock_conn.cursor.assert_called_once()
