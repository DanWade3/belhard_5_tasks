"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать программу, которая будет выводить количество четных и нечетных значений
в списке из целых чисел

even - четные
odd - нечетные
"""


def calc_even_odd(array: list) -> tuple:
    even, odd = 0, 0
    for i in range(len(array)):
        if array[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


if __name__ == '__main__':
    assert calc_even_odd([2, 1, 5, 4, 7]) == (2, 3)
    print('Решено!')
