LOGIN_SUCCESS = {
    "access_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "device_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "expires_in": 3600,
    "refresh_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "response": {
        "access_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "device_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "expires_in": 3600,
        "refresh_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "scope": "",
        "token_type": "bearer",
        "user": {
            "account": "user_xxxxxxxx",
            "id": "12345678",
            "is_mail_authorized": True,
            "is_premium": False,
            "mail_address": "me@ema.il",
            "name": "weeaboo",
            "profile_image_urls": {
                "px_16x16": "https://i.pximg.net/user-profile/img/xxxxxxxxxxx.png",
                "px_170x170": "https://i.pximg.net/user-profile/img/xxxxxxxxxxx.png",
                "px_50x50": "https://i.pximg.net/user-profile/img/xxxxxxxxxxx.png",
            },
            "x_restrict": 2,
        },
    },
    "scope": "",
    "token_type": "bearer",
    "user": {
        "account": "user_xxxxxxxx",
        "id": "12345678",
        "is_mail_authorized": True,
        "is_premium": False,
        "mail_address": "me@ema.il",
        "name": "weeaboo",
        "profile_image_urls": {
            "px_16x16": "https://i.pximg.net/user-profile/img/xxxxxxxxxxx.png",
            "px_170x170": "https://i.pximg.net/user-profile/img/xxxxxxxxxxx.png",
            "px_50x50": "https://i.pximg.net/user-profile/img/xxxxxxxxxxx.png",
        },
        "x_restrict": 2,
    },
}

LOGIN_FAILURE = {
    "error": "invalid_grant",
    "errors": {
        "system": {
            "code": 1508,
            "message": "103:pixiv ID、some japanese runes.",
        }
    },
    "has_error": True,
}

AUTHENTICATION_SUCCESS = {
    "access_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "expires_in": 3600,
    "refresh_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "response": {
        "access_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "expires_in": 3600,
        "refresh_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "scope": "",
        "token_type": "bearer",
        "user": {
            "account": "user_xxxxxxxx",
            "id": "12345678",
            "is_mail_authorized": True,
            "is_premium": False,
            "mail_address": "me@ema.il",
            "name": "weeaboo",
            "profile_image_urls": {
                "px_16x16": "https://i.pximg.net/user-profile/img/xxxxxxxxxxx.png",
                "px_170x170": "https://i.pximg.net/user-profile/img/xxxxxxxxxxx.png",
                "px_50x50": "https://i.pximg.net/user-profile/img/xxxxxxxxxxx.png",
            },
            "x_restrict": 2,
        },
    },
    "scope": "",
    "token_type": "bearer",
    "user": {
        "account": "user_xxxxxxxx",
        "id": "12345678",
        "is_mail_authorized": True,
        "is_premium": False,
        "mail_address": "me@ema.il",
        "name": "weeaboo",
        "profile_image_urls": {
            "px_16x16": "https://i.pximg.net/user-profile/img/xxxxxxxxxxx.png",
            "px_170x170": "https://i.pximg.net/user-profile/img/xxxxxxxxxxx.png",
            "px_50x50": "https://i.pximg.net/user-profile/img/xxxxxxxxxxx.png",
        },
        "x_restrict": 2,
    },
}

AUTHENTICATION_FAILURE = {
    "error": "invalid_grant",
    "errors": {"system": {"code": 1508, "message": "Invalid refresh token"}},
    "has_error": True,
}
