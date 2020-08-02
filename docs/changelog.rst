Changelog
---------

v0.3.5
^^^^^^

- Fix issue with offset not working in `fetch_illustrations_following`.

v0.3.4
^^^^^^

- Fix issue with Python 3.6 compatibility wrt. datetime module.

v0.3.3
^^^^^^

- Fix arguments of Novel class instantiation.


v0.3.1
^^^^^^

- Fix quickstart example documentation.

v0.3.0
^^^^^^

- Update authentication in response to Pixiv's changes.

v0.2.0
^^^^^^

- Change ``Client.account`` from a dict to an ``Account`` model.
- Remove ``None`` attributes from User that only applied to responses from
  ``Client.fetch_user`` and move them to a ``FullUser`` subclass.
- Change return type of ``Client.fetch_user`` to a ``FullUser``. No attributes
  were changed.
