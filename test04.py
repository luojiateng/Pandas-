from pandas import DataFrame

DataFrame.plot(x=None, y=None, kind='bar', figsize=None,
               xticks=None, yticks=None, xlim=None, ylim=None, position=0.5, table=False, sort_columns=False)
'''Parameters:
x : 指数据框列的标签或位置参数

y : 

kind : ‘bar’ :#条形图
figsize : 图片尺寸大小
use_index :默认用索引做x轴

xticks : 设置x轴刻度值，序列形式（比如列表）
yticks :设置y轴刻度，序列形式（比如列表）
xlim : 2-tuple/list#设置坐标轴的范围，列表或元组形式
ylim : 2-tuple/list
fontsize :设置轴刻度的字体大小
colormap : 设置图的区域颜色
colorbar : 图片柱子
table : 如果为正，则选择DataFrame类型的数据并且转换匹配matplotlib的布局。
sort_columns : 以字母表顺序绘制各列，默认使用前列顺序
secondary_y : 设置第二个y轴（右y轴）
'''
