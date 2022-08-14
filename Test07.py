import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('超市销售记录数据.xls')
df1 = df.groupby(by='商品名称').agg('sum').sort_values(by='数量', ascending=False).round({'数量': 0}).astype('int')
p1=df1.nlargest(10, '数量')
x_index = np.arange(10)
x_data = p1.index
y_data =p1.数量.values
bar_width = 0.5
rects1 = plt.bar(x_index, y_data, width=bar_width, alpha=0.4, color='b')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(x_index + bar_width / 2, x_data)
plt.yticks(np.arange(0, 11, 1))
plt.xlabel('前十名商品销量柱状图')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()