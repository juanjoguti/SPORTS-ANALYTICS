import pytest
from football.fbref.scraper import FbrefScraper
from football.fbref.url_builder import FBrefUrlBuilder
from utils.scraper import Scraper

@pytest.fixture
def fbref_scraper():

    return FbrefScraper()

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

def test_get_players_standard_stats_table(fbref_scraper):

    table = fbref_scraper.get_players_standard_stats_table()
    assert len(table.columns) == 33
    assert all(table.columns == fbref_scraper.standard_stats_headers)
    assert len(table) > 2000