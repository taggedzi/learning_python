import unittest.mock
from unittest.mock import patch, call
from attributes.builtins.abs import print_abs, abs_integer, abs_float, abs_complex, abs_string


class MyTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_print_abs_no_input(self):
        with self.assertRaises(TypeError) as context:
            print_abs()
        self.assertTrue("print_abs() missing 1 required positional argument: 'output_value'", context.exception.args[0])

    def test_print_abs_no_output_value(self):
        with self.assertRaises(Exception) as context:
            print_abs(1)
        self.assertTrue(
            "print_abs() missing 1 required positional argument: 'output_value'" in context.exception.args[0])

    @patch('sys.stdout')
    def test_print_abs_passing(self, mock_stdout):
        print_abs(1, 2)
        expected = [call.write('abs(1) = 2')]
        mock_stdout.assert_has_calls(expected, any_order=True)

    @patch('sys.stdout')
    @patch('attributes.builtins.abs.separator')
    @patch('attributes.builtins.abs.random_signed_integer')
    def test_abs_integer(self, mock_rand_int, mock_sep, mock_stdout):
        mock_rand_int.side_effect = [-5, -1, 0, 1, 5, 100]

        abs_integer()

        expected_sep = [call('abs(integer) - Absolute Value - Integer')]
        mock_sep.assert_has_calls(expected_sep)

        expected_std_out = [call.write('abs(-5) = 5'),
                            call.write('abs(-1) = 1'),
                            call.write('abs(0) = 0'),
                            call.write('abs(1) = 1'),
                            call.write('abs(5) = 5'),
                            call.write('abs(100) = 100')]
        mock_stdout.assert_has_calls(expected_std_out, any_order=True)

    @patch('sys.stdout')
    @patch('attributes.builtins.abs.separator')
    @patch('attributes.builtins.abs.random_signed_float')
    def test_abs_float(self, mock_rand_float, mock_sep, mock_stdout):
        mock_rand_float.side_effect = [-5.0, -1.0, 0.0, 1.0, 5.0, 100.2]

        abs_float()

        expected_sep = [call("abs(float) - Absolute Value - Floating Point")]
        mock_sep.assert_has_calls(expected_sep)

        expected_std_out = [call.write('abs(-5.0) = 5.0'),
                            call.write('abs(-1.0) = 1.0'),
                            call.write('abs(0.0) = 0.0'),
                            call.write('abs(1.0) = 1.0'),
                            call.write('abs(5.0) = 5.0'),
                            call.write('abs(100.2) = 100.2')]
        mock_stdout.assert_has_calls(expected_std_out, any_order=True)

    @patch('sys.stdout')
    @patch('attributes.builtins.abs.separator')
    @patch('attributes.builtins.abs.random_signed_complex')
    def test_abs_float(self, mock_rand_complex, mock_sep, mock_stdout):
        mock_rand_complex.side_effect = [-5j, -1j, 0j, 1j, 5j, 100j]

        abs_complex()

        expected_sep = [call("abs(complex) - Absolute Value - Complex Numbers - Returns the absolute value of the "
                             "magnitude of the complex number.")]
        mock_sep.assert_has_calls(expected_sep)

        expected_std_out = [call.write('abs((-0-5j)) = 5.0'),
                            call.write('abs((-0-1j)) = 1.0'),
                            call.write('abs(0j) = 0.0'),
                            call.write('abs(1j) = 1.0'),
                            call.write('abs(5j) = 5.0'),
                            call.write('abs(100j) = 100.0')]
        mock_stdout.assert_has_calls(expected_std_out, any_order=True)

    @patch('sys.stdout')
    def test_print_abs_string(self, mock_stdout):
        abs_string()
        expected_std_out = [call.write('abs(string) - Absolute Value - String'),
                            call.write('Attempted to execute abs("5") and it throws a TypeError.'),
                            call.write('Strings cannot be passed to the abs function even if the contents of the '
                                       'string are numbers.'),
                            call.write('The exception message is:'),
                            call.write("bad operand type for abs(): 'str'")]
        mock_stdout.assert_has_calls(expected_std_out, any_order=True)


if __name__ == '__main__':
    unittest.main()
