#案例引入
#1.过滤掉用户输入中前后多余的空白字符：
#   '  nick2008@gmail.com   '
#2.过滤某windows下编辑文本中的'\r':
#   'hello world\r\n'




#案例解决：
#方法一：字符串strip(),lstrip(),rstrip()方法去掉字符串两端字符。
#方法二：删除单个固定位置的字符，可以使用切片+拼接的方式。
#方法三：字符串的replace()方法或者正则表达式re.sub()删除任意位置字符




#方法一：（去除前后空格，前空格，后空格）注意：不能删除中间的空格
s = '  abc  123   '

s1 = s.strip() #去除前后空格
s2 = s.lstrip() #去除左空格
s3 = s.rstrip() #去除右空格

# print(s1)
# print(s2)
# print(s3)

ss = '---abc+++'
ss1 = ss.strip('-+') #去掉所有-和+
# print(ss1)



#方法二：（切片+拼接）
a = 'abc:123'
a1 = a[:3] + a[4:] #去掉":"
# print(a1)



#方法三：（字符串的替换或者正则表达式的替换）
#字符串：
b = '\tabc\t123\txyz'
b1 = b.replace('\t', '') #替换成空，但是只能替换一个
# print(b1)


#正则：
import re
n = '\tabc\t123\txyz\ropq\r'
n1 = re.sub('[\t\r]', '', n) #可以匹配多个字符
# print(n1)