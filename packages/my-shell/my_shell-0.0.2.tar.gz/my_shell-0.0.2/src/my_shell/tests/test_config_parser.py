import tempfile
import unittest
import os

from ..config_parser import ConfigParser
from ..model.alias import Alias


class TestConfigParser(unittest.TestCase):
    def test_parse_config__empty_config(self):
        self.__test_parse_config(
            config="",
            expected_aliases=[],
        )

    def test_parse_config__single_alias(self):
        self.__test_parse_config(
            config="cmnd [arg1] ??[arg2] ?id1?[arg3] id2[arg4];;command to execute",
            expected_aliases=[
                Alias(
                    alias_command="cmnd",
                    arg_matchers=["[arg1]", "??[arg2]", "?id1?[arg3]", "id2[arg4]"],
                    command_template=["command", "to", "execute"],
                )
            ],
        )

    def test_parse_config__multiple_aliases(self):
        self.__test_parse_config(
            config="cmnd [arg1] ??[arg2] ?id1?[arg3] id2[arg4];;command to execute\n"
            "cmnd2 [arg1] ??[arg2] ?id1?[arg3] id2[arg4];;command to execute 2",
            expected_aliases=[
                Alias(
                    alias_command="cmnd",
                    arg_matchers=["[arg1]", "??[arg2]", "?id1?[arg3]", "id2[arg4]"],
                    command_template=["command", "to", "execute"],
                ),
                Alias(
                    alias_command="cmnd2",
                    arg_matchers=["[arg1]", "??[arg2]", "?id1?[arg3]", "id2[arg4]"],
                    command_template=["command", "to", "execute", "2"],
                ),
            ],
        )

    def test_parse_config__with_space_in_matcher(self):
        self.__test_parse_config(
            config="cmnd [arg 1] ??[arg 2] ?id1?[arg 3] id2[arg 4];;command to execute",
            expected_aliases=[
                Alias(
                    alias_command="cmnd",
                    arg_matchers=["[arg 1]", "??[arg 2]", "?id1?[arg 3]", "id2[arg 4]"],
                    command_template=["command", "to", "execute"],
                ),
            ],
        )

    def test_parse_config__with_space_in_command(self):
        self.__test_parse_config(
            config='cmnd [arg1] ??[arg2] ?id1?[arg3] id2[arg4];;command "argument with spaces"',
            expected_aliases=[
                Alias(
                    alias_command="cmnd",
                    arg_matchers=["[arg1]", "??[arg2]", "?id1?[arg3]", "id2[arg4]"],
                    command_template=["command", "argument with spaces"],
                ),
            ],
        )

    def __test_parse_config(self, config, expected_aliases):
        config_file_path = os.path.join(tempfile.gettempdir(), "tmp_config")
        with open(config_file_path, "w") as f:
            f.write(config)

        config_parser = ConfigParser(config_file_path)
        self.assertCountEqual(
            config_parser.get_aliases(),
            expected_aliases,
        )

    def test_get_next_alias_token__empty_alias(self):
        self.__test_get_next_alias_token(
            alias="",
            expected_token=None,
            expected_remaining_alias=None,
        )

    def test_get_next_alias_token__blank_alias(self):
        self.__test_get_next_alias_token(
            alias="  ",
            expected_token=None,
            expected_remaining_alias=None,
        )

    def test_get_next_alias_token__single_token__command_name(self):
        self.__test_get_next_alias_token(
            alias="command",
            expected_token="command",
            expected_remaining_alias=None,
        )

    def test_get_next_alias_token__single_token__mandatory_argument(self):
        self.__test_get_next_alias_token(
            alias="[arg]",
            expected_token="[arg]",
            expected_remaining_alias=None,
        )

    def test_get_next_alias_token__single_token__optional_argument(self):
        self.__test_get_next_alias_token(
            alias="??[arg]",
            expected_token="??[arg]",
            expected_remaining_alias=None,
        )

    def test_get_next_alias_token__single_token__optional_argument_with_id(self):
        self.__test_get_next_alias_token(
            alias="?id?[arg]",
            expected_token="?id?[arg]",
            expected_remaining_alias=None,
        )

    def test_get_next_alias_token__single_token__mandatory_argument_with_id(self):
        self.__test_get_next_alias_token(
            alias="id[arg]",
            expected_token="id[arg]",
            expected_remaining_alias=None,
        )

    def test_get_next_alias_token__single_token__star(self):
        self.__test_get_next_alias_token(
            alias="*",
            expected_token="*",
            expected_remaining_alias=None,
        )

    def test_get_next_alias_token__single_token__mandatory_argument_with_space(self):
        self.__test_get_next_alias_token(
            alias="[arg with space]",
            expected_token="[arg with space]",
            expected_remaining_alias=None,
        )

    def test_get_next_alias_token__single_token__optional_argument_with_space(self):
        self.__test_get_next_alias_token(
            alias="??[arg with space]",
            expected_token="??[arg with space]",
            expected_remaining_alias=None,
        )

    def test_get_next_alias_token__single_token__optional_argument_with_id_and_space(
        self,
    ):
        self.__test_get_next_alias_token(
            alias="?id?[arg with space]",
            expected_token="?id?[arg with space]",
            expected_remaining_alias=None,
        )

    def test_get_next_alias_token__single_token__mandatory_argument_with_id_and_space(
        self,
    ):
        self.__test_get_next_alias_token(
            alias="id[arg with space]",
            expected_token="id[arg with space]",
            expected_remaining_alias=None,
        )

    def test_get_next_alias_token__multiple_tokens__command_name_first(self):
        self.__test_get_next_alias_token(
            alias="command [arg1] ??[arg2] ?id1?[arg3] id2[arg4]",
            expected_token="command",
            expected_remaining_alias="[arg1] ??[arg2] ?id1?[arg3] id2[arg4]",
        )

    def test_get_next_alias_token__multiple_tokens__mandatory_argument_first(self):
        self.__test_get_next_alias_token(
            alias="[arg 1] ??[arg2] ?id1?[arg3] id2[arg4]",
            expected_token="[arg 1]",
            expected_remaining_alias="??[arg2] ?id1?[arg3] id2[arg4]",
        )

    def test_get_next_alias_token__multiple_tokens__optional_argument_first(self):
        self.__test_get_next_alias_token(
            alias="??[arg 1] ?id1?[arg3] id2[arg4]",
            expected_token="??[arg 1]",
            expected_remaining_alias="?id1?[arg3] id2[arg4]",
        )

    def test_get_next_alias_token__multiple_tokens__optional_argument_with_id_first(
        self,
    ):
        self.__test_get_next_alias_token(
            alias="?id[arg 1]  id2[arg4]",
            expected_token="?id[arg 1]",
            expected_remaining_alias="id2[arg4]",
        )

    def test_get_next_alias_token__multiple_tokens__mandatory_argument_with_id_first(
        self,
    ):
        self.__test_get_next_alias_token(
            alias="id[arg 1] id2[arg4]",
            expected_token="id[arg 1]",
            expected_remaining_alias="id2[arg4]",
        )

    def test_get_next_alias_token__multiple_tokens__star_first(self):
        self.__test_get_next_alias_token(
            alias="*  [arg1] ??[arg2] ?id1?[arg3] id2[arg4]",
            expected_token="*",
            expected_remaining_alias="[arg1] ??[arg2] ?id1?[arg3] id2[arg4]",
        )

    def test_get_next_alias_token__single_token__optional_argument_with_square_brackets_inside(
        self,
    ):
        self.__test_get_next_alias_token(
            alias="??[arg with [square] brackets]",
            expected_token="??[arg with [square] brackets]",
            expected_remaining_alias=None,
        )

    def test_get_next_alias_token__single_token__optional_argument_with_opening_square_brackets_with_escape(
        self,
    ):
        self.__test_get_next_alias_token(
            alias="??[arg with \\[square brackets]",
            expected_token="??[arg with \\[square brackets]",
            expected_remaining_alias=None,
        )

    def test_get_next_alias_token__single_token__optional_argument_with_closing_square_brackets_with_escape(
        self,
    ):
        self.__test_get_next_alias_token(
            alias="??[arg with square\\] brackets]",
            expected_token="??[arg with square\\] brackets]",
            expected_remaining_alias=None,
        )

    def __test_get_next_alias_token(
        self, alias, expected_token, expected_remaining_alias
    ):
        token, remaining_alias = ConfigParser.get_next_alias_token(alias)
        self.assertEqual(token, expected_token)
        self.assertEqual(remaining_alias, expected_remaining_alias)

    def test_get_next_commnad_token__empty_command(self):
        self.__test_get_next_command_token(
            command="",
            expected_token=None,
            expected_remaining_command=None,
        )

    def test_get_next_commnad_token__blank_command(self):
        self.__test_get_next_command_token(
            command="  ",
            expected_token=None,
            expected_remaining_command=None,
        )

    def test_get_next_commnad_token__single_token(self):
        self.__test_get_next_command_token(
            command="command",
            expected_token="command",
            expected_remaining_command=None,
        )

    def test_get_next_commnad_token__multiple_tokens(self):
        self.__test_get_next_command_token(
            command="command to execute",
            expected_token="command",
            expected_remaining_command="to execute",
        )

    def test_get_next_commnad_token__multiple_tokens_with_spaces(self):
        self.__test_get_next_command_token(
            command=" command  to execute ",
            expected_token="command",
            expected_remaining_command="to execute",
        )

    def test_get_next_commnad_token__multiple_tokens_with_spaces_and_quotes(self):
        self.__test_get_next_command_token(
            command='command "to execute"',
            expected_token="command",
            expected_remaining_command='"to execute"',
        )

    def test_get_next_commnad_token__multiple_tokens_with_spaces_and_quotes_and_spaces_in_quotes(
        self,
    ):
        self.__test_get_next_command_token(
            command='"arg with space" arg1 "arg 2"',
            expected_token="arg with space",
            expected_remaining_command='arg1 "arg 2"',
        )

    def test_get_next_command_token__token_with_escaped_quotes(self):
        self.__test_get_next_command_token(
            command='"arg \\"with\\" quotes"',
            expected_token='arg \\"with\\" quotes',
            expected_remaining_command=None,
        )

    def test_get_next_commnad_token__token_with_referece_to_alias(self):
        self.__test_get_next_command_token(
            command="[reference]",
            expected_token="[reference]",
            expected_remaining_command=None,
        )

    def __test_get_next_command_token(
        self, command, expected_token, expected_remaining_command
    ):
        token, remaining_command = ConfigParser.get_next_command_token(command)
        self.assertEqual(token, expected_token)
        self.assertEqual(remaining_command, expected_remaining_command)


if __name__ == "__main__":
    unittest.main()
