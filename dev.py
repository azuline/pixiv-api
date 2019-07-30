#!/usr/bin/env python3

import os
from pprint import pprint  # noqa

from pixivapi import Client
from pixivapi.common import _struct_to_dict

c = Client()

# c.login('def', 'abc')
c.authenticate(os.environ['PIXRT'])

r = c.search_illustrations('aeolian')

pprint(_struct_to_dict(r))
