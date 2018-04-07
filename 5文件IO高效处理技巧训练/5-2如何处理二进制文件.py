#案例引入
#wav是一种音频文件格式，音频文件为二进制文件，wav文件由头部信息和音频采样数据构成，
# 前44个字节为头部信息，包括声道数，采用频率PCM位宽等等，后面则是音频采样数据。
#
#使用python，分析一个wav文件头部信息，处理音频数据




#解决方案:
#open函数以二进制模式打开,指定mode 参数为 'b'
#二进制数据可以通过readinto，读入到提前分配好的buffer中，便于数据处理,
#buffer=array.array('i',(0 for _x in range(n)) 申请一片连续的为0的空间，数据类型是短整型
#buffer.tofile(open("testNew.wav",'wb') 可以直接写入到二进制文件 

#解析二进制数据可以通过标准库中的struct模块的unpack方法
#fr=open("test.wav",'rb')
#info=fr.read()
#struct.unpack("h",info[22:24])




#处理
#使用struct.unpack可以将二进制解开
# import array
# array('c','I love china') #这个是字符  第一个参数表示的哪种数据类型
# buf=array('i','33') #是short 整型 数据类型
# buf.tofile(open('test.txt','wb') #数组可以直接输出到文件


import struct
import array

f=open('test5-2.wav','rb')
info=f.read(44)
print (struct.unpack('h',info[22:24]))  #(2,)  声道数
print (struct.unpack('i',info[24:28]))  #(44100,) 采用频率
f.seek(0,2) #将文件指针指向末尾 0是起始，1是当前，2是末尾
print ("total num is %d",f.tell()) #报告文件位置

n=(f.tell()-44)//2  #读出文件除去文件头的内容,也就是采用数据部分
buf=array.array('h',(0 for _ in range(n)))
f.seek(44) #将指针指向文件数据部分
f.readinto(buf) #将数据读入buf

#将每一个采用缩小8倍，使得声音变小
for i in range(n):
    buf[i] //=8    #//代表的是地板除法，返回int值
fw=open('demo.wav','wb')
fw.write(info)
buf.tofile(fw)
fw.close()