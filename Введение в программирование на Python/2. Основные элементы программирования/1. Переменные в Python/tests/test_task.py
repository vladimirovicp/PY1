import unittest

import task


class TestCase(unittest.TestCase):
    def test_variable(self):
        variable_name = 'some_variable'
        assert hasattr(task, variable_name), (
            f'Убедитесь, что в файле `task.py` объявлена переменная `{variable_name}`'
        )

        expected = 'Hello, World!'
        actual = task.some_variable
        assert actual == expected, (
            f'Убедитесь, что значение переменной `{variable_name}` установлено согласно заданию.'
        )
