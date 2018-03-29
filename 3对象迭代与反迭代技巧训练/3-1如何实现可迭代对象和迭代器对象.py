#案例引入
#某软件要求，从网络抓取各个城市气温信息，并依次显示：
#北京：15~20
#天津：17~22
#...
#如果一次抓去所有城市天气再显示，显示第一个城市气温时，会有很高的延迟，并且浪费存储空间。
#我们期望以“用时访问”的策略，抓取一条就显示一条，并且能把所有城市气温封装到一个对象里，
#可用for语句进行迭代，如何实现？



#解决方案：
#step1：实现一个迭代器对象WeatherIterator，next方法没次返回一个城市气温
#step2：实现一个可迭代对象WeatherIterable，__iter__方法返回一个迭代器对象





#以下为演示迭代与迭代器原理
l = [1,2,4,6,4]
s = "abcdefg"


#迭代的过程，首先是被迭代的必须是一个可迭代的数据
#然后该数据调用__iter__,如果没有则寻找__getitems__方法。从而获取迭代器。也就如下t = iter(l)一样，
# t为迭代器对象，
t = iter(l)
#迭代器对象调用__next__方法或者下一个迭代数据，如下：
print(t.__next__())
#for 循环的工作流程就是先判断是否课迭代，然后给该数据获取一个迭代器。然后不断调用__next__方法迭代下一个数据。如下：
for x in l:
    print(x)





#方案

import requests
def getWeather(city):
    r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
    data = r.json()['data']['forecast'][0]
    return '%s : %s , %s ' % (city, data['low'], data['high'])

#[u'北京', u'上海', u'广州', u'长春']
# print(getWeather(u'北京'))
# print(getWeather(u'长春'))
#北京 : 低温 -1℃ , 高温 10℃
#长春 : 低温 -6℃ , 高温 2℃



from collections import Iterable, Iterator

#迭代器对象
class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities #迭代城市
        self.index = 0 #迭代计数

    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s : %s , %s ' % (city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities): #判断如果迭代的是最后一个
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


#可迭代对象
class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities
    
    def __iter__(self):
        return WeatherIterator(self.cities)


#[u'北京', u'上海', u'广州', u'长春']
for x in WeatherIterable([u'北京', u'上海', u'广州', u'长春']):
    print(x)


#解决了两个问题，“用时访问”和将迭代数据封装起来。
#这里的思路是：将数据封装，用Iterable的__iter__生成迭代器，并将数据传入迭代器，在迭代器中调用重写的__next__
#方法一遍一遍的迭代调用下载天气请求并打印出来。

#注意：继承是便于理解，不继承的话直接用__next__和__iter__就行了，在迭代器中重写这两个。