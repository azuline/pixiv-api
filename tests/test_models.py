import responses

from pixivapi import Illustration
from tests import mocked_responses as mr


@responses.activate
def test_illustration_download_single_page(client, tmp_path):
    responses.add(
        responses.GET,
        mr.SINGLE_PAGE_ILLUSTRATION_DATA["meta_single_page"]["original_image_url"],
        body=b"owo",
        status=200,
    )

    illust = Illustration(**mr.SINGLE_PAGE_ILLUSTRATION_DATA, client=client)
    illust.download(tmp_path)

    filepath = tmp_path / "86044539.jpg"
    with filepath.open("rb") as fp:
        assert fp.read() == b"owo"


@responses.activate
def test_illustration_download_multiple_page(client, tmp_path):
    for image_urls in mr.MULTI_PAGE_ILLUSTRATION_DATA["meta_pages"]:
        responses.add(
            responses.GET,
            image_urls["image_urls"]["original"],
            body=b"owo",
            status=200,
        )

    illust = Illustration(**mr.MULTI_PAGE_ILLUSTRATION_DATA, client=client)
    illust.download(tmp_path)

    for i in range(2):
        filepath = tmp_path / "86979680" / f"86979680_p{i}.jpg"
        with filepath.open("rb") as fp:
            assert fp.read() == b"owo"
