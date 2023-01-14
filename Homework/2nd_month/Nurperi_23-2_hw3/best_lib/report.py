from datetime import date

with open('reports.txt', 'w') as file:
    file.write('Test:')

def make_report(res):
    with open('reports.txt', 'a') as file:
        file.write('\n1')


# Доп. задание (выполнять не обязательно, но даёт дополнительные баллы, если есть спорные моменты)
# 4. допишите функцию make_report таким образом, чтобы в соседнем файле reports.txt сохранялись истории статусов запросов.
# Каждый раз отправляя запрос, вызывайте эту функцию, чтобы сохранить время, url и статус ответа.
# Файл должен выглядеть примерно так:
# 01.01.2022 https://jsonplaceholder.typicode.com/posts/1/ 200
# 11.10.2022 https://habr.com/ru/company/vk/blog/692062/ 200
# 11.10.2022 https://habr.com/asdfasasdfasdf/ 404