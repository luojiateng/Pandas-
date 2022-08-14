# 3、公鸡5文钱一只， 母鸡3文钱一只，小鸡3只一文钱，
# 用100文钱买100只鸡，其中公鸡，母鸡，小鸡都必须要有，
# 问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱？请利用python程序控制结构部分的知识编程解决该问题。

for x in range(20): #x是公鸡数，不超过20只
    for y in range(33): #y是母鸡数，不超过33只
        z = 100 - x - y #z是小鸡数，总和满足一百只
        if 5 * x + 3 * y + z / 3 == 100 and x != 0 and y != 0 and z != 0:
            print('公鸡：%s 母鸡：%s 小鸡：%s' % (x, y, z))
