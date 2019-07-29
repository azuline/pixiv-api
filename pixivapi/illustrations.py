class Illustration:

    def __init__(
        self,
        caption,
        create_date,
        height,
        id_,
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
        type_,
        user,
        visible,
        width,
        x_restrict,
    ):
        self.caption = caption
        self.create_date = create_date
        self.height = height
        self.id = id_
        self.image_urls = image_urls
        self.is_bookmarked = is_bookmarked
        self.is_muted = is_muted
        self.meta_pages = meta_pages
        self.meta_single_page = meta_single_page
        self.page_count = page_count
        self.restrict = restrict
        self.sanity_level = sanity_level
        self.series = series
        self.tags = [self.Tag(**tag) for tag in tags]
        self.title = title
        self.tools = tools
        self.total_bookmarks = total_bookmarks
        self.total_view = total_view
        self.type = type_
        self.user = self.User(**user)
        self.visible = visible
        self.width = width
        self.x_restrict = x_restrict

    class User:
        def __init__(
            self,
            account,
            id_,
            is_followed,
            name,
            profile_image_urls,
        ):
            self.account = account
            self.id = id_
            self.is_followed = is_followed
            self.name = name
            self.profile_image_urls = profile_image_urls

    class Tag:
        def __init__(self, name, translated_name):
            self.name = name
            self.translated_name = translated_name
