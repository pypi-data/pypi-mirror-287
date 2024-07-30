"""
Executable file for the MCPTool

This file is used to run the MCPTool from the command line
"""
import subprocess
import time
import base64
import shutil
import sys
import os

from mccolors import mcwrite, mcreplace


class UpdateTool:
    def __init__(self) -> None:
        pass

    def check_for_update(self) -> None:
        """Check if there is an update available for the tool"""
        from mcptool.constants.update_available import UPDATE_AVAILABLE
        from mcptool.notifications.send import SendNotification
        from mcptool.inputcustom import Input
        from mcptool.constants import URLS

        if not UPDATE_AVAILABLE:
            mcwrite('&8&l[&a&lINFO&8&l] &f&lNo updates are available for MCPTool. Starting the tool...')
            time.sleep(0.5)
            return

        if Input(
                input_message='&8&l[&a&lINFO&8&l] &f&lAn update is available for MCPTool. Do you want to update it? [y/n]: ',
                input_type='boolean'
        ).get_input() is False:
            mcwrite('&8&l[&a&lINFO&8&l] &f&lStarting the tool...')
            time.sleep(0.5)
            return

        input(mcreplace(
            "&8&l[&a&lINFO&8&l] &f&lThe update will delete the current "
            "mcptool data folder (MCPToolFiles) located at %appdata%. "
            "If you don't need to backup, press any key to continue updating."
        ))

        mcwrite('&8&l[&a&lINFO&8&l] &f&lAn update is available for MCPTool. Starting the update process...')
        SendNotification(
            title='MCPTool Update Available',
            message=f'An update is available for MCPTool. Starting the update process. Visit {URLS.MCPTOOL_WEBSITE} for more information.'
        ).send()

        if os.name != 'nt':
            mcwrite(
                '&8&l[&c&lERROR&8&l] &f&lThe update process is only available for Windows. Please visit the MCPTool website to download the latest version.')
            sys.exit(0)

        self.windows_update()

    @staticmethod
    def windows_update() -> None:
        """
        Start the update process for Windows
        """

        # Paths
        appdata_path: str = os.getenv('APPDATA')  # %appdata%
        lib_folder_path: str = os.path.abspath(os.path.join(appdata_path, 'lib'))  # %appdata%/lib
        mcptool_folder_path: str = os.path.abspath(os.path.join(appdata_path, 'MCPTool'))  # %appdata%/MCPTool
        mcptool_lib_folder_path: str = os.path.abspath(
            os.path.join(mcptool_folder_path, 'lib'))  # %appdata%/MCPTool/lib
        original_updater_path = os.path.join(mcptool_folder_path,
                                             'MCPToolUpdater.exe')  # %appdata%/MCPTool/MCPToolUpdater.exe
        updater_executable = os.path.join(appdata_path, 'MCPToolUpdater.exe')  # %appdata%/MCPToolUpdater.exe

        # Command to run the updater with elevated privileges
        command: str = f'Start-Process \'{updater_executable}\' -Verb runAs'

        # Encode the command
        encoded_command: str = base64.b64encode(command.encode('utf-16le')).decode('utf-8')

        # Command to run the updater with elevated privileges and encoded command
        command = f'powershell -EncodedCommand {encoded_command}'

        # Copy ./lib and *.dll python files to the %APPDATA% folder
        mcwrite(r'&8&l[&a&lINFO&8&l] &f&lCopying the lib folder and .dll files to the %APPDATA% folder...')

        if os.path.exists(lib_folder_path):
            shutil.rmtree(lib_folder_path)

        shutil.copytree(mcptool_lib_folder_path, lib_folder_path)  # Copy the lib folder to %appdata%

        for file in os.listdir(mcptool_folder_path):  # Copy the .dll files to %appdata%
            if file.endswith('.dll'):
                if 'python' in file:
                    if os.path.exists(os.path.join(appdata_path, file)):
                        os.remove(os.path.join(appdata_path, file))

                    shutil.copyfile(os.path.join(mcptool_folder_path, file), os.path.join(appdata_path, file))

        # Copy the updater to the %APPDATA% folder
        if os.path.exists(updater_executable):
            os.remove(updater_executable)

        shutil.copyfile(original_updater_path, updater_executable)

        # Run the updater
        mcwrite(f'&8&l[&a&lINFO&8&l] &f&lThe updater has been copied to the %APPDATA% folder. Running the updater...')
        subprocess.run(command, shell=True)
        sys.exit(0)


if __name__ == '__main__':
    from mcptool.__main__ import main
    from mcptool.constants import CLI

    if not CLI.value:
        mcwrite('&8&l[&a&lINFO&8&l] &f&lChecking for updates...')
        UpdateTool().check_for_update()

    main()
