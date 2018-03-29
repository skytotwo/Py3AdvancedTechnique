#案例引出
#西班牙足球甲级联赛，每轮球员进球统计：
#第一轮：{'苏亚雷斯':1, '梅西':2, '本泽马':1, 'c罗':3...}
#第二轮：{'苏亚雷斯':2, 'c罗':1, '格里兹曼':2, '贝尔':1...}
#第三轮：{'苏亚雷斯':1, '托雷斯':2, '贝尔':1, '内马尔':1...}
#...
#统计出前N轮，每场比赛都有进球的球员


#解决方法
#利用集合(set)的交集操作
#step1：使用字典的keys()方法，得到一个字典keys的集合
#step2：使用map函数，得到所有字典的keys的集合
#step3：使用reduce函数，取所有字典的keys的集合的交集



from random import randint, sample
#sample表示取样
#sample('abcdefg', randint(3, 6))  具体范围，取值的数量
s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

jiaoji = s1.keys() & s2.keys() & s3.keys() #求前三轮的公共交集



#当多轮的情况下
# data = map(dict.keys, [s1, s2, s3])

from functools import reduce
data = reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3])) #迭代所有map中的集合，进行与操作，两个两个间交集
print(data)
