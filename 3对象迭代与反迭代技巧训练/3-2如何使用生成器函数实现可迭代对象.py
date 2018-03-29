#案例引入
#实现一个可迭代对象的类，它能迭代出给定范围内所有素数：
#pn = PrimeNumbers(1,30)
#for k in pn:
#   print(k)
#
#输出结果：2 3 5 7 11 13 17 19 23 29


#解决方案：
#将该类的__iter__方法实现成生成器函数，每次yield返回一个素数



#生成器函数包含可迭代对象和迭代器


class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        if k < 2:
            return False
        
        for i in range(2, k):
            if k % i == 0:
                return False #如果不等于0则不是素数，舍弃
        return True #则说明 k % 2 不等于0,这就说明k是素数

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k #当返回true时，就输出该数

#测试
for x in PrimeNumbers(1, 100):
    print(x)