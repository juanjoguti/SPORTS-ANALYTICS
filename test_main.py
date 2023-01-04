import pytest
import pandas as pd
from main import api
from fastapi.testclient import TestClient
from football.constants.seasons import Seasons


client = TestClient(api)


@pytest.fixture
def url():

    return f'/v1/football/{Seasons.S2223}/players'


def test_get_players_data_without_params(url):

    response = client.get(url)
    assert response.status_code == 200
    data = pd.DataFrame.from_dict(response.json())
    assert len(data.columns) == 33
    assert len(data) > 2000


def test_get_players_data_with_params(url):

    response = client.get(url, params={'player_name': 'Mbappé'})
    assert response.status_code == 200
    data = pd.DataFrame.from_dict(response.json())
    assert len(data.columns) == 33
    assert len(data) == 1
