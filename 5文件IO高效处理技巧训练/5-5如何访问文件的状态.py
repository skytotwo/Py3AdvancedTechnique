#案例引入：
#在某些项目中，我们需要获得文件状态，例如：
#1、文件的类型（普通文件，目录，符号链接，设备文件...）
#2、文件的访问权限
#3、文件的最后访问/修改/节点状态更改时间
#4、普通文件的大小
#.....




#解决方法：
#1、系统调用：标准库中os模块下的三个系统调用stat,fstat,lstat获取文件状态
#2、快捷函数：标准库中os.path下一些函数，使用起来更加简洁



#系统调用 表中库os模块中的三个系统调用 stat fstat lstat获取文件状态 
#如果是符号链接文件 stat之后渠到的是指向的文件属性 , 
#lstat才是获取到符号链接文件的属性 
#fstat需要的文件描述符 f=open(“test.txt”,”r”) f.fileno

#快捷函数 标准库中的os.path 下一些函数，使用起来更加简洁



#通过os.path下的一些方法
import os
import stat
import time
s = os.stat('a.txt')
print (s)
print (stat.S_ISDIR(s.st_mode))
print (s.st_mode &stat.S_IRUSR)   #访问权限
print (time.localtime(s.st_atime))
print (s.st_size)

if os.path.isdir('a.txt'): #是否是文件夹
    print ("ok")

if os.path.isfile('a.txt'): #是否是文件
    print ("ok")

if os.path.getatime('a.txt'): #获取文件最后访问时间   mtime是最后修改时间 ctime是创建时间
    print (os.path.getatime('a.txt'))

if os.path.getsize('a.txt'): #获取文件大小
    print (os.path.getsize('a.txt'))