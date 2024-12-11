# Задача 4. Частотный анализ
# Есть файл text.txt, который содержит текст. Напишите программу, которая
# выполняет частотный анализ, определяя долю каждой буквы английского
# алфавита в общем количестве английских букв в тексте, и выводит результат в
# файл analysis.txt. Символы, не являющиеся буквами английского алфавита,
# учитывать не нужно.
# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с
# тремя знаками в дробной части. Буквы должны быть отсортированы по
# убыванию их доли. Буквы с равной долей должны следовать в алфавитном
# порядке.
# Пример:
# Содержимое файла text.txt:
# Mama myla ramu.
# Содержимое файла analysis.txt:
# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083

# Определяем английский алфавит
english_alphabet = "abcdefghijklmnopqrstuvwxyz"
total_letters = 0
# Открываем файл text.txt и считываем текст
with open("text.txt", "r") as file:
    text = file.read().lower()  # Приводим текст к нижнему регистру
# Создаем словарь для подсчета количества каждой буквы
letter_count = {letter: 0 for letter in english_alphabet}
# Подсчитываем количество вхождений каждой буквы
for char in text:
    if char in english_alphabet:
        letter_count[char] += 1
total_letters += 1
# Вычисляем частоту встречаемости каждой буквы
letter_freq = {
    letter: (count / total_letters)
    for letter, count in letter_count.items()
    if count > 0
}
# Сортируем буквы по убыванию частоты и по алфавиту при равенстве частоты
sorted_letters = sorted(letter_freq.items(), key=lambda x: (-x[1], x[0]))
# Записываем результат в файл analysis.txt
with open("analysis.txt", "w") as file:
    for letter, freq in sorted_letters:
        file.write(f"{letter} {freq:.3f}\n")
