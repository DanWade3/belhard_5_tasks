"""
Вычисление факториала

Факториалом числа называют произведение всех натуральных
чисел до него включительно.

Например, факториал числа 5 равен произведению 1 * 2 * 3 * 4 * 5 = 120.

Формула нахождения факториала:
n! = 1 * 2 * … * n, где n – это число, а n! – факториал этого числа.
"""



def factorial(n: int) -> int:
    if n < 1:
        raise ValueError("n must be more than 0")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == '__main__':
    assert factorial(5) == 120
    print('Решено!')
