# Задание 1. Новые списки
# Даны три списка:
# 1. floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# 2. names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# 3. numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
# Напишите код, который создаёт три новых списка. Вот их содержимое:
# 1. Каждое число из списка floats возводится в третью степень и округляется
# до трёх знаков после запятой.
# 2. Из списка names берутся только имена минимум из пяти букв.
# 3. Из списка numbers берётся произведение всех чисел.
# Подсказка № 1
# Используйте функцию map() для применения одной и той же операции ко всем
# элементам списка. Для возведения числа в третью степень и округления его до трех
# знаков после запятой используйте лямбда-функцию внутри map().
# Подсказка № 2
# Функция filter() позволяет отфильтровать элементы списка на основе заданного
# условия. В данном случае используйте её для выбора имен, состоящих из пяти и
# более букв. Убедитесь, что лямбда-функция правильно проверяет длину строки.
# Подсказка № 3
# Для нахождения произведения всех чисел в списке используйте функцию reduce().
# Эта функция последовательно применяет операцию (в данном случае умножение) ко
# всем элементам списка. Убедитесь, что вы импортировали reduce из модуля
# functools.

from functools import reduce

# Исходные списки
floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]
# Применяем функцию map для возведения в третью степень и округления до трех знаков после запятой
map_result = list(map(lambda x: round(x**3, 3), floats))
# Применяем функцию filter для выбора имен из пяти и более букв
filter_result = list(filter(lambda name: len(name) >= 5, names))
# Применяем функцию reduce для нахождения произведения всех чисел в списке
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers)
# Вывод результатов
print(map_result)
print(filter_result)
print(reduce_result)
