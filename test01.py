#1、请编程实现三角形的余弦定理，即：程序运行后，从控制台输入两个边长及夹角角度（单位为度），
# 这三个量输入时用空格隔开，回车后，程序自动计算出三角形第三条边的长度。
import math

x = input('输入两边长及夹角:')
a, b, theta = map(float, x.split())  #split()方法用于切分字符串
c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(theta * math.pi / 180))# cos()参数为弧度
print('第三条边的长度为:', c)
