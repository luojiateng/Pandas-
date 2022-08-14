#2.请编程实现以下操作：列表li = ['alex', 'eric', 'arin']，
#（1）计算列表长度并输出
li = ['alex', 'eric', 'arin']
print(len(li))
#（2）列表中追加元素"seven"，并输出添加后的列表
li.append('seven')
print(li)
#（3）在列表头部第一个元素‘alex’之前插入元素“eight”
li.insert(0,'eight')
print(li)
#（4）删掉一个值为‘eric’的元素
li.remove('eric')
print(li)
