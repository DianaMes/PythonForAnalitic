# Задача 5*. Поменять местами: не всё так просто! (необязательная,
# повышенной сложности)
# Напишите программу, которая меняла бы значения двух переменных местами,
# но без использования третьей переменной и синтаксического сахара, который
# мы разбирали, а именно: без конструкции a, b = b, a. В переменные будут
# вводиться только числа.
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# print(a, b)
# # стереть эту строчку и вставить свой код здесь
# print(a, b)
# Изменять, удалять, менять местами первую, вторую, третью и последнюю
# строчки нельзя. В четвёртую строку можно вставлять сколько угодно кода, не
# трогая последний print.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(a, b)
# Меняем значения a и b без использования третьей переменной
a = a + b  # Сначала a становится суммой a и b
b = a - b  # Затем b становится старым значением a (a + b - b = a)
a = a - b  # Наконец, a становится старым значением b (a + b - a =b)
print(a, b)
