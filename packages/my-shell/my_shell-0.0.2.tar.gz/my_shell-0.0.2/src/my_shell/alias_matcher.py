import re


class AliasMatcher:
    identifier_regexp = re.compile(r"\[([a-zA-Z_][a-zA-Z0-9_]*)\]")
    optional_arg_matcher_regexp = re.compile(r"\?([a-zA-Z_][a-zA-Z0-9_]*)?\?\[(.*)]")
    mandatory_arg_matcher_regexp = re.compile(r"([a-zA-Z_][a-zA-Z0-9_]*)?\[(.*)\]")


    def __init__(self, aliases):
        self.aliases = aliases

    def match(self, command):
        """
        Returns a command that should be executed in the terminal, after
        substituting the alias command with the actual command. If the command
        is not an alias, it returns the command as is.
        """
        command, commnad_args = command[0], command[1:]

        for alias in self.aliases:
            if command != alias.alias_command:
                continue

            matches, substitution = AliasMatcher.match_arguments(
                args_matchers=alias.arg_matchers, 
                command_args=commnad_args,
            )

            if matches:
                return [
                    self.__get_token_after_substitution(token, substitution)
                    for token in alias.command_template 
                ]

        return [command] + commnad_args

    def __get_token_after_substitution(self, token, substitution):
        match = self.identifier_regexp.fullmatch(token)
        if match:
            identifier = match.group(1)
            return substitution[identifier] if identifier in substitution else token
        return token

    @staticmethod
    def match_arguments(args_matchers, command_args):
        if len(args_matchers) == 0:
            return len(command_args) == 0, dict()

        if len(command_args) == 0 and args_matchers[0] == "*":
            return AliasMatcher.match_arguments(
                args_matchers[1:],
                command_args,
            )

        if args_matchers[0] == "*":
            matches, substitution = AliasMatcher.match_arguments(
                args_matchers[1:],
                command_args,
            )
            if matches:
                return True, substitution

            matches, substitution = AliasMatcher.match_arguments(
                args_matchers, command_args[1:]
            )
            if matches:
                return True, substitution

            return False, dict()

        if len(command_args) == 0:
            return False, dict()

        optional_match = AliasMatcher.optional_arg_matcher_regexp.fullmatch(
            args_matchers[0],
        )

        if optional_match:
            identifier = optional_match.group(1)
            regexp = re.compile(optional_match.group(2))

            if regexp.fullmatch(command_args[0]):
                matches, substitution = AliasMatcher.match_arguments(
                    args_matchers[1:],
                    command_args[1:],
                )
                if matches:
                    substitution[identifier] = command_args[0]
                    return True, substitution

            return AliasMatcher.match_arguments(
                args_matchers[1:],
                command_args,
            )

        mandatory_match = AliasMatcher.mandatory_arg_matcher_regexp.fullmatch(
            args_matchers[0],
        )
        if mandatory_match:
            identifier = mandatory_match.group(1)
            regexp = re.compile(mandatory_match.group(2))

            if regexp.fullmatch(command_args[0]):
                matches, substitution = AliasMatcher.match_arguments(
                    args_matchers[1:],
                    command_args[1:],
                )

                if matches:
                    substitution[identifier] = command_args[0]
                    return True, substitution

        return False, dict()
