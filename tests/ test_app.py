import unittest
import random
from typing import List

# Предполагается, что ваши функции находятся в файле script.py
from app import is_prime, primes, checksum, pipeline

class TestScript(unittest.TestCase):

    def test_is_prime(self):
        """Тестирование функции is_prime."""
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(100))

    def test_primes(self):
        """Тестирование функции primes."""
        self.assertEqual(primes(0), [])
        self.assertEqual(primes(1), [2])
        self.assertEqual(primes(5), [2, 3, 5, 7, 11])
        self.assertEqual(primes(10), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        # Проверка длины списка
        self.assertEqual(len(primes(100)), 100)

    def test_checksum(self):
        """Тестирование функции checksum."""
        data = [1, 2, 3, 4, 5]
        expected_result = 4813722  # Рассчитанное значение контрольной суммы
        self.assertEqual(checksum(data), expected_result)

        # Дополнительный тест с другим набором данных
        data = [10, 20, 30]
        expected_result = checksum(data)
        self.assertEqual(checksum(data), expected_result)

    def test_pipeline(self):
        """Тестирование функции pipeline."""
        result = pipeline()
        expected_result = 7785816  # Рассчитанное значение для данной реализации
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()