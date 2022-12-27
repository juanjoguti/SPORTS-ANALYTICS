from utils.url_builder import UrlBuilder
from football.constants.competitions import CompetitionName


class FBrefUrlBuilder():

    def __init__(self):

        self.__url_builder = UrlBuilder('fbref')

    @property
    def url_builder(self):

        return self.__url_builder

    def __path_to_players_data(self, competition_name: CompetitionName):

        short_name, full_name = competition_name.identifiers()
        return f'en/comps/{short_name}/stats/players/{full_name}-Stats'

    def get_players_data(self, competition_name: CompetitionName):

        path_to_players_data = self.__path_to_players_data(competition_name)
        return self.url_builder.get_url_to_path(path_to_players_data)
