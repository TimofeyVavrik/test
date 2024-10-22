import random
import sys
from typing import List

def is_prime(x: int) -> bool:
    """Функция проверки простоты числа x."""
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    sqrt_x = int(x ** 0.5) + 1
    for i in range(3, sqrt_x, 2):
        if x % i == 0:
            return False
    return True

def primes(count: int) -> List[int]:
    """Функция генерации списка из первых count простых чисел."""
    primes_list = []
    num = 2
    while len(primes_list) < count:
        if is_prime(num):
            primes_list.append(num)
        num += 1
    return primes_list

def checksum(x: List[int]) -> int:
    """Функция расчёта контрольной суммы списка чисел x."""
    result = 0
    for elem in x:
        result = (result + elem) * 113
        result = result % 10000007
    return result

def pipeline() -> int:
    """Функция, выполняющая все требуемые действия и возвращающая контрольную сумму."""
    # Шаг 1: Генерация списка из 1000 первых простых чисел
    prime_numbers = primes(1000)

    # Шаг 2: Перемешивание списка с использованием seed = 100
    random.seed(100)
    random.shuffle(prime_numbers)

    # Шаг 3: Вычисление контрольной суммы полученного списка
    result = checksum(prime_numbers)
    return result

if __name__ == "__main__":
    # Проверяем, что переданы два аргумента командной строки
    if len(sys.argv) != 3:
        print("Использование: python script.py <количество_простых_чисел> <seed>")
        sys.exit(1)

    try:
        number_of_primes = int(sys.argv[1])
        seed_value = int(sys.argv[2])
    except ValueError:
        print("Оба аргумента должны быть целыми числами.")
        sys.exit(1)

    # Вызываем pipeline с заданными параметрами
    shuffled_primes = pipeline(number_of_primes, seed_value)

    # Печатаем список полученных чисел по одному в строке
    for prime in shuffled_primes:
        print(prime)