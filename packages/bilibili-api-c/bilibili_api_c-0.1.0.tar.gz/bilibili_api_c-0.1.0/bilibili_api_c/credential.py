import requests

from .request import REQUEST_HEADERS


class BilibiliCredential:
    def __init__(self,
                 uid: Union[str, int], username: str, password: str,
                 sessdata: str, csrf: str,
                 buvid3: str = None, access_token: str = None):
        self.uid: str = str(uid)
        self.username = username
        self.password = password
        self.sessdata = sessdata
        self.csrf = csrf
        self.buvid3 = buvid3
        self.access_token = access_token

    @staticmethod
    def is_not_empty(input_value: str) -> bool:
        return input_value is not None and input_value != ""

    def get_cookie(self) -> dict:
        return_dict = {}
        if self.is_not_empty(self.sessdata):
            return_dict["SESSDATA"] = self.sessdata
        if self.is_not_empty(self.csrf):
            return_dict["bili_jct"] = self.csrf
        if self.is_not_empty(self.buvid3):
            return_dict["buvid3"] = self.buvid3
        return return_dict

    def validate(self) -> bool:
        print("Validating credential...")
        resp = requests.get("https://space.bilibili.com/", headers=REQUEST_HEADERS, cookies=self.get_cookie())
        print(resp.status_code, resp.url)
        if (resp.url == "https://passport.bilibili.com/login?gourl=https://space.bilibili.com"
                or resp.url == "https://passport.bilibili.com/pc/passport/login?gourl=https%3A%2F%2Fspace.bilibili.com"):  # will try to redirect to login page if SESSDATA is expired
            print("bilibili.com credential not valid", self.get_cookie())
            return False
        print("bilibili.com credential valid")
        return True