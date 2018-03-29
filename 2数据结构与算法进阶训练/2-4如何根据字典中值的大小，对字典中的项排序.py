#案例引出
#某班英语成绩以字典形式存储为：
#{'Lilei':79,'Jim':88,'Lucy':92...}
#根据成绩高低，计算学生排名



#问题解决
#使用内置函数sorted
#1.利用zip将字典数据转化为数组
#2.传递sorted函数的key参数



from random import randint

#方法1
data = {x:randint(60,100) for x in 'xyzabc'} #生成成绩单
data2 = zip(data.values(),data.keys()) #使用zip将字典键值调换顺序
data3 = {k:v for k,v in data2 } #zip对象遍历出字典
data4 = sorted(data3) #对字典进行排序



#方法2
data5 = sorted(data.items(), key=lambda x:x[1]) #将字典的每一项传入lambda函数中，并决定哪一项作为sorted中的key
print(data5)