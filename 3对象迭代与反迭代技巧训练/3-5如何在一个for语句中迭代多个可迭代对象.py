#案例引出
# 1.某班学生期末考试成绩，语文，数学，英语分别存储在3个列表中，同时迭代三个列表，计算每个学生的总分（并行）
# 2.某年级有4个班，某次考试每班英语成绩分别存储在4个列表中，依次迭代每个列表，统计全学年成绩高于90分的人数（串行）



#解决方案
#并行：使用内置函数zip，它能将多个可迭代对象合并，每次迭代返回一个元组
#串行：使用标准库中的itertools.chain，它能将多个可迭代对象连接



from random import randint

#生成学生分数
chinese = [randint(60, 100) for c in range(40)]
math = [randint(60, 100) for m in range(40)]
english = [randint(60, 100) for e in range(40)]



#案例一：（并行————同时迭代）
#使用引索：(因为三个的总数都一样，可以一起遍历相加)
#局限性————生成器不支持引索
for i in range(len(chinese)):
    chinese[i]+ math[i]+ english[i]


#（并行方式二）：
#使用zip：zip()方法用于返回由各个可迭代参数共同组成的元组。

total = []

#for循环使用拆包的形式得到每一次循环的各个元组的项，之和相加就是总成绩，组成列表返回
for c,m,e in zip(chinese, math, english):
    total.append(c+m+e)




#案例二：（串行————依次迭代）
from itertools import chain

#先生成四个班的成绩
one = [randint(60, 100) for c in range(40)]
two = [randint(60, 100) for m in range(45)]
three = [randint(60, 100) for e in range(60)]
four = [randint(60, 100) for c in range(70)]

#将4个迭代对象串联起来，依次迭代
# for i in chain(one, two, three, four):
#     print(i)

count = 0
for a in chain(one, two, three, four):
    if a > 90:
        count += 1
print(count)