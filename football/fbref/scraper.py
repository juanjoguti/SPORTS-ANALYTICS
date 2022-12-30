from utils.scraper import Scraper
from football.fbref.url_builder import FBrefUrlBuilder
from football.constants.competitions import CompetitionName


class FbrefScraper():

    def __init__(self, scraper: Scraper, fbref_url_builder: FBrefUrlBuilder):
        
        self.__scraper = scraper
        self.__fbref_url_builder = fbref_url_builder

    @property
    def scraper(self):

        return self.__scraper

    @property
    def fbref_url_builder(self):

        return self.__fbref_url_builder

    @property
    def standard_stats_headers(self):

        return [
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
    
    def get_players_standard_stats_table(self):

        return self.scraper.get_table_by_identifier(
            self.fbref_url_builder.get_players_data_url(CompetitionName.Big5),
            {'id': 'stats_standard'},
            self.standard_stats_headers
        )
