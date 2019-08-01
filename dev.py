#!/usr/bin/env python3

import os
from pprint import pprint  # noqa

from pixivapi import Client

c = Client()

c.authenticate(os.environ['PIXRT'])

r = c.fetch_illustration_related(68656810)
pprint(r)
print(r.keys())
