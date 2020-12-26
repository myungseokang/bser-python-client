import enum
from typing import List, Optional, Dict

import requests


class BserAPIClient(object):
    """
    블랙서바이벌: 영원회귀 openapi 를 위한 클라이언트
    """
    BASE_URL = 'https://open-api.bser.io'
    api_key: Optional[str] = None
    version: Optional[str] = None

    def __init__(self, api_key: str, version: str = 'v1'):
        self.api_key = api_key
        self.version = version

    class MatchingTeamMode(enum.Enum):
        SOLO = 1
        DUO = 2
        SQUAD = 3

    @property
    def api_url(self) -> str:
        return f'{self.BASE_URL}/{self.version}'

    @property
    def header_data(self) -> dict:
        return {
            'Accept': 'application/json',
            'X-Api-Key': self.api_key,
        }

    def fetch_user_number_by_name(self, name: str) -> int:
        # TODO: 유저 이름으로 userNum 가져오기
        raise NotImplementedError()

    def fetch_user_games(self, user_number: int) -> List[dict]:
        url = f'{self.api_url}/user/games/{user_number}'
        response = requests.get(url, headers=self.header_data)
        json_resp = response.json()
        if response.status_code != 200:
            raise ValueError(json_resp.get('message', 'API Error'))

        return json_resp.get("userGames", [])

    def fetch_user_stats(self,
                         user_number: Optional[int],
                         season_id: int = 1) -> Dict:
        if not user_number:
            raise ValueError('user_number 인자가 없습니다')

        url = f'{self.api_url}/user/stats/{user_number}/{season_id}'
        response = requests.get(url, headers=self.header_data)
        json_resp = response.json()
        if response.status_code != 200:
            raise ValueError(json_resp.get('message', 'API Error'))

        return json_resp.get("userGames", [])

    def fetch_meta_data(self, meta_type: str = 'hash') -> List[dict]:
        url = f'{self.api_url}/data/{meta_type}'
        response = requests.get(url, headers=self.header_data)
        json_resp = response.json()
        if response.status_code != 200:
            raise ValueError(json_resp.get('message', 'API Error'))

        return json_resp.get("data", [])

    def fetch_rank_top(self, season_id: int = 1, matching_team_mode: int = 1) -> List[dict]:
        url = f'{self.api_url}/rank/top/{season_id}/{matching_team_mode}'
        response = requests.get(url, headers=self.header_data)
        json_resp = response.json()
        if response.status_code != 200:
            raise ValueError(json_resp.get('message', 'API Error'))

        return json_resp.get("topRanks", [])

    def fetch_rank_user(self,
                        user_number: Optional[int],
                        season_id: int = 1,
                        matching_team_mode: int = 1) -> Dict:
        if not user_number:
            raise ValueError('user_number 인자가 없습니다')

        url = f'{self.api_url}/rank/{user_number}/{season_id}/{matching_team_mode}'
        response = requests.get(url, headers=self.header_data)
        json_resp = response.json()
        if response.status_code != 200:
            raise ValueError(json_resp.get('message', 'API Error'))

        return json_resp.get("userRank", {})
