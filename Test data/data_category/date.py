import random
import time
class date():
    def get_date_list(self,num):
        list0 = []
        list1 = []
        list2 = []
        for i in range(0,num):
            stage = random.choice([2,3,5])
            year = random.randint(2000,2021)
            month = random.randint(1,13)
            day = random.randint(1,28)
            p1 = str(year) + '-' + str(month) + '-' + str(day)
            p2 = str(year + stage) + '-' + str(month) + '-' + str(day)
            list0.append(p1)
            list1.append(p2)
            list2.append(stage)
        return list2,list0,list1