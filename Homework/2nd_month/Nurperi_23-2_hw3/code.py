# 1. Создайте файл code.py и модуль best_lib (папка с файлом init) ✔
# 2. Внутри модуля создайте 2 файла: balance.py (с классом Balance) и report.py (с функцией make_report).
#    Функцию и класс можете оставить пустыми, используя pass ✔
# 3. В code.py импортируйте эти функцию и класс, создайте 1 объект класса и вызовите функцию ✔

import best_lib

my_balance = best_lib.Balance(1234)
print(my_balance.money)

# 4. Также импортируйте библиотеку requests и отправьте запросы в эти url:
# https://habr.com/ru/company/vk/blog/692062/
# https://jsonplaceholder.typicode.com/posts/1/  ✔

import requests

res_1 = requests.get('https://jsonplaceholder.typicode.com/posts/1/')
res_2 = requests.get('https://habr.com/ru/company/vk/blog/692062/')
res_3 = requests.get('https://habr.com/ru/primer')

# выведите и сравните их свойства text и status_code ✔

print(res_1.url, res_1.status_code)
print(res_2.url, res_2.status_code)
print(res_3.url, res_3.status_code)
# print(res_1.text)
# print(res_2.text)

# Доп. задание (выполнять не обязательно, но даёт дополнительные баллы, если есть спорные моменты)
# 4. допишите функцию make_report таким образом, чтобы в соседнем файле reports.txt сохранялись истории статусов запросов.
# Каждый раз отправляя запрос, вызывайте эту функцию, чтобы сохранить время, url и статус ответа.
# Файл должен выглядеть примерно так:
# 01.01.2022 https://jsonplaceholder.typicode.com/posts/1/ 200
# 11.10.2022 https://habr.com/ru/company/vk/blog/692062/ 200
# 11.10.2022 https://habr.com/asdfasasdfasdf/ 404

best_lib.make_report(res_1)
best_lib.make_report(res_2)
best_lib.make_report(res_3)

# Задания соберите в одну папку, заархивируйте перед отправкой и отправляйте одним файлом-архивом