from enum import Enum


class Duration(Enum):
    LAST_DAY = 'within_last_day'
    LAST_WEEK = 'within_last_week'
    LAST_MONTH = 'within_last_month'


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
