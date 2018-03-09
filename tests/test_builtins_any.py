#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock, patch, call
from src.attributes.builtins.any import any_list_with_a_single_non_falsy_value
from src.attributes.builtins.any import any_list_with_all_falsy_values
from src.attributes.builtins.any import main as any_main


class TestAny(unittest.TestCase):

    @patch('sys.stdout')
    def test_any_list_with_a_single_non_falsy_value(self, mock_print):
        any_list_with_a_single_non_falsy_value()
        expected_call = [call.write("True")]
        mock_print.assert_has_calls(expected_call, any_order=True)

    @patch('sys.stdout')
    def test_any_list_with_all_falsy_values(self, mock_print):
        any_list_with_all_falsy_values()
        expected_call = [call.write("False")]
        mock_print.assert_has_calls(expected_call, any_order=True)

    @patch('src.attributes.builtins.all.separator', Mock())
    @patch('src.attributes.builtins.any.any_list_with_a_single_non_falsy_value')
    @patch('src.attributes.builtins.any.any_list_with_all_falsy_values')
    def test_main(self, mock_all_false, mock_mostly_false):
        any_main()
        mock_all_false.assert_called_once()
        mock_mostly_false.assert_called_once()


if __name__ == "__main__":
    # execute only if run as a script
    unittest.main()
