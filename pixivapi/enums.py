"""
The enums package defines the constants used in this library's API.
"""

from enum import Enum


class ContentType(Enum):
    """
    This Enum represents the various types of content that are
    present on Pixiv.
    """

    ILLUSTRATION = "illust"
    MANGA = "manga"
    UGOIRA = "ugoira"
    NOVEL = "novel"


class Duration(Enum):
    """
    This Enum is used when searching Pixiv to limit the age of the
    returned results.
    """

    LAST_DAY = "within_last_day"
    LAST_WEEK = "within_last_week"
    LAST_MONTH = "within_last_month"


class RankingMode(Enum):
    """
    This Enum is used to specify which ranking list of illustrations
    should be fetched.
    """

    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    DAY_MALE = "day_male"
    DAY_FEMALE = "day_female"
    WEEK_ORIGINAL = "week_original"
    WEEK_ROOKIE = "week_rookie"
    DAY_MANGA = "day_manga"


class SearchTarget(Enum):
    """
    This Enum determines how the search should match the searched
    words to the possible results.
    """

    TAGS_PARTIAL = "partial_match_for_tags"
    TAGS_EXACT = "exact_match_for_tags"
    TITLE_AND_CAPTION = "title_and_caption"


class Size(Enum):
    """
    This Enum represents the possible sizes of an image. ``ORIGINAL``
    has the best quality.
    """

    LARGE = "large"
    MEDIUM = "medium"
    ORIGINAL = "original"
    SQUARE_MEDIUM = "square_medium"


class Sort(Enum):
    """
    This Enum determines how the search results are sorted by date;
    either oldest first or newest first.
    """

    DATE_DESC = "date_desc"
    DATE_ASC = "date_asc"


class Visibility(Enum):
    """
    This Enum represents the visibility restrictions that a Pixiv user
    can enforce on their bookmarks, followed users, etc.
    """

    PUBLIC = "public"
    PRIVATE = "private"
