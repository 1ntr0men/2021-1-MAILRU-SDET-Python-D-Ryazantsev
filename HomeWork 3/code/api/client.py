import requests
from requests.cookies import cookiejar_from_dict

from files.files_path import files_path


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None

    def get_token(self):
        get_cookie = self.session.get("https://target.my.com/csrf/")
        return get_cookie.cookies.get("csrftoken")

    def post_login(self, user, password):

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            "Origin": "https://target.my.com",
            'Connection': "keep-alive",
            "Referer": "https://target.my.com/",
            "Host": "auth-ac.my.com"
        }

        data = {
            'email': user,
            'password': password,
            'continue': "https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email",
            'failure': "https://account.my.com/login/"
        }

        result = self.session.post("https://auth-ac.my.com/auth?lang=ru&nosavelogin=0", headers=headers, data=data,
                                   allow_redirects=False)

        response_cookies = result.headers['Set-Cookie'].split(';')
        mc_token = [c for c in response_cookies if 'mc' in c][0].split('=')[-1]
        ssdc_token = [c for c in response_cookies if 'ssdc' in c][0].split('=')[-1]

        self.session.cookies = cookiejar_from_dict({'mc': mc_token, 'ssdc': ssdc_token})
        self.session.get("https://target.my.com/dashboard")
        return result.cookies.get_dict()

    def post_set_image(self, size):
        headers = {
            "X-CSRFToken": self.get_token()
        }
        data = {
            'width': size,
            'height': size
        }
        files = {
            "file": open(files_path(f"{size}_{size}.jpg"), 'rb')
        }

        send_image = self.session.post("https://target.my.com/api/v2/content/static.json", headers=headers, data=data,
                                   files=files).json()
        return send_image["id"]

    def post_topic(self):
        image600 = self.post_set_image(600)
        image256 = self.post_set_image(256)
        request_payload = {"name": "Название кампании", "conversion_funnel_id": None, "objective": "traffic",
                           "enable_offline_goals": False,
                           "targetings": {"split_audience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "sex": ["male", "female"],
                                          "age": {
                                              "age_list": [0, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                                                           26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                                                           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,
                                                           56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
                                                           71, 72, 73, 74, 75], "expand": True},
                                          "geo": {"regions": [188]}, "interests_soc_dem": [], "segments": [],
                                          "interests": [],
                                          "fulltime": {"flags": ["use_holidays_moving", "cross_timezone"],
                                                       "mon": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                                               17, 18, 19, 20, 21, 22, 23],
                                                       "tue": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                                               17, 18, 19, 20, 21, 22, 23],
                                                       "wed": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                                               17, 18, 19, 20, 21, 22, 23],
                                                       "thu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                                               17, 18, 19, 20, 21, 22, 23],
                                                       "fri": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                                               17, 18, 19, 20, 21, 22, 23],
                                                       "sat": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                                               17, 18, 19, 20, 21, 22, 23],
                                                       "sun": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                                               17, 18, 19, 20, 21, 22, 23]}, "pads": [102634, 102643],
                                          "mobile_types": ["tablets", "smartphones"], "mobile_vendors": [],
                                          "mobile_operators": []}, "age_restrictions": None, "date_start": None,
                           "date_end": None, "autobidding_mode": "second_price_mean", "budget_limit_day": "1000",
                           "budget_limit": "2000", "mixing": "recommended", "utm": None, "enable_utm": True,
                           "price": "2.84", "max_price": "0",
                           "package_id": 814,
                           "banners": [{"urls": {
                               "url_slide_1": {"id": 47240277}, "url_slide_2": {"id": 47240277},
                               "url_slide_3": {"id": 47240277},
                               "header_click": {"id": 47240277}}, "textblocks": {
                               "title_25_slide_1": {"text": "Название первого слайда"},
                               "title_25_slide_2": {"text": "Заголовок второго слайда"},
                               "title_25_slide_3": {"text": "Заголовок третьего слайда"},
                               "title_25": {"text": "Заголовок объявления"},
                               "text_50": {"text": "Текст объявления"}, "cta_sites_full": {"text": "visitSite"}},
                               "content": {
                                   "image_600x600_slide_1": {"id": image600}, "image_600x600_slide_2": {"id": image600},
                                   "image_600x600_slide_3": {"id": image600}, "icon_256x256": {"id": image256}},
                               "name": ""}
                           ]
                           }

        headers = {
            "X-CSRFToken": self.get_token()
        }
        send_company = self.session.post("https://target.my.com/api/v2/campaigns.json", json=request_payload,
                                         headers=headers)
        return send_company.json()

    def get_check_company(self, id):
        companys = self.session.get("https://target.my.com/api/v2/campaigns.json?_status=active").json()
        for i in companys["items"]:
            print(i["id"])
            if i["id"] == id:
                return True
        return False

    def post_delete_company(self, id):
        request_payload = {"status": "deleted"}
        headers = {
            "X-CSRFToken": self.get_token()
        }
        print(self.session.post(f"https://target.my.com/api/v2/campaigns/{id}.json", json=request_payload,
                                headers=headers).text)

    def post_create_segment(self):

        request_payload = {"name": "Тестовый сегмент", "pass_condition": 1, "relations": [
            {"object_type": "remarketing_player", "params": {"type": "positive", "left": 365, "right": 0}}],
                           "logicType": "or"}
        headers = {
            "X-CSRFToken": self.get_token()
        }
        segment = self.session.post("https://target.my.com/api/v2/remarketing/segments.json", json=request_payload,
                                    headers=headers)
        return segment.json()["id"]

    def get_check_segment(self, id):
        segments = self.session.get(f"https://target.my.com/api/v2/remarketing/segments.json?_id={id}").json()
        return bool(segments["count"])

    def delete_segment(self, id):
        headers = {
            "X-CSRFToken": self.get_token()
        }
        self.session.delete(f"https://target.my.com/api/v2/remarketing/segments/{id}.json", headers=headers)
