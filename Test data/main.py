import numpy as np
import pandas as pd
import random
from data_category import EncodingClass
from data_category import textclass
from data_category import date
from data_category import ratio
from data_category import number

def gen_title(df, table_name):
    df_table = df.loc[df["中文表名"] == table_name] #筛选表
    df_table = df_table[["中文字段名","标准编号"]].drop_duplicates() #选择中文字段列并去重
    df_T = pd.DataFrame(df_table.values.T) #转置
    new_title = df_T.iloc[0]
    df_o = pd.DataFrame(columns=new_title)
    return df_o

def clean_list(column):
    column = {}.fromkeys(column).keys()  #去重
    list0 = list(column)
    for i in list0:#去空格
        if i == '/':
            list0.remove('/')
    return list0

def get_numbering(df,field):
    df_tmp = df.loc[df["中文字段名"] == field]  # 筛选表
    return(df_tmp.iloc[0,0])

def gen_list(df,numbering):
    df_tmp = df.loc[df["标准编号"] == numbering]  # 筛选表
    return(df_tmp['代码取值'])

def main():
# 定义变量
    num = 1000
    filename_in = './基础数据标准_1.0版本.xlsx'
    sheet_in = '表4.标准映射'
    # 载入数据标准表....
    df_pre = pd.read_excel(filename_in, sheet_name=sheet_in)
    df_code = pd.read_excel(filename_in, sheet_name='表3.代码扩展定义')

    # 筛表名
    table_list = clean_list(df_pre['中文表名'])

    # 创建表并将所有表名写入sheet1

    for table in table_list:

        df_out = gen_title(df_pre, table)  # 每个表的表头

        for i in df_out:

            numbering = get_numbering(df_pre,i)

            # 代码类型，从《表3.代码扩展定义》获取每个标准编号对应的代码列表（如[01，02，03，09]）
            if numbering in clean_list(df_code['标准编号']):
                code_list1 = []
                for j in range(0,num):
                    tmp_list = list(gen_list(df_code, numbering))
                    tmp = random.choice(tmp_list)
                    code_list1.append(tmp)
                df_out[i] = code_list1

            # 编码类
            elif numbering == 'PT000004':
                df_out[i] = EncodingClass.phone().get_encoding_list(num)
            elif numbering == 'PT000005':
                df_out[i] = EncodingClass.email().create_encoding_list(num)
            elif numbering == 'PT000008':
                df_out[i] = EncodingClass.CIF().get_encoding_list(num)
            elif numbering == 'PT000009':
                df_out[i] = EncodingClass.ECIF().get_encoding_list(num)
            elif numbering == 'PT000014':
                df_out[i] = EncodingClass.credit().get_encoding_list(num)
            elif numbering == 'PT000021':
                df_out[i] = EncodingClass.id().get_encoding_list(num)
            elif numbering == 'PT000023':
                df_out[i] = EncodingClass.trustee().get_encoding_list(num)
            elif numbering == 'PT000025':
                df_out[i] = EncodingClass.account().get_encoding_list(num)
            elif numbering == 'PT000027':
                df_out[i] = EncodingClass.investor().get_encoding_list(num)
            elif numbering == 'PT000029':
                df_out[i] = EncodingClass.trusteecode().get_encoding_list(num)
            elif numbering == 'PT000031':
                df_out[i] = EncodingClass.employee().get_encoding_list(num)
            elif numbering == 'PD000007':
                df_out[i] = EncodingClass.project().get_encoding_list(num)
            elif numbering in ['PD000013','PD000017']:
                df_out[i] = EncodingClass.PD1317().get_encoding_list(num)
            elif numbering == 'PD000019':
                df_out[i] = EncodingClass.PD19().get_encoding_list(num)
            elif numbering == 'PD000024':
                df_out[i] = EncodingClass.PD24().get_encoding_list(num)
            elif numbering == 'PD000028':
                df_out[i] = EncodingClass.PD28().get_encoding_list(num)
            elif numbering in ['AG000001','AG000020','AG000023','AG000024','AG000028','AG000029']:
                df_out[i] = EncodingClass.bank_id().get_encoding_list(num)

            #文本类型
            elif numbering == 'PT000002':
                df_out[i] = textclass.address().gen_text_list(num)
            # # '企业基本信息 ' 和'客户资料表 ' 原表都有空格，不加空格匹配不到
            elif numbering == 'PT000010':
                if table == '企业基本信息 ':
                    df_out[i],df_out['企业简称'] = textclass.company().gen_text_list(num)
                elif table == '客户资料表 ':
                    df_out[i],df_out['客户简称'] = textclass.company().gen_text_list(num)
                elif table == '企业信息表':
                    df_out[i],df_out['简称'] = textclass.company().gen_text_list(num)
            elif numbering in ['PT000015','PT000018','PT000019','PT000032']:
                df_out[i] = textclass.name().gen_text_list(num)
            # PT16 3个字段各不相同，暂时都用客户名称
            elif numbering == 'PT000016':
                df_out[i],tmp_list = textclass.company().gen_text_list(num)
            elif numbering == 'PT000017':
                tmp_list,df_out[i] = textclass.company().gen_text_list(num)
            elif numbering in ['PT000024','PT000026','PT000028','PT000030']:
                df_out[i] = textclass.bank().gen_text_list(num)
            elif numbering == 'PD000005':
                if table == '产品信息表':
                    df_out[i],df_out['产品简称'] = textclass.plan().gen_text_list(num)
                elif table == '企业计划信息':
                    df_out[i] = EncodingClass.PD1317().get_encoding_list(num)
                else:
                    df_out[i], df_out['计划简称'] = df_out[i],df_out['产品简称'] = textclass.plan().gen_text_list(num)
            elif numbering == 'PD000006':
                if table == '计划基本信息':
                    tmp_list1,df_out[i] = textclass.plan().gen_text_list(num)
            elif numbering in ['PD000014','PD000020']:
                df_out[i] = textclass.offering().gen_text_list(num)
            elif numbering == 'PD000025':
                if table == '基金信息表':
                    df_out[i],df_out['基金简称'] = textclass.comb().gen_text_list(num)
                else:
                    df_out[i],tmp_list1 = textclass.comb().gen_text_list(num)
            elif numbering in ['PD000029','AG000019','AG000022','AG000025','AG000026','AG000027']:
                df_out[i],tmp_list1 = textclass.company().gen_text_list(num)

            # 日期
            elif numbering == 'AG000003':
                if table == '合同信息表':
                    df_out[i], df_out['合同生效日期'], df_out['合同终止日期'] = date.date().get_date_list(num)
                elif table == '年金合同表':
                    df_out[i], df_out['合同生效日期'], df_out['合同到期日期'] = date.date().get_date_list(num)
            # 比例
            elif numbering in ['AG000012','AG000013','AG000014','AG000016','AG000015']:
                df_out[i] = ratio.ratio().get_ratio_list(num)
            elif numbering in ['AG000008','AG000009']:
                df_out[i] = ratio.rule1().get_ratio_list(num)

            #   数值
            elif numbering == 'PD000002':
                if table == '基金日信息':
                    df_out[i],df_out['昨日总份额'],df_out['昨日总净值'] = number.general().get_number_list(num)
                elif table == '净值信息表':
                    df_out[i],df_out['基金总份额'],df_out['基金总净值'] = number.general().get_number_list(num)
                elif table == '组合净值':
                    df_out[i],df_out['份额'],df_out['当日基金净值'] = number.general().get_number_list(num)
                elif table == '投资组合净值':
                    df_out[i],tmp_list1,df_out['总净值'] = number.general().get_number_list(num)
            elif numbering == 'PD000003':
                if table == '交易报表投资组合明细':
                    tmp_list1,df_out[i], tmp_list2 = number.general().get_number_list(num)
            elif numbering == 'AG000007':
                df_out[i] = number.base().get_number_list(num)
            elif numbering == 'AG000006':
                df_out[i] = number.base().get_number_list(num)
                df_out['企业缴纳基数'] = df_out[i]
            elif numbering == 'AG000021':
                df_out[i] = number.balance().get_number_list(num)

        df_out = df_out.iloc[:, ~df_out.columns.duplicated()]
        # # #  修改好的表写入exc
        filename_out = './out/' + str(table) + '.csv'
        df_out.to_csv(filename_out,encoding='utf_8_sig',index=0)
        print("writing in" + filename_out)
if __name__ == "__main__":
    main()


