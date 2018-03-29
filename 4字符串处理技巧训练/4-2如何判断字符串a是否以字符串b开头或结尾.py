#案例引入
#某文件系统目录下有一系列文件：
#quicksort.c
#graph.py
#heap.java
#install.sh
#stack.cpp
#
#....
#编写程序给其中所有.sh文件和.py文件加上用户可执行权限





#解决方法
#使用字符串的str.startswith()和str.endswith()方法。
#注意：多个匹配时参数使用元组



#方法：
lis = ['e.py', 'g.sh', 'd.java', 'h.c', 'f.cpp', 'a.sh', 'c.h', 'b.py'] #先生成文件

#多个参数的时候必须是元组
lia = '.sh'
s = lia.endswith(('.sh', '.java'))
print(s)


lisdata = [name for name in lis if name.endswith(('.sh', '.java'))]
print(lisdata)