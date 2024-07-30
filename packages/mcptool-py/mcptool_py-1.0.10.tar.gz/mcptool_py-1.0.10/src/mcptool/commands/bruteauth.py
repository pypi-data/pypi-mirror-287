import os
import subprocess
from typing import Union

from ezjsonpy import get_config_value
from loguru import logger
from mccolors import mcwrite

from .. import MCPToolPath
from ..commands.arguments.argument_validator import ValidateArgument
from ..constants import CLI, MCPToolStrings
from ..minecraft.server import JavaServerData, BedrockServerData
from ..minecraft.server.server_data import ServerData
from ..utilities.language.utilities import LanguageUtils as Lm


class Command:
    @logger.catch
    def __init__(self):
        self.name: str = 'bruteauth'
        self.command_arguments: list = [i for i in Lm.get(f'commands.{self.name}.arguments')]
        self.passwords: list = []

    @logger.catch
    def validate_arguments(self, user_arguments: list) -> bool:
        """
        Method to validate the arguments
        :param user_arguments: list: The arguments to validate
        :return: bool: True if the arguments are valid, False otherwise
        """
        if not ValidateArgument.validate_arguments_length(
                command_name=self.name,
                command_arguments=self.command_arguments,
                user_arguments=user_arguments
        ):
            return False

        if not ValidateArgument.is_domain(domain=user_arguments[0]) and not ValidateArgument.is_ip_and_port(
                ip=user_arguments[0]) and not ValidateArgument.is_domain_and_port(domain=user_arguments[0]):
            mcwrite(Lm.get('errors.invalidServerFormat'))
            return False

        if not os.path.exists(user_arguments[3]):
            mcwrite(Lm.get('errors.invalidFile'))
            return False

        return True

    @logger.catch
    def execute(self, user_arguments: list) -> bool:
        """
        Method to execute the command
        :param user_arguments: list: The arguments to execute the command
        """
        if not self.validate_arguments(user_arguments):
            return False

        # Save user arguments
        original_target: str = user_arguments[0]
        version: str = user_arguments[1]
        username: str = user_arguments[2]
        password_file: str = user_arguments[3]

        # Get the server data
        server_data: Union[JavaServerData, BedrockServerData, None] = ServerData(target=original_target,
                                                                                 bot=False).get_data()

        if server_data is None:
            mcwrite(Lm.get('errors.serverOffline'))
            return False

        if server_data.platform != 'Java':
            mcwrite(Lm.get('errors.notJavaServer'))
            return False

        if ':' in user_arguments[0]:
            ip_address: str = original_target.split(':')[0]
            port: str = original_target.split(':')[1]

        else:
            ip_address: str = original_target
            port: str = str(server_data.port)

        # Execute the command
        mcwrite(Lm.get(f'commands.{self.name}.gettingPasswords').replace('%file%', password_file))

        # Get absolute path of the password file
        password_file = os.path.abspath(password_file)

        with open(password_file, 'r') as file:
            self.passwords = file.read().splitlines()

        # Check if the password file is empty
        if len(self.passwords) == 0:
            mcwrite(Lm.get('errors.passwordFileEmpty'))
            return False

        mcwrite(Lm.get(f'commands.{self.name}.bruteForcing')
                .replace('%ip%', original_target)
                .replace('%username%', username)
                .replace('%passwordFile%', password_file)
                .replace('%numberOfPasswords%', str(len(self.passwords)))
                )

        # Prepare and run the command
        path: str = MCPToolPath.get_path()
        spaces: str = '0' if CLI.value else MCPToolStrings.SPACES
        command: str = f'cd {path} && node scripts/brute_auth.mjs {ip_address} {port} {username} {version} {password_file} {spaces}'

        if MCPToolStrings.OS_NAME == 'windows':
            command = f'C: && {command}'

        if get_config_value('debug'):
            logger.debug(f'Bruteauth command: {command}')

        subprocess.run(command, shell=True)
        return True
