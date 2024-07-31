import httpx
from urllib.parse import unquote

from .api import (
    get_info_api1,
    get_last_post_api,
    search_api,
    get_explore_api,
    login_api,
    code_api,
    get_login_token_api,
    check_in_api,
    upvote_api,
    get_mate_page,
    update_mate_info_api,
)


class APIClient:
    def __init__(self):
        self.headers = {"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"}
        self.timeout = httpx.Timeout(timeout=10)

    async def _make_request(self, method, url, headers=None, params=None, json_data=None, cookies=None):
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.request(
                method=method,
                url=url,
                headers=headers or self.headers,
                params=params,
                json=json_data,
                cookies=cookies
            )
            if response.status_code == 200:
                result = response.json()
                cookies = response.cookies.jar
                cookies_dict = {cookie.name: unquote(cookie.value) for cookie in cookies}
                return result, cookies_dict
            if response.status_code == 302:
                cookies = response.cookies.jar
                cookies_dict = {cookie.name: unquote(cookie.value) for cookie in cookies}
                return {'code': 302}, cookies_dict
            return {'code': response.status_code}, {}

    async def get_info(self, UUID: str) -> dict:
        """
        通过UUID获取用户信息。

        参数:
            UUID (str): 用户的UUID。

        返回:
            dict: 包含用户信息的字典。如果请求失败，则返回默认的空信息字典。
        """
        url = get_info_api1 + UUID
        return await self._make_request('GET', url)

    async def search(self, name: str, perPage: int = 5) -> dict:
        """
        通过名称搜索用户信息。

        参数:
            name (str): 要搜索的用户名。
            perPage (int): 每页返回的结果数量。默认值为5。

        返回:
            dict: 包含搜索结果的字典。如果请求失败，则返回None。
        """
        url = search_api
        params = {"pagination[perPage]": max(perPage, 5), "filter[query]": name}
        return await self._make_request('GET', url, params=params)

    async def get_last_post(self, mateId: str, perPage: int = 5) -> dict:
        """
        通过mateId获取用户的最新动态。

        参数:
            mateId (str): 用户的mateId。
            perPage (int): 每页返回的结果数量。默认值为5。

        返回:
            dict: 包含最新动态的字典。如果请求失败，则返回None。
        """
        url = get_last_post_api
        params = {
            "sort[field]": "dtCreate",
            "sort[order]": "desc",
            "filter[mateId]": mateId,
            "pagination[perPage]": max(perPage, 5),
        }
        return await self._make_request('GET', url, params=params)

    async def get_explore_post(self, perPage: int = 5) -> dict:
        """
        获取发现页的最新动态。

        参数:
            perPage (int): 每页返回的结果数量。默认值为5。

        返回:
            dict: 包含发现页最新动态的字典。如果请求失败，则返回None。
        """
        url = get_explore_api
        params = {
            "pagination[perPage]": max(perPage, 5),
            "sort[field]": "dtCreate",
            "sort[order]": "desc",
        }
        return await self._make_request('GET', url, params=params)

    async def login(self, email: str, cookies: dict) -> dict:
        """
        登录操作

        参数:
            email (str): 用户邮箱。
            cookies (dict): 登录所需的cookies。

        返回:
            dict: 登录结果的字典。如果请求失败，则返回包含错误代码的字典。
        """
        json_data = {"email": email}
        headers = {**self.headers, "X-Xsrf-Token": cookies["XSRF-TOKEN"]}
        
        for _ in range(10):
            result, cookies_dict = await self._make_request('POST', login_api, headers=headers, json_data=json_data, cookies=cookies)
            if result['code'] != 408:  # 408 is a placeholder for timeout error
                break
        return result, cookies_dict

    async def post_code(self, email: str, code: str, cookies: dict) -> dict:
        """
        提交邮箱验证码

        参数:
            email (str): 用户邮箱。
            code (str): 验证码。
            cookies (dict): 验证所需的cookies。

        返回:
            dict: 验证结果的字典。如果请求失败，则返回包含错误代码的字典。
        """
        name = email.split("@")[0]
        json_data = {
            "email": email,
            "name": name,
            "settingDisplayLanguageId": "2",
            "settingMateLanguageId": "2",
            "token": int(code),
        }
        headers = {**self.headers, "X-Xsrf-Token": cookies["XSRF-TOKEN"]}
        return await self._make_request('POST', code_api, headers=headers, json_data=json_data, cookies=cookies)

    async def get_login_token(self) -> dict:
        """
        获取预登录token。

        返回:
            dict: 包含token的cookies字典。
        """
        return await self._make_request('GET', get_login_token_api)

    async def check_in(self, cookies: dict) -> dict:
        """
        签到操作

        参数:
            cookies (dict): 签到所需的cookies。

        返回:
            dict: 签到结果的字典。如果请求失败，则返回包含错误代码的字典。
        """
        json_data = {"coinQuestId": 1}
        headers = {**self.headers, "X-Xsrf-Token": cookies["XSRF-TOKEN"]}
        return await self._make_request('POST', check_in_api, headers=headers, json_data=json_data, cookies=cookies)

    async def get_token_by_remember(self, cookies: dict) -> dict:
        """
        通过remember获取token。

        参数:
            cookies (dict): 记住登录所需的cookies。

        返回:
            dict: 包含token的cookies字典。
        """
        headers = self.headers
        return await self._make_request('GET', get_login_token_api, headers=headers, cookies=cookies)

    async def upvote(self, emojiId: int, replyId: int, UUID: str, cookies: dict) -> dict:
        """
        点赞功能

        参数:
            emojiId (int): 表情ID。
            replyId (int): 回复ID。
            UUID (str): 用户UUID。
            cookies (dict): 点赞所需的cookies。

        返回:
            dict: 点赞结果的字典。如果请求失败，则返回包含错误代码的字典。
        """
        json_data = {"emojiId": emojiId, "replyId": replyId, "mateId": UUID}
        headers = {**self.headers, "X-Xsrf-Token": cookies["XSRF-TOKEN"]}
        return await self._make_request('POST', upvote_api, headers=headers, json_data=json_data, cookies=cookies)

    async def get_mate_page(self, cookies: dict) -> dict:
        """
        通过token获取账户mate信息

        参数:
            cookies (dict): 存有token的cookies

        返回:
            dict: 包含账户mate信息的字典。如果请求失败，则返回包含错误代码的字典。
        """
        url = get_mate_page
        headers = {**self.headers, "X-Xsrf-Token": cookies["XSRF-TOKEN"]}
        params = {
            "sort[field]": "id",
            "sort[order]": "desc",
            "pagination[page]": "1",
            "pagination[perPage]": "999"
        }
        return await self._make_request('GET', url, headers=headers, params=params, cookies=cookies)
    
    async def update_mate_info(self, name: str, UUID: str, cookies: dict) -> dict:
        # 未完善，请勿使用！
        """
        更新角色信息功能

        参数:
            name (str): 角色名称。
            UUID (str): 用户UUID。
            cookies (dict): 所需的cookies。

        返回:
            dict: 更新结果的字典。如果请求失败，则返回包含错误代码的字典。
        """
        mate_info = {
            "name": name,
            "type": "Original",
            "age": 0,
            "bio": "",
            "mediaUrl": "",
            "bannerUrl": "",
            "momentVisibility": 1,
            "profileVisibility": 1,
            "gender": 0,
            "mateToneId": 0,
            "agentEnabled": 1,
            "greeting": "",
            "summary": "",
            "personalityPrompt": "",
            "admirePermission": 3,
            "isSuperAdmireEnabled": False,
            "isNsfwBlurry": 1,
            "isNsfwVisible": 0,
            "allowSwitchToNsfwChat": 1
        }
        
        headers = {**self.headers, "X-Xsrf-Token": cookies["XSRF-TOKEN"]}
        return await self._make_request('PUT', update_mate_info_api + UUID, headers=headers, json_data=mate_info, cookies=cookies)


api_client = APIClient()