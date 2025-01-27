from uuid import uuid4

from charging.infrastructure.repositories.charging_station_repository import (
    ChargingStationRepository,
)
from charging.application.services.charging_station_service import (
    ChargingStationService,
)

import streamlit as st

from rating.application.services.rating_service import RatingService
from rating.infrastructure.repositories.rating_repository import RatingRepository

charging_station_service = ChargingStationService(ChargingStationRepository())
rating_service = RatingService(RatingRepository())

st.title("Charging Station Search")

zip_code = st.text_input("Enter your zip code")

if st.button("Search"):
    result = charging_station_service.find_charging_station_by_postal_code(zip_code)
    stations = result.stations

    if len(stations) == 0:
        st.write("No charging stations found.")
    else:
        st.table(
            [
                {
                    "Address": str(station.location),
                    "Postal Code": str(station.postal_code.value),
                    "Type": str(station.type.value),
                    "Status": str(station.status.value),
                }
                for station in stations
            ]
        )


st.title("Rate a CS")

value = st.slider("Rate this CS", 0, 5)
comment = st.text_area("Leave a comment")

if st.button("Submit"):
    result = rating_service.create_rating(uuid4(), value, comment)

    st.write("Rating created successfully")
    st.write(result)
