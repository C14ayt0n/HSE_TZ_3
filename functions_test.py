from time import time
import unittest
import math
from functions import minimum, maximum, s, p, read_file


start_time = time()  # засечем таймер
test_data = []  # создадим список,в который считаем данные из файла
read_file('numbers.txt', test_data)


class TestFunctions(unittest.TestCase):
    def test_minimum(self):
        self.assertEqual(minimum(test_data), min(test_data))

    def test_maximum(self):
        self.assertEqual(maximum(test_data), max(test_data))

    def test_s(self):
        self.assertEqual(s(test_data), sum(test_data))

    def test_p(self):
        self.assertEqual(p(test_data), math.prod(test_data))

    def test_no_0_in_test_data(self):  # дополнительный тест, проверяющий, нет ли в файле 'numbers.txt' числа 0
        self.assertTrue(p(test_data))  # если произведение равно нулю, то число 0 есть и тест выдает ошибку


if __name__ == "__main__":
    unittest.main()

end_time = time()  # остановим таймер
time_taken = end_time - start_time  # подсчитаем время, затраченное на работу программы
print(f'Программа завершила работу за {time_taken} секунд')
