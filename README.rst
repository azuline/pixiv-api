=========
pixiv-api
=========

|CI| |Codecov| |Docs| |PyPI|

.. |CI| image:: https://img.shields.io/github/workflow/status/azuline/pixiv-api/CI
   :target: https://github.com/azuline/pixiv-api/actions
.. |Codecov| image:: https://img.shields.io/codecov/c/github/azuline/pixiv-api?token=TJSEWBI2ZC
   :target: https://codecov.io/gh/azuline/pixiv-api
.. |Docs| image:: https://readthedocs.org/projects/pixiv-api/badge/?version=latest
   :target: https://pixiv-api.readthedocs.io/en/latest/?badge=latest
.. |PyPI| image:: https://img.shields.io/pypi/v/pixiv-api.svg
   :target: https://pypi.python.org/pypi/pixiv-api

A documented, idiomatic, and tested wrapper library around Pixiv's App API.

Supports Python versions 3.6+.

Install with:

.. code-block:: bash

   $ pip install pixiv-api

Quickstart
==========

To start making requests to the Pixiv API, instantiate a client object.

.. code-block:: python

   from pixivapi import Client

   client = Client()

The client can be authenticated to Pixiv's API in multiple ways. One is by
logging in with a username and password:

.. code-block:: python

   client.login("username", "password")

And another is with a refresh token.

.. code-block:: python

   client.authenticate("refresh_token")

Once authenticated, a refresh token can be saved for future authorizations.

.. code-block:: python

   refresh_token = client.refresh_token

After authenticating, the client can begin making requests to all of the
Pixiv endpoints. For example, the following code block downloads an
image from Pixiv.

.. code-block:: python

   from pathlib import Path
   from pixivapi import Size

   illustration = client.fetch_illustration(75523989)

   illustration.download(
       directory=Path.home() / "my_pixiv_images",
       size=Size.ORIGINAL,
   )

And the next code block downloads all illustrations of an artist.

.. code-block:: python

   from pathlib import Path
   from pixivapi import Size

   artist_id = 2188232
   directory = Path.home() / "wlop"

   response = client.fetch_user_illustrations(artist_id)

   while True:
       for illust in response["illustrations"]:
           illust.download(directory=directory, size=Size.ORIGINAL)

       if not response["next"]:
           break

       response = client.fetch_user_illustrations(
           artist_id,
           offset=response["next"],
       )

Read the full documentation at https://pixiv-api.readthedocs.io.
