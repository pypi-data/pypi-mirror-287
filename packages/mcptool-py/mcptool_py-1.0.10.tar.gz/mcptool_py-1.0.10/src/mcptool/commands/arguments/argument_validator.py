import socket

from ezjsonpy import get_languages
from loguru import logger
from mccolors import mcwrite

from ...utilities.language.utilities import LanguageUtils as Lm


class ValidateArgument:
    @staticmethod
    @logger.catch
    def validate_arguments_length(command_name: str, command_arguments: list, user_arguments: list) -> bool:
        """
        Method to validate the length of the arguments
        :param command_name: The name of the command
        :param command_arguments: Command arguments
        :param user_arguments: User arguments
        :return: True if the arguments are valid, False otherwise
        """

        for i in range(0, len(command_arguments)):
            try:
                user_arguments[i]

            except IndexError:
                error_message: str = Lm.get('commands.missingArguments')
                arguments_message: str = ''

                for argument_valid in command_arguments[:i]:
                    arguments_message += f'&a{argument_valid} '

                for argument_invalid in command_arguments[i:]:
                    arguments_message += f'&c&n{argument_invalid}&r '

                # Add the name of the command
                error_message = error_message.replace('%command%', command_name)

                # Add th arguments
                error_message = error_message.replace('%arguments%', arguments_message)

                # Print the error message
                mcwrite(error_message)
                return False

        return True

    @staticmethod
    @logger.catch
    def is_domain(domain: str) -> bool:
        """
        Method to validate if a string is a domain
        :param domain: The domain
        :return: True if the domain is valid, False otherwise
        """
        if ValidateArgument.is_ip_address(domain):
            return False

        try:
            socket.gethostbyname(domain)
            return True

        except socket.gaierror:
            return False

    @staticmethod
    @logger.catch
    def is_domain_and_port(domain: str) -> bool:
        """
        Method to validate if a string is a domain and port
        :param domain: The domain and port
        :return: True if the domain and port is valid, False otherwise
        """
        if ':' not in domain:
            return False

        domain_parts: list = domain.split(':')

        if len(domain_parts) != 2:
            return False

        domain: str = domain_parts[0]
        port: str = domain_parts[1]

        if not domain or not port:
            return False

        if not ValidateArgument.is_domain(domain):
            return False

        try:
            port: int = int(port)

            if port < 0 or port > 65535:
                return False

        except ValueError:
            return False

        return True

    @staticmethod
    @logger.catch
    def is_ip_address(ip: str) -> bool:
        """
        Method to validate if a string is an IP address
        :param ip: The IP address
        :return: True if the IP address is valid, False otherwise
        """
        ip_parts: list = ip.split('.')

        if len(ip_parts) != 4:
            return False

        for part in ip_parts:
            try:
                part: int = int(part)

                if part < 0 or part > 255:
                    return False

            except ValueError:
                return False

        return True

    @staticmethod
    @logger.catch
    def is_ip_and_port(ip: str) -> bool:
        """
        Method to validate if a string is an IP and port
        :param ip: The IP and port
        :return: True if the IP and port is valid, False otherwise
        """
        if ':' not in ip:
            return False

        ip_parts: list = ip.split(':')

        if len(ip_parts) != 2:
            return False

        ip_address: str = ip_parts[0]
        port: str = ip_parts[1]

        if not ip_address or not port:
            return False

        try:
            port: int = int(port)

            if port < 0 or port > 65535:
                return False

        except ValueError:
            return False

        ip_parts: list = ip_address.split('.')

        if len(ip_parts) != 4:
            return False

        for part in ip_parts:
            try:
                part: int = int(part)

                if part < 0 or part > 255:
                    return False

            except ValueError:
                return False

        return True

    @staticmethod
    @logger.catch
    def is_port_range_py_method(port_range: str) -> bool:
        """
        Method to validate if a string is a port range for the py method
        :param port_range: The port range
        :return: True if the port range is valid, False otherwise
        """
        if '-' not in port_range:
            if not port_range.isnumeric():
                return False

            if int(port_range) < 0 or int(port_range) > 65535:
                return False

            return True

        # Split the port range into start and end
        start, end = port_range.split('-')

        try:
            start: int = int(start)
            end: int = int(end)

            if start < 0 or start > 65535 or end < 0 or end > 65535:
                return False

            if start > end:
                return False

        except ValueError:
            return False

        return True

    @staticmethod
    @logger.catch
    def is_seeker_subcommand(subcommand: str) -> bool:
        """
        Method to validate if a string is a seeker subcommand
        :param subcommand: The subcommand
        :return: True if the subcommand is valid, False otherwise
        """
        if subcommand not in ['token', 'servers']:
            return False

        return True

    @staticmethod
    @logger.catch
    def is_scan_method(method: str) -> bool:
        """
        Method to validate if a string is a scanner method
        :param method: The scanner method
        :return: True if the scanner method is valid, False otherwise
        """
        if method not in ['nmap', 'qubo', 'masscan', 'py']:
            return False

        return True

    @staticmethod
    @logger.catch
    def is_yes_no(value: str) -> bool:
        """
        Method to validate if a string is a yes or no value
        :param value: The value
        :return: True if the value is valid, False otherwise
        """
        if value not in ['y', 'n']:
            return False

        return True

    @staticmethod
    @logger.catch
    def is_proxy_type(proxy_type: str) -> bool:
        """
        Method to validate if a string is a proxy type
        :param proxy_type: The proxy type
        :return: True if the proxy type is valid, False otherwise
        """
        if proxy_type not in ['waterfall', 'velocity']:
            return False

        return True

    @staticmethod
    @logger.catch
    def is_velocity_forwading_mode(mode: str) -> bool:
        """
        Method to validate if a string is a velocity forwarding mode
        :param mode: The velocity forwarding mode
        :return: True if the velocity forwarding mode is valid, False otherwise
        """
        if mode not in ['none', 'legacy', 'bungeeguard', 'modern']:
            return False

        return True

    @staticmethod
    @logger.catch
    def is_valid_language(language: str) -> bool:
        """
        Method to validate if a string is a valid language
        :param language: The language
        :return: True if the language is valid, False otherwise
        """
        if language not in get_languages():
            return False

        return True

    @staticmethod
    @logger.catch
    def is_valid_settings_name(settings_name: str) -> bool:
        """
        Method to validate if a string is a valid settings name
        :param settings_name: The settings name
        :return: True if the settings name is valid, False otherwise
        """
        if settings_name not in [
            'settings',
            'nordify',
            'scanner',
            'proxy',
            'mcserver-scrapper',
            'bruteforce_settings',
            'sendcmd_settings',
            'velocity'
        ]:
            return False

        return True
