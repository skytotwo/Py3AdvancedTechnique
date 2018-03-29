#案例引出
# 某随机序列[12,5,6,4,6,5,5,7,...]中，找到出现次数最高的3个元素，它们出现的次数是多少？


#解决方法
#使用collections.Counter对象，将序列传入Counter的构造器，得到Counter对象是元素频度的字典，
#Counter.most_common(n)方法的到的频度最高的n个元素的列表


from random import randint
from collections import Counter

data = [randint(0,30) for x in range(30)]
c = Counter(data) #py3中是倒叙排列的，频率由大到小
c.most_common(3) #找出出现频率最高的3个元素