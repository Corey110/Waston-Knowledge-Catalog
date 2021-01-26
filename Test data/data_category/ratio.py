import random
class ratio():
    def get_ratio_list(self,num):
        list0 = []
        ratio = random.choice([0.005,0.008,0.01,0.015,0.012,0.02,0.03,0.05])
        for i in range(0,num):
            list0.append(ratio)
        return list0
class rule1(ratio):
    def get_ratio_list(self,num):
        list0 = []
        for i in range(0,num):
            list0.append(0.5)
        return list0
class rule2(ratio):
    def get_ratio_list(self,num):
        list0 = []
        list1 = []
        for i in range(0,num):
            list0.append(0.8)
            list1.append(0.2)
        return list0,list1
