import pandas as pd

df = pd.read_excel('超市销售记录数据.xls')
df1 = df.groupby(by='商品名称'
                 ).agg('sum'
                       ).sort_values(by='数量', ascending=False
                                     ).round({'数量': 0}
                                             ).astype('int')
print('商品按照销量排序为：')
print(df1.数量)