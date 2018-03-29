#案例引出
#很多应用都有浏览用户历史记录的功能：如浏览器查看历史记录等...


#以下是一个猜数字的小游戏：
#首先随机生成一个100以内的数字，用户输入值来猜，根据对比大了还是小了来多次输入猜测，知道最后猜中
#通过deque双端队列来存储输入历史，先设定好队列的容量，存入的值会一直保持这个容量，多了会吧第一个挤出去。
#通过pickle来序列化队列，存储在文件中，下次打开时，用pickle反序列化读取文件的队列，历史数据就不会丢失了

from random import randint
from collections import deque
import pickle

N = randint(0, 100)
history = deque([],5) #初始化建立一盒队列，用于存储输入历史信息

try:
    pickle_file = open("my_list.pkl", "rb") #开始程序就默认先看下是否有序列化的队列文件，有就打开
    history = pickle.load(pickle_file)  #将值赋给初始化的队列
except:
    print("无文件")


def guess(k):
     if k==N:
        print("right")
        return True
     if k>N:
        print("%s is greater than N" % k)
     else:
        print("%s is less than N" % k)
     return False

while (True):
    line =input("please input a numble...")
    if line.isdigit(): #判断输入是否是数字字符
        k = int(line) 
        history.append(k) #输入后就将输入值存至队列中
        if guess(k):
            pickle_file = open("my_list.pkl", "wb") #当输入正确后，将队列中的数据序列化保存
            pickle.dump(history, pickle_file)
            pickle_file.close()
            break
    elif line == 'history' or line == 'h?':
        print (list(history))