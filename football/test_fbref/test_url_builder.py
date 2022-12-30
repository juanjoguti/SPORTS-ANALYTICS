import pytest
import requests
from unittest.mock import Mock
from utils.url_builder import UrlBuilder
from football.constants.seasons import Seasons
from football.fbref.url_builder import FBrefUrlBuilder
from football.constants.competitions import CompetitionName


@pytest.fixture
def expected_url():

    return 'https://test_url.com'

@pytest.fixture
def url_builder_mock(expected_url):

    mock = Mock(spec=UrlBuilder)
    mock.get_url_to_path.return_value = expected_url
    yield mock

@pytest.fixture
def expected_2223_big5_path():

    season = Seasons.S2223
    short_name, full_name = CompetitionName.Big5.identifiers()
    return f'en/comps/{short_name}/{season}/stats/players/{season}-{full_name}-Stats'

def test_url_builder():

    fbref_url_builder = FBrefUrlBuilder()
    assert isinstance(fbref_url_builder.url_builder, UrlBuilder)
    url = fbref_url_builder.url_builder.domain_url
    assert url == 'https://fbref.com'
    assert requests.get(url).ok

def test_get_players_data(url_builder_mock, expected_url, expected_2223_big5_path):

    fbref_url_builder = FBrefUrlBuilder(url_builder_mock)

    url = fbref_url_builder.get_players_data_url(Seasons.S2223, CompetitionName.Big5)
    
    assert url == expected_url
    url_builder_mock.get_url_to_path.assert_called_once_with(expected_2223_big5_path)
