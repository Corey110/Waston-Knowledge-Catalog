import random
import string
import numpy as np
import time

print("importing EncodingClass.py")
class encoding():
    def get_encoding_list(self,num):
        list0 = []
        for i in range(0,num):
            p1 = ''.join(random.sample(string.ascii_lowercase + string.digits, 10))
            p = p1
            list0.append(p)
        return list0

# phone PT04
class phone(encoding):
    def get_encoding_list(self,num):
        list0 = []
        for i in range(0, num):
            phase1 = np.random.randint(13, 20)
            phase2 = np.random.randint(0, 1e9)
            phone = str(phase1) + str(phase2).zfill(9)
            list0.append(phone)
        return list0
# email PT05
class email(encoding):
    def create_encoding_list(self,num):
        Top_level_domain_list = ['.xyz','.top','.com','.cn','.vip','.ink','.com.cn','.net','.work','.site','.email','.club','edu','.gov','.biz']
        email_list =[]
        for i in range(0, num):
            phase4 = random.choice(Top_level_domain_list)
            phase1 = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))
            phase3 = ''.join(random.sample(string.ascii_lowercase, 3))
            email_address =  phase1 + '@' + phase3 + phase4
            email_list.append(email_address)
        return email_list
# CIF PT08
class CIF(encoding):
    # 32位数字与字符编码，由主数据系统根据客户要素进行唯一性识别，基于一定转换规则系统自动生成
    def get_encoding_list(self, num):
        list_CIF = []
        for i in range(0, num):
            p1 = ''.join(random.sample(string.digits, 10))
            p2 = ''.join(random.sample(string.digits, 10))
            p3 = ''.join(random.sample(string.digits, 10))
            p4 = ''.join(random.sample(string.digits, 2))
            p = p1 + p2 + p3 +p4
            list_CIF.append(str(p))
        return list_CIF
# ECIF PT09
class ECIF(encoding):
    # ECIF号由14位数字与字符编码构成，第 1 位：标识位，表示客户类型，1-5 表示个人客户；6-9 表示团体客户。 第 2-12 位：11 位流水号。 第 13-14 位：校验位。
    # 校验位生成规则为： 校验位 = [（所有偶数位的数字相加之和）* 3 + （所有奇数位的数字相加之和）] mod 23
    def get_encoding_list(self, num):
        list_ECIF = []
        for i in range(0, num):
            p1 = np.random.randint(1, 10)
            p2 = np.random.randint(0, 10)
            p3 = np.random.randint(0, 10)
            p4 = np.random.randint(0, 10)
            p5 = np.random.randint(0, 10)
            p6 = np.random.randint(0, 10)
            p7 = np.random.randint(0, 10)
            p8 = np.random.randint(0, 10)
            p9 = np.random.randint(0, 10)
            p10 = np.random.randint(0, 10)
            p11 = np.random.randint(0, 10)
            p12 = np.random.randint(0, 10)
            p0 = ((p2+p4+p6+p8+p10+p12)*3 + (p1+p3+p5+p7+p9+p11))%23
            p = str(p1)+str(p2)+str(p3)+str(p4)+str(p5)+str(p6)+str(p7)+str(p8)+str(p9)+str(p10)+str(p11)+str(p12)+str(p0).zfill(2)
            list_ECIF.append(str(p))
        return list_ECIF
# 委托人统一社会信用代码 PT14
class credit(encoding):
    def get_encoding_list(self,num):
        list_credit = []
        for i in range(0,num):
            # 第1位，登记管理部门
            p1 = random.choice(['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','Y'])
            # 第2位，机构类型代码
            if p1 in ['2','3','4','6','7','8','A','B','C','D','E','F','G','Y']:
                p2 = '1'
            if p1 in ['1','5','9']:
                p2 = random.choice(['1','2','3','9'])
            # 3-8位，参考GB/T 2260，有空再去参考
            p3 = ''.join(random.sample(string.digits, 6))
            #  9-17位，GB11714 大写英文或者数字
            p4 = random.choice([chr(i) for i in range(65,91)]+[ str(i) for i in range(10)])
            # 18位 GB17710 校验位
            p5 = str(np.random.randint(0, 10))
            list_credit.append(p1 + p2 + p3 + p4 +p5)
        return list_credit
# 个人客户证件号码 PT21
class id(encoding):
    def get_encoding_list(self,num):
        list0 = []
        for i in range(0,num):
            p1 = random.choice(
                ['11', '12', '13', '14', '15', '21', '22', '23', '31', '32', '33', '34', '35', '36', '37', '41', '42',
                 '43', '44', '45', '46','50','51','52','53','54','61','62','63','64','65','81','82'])
            p2 = random.choice(['01','02','03','04','05','06','07','08','09','10'])
            p3 = random.choice(['0','1','2','8'])
            p4 = str(random.randint(0,10))

            start = time.mktime(1930, 1, 1, 0, 0, 0, 0, 0, 0)  # 生成开始时间戳
            end = time.mktime((2020, 9, 11, 23, 59, 59, 0, 0, 0))  # 生成结束时间戳
            date_touple = time.localtime(random.randint(start, end))  # 将时间戳生成时间元组
            date = str(time.strftime("%Y%m%d", date_touple))  # 将时间元组转成格式化字符串（19760521）
            p5 = ''.join( random.sample(string.digits, 4))
            p = p1 + p2 + p3  + p4 + date + p5
            list0.append(p)
        return list0

# 受托人代码 PT23
class trustee(encoding):
    def get_encoding_list(self,num):
        list_trustee = []
        for i in range(0,num):
            p1 = str(1)
            p2 = ''.join( random.sample(string.digits, 5))
            p = p1 + p2
            list_trustee.append(p)
        return list_trustee

# 账户管理人代码 PT25
class account(encoding):
    def get_encoding_list(self,num):
        list_account = []
        for i in range(0,num):
            p1 = str(3)
            p2 = ''.join( random.sample(string.digits, 5))
            p = p1 + p2
            list_account.append(p)
        return list_account
# 投资管理人代码 PT27
class investor(encoding):
    def get_encoding_list(self,num):
        list_investor = []
        for i in range(0,num):
            p1 = str(4)
            p2 = ''.join( random.sample(string.digits, 5))
            p = p1 + p2
            list_investor.append(p)
        return list_investor
# 托管人代码 PT29
class trusteecode(encoding):
    def get_encoding_list(self,num):
        list_trusteecode= []
        for i in range(0,num):
            p1 = str(2)
            p2 = ''.join( random.sample(string.digits, 5))
            p = p1 + p2
            list_trusteecode.append(p)
        return list_trusteecode

# 员工编号 PT31
class employee(encoding):
    def get_encoding_list(self,num):
        list_employee= []
        for i in range(0,num):
            p = ''.join(random.sample(string.ascii_uppercase + string.digits, 4))
            while p in list_employee:
                p = ''.join(random.sample(string.ascii_uppercase + string.digits, 4))
                continue
            list_employee.append(p)
        return list_employee

# PD000007 计划登记号
class project(encoding):
    def get_encoding_list(self,num):
        list_project= []
        for i in range(0,num):
            year = str(np.random.randint(1990,2020))
            n = np.random.randint(1,4)
            if n == 1:
                p1 = ''.join( random.sample(string.digits, 4))
                p2 =  'ZY' 
                p3 = ''.join( random.sample(string.digits, 2))
                p = str(p1) + str(p2) + year + str(p3) 
            elif n == 2:
                p1 = '99JH'
                p2 = ''.join( random.sample(string.digits, 4))
                p = p1 + year + p2
            elif n == 3:
                p1 = '32'
                p2 = ''.join( random.sample(string.digits, 10))
                p = p1 + p2
            list_project.append(p)
        return list_project
# 团体养老保障 个人养老保障 PD13，PD17
class PD1317(encoding):
    def get_encoding_list(self,num):
        list0 = []
        for i in range(0,num):
            p = ''.join(random.sample(string.digits, 6))
            list0.append(p)
        return list0
class PD19(encoding):
    def get_encoding_list(self,num):
        list0=[]
        for i in range(0,num):
            p = 'RB'.join(random.sample(string.digits, 6))
            list0.append(p)
        return list0
'''
职业年金投资组合代码长度为8位，投资管理人投资组合代码编制方法为“3位投资管理人机构代码+Z+4位序列号”，受托人直投组合代码编制方法为“3位受托人机构代码+Z+4位序列号”。职业年金计划和统一计划的虚拟投资组合代码为其计划登记号。投资管理人机构代码、受托人机构代码以《职业年金基金数据交换规范》中为准
企业年金投资管理组合代码长度为8位，投资管理人投资组合代码编制方法为“3位投资管理人机构代码+Q+4位序列号”，受托人直投组合代码编制方法为“3位受托人机构代码+Q+4位序列号”。
团体养老保障投资组合建议以6开头的4位数字编码，个人养老保障投资组合建议以7开头的4位数字编码；
基本养老保险基金组合建议以4开头的4位数字编码。
'''
class PD24(encoding):
    def get_encoding_list(self,num):
        list0=[]
        for i in range(0,num):
            for j in range(1, 6):
                if j==1:
                    p = ''.join(random.sample(string.digits, 3)) + 'Z' + ''.join(random.sample(string.digits, 4))
                elif j==2:
                    p = ''.join(random.sample(string.digits, 3)) + 'Q' + ''.join(random.sample(string.digits, 4))
                elif j==3:
                    p = '4'.join(random.sample(string.digits, 3))
                elif j==4:
                    p = '7'.join(random.sample(string.digits, 3))
                elif j==5:
                    p = '4'.join(random.sample(string.digits, 3))
            list0.append(p)
        return list0
'''
标准化产品取中登公司记录的编号，如600320（振华重工）；非标准化产品由人保养老业务系统根据一定规则编号生成
'''
# 按照国内股票编号生成数据
class PD28(encoding):
    def get_encoding_list(self, num):
        list0 = []
        for i in range(0, num):
            p1 = random.choice(['300','600','601','603','605','900','688','000','002','200'])
            p2 = ''.join(random.sample(string.digits, 3))
            p = p1 + p2
            list0.append(p)
        return list0

class AG01(encoding):
    def get_encoding_list(self,num):
        list0 = []
        for i in range(0, num):
            p = ''.join(random.sample(string.digits, 10))
            list0.append(p)
        return list0

class bank_id(encoding):
    def get_encoding_list(self,num):
        list0 = []
        for i in range(0, num):

            j= random.randint(0,4)

            if j == 0:
                p = random.randint(6227007201360049787, 6227007201360049987)
            elif j == 1:
                p = random.randint(6215593700011926793, 6215593700011926993)
            elif j == 2:
                p = random.randint(6212261001080775106, 6212261001080799999)
            else:
                p = random.randint(6217856200015168391, 6217856200015168591)

            list0.append(p)
        return list0

class AG28(encoding):
    def get_encoding_list(self,num):
        list0 = []
        for i in range(0, num):
            p = ''.join(random.sample(string.digits, 4))
        return list0

class AG29(encoding):
    def get_encoding_list(self,num):
        list0 = []
        for i in range(0, num):
            p = ''.join(random.sample(string.digits, 10))
        return list0
if __name__ == '__main__':
    e = PD24()
    print(e.get_encoding_list(10))
