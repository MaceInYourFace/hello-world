# state - data

# behaviour - functions

class Person:
    age = 0
    name = ""
    money = 0.0

    def __init__(self, age, name, money):
        self.age = age
        self.name = name
        self.money = money

    def birthday(self):
        self.age = self.age + 1

    def name_change_by_deedpole(self, new_name):
        self.name = new_name

    def payday(self, paid_amount):
        self.money = self.money + paid_amount
        self.money = round(self.money, 2)

    def spend_money(self, money_spent):
        self.money = self.money - money_spent
    

dave = Person(32, "Dave", 100.32)
bob = Person(23, "Bob", 52.32)
james = Person(30, "James", 321.32)
sophie = Person(23, "Sophie", 31.32)
sarah = Person(32, "Sarah", 412.32)
linda = Person(12, "Linda", 31.32)

james.payday(525)
james.spend_money(300)

print(james.money)