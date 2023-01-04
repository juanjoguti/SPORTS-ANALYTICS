import pytest
import pandas as pd
from utils.scraper import Scraper


@pytest.fixture
def scraper():

    return Scraper()


@pytest.fixture
def url():

    return 'https://www.skysports.com/premier-league-table'


@pytest.fixture
def identifier():

    return {'class': 'standing-table__table'}


@pytest.fixture
def headers():

    return ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6']


def test_get_table_by_identifier_when_headers_are_unknown_and_have_one_level(
    scraper, url, identifier, headers
):

    table = scraper.get_table_by_identifier(url, identifier)
    assert len(table) == 20
    assert all(table.columns == headers)

def test_get_table_by_identifier_when_headers_are_unknown_and_have_multiple_levels(scraper):

    table = scraper.get_table_by_identifier(
        'https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats',
        {'id': 'compare_standard'}
    )
    assert len(table) == 5
    assert isinstance(table.columns, pd.MultiIndex)


def test_get_table_by_identifier_when_headers_are_known(
    scraper, url, identifier, headers
):

    table = scraper.get_table_by_identifier(url, identifier, headers)
    assert len(table) == 20
    assert all(table.columns == headers)
