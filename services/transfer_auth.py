import requests

class TransferAuthService:
    def __init__(self):
        self.__base_url = 'https://util.devi.tools/api/v2/authorize'

    def authorized_transfer(self) -> dict:
        response = requests.get(self.__base_url).json()
        return response

