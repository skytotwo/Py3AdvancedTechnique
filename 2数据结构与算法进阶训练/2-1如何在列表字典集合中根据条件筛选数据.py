#案例引出
#过滤掉列表[3,9,-1,10,20,-2...]中的负数
#筛选出字典{'LiLei':79,'Jim':88,'Lucy':92...}中值高于90的项
#筛选出集合{77,89,32,20...}中能被3整除的元素


#解决方案
#列表（匿名函数）—— filter函数：filter(lambda x:x>=0,data)
#列表（列表解析）—— [x for x in data if x>=0]
#字典解析—— {k:v for k,v in d.items() if v>90}
#集合解析—— {x for x in s if x%3 ==0}

from random import randint

data = [randint(-10,10) for x in range(10)] #生成10个范围在-10至10之间元素的列表

#filter函数，接收两个参数，第一个参数可以是一个函数也可以是none，如果是函数的话，
#则将第二个可迭代数据中的每一个元素作为函数的参数进行计算，把返回的true值筛选出来；
#如果第一个参数是none，则直接将第二个参数中的true值筛选出来
data1 = filter(lambda y: y>=0, data)



#列表解析
data2 = [z for z in data if z>=0]

#一般来说，列表解析速度比匿名函数更快



#字典解析
zidian = {x:randint(-10,10) for x in range(10)}
zidian2 = {k:v for k,v in zidian.items() if v>=0}#列表解析字典



#集合解析
jihe = {randint(-10,10) for c in range(10)}
jihe2 = {n for n in jihe if n%3==0}