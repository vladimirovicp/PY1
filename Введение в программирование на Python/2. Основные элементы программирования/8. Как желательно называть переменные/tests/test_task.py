import unittest

import task


class TestCase(unittest.TestCase):
    def test_seconds_in_day(self):
        assert hasattr(task, 'SECONDS_IN_DAY'), (
            'Убедитесь, что название константы с количеством секунд в одном дне записано согласно заданию.'
        )
        expected = 24 * 60 * 60
        assert task.SECONDS_IN_DAY == expected, (
            'Убедитесь, что количество секунд в одном дне, посчитано верно.'
        )

    def test_total_seconds_in_ten_days(self):
        assert hasattr(task, 'total_seconds_in_ten_days'), (
            'Убедитесь, что название переменной с количеством секунд в десяти днях записано согласно заданию.'
        )
        seconds_in_day = 24 * 60 * 60
        count_days = 10
        expected = count_days * seconds_in_day
        assert task.total_seconds_in_ten_days == expected, (
            'Убедитесь, что выражение, которое считает количество секунд в десяти днях, записано верно.'
        )
