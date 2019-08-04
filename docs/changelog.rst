Changelog
---------

v0.2
^^^^

- Change ``Client.account`` from a dict to an ``Account`` model.
- Remove ``None`` attributes from User that only applied to responses from
  ``Client.fetch_user`` and move them to a ``FullUser`` subclass.
- Change return type of ``Client.fetch_user`` to a ``FullUser``. No attributes
  were changed.
