# 5、某家庭全年家庭支出情况如下表所示：
# 请根据此数据，画出该家庭全年在各个类别上花销情况的饼状图
# （每个扇形为一类开支，数值为该家庭在该类别上的开支占总开支的百分比）
import matplotlib.pyplot as plt
import pandas as pd

'''将所给数据写入某家庭全年支出表.xlsx表中'''
df = pd.read_excel('某家庭全年支出表.xlsx')
spend = {}  # 准备一个空的字典 spend

for i in range(7):
    item = 0  # 每次循环清空该支出项目的总金额
    lines = df.iloc[i].values  # 读取列表第i(i+1)行的数据存入lines列表中
    for j in range(1, 13):
        item = lines[j] + item  # 对i行的数据进行累加
    spend[lines[0]] = item  # lines表示key，算出的钱数为values，存入准备好的字典

data1 = pd.Series(spend)  # 构建序列
data1.name = ''  # 将序列的名称设置为空字符，否则绘制的饼图左边会出现None这样的字眼
plt.axes(aspect='equal')  # 控制饼图为正圆
# plot方法对序列进行绘图
data1.plot(kind='pie',  # 选择图形类型
           autopct='%.1f%%',  # 饼图中添加数值标签
           radius=1,  # 设置饼图的半径
           startangle=180,  # 设置饼图的初始角度
           counterclock=False,  # 将饼图的顺序设置为顺时针方向
           title='某家庭全年支出表',  # 为饼图添加标题
           wedgeprops={'linewidth': 1.5, 'edgecolor': 'green'},  # 设置饼图内外边界的属性值
           textprops={'fontsize': 10, 'color': 'black'}  # 设置文本标签的属性值
           )
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 解决负号“-”显示为方块的问题
plt.show()  # 显示图形
