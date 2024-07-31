import requests
from .exceptions import InvalidQuery, DailyUsageLimitExceeded, MonthlyUsageLimitExceeded, InvalidMembership, Unauthorized

class DabomApiClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.dabomai.com"  # 실제 API의 기본 URL로 변경

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def search(self, query: str, max_results: int):
        endpoint = f"{self.base_url}/search"
        payload = {
            "query": query,
            "max_results": max_results
        }
        response = requests.post(endpoint, json=payload, headers=self._get_headers())

        if response.status_code != 200:
            if response.status_code == 401:
                raise Unauthorized("Invalid API key")
            else:
                raise Exception(f"API request failed with status code {response.status_code}")

        response_data = response.json()
        
        if response.status_code == 200:
            if not response_data['success']:
                message = response_data.get('message', '')
                if message == 'User has no membership' or message == 'You must have an active membership to search':
                    raise InvalidMembership(message)
                elif message == 'Daily limit exceeded':
                    raise DailyUsageLimitExceeded(message)
                elif message == 'Monthly limit exceeded':
                    raise MonthlyUsageLimitExceeded(message)
                else:
                    raise InvalidQuery(message)

            return {
                "success": response_data['success'],
                "message": response_data['message'],
                "query": response_data['query'],
                "results": response_data['results']
            }
