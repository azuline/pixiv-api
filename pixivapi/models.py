"""
The models package contains dataclasses that wrap entities returned
from Pixiv's API.
"""

from os.path import splitext

from pixivapi.common import parse_timestamp
from pixivapi.enums import ContentType, Size


class User:
    """
    A model that represents a user. Not all instance variables
    will be populated; the variables that are populated depends
    on the endpoint that the user is fetched from.

    Typically, the ``profile_image_urls`` dict will contain a ``'medium'``
    key.

    :ivar str account: Their account name
    :ivar int id: Their account ID
    :ivar str name: Their display name
    :ivar dict profile_image_urls: A dictionary of URLs for their profile
        image. The keys are the size and the value is the URL.
    :ivar bool is_followed: If the user is followed. If the endpoint
        does not return this (e.g. comments), it will be ``None``.
    """

    def __init__(
        self,
        account,
        id,
        name,
        profile_image_urls,
        is_followed=None,
    ):
        self.account = account
        self.id = id
        self.name = name
        self.profile_image_urls = profile_image_urls
        self.is_followed = is_followed

    def __repr__(self):
        return f"<User id={self.id} name={self.name}>"


class Account(User):
    """
    A model for the authenticating user that inherits from ``User``.
    The properties present in the ``User`` model are also present here.

    The profile images have the sizes 16x16, 50x50, 170x170.

    :ivar str mail_address: The user's email
    :ivar bool is_premium: Whether or not user has Pixiv premium
    :ivar int x_restrict: User's x restriction
    :ivar bool is_mail_authorized: Whether user's email was authorized
    """

    def __init__(
        self,
        profile_image_urls,
        account,
        id,
        name,
        mail_address,
        is_premium,
        x_restrict,
        is_mail_authorized,
    ):
        super().__init__(account, id, name, profile_image_urls)
        self.mail_address = mail_address
        self.is_premium = is_premium
        self.x_restrict = x_restrict
        self.is_mail_authorized = is_mail_authorized

    def __repr__(self):
        return f"<Account id={self.id} name={self.name}>"


class FullUser(User):
    """
    This model inherits the properties that the ``User`` model has.

    :ivar str comment: The comment on the user's account. Only provided
        when fetching user via ``Client.fetch_user``.
    :ivar dict profile: Profile information fetched from the
        ``Client.fetch_user`` endpoint. Example below.

        .. code-block:: python

           {
               'address_id': 01,
               'background_image_url': None,
               'birth': '',
               'birth_day': '01-01',
               'birth_year': 0,
               'country_code': 'CN',
               'gender': '',
               'is_premium': True,
               'is_using_custom_profile_image': True,
               'job': 'Something',
               'job_id': 1,
               'pawoo_url': (
                   'https://pawoo.net/oauth_authentications/123?provider=pixiv'
               ),
               'region': 'China',
               'total_follow_users': 0,
               'total_illust_bookmarks_public': 1,
               'total_illust_series': 0,
               'total_illusts': 0,
               'total_manga': 0,
               'total_mypixiv_users': 0,
               'total_novel_series': 0,
               'total_novels': 0,
               'twitter_account': 'twittername',
               'twitter_url': 'https://twitter.com/twittername',
               'webpage': 'https://webpage.com'
           }

    :ivar dict profile_publicity: A dictionary detailling which parts
        of the user's profile are public and which are private. Only
        provided from the ``Client.fetch_user`` endpoint. Example below.

        .. code-block:: python

           {
               'birth_day': 'public',
               'birth_year': 'public',
               'gender': 'public',
               'job': 'public',
               'pawoo': True,
               'region': 'public'
           }

    :ivar dict workspace: A dictionary containing information about the
        user's workspace. Only provided from the ``Client.fetch_user``
        endpoint. Example below.

        .. code-block:: python

           {
               'chair': '',
               'comment': '',
               'desk': '',
               'desktop': '',
               'monitor': '',
               'mouse': '',
               'music': '',
               'pc': '',
               'printer': '',
               'scanner': '',
               'tablet': '',
               'tool': '',
               'workspace_image_url': None
           }
    """

    def __init__(
        self,
        account,
        id,
        name,
        profile_image_urls,
        is_followed=None,
        comment=None,
        profile=None,
        profile_publicity=None,
        workspace=None,
    ):
        super().__init__(account, id, name, profile_image_urls, is_followed)
        self.comment = comment
        self.profile = profile
        self.profile_publicity = profile_publicity
        self.workspace = workspace

    def __repr__(self):
        return f"<FullUser id={self.id} name={self.name}>"


class Illustration:
    """
    The illustration models encapsulates an illustration and provides
    methods for convenient fetching of related objects.

    :ivar str caption: Caption
    :ivar datetime.datetime create_date: Creation date
    :ivar int height: Height
    :ivar int id: ID
    :ivar dict image_urls: A dict of Image URLs mapping the Size enum
        to the URL. If the image has multiple pages, `Size.ORIGINAL`
        will be None.
    :ivar bool is_bookmarked: If the image is bookmarked.
    :ivar bool is_muted: If the image is muted.
    :ivar list meta_pages: If the image has multiple
        images, list this will be a list of dicts mapping the Size
        enum to image urls. If not, this will be an empty list.
    :ivar int page_count: The number of pages.
    :ivar int restrict: The restriction.
    :ivar int sanity_level: The sanity level.
    :ivar series: If the illustration is in a series, this will be a dict
        with the ``id`` and ``title`` key/value pairs of the series.
        If the illustration is not in a series, this will be ``None``.
    :ivar list tags: A list of dicts containing two keys: ``name``
        and ``translated_name``. The ``translated_name`` will be
        ``None`` if the client language is not set.
    :ivar str title: The title of the work.
    :ivar list tools: The listed tools used to create the illustration.
    :ivar int total_bookmarks: The number of times the illustration has
        been bookmarked.
    :ivar int total_view: The number of times the illustration has been viewed.
    :ivar ContentType type: The content type (illustration, manga).
    :ivar User user: The artist of the image.
    :ivar bool visible: The visibility.
    :ivar int width: The width of the illustration.
    :ivar int x_restrict: The x restrict.
    :ivar Client client: The client used to fetch the image information.
    :ivar int total_comments: The total number of comments on the illustration.
        This value may be ``None`` depending on which method this illustration
        was fetched from. For example, this value is not returned when
        searching illustrations.
    """

    def __init__(
        self,
        caption,
        create_date,
        height,
        id,
        image_urls,
        is_bookmarked,
        is_muted,
        meta_pages,
        meta_single_page,
        page_count,
        restrict,
        sanity_level,
        series,
        tags,
        title,
        tools,
        total_bookmarks,
        total_view,
        type,
        user,
        visible,
        width,
        x_restrict,
        client=None,
        total_comments=None,
    ):
        self.caption = caption
        self.create_date = parse_timestamp(create_date)
        self.height = height
        self.id = id
        self.image_urls = {
            **{Size(s): u for s, u in image_urls.items()},
            Size.ORIGINAL: meta_single_page.get("original_image_url", None),
        }
        self.is_bookmarked = is_bookmarked
        self.is_muted = is_muted
        self.meta_pages = [
            {Size(s): u for s, u in p["image_urls"].items()} for p in meta_pages
        ]
        self.page_count = page_count
        self.restrict = restrict
        self.sanity_level = sanity_level
        self.series = series
        self.tags = tags
        self.title = title
        self.tools = tools
        self.total_bookmarks = total_bookmarks
        self.total_view = total_view
        self.type = ContentType(type)
        self.user = User(**user)
        self.visible = visible
        self.width = width
        self.x_restrict = x_restrict
        self.client = client
        self.total_comments = total_comments

    def __repr__(self):
        return f"<Illustration id={self.id} user={self.user.name}>"

    def download(self, directory, size=Size.ORIGINAL, filename=None):
        """
        Download the illustration to the desired directory. If the
        illustration has multiple pages, a folder will be created and
        the images placed inside.

        :param pathlib.Path directory: The illustration will be downloaded
            to this directory.
        :param Size size: The size of the image to download.
        :param filename: Do not include the file extension. This will be
            the filename of a single-page illustration and the folder name
            of a multi-page illustration. By default this will be the
            ID of the illustration.

        :raises requests.RequestException: If the request fails.
        :raises FileNotFoundError: If the destination's directory does
            not exist.
        :raises PermissionError: If the destination cannot be written to.
        """
        referer = (
            "https://www.pixiv.net/member_illust.php?mode=medium"
            f"&illust_id={self.id}"
        )
        if self.meta_pages:
            illust_dir = directory / (filename or str(self.id))
            illust_dir.mkdir(parents=True, exist_ok=True)
            for page in self.meta_pages:
                destination = illust_dir / page[Size.ORIGINAL].split("/")[-1]
                self.client.download(
                    url=page[size],
                    destination=destination,
                    referer=referer,
                )
        else:
            ext = splitext(self.image_urls[size])[1]
            directory.mkdir(parents=True, exist_ok=True)
            self.client.download(
                url=self.image_urls[size],
                destination=directory / f"{filename or self.id}{ext}",
                referer=referer,
            )


class Novel:
    """
    A model that encapsulates a novel.

    :ivar str caption: Caption
    :ivar datetime.datetime create_date: Creation date
    :ivar int id: ID
    :ivar dict image_urls: A dict of Image URLs mapping the Size enum
        to the URL. There is no ``Size.ORIGINAL``.
    :ivar bool is_bookmarked: If the novel is bookmarked.
    :ivar bool is_muted: If the novel is muted.
    :ivar bool is_mypixiv_only: If the novel is mypixiv only.
    :ivar bool is_x_restricted: If the novel is X restricted.
    :ivar bool is_original: If the novel is an original.
    :ivar int page_count: The number of pages.
    :ivar int restrict: The restriction.
    :ivar series: If the novel is in a series, this will be a dict
        with the ``id`` and ``title`` key/value pairs of the series.
        If the novel is not in a series, this will be ``None``.
    :ivar list tags: A list of dicts containing three keys: ``name``,
        ``translated_name``, and ``added_by_uploaded_user``.
        The ``translated_name`` will be ``None`` if the client language
        is not set.
    :ivar int text_length: The length of the novel.
    :ivar str title: The title of the novel.
    :ivar int total_bookmarks: The number of times the novel has been
        bookmarked.
    :ivar int total_comments: The total number of comments on the novel.
    :ivar int total_view: The number of times the novel has been viewed.
    :ivar User user: The author of the novel.
    :ivar bool visible: The visibility.
    :ivar int x_restrict: The X restrict.
    :ivar Client client: The client used to fetch the novel information.
    """

    def __init__(
        self,
        caption,
        create_date,
        id,
        image_urls,
        is_bookmarked,
        is_muted,
        is_mypixiv_only,
        is_x_restricted,
        is_original,
        page_count,
        restrict,
        series,
        tags,
        text_length,
        title,
        total_bookmarks,
        total_comments,
        total_view,
        user,
        visible,
        x_restrict,
        client=None,
    ):
        self.caption = caption
        self.create_date = parse_timestamp(create_date)
        self.id = id
        self.image_urls = {Size(s): u for s, u in image_urls.items()}
        self.is_bookmarked = is_bookmarked
        self.is_muted = is_muted
        self.is_mypixiv_only = is_mypixiv_only
        self.is_x_restricted = is_x_restricted
        self.is_original = is_original
        self.page_count = page_count
        self.restrict = restrict
        self.series = series
        self.tags = tags
        self.text_length = text_length
        self.title = title
        self.total_bookmarks = total_bookmarks
        self.total_comments = total_comments
        self.total_view = total_view
        self.user = User(**user)
        self.visible = visible
        self.x_restrict = x_restrict
        self.client = client

    def __repr__(self):
        return f"<Novel id={self.id} user={self.user.name}>"


class Comment:
    """
    A model that encapsulates a comment.

    :ivar str comment: Content of the comment
    :ivar datetime.datetime date: Date the comment was posted
    :ivar int id: ID of the comment
    :ivar Comment parent_comment: A parent comment to this comment
        (can be ``None``)
    :ivar User user: The poster of the comment. Does not return whether
        or not the user is followed.
    """

    def __init__(self, comment, date, id, parent_comment, user, client=None):
        self.comment = comment
        self.date = parse_timestamp(date)
        self.id = id
        self.parent_comment = (
            Comment(
                comment=parent_comment["comment"],
                date=parent_comment["date"],
                id=parent_comment["id"],
                parent_comment={},
                user=parent_comment["user"],
                client=client,
            )
            if parent_comment
            else None
        )
        self.user = User(**user)
        self.client = client

    def __repr__(self):
        return f"<Comment id={self.id} user={self.user.name}>"
