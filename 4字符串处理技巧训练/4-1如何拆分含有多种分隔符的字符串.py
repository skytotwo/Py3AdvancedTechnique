#案例引入
#我们要把某个字符串依据分隔符拆分不同的字段，该字段包含多种不同的分隔符，例如：
#
# s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
#其中<,>,<;>,<|>,<\t>都是分隔符号，如何处理？



#解决方案
#方法一：连续使用str.split()方法，每次处理一种分隔符号
#方法二：使用正则表达式的re.split()方法，一次性拆分字符串







#解决方案一


s = "ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz"
s.split(';')

res = s.split(';')
print(res)

#map(lambda x: x.split('|'), res)
#为使得map得出的序列是一个一维的序列，这里将x.split结果添加到一个新的列表里：
t=[]
c = list(map(lambda x: t.extend(x.split('|')), res))
#此时t就是一个新的分隔后的一维列表，此时再对t进行分割
print(t)
#以此类推~得到最终的结果

#也可使用下列函数解决：
def mySplit(s, ds):
    res=[s]

    for d in ds:
        t=[]
        list(map(lambda x: t.extend(x.split('|')), res))
        res = t
    
    return [x for x in res if x] #对结果去除空值

s1 = "ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz"
print(mySplit(s1, ';,|\t'))





#解决方案二：(推荐)
import re

s2 = "ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz"
c = re.split('[,;\t|]+', s2)
print(c)
