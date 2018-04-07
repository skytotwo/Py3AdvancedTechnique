#python2.x 写入文件前对unicode编码，读入文件后对二进制字符串编码
#python3.x open函数指定’t’的文本模式,encoding指定编码格式




#python2.x 写入文件前对unicode编码，读入文件后对二进制字符串编码
#默认是通过unicode编码写进文件，通过unicode解码读出文件可以 
#可以通过str1.encode(“utf8”)和str1.decode(“utf8”)解开文件
#
str1=u"你好，我爱中国"

f=open("xx.txt",'w')
f.write(str1.encode('utf8'))
f.close()
f=open("xx.txt",'r')
t=f.read()
#print t.decode('utf8')  #==>你好，我爱中国






#python3.x open函数指定’t’的文本模式,encoding指定编码格式

f = open("text2.txt","wt",encoding='utf-8')
f.write("hello,world")
f.close()

fr = open("text2.txt","rt",encoding='utf-8')
print(fr.read())
#hello,world
