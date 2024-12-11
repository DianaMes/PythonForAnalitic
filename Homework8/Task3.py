# Задача 3. Турнир
# В файле first_tour.txt записано число K и данные об участниках турнира по
# настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных в
# первом туре. Во второй тур проходят участники, которые набрали более K
# баллов в первом туре.
# Напишите программу, которая выводит в файл second_tour.txt данные всех
# участников, прошедших во второй тур, с нумерацией.
# В первой строке нужно вывести в файл second_tour.txt количество участников
# второго тура. Затем программа должна вывести фамилии, инициалы и
# количество баллов всех участников, прошедших во второй тур, с нумерацией.
# Имя нужно сократить до одной буквы. Список должен быть отсортирован по
# убыванию набранных баллов.
# Пример:
# Содержимое файла first_tour.txt:
# 80
# Ivanov Serg 80
# Sergeev Petr 92
# Petrov Vasiliy 98
# Vasiliev Maxim 78
# Содержимое файла second_tour.txt:
# 2
# 1) V. Petrov 98
# 2) P. Sergeev 92

# Открываем файл first_tour.txt для чтения
with open("first_tour.txt", "r") as file:
    lines = file.readlines()
# Первая строка содержит число K
K = int(lines[0])
# Словарь для хранения данных участников
participants = {}
# Словарь для хранения участников, прошедших во второй тур
filter_player = {}
count = 1
# Обрабатываем оставшиеся строки
for line in lines[1:]:
    # Разделяем строку на части
    data = line.strip().split()
# Формируем имя участника с инициалом
name = f"{data[1][0]}. {data[0]}"
# Получаем количество баллов
score = int(data[-1])
# Сохраняем участника и его баллы
participants[name] = score
# Фильтруем участников, набравших более K баллов
for player, score in participants.items():
    if score > K:
        filter_player[player] = score
# Сортируем участников по убыванию баллов
sorted_filter_player = dict(
    sorted(filter_player.items(), key=lambda x: x[1], reverse=True)
)
# Открываем файл second_tour.txt для записи
with open("second_tour.txt", "w") as file:
    # Записываем количество участников второго тура
    file.write(f"{len(sorted_filter_player)}\n")
# Записываем данные участников с нумерацией
for player, score in sorted_filter_player.items():
    file.write(f"{count}) {player} {score}\n")
count += 1