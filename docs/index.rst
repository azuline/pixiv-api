pixiv-api documentation
-----------------------

A library for the Pixiv API.

Usage
-----

The library can be found on PyPI as ``pixiv-api``.

To access the Pixiv API, instantiate a client object.

.. code-block:: python

   from pixivapi import Client

   client = Client()

The client can be authenticated to Pixiv's API in multiple ways. One is by
logging in with a username and password:

.. code-block:: python

   client.login('username', 'password')

And another is with a refresh token.

.. code-block:: python

   client.authorize('refresh_token')

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
       directory=Path.home() / 'my_pixiv_images',
       size=Size.LARGE,
   )

And the next code block downloads all illustrations of an artist.

.. code-block:: python

   from pathlib import Path
   from pixivapi import Size

   artist_id = 2188232
   directory = Path.home() / 'wlop'

   response = client.fetch_user_illustrations(artist_id)
   for illust in response['illustrations']:
       illust.download(directory=directory, size=Size.LARGE)

       if response['next']:
           response = client.fetch_user_illustrations(
               artist_id,
               offset=response['next'],
           )
       else:
           break

Refer to the `Client` section for documentation on the supported
endpoints and the `Models` section for documentation on model
functionality.

TODO: Stuff

Client
------

.. automodule:: pixivapi.client
    :members:

Models
------

.. automodule:: pixivapi.models
    :members:

Enums
-----

.. automodule:: pixivapi.enums
    :members:
    :inherited-members:
    :undoc-members:

Exceptions
----------

.. automodule:: pixivapi.errors
    :members:
    :show-inheritance:
