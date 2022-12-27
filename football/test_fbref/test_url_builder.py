import pytest
import requests
from utils.url_builder import UrlBuilder
from football.fbref.url_builder import FBrefUrlBuilder
from football.constants.competitions import CompetitionName


@pytest.fixture
def fbref_url_builder():

    return FBrefUrlBuilder()

def test_url_builder(fbref_url_builder):

    assert isinstance(fbref_url_builder.url_builder, UrlBuilder)
    url = fbref_url_builder.url_builder.domain_url
    assert url == 'https://fbref.com'
    assert requests.get(url).ok

def test_get_players_data(fbref_url_builder):

    assert fbref_url_builder.get_players_data_url(CompetitionName.Big5) ==\
        'https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats'
