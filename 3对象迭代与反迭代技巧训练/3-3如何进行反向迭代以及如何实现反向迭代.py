#案例引出
#实现一个连续浮点数发生器FloatRange(和range类似)，
# 根据给定范围(start, end)和步进值(step)产生一系列连续浮点数，
#如迭代FloatRange(3.0,4.0,0.2)可产生序列：
#
#正向：3.0 - 3.2 - 3.4 - 3.6 - 3.8 - 4.0
#反向：4.0 - 3.8 - 3.6 - 3.4 - 3.2 - 3.0



#解决方案
#实现反向迭代协议的__reversed__方法，他返回一个方向迭代器

#示例
l = [1,2,3,4,5,6]
#iter()实现正向迭代
for c in iter(l):
    print(c)

#reversed()实现方向迭代
for x in reversed(l):
    print(x)
#reversed方法用于返回一个逆向排序的的迭代器对象，和reverse不一样，内建的reverse是列表的原地反转





#解决：利用生成器

class FloatRange():
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self): #使用生成器产生正向迭代器
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):#使用生成器生成反向迭代器
        t = self.end
        while t >=self.start:
            yield t
            t -= self.step



#正向迭代
for a in FloatRange(1.0, 4.0, 0.5): 
    print(a)
#反向迭代
for b in reversed(FloatRange(1.0, 4.0, 0.5)):
    print(b)