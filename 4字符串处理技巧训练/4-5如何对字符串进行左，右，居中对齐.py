#案例引入
#某个字典存储了一系列属性值，
#{
#   "lodDist":100.0,
#   "SmallCull":0.04,
#   "DistCull":500.0,
#   "trillinear":40,
#   "farclip":477
# }
#
#在程序中，我们想以以下工整的格式将其内容输出，如何处理？
#SmallCull :0.04
#farclip   :477
#lodDist   :100.0
#DistCull  :500.0
#trillinear:40




#解决方法：
#方法一：使用字符串的str:ljust(),str.rjust(),str.center()进行左，右，居中对齐。
#方法二：使用format()方法，传递类似'<20','>20','^20'参数完成同样任务。




#方法一：
s = 'abc'
s1 = s.ljust(20) #左对齐，右边填充空白
s2 = s.rjust(20) #右对齐，左边填充空白
s3 = s.center(20)#中对齐，左右填充空白

# print(s1)
# print(s2)
# print(s3)

s4 = s.ljust(20, 'x') #左对齐，右边填充x
s5 = s.rjust(20, 'x') #右对齐，左边填充x
s6 = s.center(20, 'x')#中对齐，左右填充x

# print(s4)
# print(s5)
# print(s6)



#方法二：
#使用format()格式化字符串。
a = 'abc'

a1 = format(a, '<20') #左对齐，右边填充空白
a2 = format(a, '>20') #右对齐，左边填充空白
a3 = format(a, '^20') #中对齐，左右填充空白

# print(a1)
# print(a2)
# print(a3)





#案例：
d = {
    "lodDist":100.0,
    "SmallCull":0.04,
    "DistCull":500.0,
    "trillinear":40,
    "farclip":477
    }

#先获取最长的k的值
m = max(map(len, d.keys()))
print(m)

for k in d:
    print(k.ljust(m), ':', d[k]) #左对齐，将最长的值最为值作为参数传入