print("importing number.py")
import random
class number():
    def __init__(self):
        pass
class general(number):
    def get_number_list(self,num):
        list0 = []
        list1 = []
        list2 = []
        for i in range(0,num):
            unit_worth = 3 * random.random()
            number = random.randrange(1000, 1000000, 100)
            total_worth = unit_worth * number
            list0.append(unit_worth)
            list1.append(number)
            list2.append(total_worth)
        return list0,list1,list2
class base(number):
    def get_number_list(self,num):
        list0 = []
        for i in range(0,num):
            base = random.randrange(5000,100000)
            list0.append(base)
        return list0
class balance(number):
    def get_number_list(self,num):
        list0 = []
        for i in range(0,num):
            balance = 50000
            list0.append(balance)
        return list0

