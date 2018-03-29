#案例引出
#学生信息系统中数据为固定格式：
#(名字,年龄,性别,邮箱地址...)
#
#学生数量很大，为了减小存储开销，对每个学生信息用元组表示：
#('Jim',16,'male','jim8721@gmail.com')...
#
#访问时，我们使用索引（index）访问,大量索引会降低程序可读性,如何解决这个问题？



#解决方法
#方案1：定义类似于其他语言的枚举类型，也就是定义一系列数值常量
#方案2：使用标准库中collections.namedtuple替代内置tuple



#方案1
NAME = 0
AGE = 1
SEX = 2
EMAIL = 3
#或者这样拆包写：NAME,AGE,SEX,EMAIL = range(4)

student = ('Jim',16,'male','jim8721@gmail.com')
student[NAME]
student[AGE]



#方案2
from collections import namedtuple
#namedtuple会返回一个内置元组的子类
#给创建的子类取一个名字Student,返回一个子类，类似于类的工厂
Student = namedtuple('Student', ['name','age','sex','email']) 

s = Student('Jim', 16, 'male', 'jim8721@gmail.com')#将参数传入
s2 = Student(name='Jim', age=16, sex='male', email='jim8721@gmail.com')#也可以用关键字传参

name = s.name
age = s.age