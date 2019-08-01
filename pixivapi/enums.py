from enum import Enum


class ContentType(Enum):
    ILLUSTRATIONS = 'illust'
    MANGA = 'manga'


class Duration(Enum):
    LAST_DAY = 'within_last_day'
    LAST_WEEK = 'within_last_week'
    LAST_MONTH = 'within_last_month'


class RankingMode(Enum):
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    DAY_MALE = 'day_male'
    DAY_FEMALE = 'day_female'
    WEEK_ORIGINAL = 'week_original'
    WEEK_ROOKIE = 'week_rookie'
    DAY_MANGA = 'day_manga'


class SearchTarget(Enum):
    TAGS_PARTIAL = 'partial_match_for_tags'
    TAGS_EXACT = 'exact_match_for_tags'
    TITLE_AND_CAPTION = 'title_and_caption'


class Sort(Enum):
    DATE_DESC = 'date_desc'
    DATE_ASC = 'date_asc'


class Visibility(Enum):
    PUBLIC = 'public'
    PRIVATE = 'private'
