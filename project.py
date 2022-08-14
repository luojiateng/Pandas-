import pandas as pd

df1 = pd.read_excel('超市营业额2.xlsx', sheet_name=0)  # 读取Excel文件表一的数据
df2 = pd.read_excel('超市营业额2.xlsx', sheet_name=1)  # 读取Excel文件表二的数据
df = pd.concat([df1, df2])  # 合并表一二的数据
print('-------------------------------------第一题---------------------------------')
print('超市营业额三四月份总的数据行数\t' + str(df.shape[0]))
df.drop_duplicates(subset=['工号', '姓名', '日期', '时段', '交易额', '柜台'], inplace=True, keep='first')  # 清除重复数据
print('超市营业额三四月份总的数据清除重复数据之后的行数\t' + str(df.shape[0]))

sum_nu = df.isna().sum()
print("填充前缺失值情况\n" + str(sum_nu))


# 返回该员工的交易额平均值的函数
def aver(name):
    return df[df['姓名'].isin([name])]['交易额'].mean()


for i in df[df.交易额.isna()].index:  # 遍历所有的缺失值
    df.loc[i, '交易额'] = round(aver(df.iloc[i].姓名))  # 将空值使用该人的销售平均值填充,并四舍五入
# 对异常值进行填充
df.loc[df.交易额 < 100, '交易额'] = 100
df.loc[df.交易额 > 5000, '交易额'] = 5000
# 计算该表缺失值的个数
sum_nu = df.isna().sum()
print("填充后缺失值情况\n" + str(sum_nu))


print('--------------------------------第二题---------------------------------')
# 创建一个字典
all_staff = {}
# 使用key—_>value对字典进行填充
all_staff['张三'] = round(aver('张三'))
all_staff['李四'] = round(aver('李四'))
all_staff['王五'] = round(aver('王五'))
all_staff['赵六'] = round(aver('赵六'))
all_staff['周七'] = round(aver('周七'))
all_staff['钱八'] = round(aver('钱八'))
# 先使用sorted对字典排序，得到一个列表，然后使用reversed对其倒置，达到从大到小排序目的
print('三月份业绩考核为')
print(list(reversed(sorted(all_staff.items(), key=lambda kv: (kv[1], kv[0])))))
print('-------------------------------第三题-----------------------------------')
print('\n三月业绩透视表:')
days = pd.crosstab(df1.姓名, df1.日期, df1.交易额, aggfunc='sum')
print(days)
print()
items = pd.crosstab(df1.姓名, df1.柜台, df1.交易额, aggfunc='sum')
print(items)
print('\n四月业绩透视表:')
days = pd.crosstab(df2.姓名, df2.日期, df2.交易额, aggfunc='sum')
print(days)
print()
items = pd.crosstab(df2.姓名, df2.柜台, df2.交易额, aggfunc='sum')
print(items)
