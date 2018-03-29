#案例引出
#有某个文本文件，我们想读取其中某范围的内容，如100~300行之间的内容，
#python中文本文件是可迭代对象，我们是否可以使用类似列表切片的方式得到
#一个100~300行文件内容的生成器
#
#f=open('var/log/dmesg')
#f[100:300] 可以么？




#解决方案
#使用标准库中的itertools.islice，它能返回一个迭代对象切片的生成器


from itertools import islice

f = open('test3-4.txt', 'r')
# print(f.read())
# f.seek(0)


#islice用于切片操作
#islice(iterable, [start,] stop [, step]) --> islice object
# islice(f,0,10)        #取文件的前10行
# islice(f,100,300)     #生成 文件 100 到  300 行的生成器,不包含第300行
# islice(f,500)         #生成500行以内的生成器
# islice(f,500,None)    #生成500行以后的生成器
for line in islice(f, 10):
    print(line)


#islice是会对迭代对象进行消耗的
l = [x for x in range(20)]
t = iter(l)
for x in islice(t,5,10):
    print(x)
#此处会打印5到9，其实前面的1到4都有迭代，只是被islice抛弃了，直到迭代到5，所以t是经过迭代的，它的数据被消耗了


#下面可以接着迭代t，发现会接着从10开始迭代，这就说明islice是会消耗迭代数据的，
# 所以如果每次需要重新迭代的话，就需要在islice迭代完，重新生成迭代数据才行
for c in t:
    print(c)