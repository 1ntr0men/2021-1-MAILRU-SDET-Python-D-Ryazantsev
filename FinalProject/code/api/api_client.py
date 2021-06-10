import requests
from requests.cookies import cookiejar_from_dict


class WrongResponseCode(Exception):
    pass


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None

    def post_add_user(self, username, email, password):
        headers = {
            'Content-Type': "application/json",
        }

        body = {
            "username": username,
            "password": password,
            "email": email
        }

        resp = self.session.post(self.base_url + "api/add_user", headers=headers, data=body)
        return resp
        # if resp.status_code == 201:
        #     return resp
        # else:
        #     assert WrongResponseCode

    def get_user_delete(self, username):
        resp = self.session.get(self.base_url + f"api/del_user/{username}")
        if resp.status_code == 204:
            return resp.json()
        else:
            assert WrongResponseCode

    def get_block_user(self, username):
        resp = self.session.get(self.base_url + f"api/block_user/{username}")
        if resp.status_code == 200:
            return resp.json()
        else:
            assert WrongResponseCode

    def get_unblock_user(self, username):
        resp = self.session.get(self.base_url + f"api/accept_user/{username}")
        if resp.status_code == 200:
            return resp.json()
        else:
            assert WrongResponseCode

    def get_status(self):
        resp = self.session.get(self.base_url + f"status")
        if resp.status_code == 200:
            return resp.json()
        else:
            assert WrongResponseCode

    def get_auth_cookie(self):
        return self.session.cookies.get("session")
