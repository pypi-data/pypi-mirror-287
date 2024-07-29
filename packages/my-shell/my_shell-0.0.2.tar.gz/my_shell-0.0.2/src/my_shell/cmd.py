import sys
import os
import subprocess

from my_shell.alias_matcher import AliasMatcher
from my_shell.config_parser import ConfigParser


CONFIG_PATH = os.path.join(os.environ["HOME"], ".config/my-shell/config.cfg")
ALIASES_PATH = os.path.join(os.environ["HOME"], ".config/my-shell/aliases")


def decorate_with_dev_config():
    """
    Overwrites the config path for the development mode. In the development mode
    the config file is located in the `venv/bin/.config/my-shell/` directory
    where `venv` is the location of the active python virtual environment.
    """
    from pathlib import Path

    global CONFIG_PATH
    global ALIASES_PATH
    CONFIG_PATH = Path(sys.argv[0]).parent.absolute() / ".config/my-shell/config.cfg"
    ALIASES_PATH = Path(sys.argv[0]).parent.absolute() / ".config/my-shell/aliases"


def refresh_config():
    """
    FIXME: aliases_path is not the best name for that. In this context it describes
           a file that is supposed to be imported from .zshrc file and includes
           alliases for ms commands in that way, the user does not need to write
           `ms command` in the terminal all the time and can type just `command`
           instead
    """
    shell_aliases = {
         f'alias {alias.alias[0]}="ms {alias.alias[0]}"'
         for alias in ConfigParser(CONFIG_PATH).get_aliases()
    }
    with open(ALIASES_PATH, "w") as f:
        f.write("\n".join(shell_aliases))


def main():
    try:
        if len(sys.argv) > 1 and sys.argv[1] == "refresh":
            refresh_config()
            return

        command = sys.argv[1:]
        aliases = ConfigParser(CONFIG_PATH).get_aliases()
        command_to_execute = AliasMatcher(aliases).match(command)
        
        command_result = subprocess.run(
            command_to_execute,
            capture_output=True,
        )

        sys.stderr.write(command_result.stderr.decode())
        sys.stdout.write(command_result.stdout.decode())
        exit(command_result.returncode)
    except Exception as e:
        sys.stderr.write("An error in my-shell occurred.")
        exit(1)

def main_dev():
    decorate_with_dev_config()
    main()


if __name__ == "__main__":
    main()
