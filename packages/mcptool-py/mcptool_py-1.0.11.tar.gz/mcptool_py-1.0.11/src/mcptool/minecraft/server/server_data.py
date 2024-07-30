from typing import Union

from ezjsonpy import get_config_value
from loguru import logger
from mccolors import mcwrite

from ...minecraft.server import JavaServerData, BedrockServerData
from ...minecraft.server.mcstatus_local import MCServerData
from ...minecraft.server.mcstatusio_api import MCStatusIOAPI
from ...utilities.language.utilities import LanguageUtils as Lm


class ServerData:
    def __init__(self, target: str, bot: bool = True) -> None:
        self.target = target
        self.bot = bot

    @logger.catch
    def get_data(self) -> Union[JavaServerData, BedrockServerData, None]:
        """
        Method to get the server data from the server class.
        :return: The server data if the server is online, otherwise None
        """
        data: Union[JavaServerData, BedrockServerData, None] = None

        if get_config_value('serverDataApi') == 'serverDataApi' or get_config_value('serverDataApi') not in ['local',
                                                                                                             'mcstatus.io']:  # :TODO: Replace with None after testing
            logger.error('The serverDataApi is not set in the configuration file')
            mcwrite(Lm.get('errors.serverDataApiNotSet'))
            return None

        if get_config_value('serverDataApi') == 'local':
            data: Union[JavaServerData, BedrockServerData, None] = MCServerData(server=self.target, bot=self.bot).get()

        if get_config_value('serverDataApi') == 'mcstatus.io':
            data: Union[JavaServerData, BedrockServerData, None] = MCStatusIOAPI(target=self.target, bot=self.bot).get()

        return data
