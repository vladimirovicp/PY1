import unittest


class TestCase(unittest.TestCase):
    def test_check_indentation(self):
        try:
            from task import main
        except IndentationError as e:
            raise AssertionError(
                "Проверьте, что все инструкции внутри функции установлены на уровне одного отступа."
            ) from e
