# Задача 3. Счастливый билет
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за
# проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где
# сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с
# номером n и выводит на экран yes или no.
# Подсказка № 1
# Для того чтобы получить каждую цифру номера билета, используйте операции
# целочисленного деления (//) и остатка от деления (%). Эти операции помогут
# выделить каждую цифру в номере. Например, чтобы получить первую цифру
# шестизначного числа, нужно разделить его на 100000.
# Подсказка № 2
# После того как вы выделили каждую цифру, разделите их на две группы. Первые три
# цифры и последние три цифры. Найдите сумму цифр для каждой группы. Это можно
# сделать с помощью обычных арифметических операций.
# Подсказка № 3
# Сравните суммы первых и последних трех цифр. Если они равны, билет считается
# счастливым. В противном случае билет не счастливый. Для этого используйте
# условные операторы if и else.

# Ввод номера билета
n = int(input("Введите номер билета: "))
# Разделение числа на отдельные цифры
n1 = n // 100000  # первая цифра
n2 = (n % 100000) // 10000  # вторая цифра
n3 = (n % 10000) // 1000  # третья цифра
n4 = (n % 1000) // 100  # четвертая цифра
n5 = (n % 100) // 10  # пятая цифра
n6 = n % 10  # шестая цифра
# Проверка на счастливость билета
if n1 + n2 + n3 == n4 + n5 + n6:
    print("yes")  # Вывод 'yes', если билет счастливый
else:
    print("no")  # Вывод 'no', если билет не счастливый