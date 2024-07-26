"""Tests for dedicated geocoding function."""

from typing import Union

import pytest
from osmnx.geocoder import geocode_to_gdf

from quackosm import geocode_to_geometry
from quackosm._exceptions import QueryNotGeocodedError


@pytest.mark.parametrize(  # type: ignore
    "query",
    [
        "Vatican",
        "Monaco",
        "Poland",
        ["United Kingdom", "Greater London"],
        ["Madrid", "Barcelona", "Seville"],
    ],
)
def test_geocoding(query: Union[str, list[str]]) -> None:
    """Test if geocoding works the same as osmnx."""
    assert geocode_to_gdf(query).unary_union.equals(geocode_to_geometry(query))


@pytest.mark.parametrize(  # type: ignore
    "query",
    [
        "Broadway",
        "nonexistent_query",
        ["Poland", "Broadway"],
    ],
)
def test_geocoding_errors(query: Union[str, list[str]]) -> None:
    """Test if geocoding throws error for two wrong queries."""
    with pytest.raises(QueryNotGeocodedError):
        geocode_to_geometry(query)
