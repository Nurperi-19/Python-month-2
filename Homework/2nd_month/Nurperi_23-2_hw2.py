current_money = 0

# 1) Создать класс Balance с конструктором, принимающий название файла
class Balance:
    def __init__(self, file_name):
        self.file_name = file_name
        self.get_balance()
        print('Объект создан', self)

# 2) Добавить в метод для считывания текущего баланса с файла, если файла нет или он пустой, то баланс должен быть 0
    def get_balance(self):
        try:
            with open(self.file_name, "w+") as file:
                balance = file.read()
                if balance:
                    current_money = int(balance)
                else:
                    current_money = 0
                    file.write("0")
                    self.current_money = current_money
        except FileNotFoundError:
            with open(self.file_name, 'w+') as file:
                file.write('0')
                current_money = 0

        self.current_money = current_money

    def add_money(self, money):
        self.current_money += money
        self.write_current_balance()
        print(f'Добавление баланса: {money}', self)

# 3) Добавить метод для записи текущего баланса в файл
    def write_current_balance(self):
        with open(self.file_name, 'w+') as file:
            file.write(str(self.current_money))

# 4) Добавить метод для инкассации
    def cash_collection(self):
        if self.current_money > 0:
            print(f"Инкассация {self.current_money}")
            self.current_balance = 0
            print(self)
        else:
            print("Инкассация невозможна, касса пуста!", self)

# 5) Добавить магический метод str который будет отображать текущий баланс
    def __str__(self):
        return f'Текущий баланс: {self.current_money}'

# Тест:
bal = Balance('test_1.txt')
bal.add_money(120)
bal.add_money(30)
bal.cash_collection()