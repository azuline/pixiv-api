#!/usr/bin/env python3

import os
from pprint import pprint  # noqa

from pixivapi import Client, Duration, SearchTarget, Sort
from pixivapi.common import _struct_to_dict

c = Client()

# c.login('un', 'password')
c.authenticate(os.environ['PIXRT'])

"""
r = c.search_illustrations(
    'flowers',
    search_target=SearchTarget.TITLE_AND_CAPTION,
    sort=Sort.DATE_ASC,
    # duration=Duration.LAST_MONTH,
    # offset=5,
)

pprint(_struct_to_dict(r))
print(r.illusts[0].title)
"""
