import math

class Consts:
    BASE_PRICE = {'worker': 200, 'teacher': 150, 'engineer': 250}
    BASE_COST = {'worker': 200, 'teacher': 150, 'engineer': 300}
    BASE_INCOME = {'worker': {'mine': 800, 'school': 500, 'company': 600},
                   'teacher': {'mine': 400, 'school': 900, 'company': 700},
                   'engineer': {'mine': 1000, 'school': 800, 'company': 900}}
    MIN_AGE = 5
    AGE_MUL = 5

class Person:
    instances = []

    def __init__(self, name, age):
        Person.instances.append(self)
        self.name = name
        self.age = age
        self.level = 1
        self.job = ""
        self.work_place = None

    def do_level(self, income):
        return income * math.sqrt(self.level * self.work_place.level)

    def calc_income(self):
        pass

    def calc_life_cost(self):
        pass

    def calc(self):
        income = self.calc_income()
        cost = self.calc_life_cost()
        return self.do_level(income) - cost

    def get_job(self):
        return self.job

    def upgrade(self):
        self.level += 1

    @staticmethod
    def calc_all():
        return sum([person.calc() for person in  Person.instances])
    
