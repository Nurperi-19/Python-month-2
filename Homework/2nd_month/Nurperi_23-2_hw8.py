# Задачи для регулярных выражений:
import re

# 1. У вас есть список номеров, вам нужно разбить их на 3 группы по сотовым операторам (О, Билайн, Мегаком).
# Коды смотрите на их сайтах
numbers = '0222987654 0500123456 0990987654 0501123456 0550987654 0502123456 0555987654 0220987654 0505123456 0224987654'
o_kg = re.findall(r"", numbers)
beeline = re.findall(r"", numbers)
megacom = re.findall(r"", numbers)

# 2. Напишите программу, которая определяет фамилию и имя:

while True:
    full_name = input('Ввод: ')
    last_name = re.findall(r"\w+ва|\w+в", full_name)
    # first_name =
    print(f'Фамилия: {last_name[0]}\nИмя: ')

# 4. Напишите валидатор (программу, проверяющую правильность) email:
# Сначала буквы на латинице, затем собачка, а в конце домен, точка и зона, то есть, вот валидные:
# kaium@mail.ru
# example@gmail.com
# А это нет:
# test.ru
# example@com


