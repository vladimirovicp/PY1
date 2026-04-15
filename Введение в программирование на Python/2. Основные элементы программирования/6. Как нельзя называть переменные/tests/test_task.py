import unittest

import task


class TestCase(unittest.TestCase):
    def test_underscore_(self):

        variable_name = 'False_'
        assert hasattr(task, variable_name), (
            f'Убедитесь, что в файле `task.py` ключевому слову `False` был добавлен символ нижнего подчеркивания.'
        )
