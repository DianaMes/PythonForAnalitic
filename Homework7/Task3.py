# Задача 3. Палиндром
# Используя модуль collections, реализуйте функцию can_be_poly, которая
# принимает на вход строку и проверяет, можно ли получить из неё палиндром.
# Пример кода:
# print(can_be_poly('abcba'))
# print(can_be_poly('abbbc'))
# Результат:
# True
# False
# Подсказка № 1
# Перед реализацией функции can_be_poly, импортируйте модуль Counter из пакета
# collections. Он понадобится для подсчета частоты вхождения каждого символа в
# строку. Counter поможет создать частотный словарь, который упрощает подсчет и
# анализ символов в строке.
# Подсказка № 2
# Для проверки, можно ли получить палиндром, вычислите количество символов с
# нечетной частотой. Используйте функцию filter и лямбда-функцию для фильтрации
# значений частот, оставляя только те, которые имеют нечетное количество вхождений.
# Подсказка № 3
# Подсчитайте количество элементов в отфильтрованном списке и проверьте, что их
# количество меньше 2. Это условие указывает на то, что строка может быть
# переставлена в палиндром.

from collections import Counter


def can_be_poly(val: str) -> bool:
    # Создаем счетчик частот символов в строке
    char_counts = Counter(val)

    # Проверяем количество символов с нечетным количеством вхождений
    odd_count = len(list(filter(lambda x: x % 2, char_counts.values())))
    # Условие для проверки возможности формирования палиндрома
    return odd_count < 2


print(can_be_poly("eerru"))  # Ожидаемый результат: True
print(can_be_poly("abbcba"))  # Ожидаемый результат: True
print(can_be_poly("abbbc"))  # Ожидаемый результат: False
