import os
import sys

from loguru import logger


class TermuxUtilities:
    @staticmethod
    @logger.catch
    def is_termux() -> bool:
        """
        Method to check if the current environment is Termux
        :return: True if the current environment is Termux, False otherwise
        """
        return 'ANDROID_ROOT' in os.environ

    @staticmethod
    @logger.catch
    def fix_dnspython() -> None:
        """Method to fix the dnspython library in Termux"""

        filepath: str = f'/data/data/com.termux/files/usr/lib/python{sys.version_info.major}.{sys.version_info.minor}/dns/resolver.py'

        if not TermuxUtilities.fix(filepath=filepath):
            filepath = f'/data/data/com.termux/files/usr/lib/python{sys.version_info.major}.{sys.version_info.minor}/site-packages/dns/resolver.py'
            TermuxUtilities.fix(filepath)

    @staticmethod
    @logger.catch
    def fix(filepath: str) -> bool:
        """
        Method to fix the dnspython library in Termux
        :param filepath: The path to the file to fix
        :return: True if the file was fixed, False otherwise
        """
        try:
            old_text: str = '/etc/resolv.conf'
            new_text: str = '/data/data/com.termux/files/usr/etc/resolv.conf'

            # Check if the file has already been modified
            with open(filepath, 'r') as f:
                if f'/data/data/com.termux/files/usr/etc/resolv.conf' in f.read():
                    return

            # Read the file and replace the old text with the new text
            with open(filepath, 'r') as file:
                lines: list = file.readlines()

            updated_lines: list = [line.replace(old_text, new_text) for line in lines]

            # Write the updated content back to the file
            with open(filepath, 'w') as file:
                file.writelines(updated_lines)

            return True

        except FileNotFoundError:
            return False
