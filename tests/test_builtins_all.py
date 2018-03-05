#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest.mock
import unittest
from unittest.mock import Mock, patch, call
from src.attributes.builtins.all import print_all, all_list_with_all_good_elements, all_list_with_empty_element, main as all_main


class TestAll(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_print_all_no_input(self):
        with self.assertRaises(TypeError) as context:
            print_all()
        self.assertTrue(
            "print_all() missing 2 required positional arguments: 'input_' and 'result_'" in context.exception.args[0])

    def test_print_all_missing_1_input(self):
        with self.assertRaises(TypeError) as context:
            print_all(1)
        self.assertTrue("print_all() missing 1 required positional argument: 'result_'" in context.exception.args[0])

    @patch('sys.stdout')
    def test_print_all_passing(self, mock_print):
        print_all([1, 2], True)
        expected_print = [call.write('Running all([1, 2]) returns True')]
        mock_print.assert_has_calls(expected_print)

    @patch('src.attributes.builtins.all.separator', Mock())
    @patch('src.attributes.builtins.all.print_all')
    def test_all_list_with_all_good_elements(self, mock_print_all):
        all_list_with_all_good_elements()
        expected_print_all = [call([1, 2, 3, 4, 5, 'Cat', {'Carbon'}, ['Bacon']], True)]
        mock_print_all.assert_has_calls(expected_print_all)

    @patch('src.attributes.builtins.all.separator', Mock())
    @patch('src.attributes.builtins.all.print_all')
    def test_all_list_with_empty_element(self, mock_print_all):
        all_list_with_empty_element()
        expected_print_all = [call([1, 2, None, 4, 5], False)]
        mock_print_all.assert_has_calls(expected_print_all)

    @patch('src.attributes.builtins.all.separator', Mock())
    @patch('src.attributes.builtins.all.all_list_with_all_good_elements')
    @patch('src.attributes.builtins.all.all_list_with_empty_element')
    def test_all_main(self, mock_empty, mock_full):
        all_main()
        mock_empty.assert_called_once()
        mock_full.assert_called_once()


if __name__ == '__main__':
    unittest.main()
