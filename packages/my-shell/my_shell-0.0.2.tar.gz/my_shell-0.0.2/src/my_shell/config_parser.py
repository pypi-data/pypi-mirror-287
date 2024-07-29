import re

from my_shell.model.alias import Alias


class ConfigParser:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config = self.__parse_config()

    def get_aliases(self):
        return self.config

    def __parse_config(self):
        with open(self.config_file_path) as f:
            config_lines = f.readlines()

        return [self.__process_config_line(line) for line in config_lines]

    def __process_config_line(self, line):
        alias, command = line.split(";;")
        alias_command, arg_matchers = ConfigParser.get_next_alias_token(alias)
        return Alias(
            alias_command=alias_command,
            arg_matchers=list(self.__arg_matchers(arg_matchers)),
            command_template=list(self.__split_command(command)),
        )

    def __arg_matchers(self, alias):
        while alias:
            token, alias = ConfigParser.get_next_alias_token(alias)
            if token:
                yield token

    @staticmethod
    def get_next_alias_token(alias):
        """
        Assumes that the alias is correct.
        FIXME: there's need to add a verifying function for the above
          assumption.
        """
        alias = alias.strip()
        if not alias:
            return None, None

        commnad_name_regexp = re.compile(r"^\s*(([a-zA-Z0-9][a-zA-Z0-9_]*)|(\*))(\s|$)")
        match = commnad_name_regexp.match(alias)
        if match:
            token = match.group().strip()
            rest = alias.replace(match.group(), "", 1).strip()
            return (
                ConfigParser.__stripped_string_or_none(token),
                ConfigParser.__stripped_string_or_none(rest),
            )

        index = 0
        index = alias.find("[")
        number_of_open_brackets = 1
        index += 1
        while number_of_open_brackets > 0:
            if alias[index] == "\\":
                index += 1
            elif alias[index] == "[":
                number_of_open_brackets += 1
            elif alias[index] == "]":
                number_of_open_brackets -= 1
            index += 1

        return (
            ConfigParser.__stripped_string_or_none(alias[:index]),
            ConfigParser.__stripped_string_or_none(alias[index:]),
        )

    def __split_command(self, command):
        while command:
            token, command = ConfigParser.get_next_command_token(command)
            if token:
                yield token

    @staticmethod
    def get_next_command_token(command):
        command = command.strip()
        if not command:
            return None, None

        comand_token_with_quotes_regexp = re.compile(
            r'^"((\\")|([^"]))*"',
        )
        match = comand_token_with_quotes_regexp.match(command)
        if match:
            token = match.group().strip()
            rest = command.replace(match.group(), "", 1).strip()
            return (
                ConfigParser.__stripped_string_or_none(token)[1:-1],
                ConfigParser.__stripped_string_or_none(rest),
            )

        comand_token_without_quotes_regexp = re.compile(
            r"^([a-zA-Z0-9][a-zA-Z0-9_]*)|(\[[a-zA-Z0-9][a-zA-Z0-9_]*\])",
        )
        match = comand_token_without_quotes_regexp.match(command)
        token = match.group().strip()
        rest = command.replace(match.group(), "", 1).strip()
        return (
            ConfigParser.__stripped_string_or_none(token),
            ConfigParser.__stripped_string_or_none(rest),
        )

    @staticmethod
    def __stripped_string_or_none(string):
        stripped = string.strip()
        return stripped if stripped else None
