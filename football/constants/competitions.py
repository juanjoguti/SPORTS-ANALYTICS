from enum import Enum, unique

@unique
class CompetitionName(str, Enum):

    Big5 = 'Big-5-European-Leagues'

    def identifiers(self):

        return 'Big5', self.value