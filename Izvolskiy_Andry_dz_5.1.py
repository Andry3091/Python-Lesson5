"""
Task 1
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
"""


def odd_nums(max_value):
    n = -1
    while n <= max_value:
        n += 2
        yield n


odd_to_20 = odd_nums(20)
print(next(odd_to_20))
