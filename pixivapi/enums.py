from enum import Enum


class SearchTarget(Enum):
    TAGS_PARTIAL = 'partial_match_for_tags'
    TAGS_EXACT = 'exact_match_for_tags'
    TITLE_AND_CAPTION = 'title_and_caption'


class Visibility(Enum):
    PUBLIC = 'public'
    PRIVATE = 'private'
