import unittest

from my_shell.alias_matcher import AliasMatcher
from my_shell.model.alias import Alias


class TestAliasMatcher(unittest.TestCase):

    def test_match__no_match(self):
        self.__test_match(
            aliases=[
                Alias(
                    alias_command="command", 
                    arg_matchers=[], 
                    command_template=["command", "to", "execute"],
                ),
            ],
            command=["not", "matching"],
            expected_method_to_executed=["not", "matching"],
        )

    def test_match__command_matches(self):
        self.__test_match(
            aliases=[
                Alias(
                    alias_command="command",
                    arg_matchers=["*"],
                    command_template=["command", "to", "execute"],
                ),
            ],
            command=["command", "arg"],
            expected_method_to_executed=["command", "to", "execute"],
        )

    def test_match__command_matches_with_reference(self):
        self.__test_match(
            aliases=[
                Alias(
                    alias_command="command",
                    arg_matchers=["?id?[\\w+]"],
                    command_template=["command", "to", "[id]"],
                ),
            ],
            command=["command", "execute"],
            expected_method_to_executed=["command", "to", "execute"],
        )

    def test_match__command_matches_star__multiple_args(self):
        self.__test_match(
            aliases=[
                Alias(
                    alias_command="command",
                    arg_matchers=["*"],
                    command_template=["command", "to", "execute"],
                ),
            ],
            command=["command", "arg1", "arg2"],
            expected_method_to_executed=["command", "to", "execute"],
        )

    def __test_match(self, aliases, command, expected_method_to_executed):
        commnad_to_execute = AliasMatcher(aliases).match(command)
        self.assertEqual(expected_method_to_executed, commnad_to_execute)

    def test_match_arguments__both_empty(self):
        self.__test_match_arguments(
            args_matchers=[],
            command_args=[],
            expected_matches=True,
            expected_substitution=dict(),
        )

    def test_match_arguments__star_with_empty_command(self):
        self.__test_match_arguments(
            args_matchers=["*"],
            command_args=[],
            expected_matches=True,
            expected_substitution=dict(),
        )

    def test_match_arguments__star_with_single_argument(self):
        self.__test_match_arguments(
            args_matchers=["*"],
            command_args=["a"],
            expected_matches=True,
            expected_substitution=dict(),
        )

    def test_match_arguments__star_with_multiple_arguments(self):
        self.__test_match_arguments(
            args_matchers=["*"],
            command_args=["a", "b"],
            expected_matches=True,
            expected_substitution=dict(),
        )

    def test_match_arguments__empty_matcher_with_non_empty_arguments(self):
        self.__test_match_arguments(
            args_matchers=[],
            command_args=["a"],
            expected_matches=False,
        )

    def test_match_arguments__optional_matcher_with_matching_arg(self):
        self.__test_match_arguments(
            args_matchers=["?key?[value]"],
            command_args=["value"],
            expected_matches=True,
            expected_substitution={"key": "value"},
        )

    def test_match_arguments__optional_matchers_with_not_matching_arg(self):
        self.__test_match_arguments(
            args_matchers=["?key?[value]"],
            command_args=["not_a_value"],
            expected_matches=False,
        )

    def test_match_arguments__optional_matcher_and_star_with_not_matching_arg(self):
        self.__test_match_arguments(
            args_matchers=["?key?[value]", "*"],
            command_args=["not_a_value"],
            expected_matches=True,
            expected_substitution=dict(),
        )

    def test_match_arguments__mandatory_matcher_with_matching_arg(self):
        self.__test_match_arguments(
            args_matchers=["key[value]"],
            command_args=["value"],
            expected_matches=True,
            expected_substitution={"key": "value"},
        )

    def test_match_arguments__mandatory_matcher_with_not_matching_arg(self):
        self.__test_match_arguments(
            args_matchers=["key[value]"],
            command_args=["not_a_value"],
            expected_matches=False,
        )

    def test_match_arguments__mandatory_matcher_and_star_with_not_matching_arg(self):
        self.__test_match_arguments(
            args_matchers=["key[value]", "*"],
            command_args=["not_a_value"],
            expected_matches=False,
        )

    def test_match_arguments__regex_matcher_with_matching_arg(self):
        self.__test_match_arguments(
            args_matchers=["key[.*]"],
            command_args=["value"],
            expected_matches=True,
            expected_substitution={"key": "value"},
        )

    def test_match_arguments__regex_matcher_with_not_matching_arg(self):
        self.__test_match_arguments(
            args_matchers=["key[[a-z]+]"],
            command_args=["not_a_value"],
            expected_matches=False,
        )

    def test_match_arguments__optinal_matcher_with_matching_arg_but_but_it_needs_to_be_skipped(
        self,
    ):
        self.__test_match_arguments(
            args_matchers=["?key?[value]", "[value]"],
            command_args=["value"],
            expected_matches=True,
            expected_substitution=dict(),
        )

    def __test_match_arguments(
        self,
        args_matchers,
        command_args,
        expected_matches,
        expected_substitution=None,
    ):
        matches, substitutaion = AliasMatcher.match_arguments(
            args_matchers=args_matchers,
            command_args=command_args,
        )
        self.assertEqual(expected_matches, matches)
        if expected_substitution:
            self.assertEqual(expected_substitution, substitutaion)


if __name__ == "__main__":
    unittest.main()
