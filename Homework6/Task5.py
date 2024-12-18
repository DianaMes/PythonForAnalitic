# Задача 5. Шифр Цезаря
# Юлий Цезарь использовал свой способ шифрования текста. Каждая буква
# заменялась на следующую по алфавиту через K позиций по кругу. Если взять
# русский алфавит и K, равное 3, то в слове, которое мы хотим зашифровать,
# буква А станет буквой Г, Б станет Д и так далее.
# Пользователь вводит сообщение и значение сдвига. Напишите программу,
# которая изменит фразу при помощи шифра Цезаря.
# Пример:
# Введите сообщение: это питон.
# Введите сдвиг: 3
# Зашифрованное сообщение: ахс тлхср.
# Подсказка № 1
# Перед началом работы убедитесь, что алфавит включает все буквы, включая букву 'ё',
# чтобы избежать ошибок в шифровании.
# Подсказка № 2
# При определении индекса нового символа используйте операцию взятия остатка (%),
# чтобы избежать выхода за пределы длины алфавита.
# Подсказка № 3
# Учтите, что пробелы и другие символы, не входящие в алфавит, должны оставаться
# без изменений. Это можно сделать, проверяя наличие символа в строке alphabet.
# Подсказка № 4
# Используйте функцию join() для преобразования списка зашифрованных символов в
# единую строку, что позволяет избежать использования дополнительного цикла для
# создания строки.

# Определение русского алфавита, включая букву 'ё'
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


# Функция для шифрования текста по методу Цезаря
def caesar_cipher(string, user_shift):
    # Создание списка зашифрованных символов
    char_list = [
        (
            alphabet[(alphabet.index(sym) + user_shift) % len(alphabet)]
            if sym in alphabet
            else sym
        )
        for sym in string
    ]

    # Преобразование списка символов в строку
    new_str = "".join(char_list)
    return new_str


# Ввод пользователем исходного сообщения и сдвига
input_str = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))
# Шифрование сообщения
output_str = caesar_cipher(input_str, shift)
# Вывод зашифрованного сообщения
print("Зашифрованное сообщение:", output_str)
