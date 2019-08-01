pixiv-api
=========

A library for the Pixiv API.

Usage
=====

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
Pixiv endpoints.

The following code fetches details about an image from Pixiv's API and
downloads the image.

.. code-block:: python

   illustration = client.fetch_illustration(75523989)
   client.download(
       illustration.image_urls.large,
       f'~/my_pixiv_images/{illustration.title}.jpg',
   )

Refer to the ``Client`` section for documentation on the supported endpoints.

TODO: Stuff

Client
======

.. automodule:: pixivapi.client
    :members:

Classes
=======

TODO

Enums
=====

.. automodule:: pixivapi.enums
    :members:
    :inherited-members:
    :undoc-members:

Exceptions
==========

.. automodule:: pixivapi.errors
    :members:
    :show-inheritance:
