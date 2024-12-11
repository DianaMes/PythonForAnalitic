# Задача 2. Обычный день на работе
# Максим программирует целый день на работе и вечером идёт домой. Каждый час
# начальство кидает ему несколько задач, которые нужно решить до следующего
# рабочего часа. Вдобавок каждый час Максиму звонит супруга. Он знает, что если он
# возьмёт трубку, то жена попросит зайти вечером в магазин.
# Напишите программу, в которой считается, сколько задач выполнил Максим за день
# (восемь часов). Если он хотя бы раз взял трубку, то в конце дополнительно выводите
# сообщение: «Нужно зайти в магазин».

hour = 0  # Счетчик часов рабочего дня
tasks_sum = 0  # Суммарное количество выполненных задач
go_to_store = False  # Флаг, указывающий на необходимость зайти в магазин
print("Начался 8-часовой рабочий день")
while hour != 8:  # Цикл на 8 часов
    hour += 1  # Увеличение счетчика часов
print(hour, "час")
# Ввод количества задач, решенных в текущий час
solved_tasks = int(input("Сколько задач решит Максим? "))
tasks_sum += solved_tasks  # Увеличение общего числа задач
# Ввод решения о том, брать ли трубку, если звонит жена
call = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет):"))
if call == 1:
    go_to_store = True  # Если ответ "да", устанавливаем флаг для захода в магазин
# Вывод результатов после окончания рабочего дня
print("Рабочий день закончился. Всего выполнено задач:", tasks_sum)
if go_to_store:
    print("Нужно зайти в магазин")  # Вывод сообщения о необходимости зайти в магазин
