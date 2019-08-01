from datetime import datetime
from os.path import splitext

from pixivapi.enums import ContentType, Size


class User:
    """
    A model to represent a user.

    :ivar str account: Their account name
    :ivar int id: Their account ID
    :ivar str name: Their display name
    :ivar dict profile_image_urls: A dictionary of URLs for their profile
        image, mapping a `Size` enum to the URL. This will not always
        contain all sizes depending on which endpoint the user was fetched
        from. Typically it will contain `Size.MIDDLE`.
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


class Illustration:
    """
    The illustration class encapsulates an illustration and provides
    various methods for convenient fetching of related objects.

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
        self.create_date = datetime.fromisoformat(create_date)
        self.height = height
        self.id = id
        self.image_urls = {
            **{Size(s): u for s, u in image_urls.items()},
            Size.ORIGINAL: meta_single_page.get('original_image_url', None),
        }
        self.is_bookmarked = is_bookmarked
        self.is_muted = is_muted
        self.meta_pages = [
            {Size(s): u for s, u in p['image_urls'].items()}
            for p in meta_pages
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

    def download(self, directory, size=Size.LARGE, filename=None):
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
            'https://www.pixiv.net/member_illust.php?mode=medium'
            f'&illust_id={self.id}'
        )
        if self.meta_pages:
            illust_dir = directory / (filename or str(self.id))
            illust_dir.mkdir(parents=True, exist_ok=True)
            for page in self.meta_pages:
                destination = illust_dir / page[Size.ORIGINAL].split('/')[-1]
                self.client.download(
                    url=page[size],
                    destination=destination,
                    referer=referer,
                )
        else:
            ext = splitext(self.image_urls[size])
            directory.mkdir(parents=True, exist_ok=True)
            self.client.download(
                url=self.image_urls[size],
                destination=directory / f'{filename or self.id}{ext}',
                referer=referer,
            )


class Comment:
    """
    A class that encapsulates a comment.

    :ivar str comment: Content of the comment
    :ivar datetime.datetime date: Date the comment was posted
    :ivar int id: ID of the comment
    :ivar Comment parent_comment: A parent comment to this comment
        (can be ``None``)
    :ivar User user: The poster of the comment. Does not return whether
        or not the user is followed.
    """

    def __init__(self, comment, date, id, parent_comment, user, client):
        self.comment = comment
        self.date = datetime.fromisoformat(date)
        self.id = id
        self.parent_comment = Comment(
            comment=parent_comment['comment'],
            date=parent_comment['date'],
            id=parent_comment['id'],
            parent_comment={},
            user=parent_comment['user'],
            client=client,
        ) if parent_comment else None
        self.user = User(**user)
        self.client = client
