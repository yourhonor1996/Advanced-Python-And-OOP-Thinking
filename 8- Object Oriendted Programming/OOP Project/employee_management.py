import math
from .person import *
from .person import Consts as c

# import math
# from person import Person
# from person import Consts as c

class Worker(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.job = 'worker'

    def get_price(self):
        return math.floor(c.BASE_PRICE[self.job] * c.MIN_AGE / self.age)

    def calc_life_cost(self):
        return math.floor(c.BASE_COST[self.job] * self.age / c.MIN_AGE)

    def calc_income(self):
        return math.floor(c.BASE_INCOME[self.job][self.work_place.get_expertise()] * c.MIN_AGE / self.age)

    
class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.job = 'teacher'

    def get_price(self):
        return int(c.BASE_PRICE[self.job] - (self.age - c.MIN_AGE) * c.AGE_MUL)

    def calc_life_cost(self):
        return c.BASE_COST[self.job] + (self.age - c.MIN_AGE) * c.AGE_MUL

    def calc_income(self):
        return c.BASE_INCOME[self.job][self.work_place.get_expertise()] - (self.age - c.MIN_AGE) * c.AGE_MUL
    
    
class Engineer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.job = 'engineer'

    def get_price(self):
        return math.floor(c.BASE_PRICE[self.job] * math.sqrt(c.MIN_AGE / self.age))

    def calc_life_cost(self):
        return math.floor(c.BASE_COST[self.job] * math.sqrt(self.age / c.MIN_AGE))

    def calc_income(self):
        return math.floor(c.BASE_INCOME[self.job][self.work_place.get_expertise()] * math.sqrt(c.MIN_AGE / self.age))