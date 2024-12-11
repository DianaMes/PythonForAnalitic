# Задача 2. Палиндром
# Пользователь вводит строку. Необходимо написать программу, которая
# определяет, существует ли у этой строки перестановка, при которой она станет
# палиндромом. Затем она должна выводить соответствующее сообщение.
# Пример 1
# Введите строку: aab
# Можно сделать палиндромом
# Пример 2
# Введите строку: aabc
# Нельзя сделать палиндромом


def is_poly(string):
    # Создаем словарь для подсчета количества вхождений каждого символа
    char_dict = dict()
    # Проходим по каждому символу в строке
    for i_sym in string:
        # Увеличиваем счетчик для текущего символа
        char_dict[i_sym] = char_dict.get(i_sym, 0) + 1
    # Переменная для подсчета символов с нечетным количеством вхождений
    odd_count = 0
    # Проходим по значениям словаря (количеству вхождений символов)
    for i_value in char_dict.values():
        # Если количество вхождений нечетное, увеличиваем счетчик нечетных
        if i_value % 2 != 0:
            odd_count += 1
    # Палиндром может быть составлен, если не более одного символа имеет нечетное количество вхождений
    return odd_count <= 1


# Запрашиваем у пользователя ввод строки
my_string = input("Введите строку: ")
# Проверяем, можно ли сделать палиндром из введенной строки
if is_poly(my_string):
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")