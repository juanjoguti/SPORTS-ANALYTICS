from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI, version
from typing import Union
from utils.scraper import Scraper
from football.constants.seasons import Seasons
from football.fbref.scraper import FbrefScraper
from football.fbref.url_builder import FBrefUrlBuilder


api = FastAPI()
fbref_scraper = FbrefScraper(Scraper(), FBrefUrlBuilder())

@version(1)
@api.get('/football/{season}/players')
async def get_players_data(
    season: Seasons,
    player_name: Union[str, None] = None
):

    players_data = fbref_scraper.get_players_standard_stats_table(season)
    if player_name is None:
        return players_data.to_dict()
    else:
        mask = players_data['Player'].str.contains(player_name)
        return players_data[mask].to_dict()

api = VersionedFastAPI(api, version_format='{major}', prefix_format='/v{major}')
