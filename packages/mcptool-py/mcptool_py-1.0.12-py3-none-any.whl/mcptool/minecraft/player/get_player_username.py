from json import JSONDecodeError
from typing import Union

import requests
from loguru import logger


class PlayerUsername:
    def __init__(self, uuid: str):
        self.uuid = uuid

    @logger.catch
    def get_username(self) -> Union[str, None]:
        """
        Method to get the username of the player
        :return: The username of the player
        """
        try:
            response: requests.Response = requests.get(
                f"https://sessionserver.mojang.com/session/minecraft/profile/{self.uuid}")

            if response.status_code != 200:
                return None

            response_json = response.json()
            return response_json['name']

        except (JSONDecodeError, KeyError, requests.exceptions.HTTPError):
            logger.error(f"Failed to get the username of the player with UUID: {self.uuid}")
            return self.uuid
