import requests


class NotifyService:
    def __init__(self):
        self.__base_url = "https://util.devi.tools/api/v1/notify"


    def notify_by_email(self, payload: dict) -> dict:
        try:
            response = requests.post(
                self.__base_url,
                json=payload
            )
            return response.status_code
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
