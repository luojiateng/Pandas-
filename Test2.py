import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pylab import *

'''
# 解决不显示中文，负号显示为方框
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

x = [50, 69, 58, 12, 39, 75]
y = [101, 25, 10, 12, 300, 90]
index = np.arange(1, 7, 1)
width = 0.2

plt.bar(x=index, height=x, width=width, color='yellow', label=u'汽车销售')
plt.bar(x=index + width, height=y, width=width, color='green',
        label=u'电脑销售')  # width=index+width 表示从向右x平移width的单位，刚好靠在一起
plt.xlabel('2019年')
plt.ylabel('销售数量')
plt.title('2019年销售报告')
plt.legend(loc='best')
plt.show()
'''

'''
df = pd.DataFrame({'code':[1,2,3,4,5,6,7,8],
          'value':[np.nan,5,7,8,9,10,11,12],
          'value2':[5,np.nan,7,np.nan,9,10,11,12],
          'indstry':['农业1','农业1','农业1','农业2','农业2','农业4','农业2','农业3']},
          columns=['code','value','value2','indstry'],
          index=list('ABCDEFGH'))
'''

df = pd.read_excel('超市营业额2.xlsx')

# 只留下需要处理的列
cols = [col for col in df.columns if col not in ['交易额']]
# 分组的列
gp_col = '交易额'
# 查询nan的列
df_na = df[cols].isna()
# 根据分组计算平均值
df_mean = df.groupby(gp_col)[cols].mean()

print(df)
print('--------')
# 依次处理每一列
for col in cols:
    na_series = df_na[col]
    names = list(df.loc[na_series, gp_col])

    t = df_mean.loc[names, col]
    t.index = df.loc[na_series, col].index

    # 相同的index进行赋值
    df.loc[na_series, col] = t

print(df)
