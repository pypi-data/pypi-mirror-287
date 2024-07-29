from typing import Optional, Generator
import logging

import requests

from .credential import BilibiliCredential
from .data_types import BilibiliVideoDetailCreativeCenter
from .request import REQUEST_HEADERS


class BilibiliCreativeCenter:
    def __init__(self, credential: BilibiliCredential,
                 logger: logging.Logger = logging.getLogger("bilibili_api_c")
                 ):
        self.credential = credential
        self.requests_session = requests.Session()
        self.logger = logger

    def _get_request(self, url: str, params: dict, use_credential: bool = True) -> requests.Response:
        return self.requests_session.get(url=url, params=params, cookies=self.credential.get_cookie() if url.find("bilibili.com") > 0 and use_credential else {}, headers=REQUEST_HEADERS)

    def _post_request(self, url: str, params: dict, data: dict, use_credential: bool = True) -> requests.Response:
        return self.requests_session.post(url=url, params=params, data=data, cookies=self.credential.get_cookie() if url.find("bilibili.com") > 0 and use_credential else {}, headers=REQUEST_HEADERS)

    def get_videos_by_page(self, page_number: int = 1) -> Optional[list[BilibiliVideoDetailCreativeCenter]]:
        resp = self._get_request(url="https://member.bilibili.com/x/web/archives",
                                 params={"status": "pubed", "pn": page_number, "ps": 10, "coop": 1, })
        if resp.status_code >= 400:
            self.logger.error(f"got status code {resp.status_code} from {resp.url}")
            return None

        try:
            response_json = resp.json()
        except ValueError:
            self.logger.error("unable to decode json")
            return None

        print(response_json)
        if response_json["code"] != 0:
            self.logger.error(f"got error code {response_json['code']} {response_json['message']}")
            return None

        return_list: list[BilibiliVideoDetailCreativeCenter] = []
        try:
            for each_video in response_json["data"]["arc_audits"]:
                # print(each_video)
                return_list.append(BilibiliVideoDetailCreativeCenter(
                    aid=each_video["Archive"]["aid"],
                    bvid=each_video["Archive"]["bvid"],
                    title=each_video["Archive"]["title"],
                    description=each_video["Archive"]["desc"],
                    tags=each_video["Archive"]["tag"],
                    duration=each_video["Archive"]["duration"],
                    copyright=each_video["Archive"]["copyright"],
                    source=each_video["Archive"]["source"],
                    ptime=each_video["Archive"]["ptime"],
                    ctime=each_video["Archive"]["ctime"],
                    zone_id=each_video["Archive"]["tid"],
                    zone_name=each_video["typename"],
                    subtitle_count=each_video["captions_count"],
                ))
            # END for
        except KeyError:
            self.logger.error("unable to find parse arc_audits (KeyError)")
            return None
        return return_list

    def get_videos_generator(self, page_limit: int = 10) -> Generator[BilibiliVideoDetailCreativeCenter, None, None]:
        for page_number in range(1, page_limit + 1):
            video_list = self.get_videos_by_page(page_number=page_number)
            if video_list is None:
                self.logger.error(f"Failed to get video list from page {page_number}")
                return
            for video in video_list:
                yield video
            # END for
            self.logger.info(f"Page {page_number} done")
        # END for
