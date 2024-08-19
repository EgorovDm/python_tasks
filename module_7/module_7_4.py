#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b + fixes

team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебников данных!'

# Использование % для форматирования строки
team1_str = "Команда Мастеров кода участников: %s !" % (team1_num)
team2_str = "Итого сегодня в командах участников: %(total)s и %(team2_num)s !" % (
    {"total": team1_num + team2_num, "team2_num": team2_num}
)

# Использование format() для форматирования строки
team2_score_str = "Команда Волшебников данных решила задач: {score2} !".format(score2 = score2)
team2_time_str = "{team2_num} решили задачи за {time} секунд!".format(
    team2_num=team2_num, 
    time=round(team2_time, 2) if team2_time else "Время не указано!"
)

# Использование f-строк для форматирования строки
team1_score_str = f"Команды решили {score1} и {score2} задач."

print(
    team1_str,
    team2_str,
    team2_score_str,
    team2_time_str,
    sep="\n")

# Решение задачи с проверкой результата
def get_challenge_result(score1, score2, team1_time, team2_time):
    if score1 > score2 or (score1 == score2 and team1_time > team2_time):
        result = 'Победа команды Мастеров кода!'
    elif score1 < score2 or (score1 == score2 and team1_time < team2_time):
        result = 'Победа команды Волшебников данных!'
    else:
        result = 'Ничья!'
    return f"Результат битвы: {result}"

# Использование f-строк для форматирования строки с общем результатом
average_str = f"Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 2)} секунды на задачу!"
print(f"{average_str}\n{get_challenge_result(score1, score2, team1_time, team2_time)}")
