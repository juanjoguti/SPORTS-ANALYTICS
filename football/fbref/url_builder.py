from utils.url_builder import UrlBuilder
from football.constants.seasons import Seasons
from football.constants.competitions import CompetitionName


class FBrefUrlBuilder():

    def __init__(self, url_builder: UrlBuilder = UrlBuilder('fbref')):

        self.__url_builder = url_builder

    @property
    def url_builder(self):

        return self.__url_builder

    def __path_to_players_data(
        self,
        season: Seasons,
        competition_name: CompetitionName
    ):

        short_name, full_name = competition_name.identifiers()
        return f'en/comps/{short_name}/{season}/stats/players/{season}-{full_name}-Stats'

    def get_players_data_url(self, season: Seasons, competition_name: CompetitionName):

        path_to_players_data = self.__path_to_players_data(season, competition_name)
        return self.url_builder.get_url_to_path(path_to_players_data)
