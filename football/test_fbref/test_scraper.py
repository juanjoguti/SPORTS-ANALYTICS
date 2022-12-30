import pytest
import pandas as pd
from unittest.mock import Mock
from utils.scraper import Scraper
from football.fbref.scraper import FbrefScraper
from football.fbref.url_builder import FBrefUrlBuilder
from football.constants.competitions import CompetitionName


@pytest.fixture
def fbref_scraper():

    return FbrefScraper(Scraper(), FBrefUrlBuilder())

@pytest.fixture
def expected_table():

    return pd.DataFrame([1, 2, 3], columns=['Test'])

@pytest.fixture
def scraper_mock(expected_table):

    mock = Mock(spec=Scraper)
    mock.get_table_by_identifier.return_value = expected_table
    yield mock

@pytest.fixture
def expected_url():

    return 'https://test_url.com'

@pytest.fixture
def fbref_url_builder_mock(expected_url):

    mock = Mock(spec=FBrefUrlBuilder)
    mock.get_players_data_url.return_value = expected_url
    yield mock

def test_scraper(fbref_scraper):

    assert isinstance(fbref_scraper.scraper, Scraper)

def test_fbref_url_builder(fbref_scraper):

    assert isinstance(fbref_scraper.fbref_url_builder, FBrefUrlBuilder)

@pytest.mark.parametrize(
    'header', [
        'Player',
        'Nationality',
        'Position',
        'Squad',
        'Competition',
        'Age',
        'Born',
        'MP',
        'Starts',
        'Min',
        '90s',
        'Gls',
        'Ast',
        'G-PK',
        'PK',
        'PKatt',
        'CrdY',
        'CrdR',
        'Gls per 90',
        'Ast per 90',
        'G+A per 90',
        'G-PK per 90',
        'G+A-PK per 90',
        'xG',
        'npxG',
        'xAG',
        'npxG+xAG',
        'xG per 90',
        'xAG per 90',
        'xG+xAG per 90',
        'npxG per 90',
        'npxG+xAG per 90',
        'Matches'
    ]
)
def test_standard_stats_headers(fbref_scraper, header):

    assert len(fbref_scraper.standard_stats_headers) == 33
    assert header in fbref_scraper.standard_stats_headers

def test_get_players_standard_stats_table(
    scraper_mock,
    fbref_url_builder_mock,
    expected_table,
    expected_url
):

    fbref_scraper = FbrefScraper(scraper_mock, fbref_url_builder_mock)

    table = fbref_scraper.get_players_standard_stats_table()

    scraper_mock.get_table_by_identifier.assert_called_once_with(
        expected_url,
        {'id': 'stats_standard'},
        fbref_scraper.standard_stats_headers
    )
    fbref_url_builder_mock.get_players_data_url.assert_called_once_with(
        CompetitionName.Big5
    )
    assert len(table) == len(expected_table)
    assert all(table.columns == expected_table.columns)