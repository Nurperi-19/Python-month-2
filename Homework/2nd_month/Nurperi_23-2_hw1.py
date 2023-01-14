#1) Создайте класс Product с конструктором (init), принимающий название, цену и дату упаков. (name, price, pack_date)
class Product:
    def __init__(self, name, price, pack_date):
        self.name = name
        self.price = price
        self.pack_date = pack_date

#2) Создайте метод для определения даты окончания срока годности (пример был на уроке)
    def exp_date(self):
        mfg_date = int(self.pack_date[:2])
        mfg_date += 10
        expiry_date = f'{mfg_date}{self.pack_date[2:]}'
        self.expiry_date = expiry_date
        print(expiry_date)

#3) Создайте 3 объекта с соответсвтующий параметрами
cheese = Product('Сыр', 90, '01.09.2022')
bread = Product('Хлеб', 75, '02.10.2022')
sandwich = Product('Сэндвич', 85, '05.10.2022')

with open('product.txt', 'w', encoding='UTF-8') as file:
    file.write(f'Products: \n{cheese.name} {cheese.price}soms (Mfg date:{cheese.pack_date})'
               f'\n{bread.name} {bread.price}soms (Mfg date:{bread.pack_date})'
               f'\n{sandwich.name} {sandwich.price}soms (Mfg date:{sandwich.pack_date}')

# Тест:
print(cheese.name)
print(cheese.price)
print(cheese.pack_date)
cheese.exp_date()

