from typing import Union

from loguru import logger
from mccolors import mcwrite

from ...minecraft.server import JavaServerData, BedrockServerData
from ...utilities.language.utilities import LanguageUtils as Lm


class Messages:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_server_message(server_data: Union[JavaServerData, BedrockServerData]) -> str:
        """
        Method to get the server message
        :param server_data: The server data
        :return: The server message
        """
        server_message: str = f'''
{Lm.get('commands.server.ip_and_port').replace('%ip%', server_data.ip_address).replace('%port%', str(server_data.port))}
{Lm.get('commands.server.motd').replace('%motd%', server_data.motd)}
{Lm.get('commands.server.version').replace('%version%', server_data.version)}
{Lm.get('commands.server.protocol').replace('%protocol%', str(server_data.protocol))}
{Lm.get('commands.server.connected').replace('%connectedPlayers%', str(server_data.connected_players)).replace('%maxPlayers%', str(server_data.max_players))}'''

        if isinstance(server_data, JavaServerData):
            if server_data.players:
                server_message += f'''
{Lm.get('commands.server.playerList').replace('%playerList%', server_data.players)}'''

            if server_data.mod:
                server_message += f'''
{Lm.get('commands.server.mod').replace('%mod%', server_data.mod)}
{Lm.get('commands.server.modList').replace('%modList%', str(server_data.mods))}'''

        elif isinstance(server_data, BedrockServerData):
            if server_data.brand:
                server_message += f'''
{Lm.get('commands.server.brand').replace('%brand%', server_data.brand)}'''

            if server_data.map:
                server_message += f'''
{Lm.get('commands.server.map').replace('%map%', server_data.map)}'''

            if server_data.gamemode:
                server_message += f'''
{Lm.get('commands.server.gamemode').replace('%gamemode%', server_data.gamemode)}'''

        if server_data.ping:
            server_message += f'''
{Lm.get('commands.server.ping').replace('%ping%', str(server_data.ping))}'''

        server_message += f'''
{Lm.get('commands.server.bot').replace('%bot%', str(server_data.bot_output))}'''

        return server_message


class ShowMinecraftServer:
    @staticmethod
    @logger.catch
    def show(server_data: Union[JavaServerData, BedrockServerData]) -> None:
        """
        Method to show the server data
        :param server_data: The server data
        """
        server_message: str = Messages.get_server_message(server_data)
        mcwrite(server_message)
