from enum import Enum, unique


@unique
class Seasons(str, Enum):

    S2223 = '2022-2023'
    S2122 = '2021-2022'
    S2021 = '2020-2021'
    S1920 = '2019-2020'
    S1819 = '2018-2019'
