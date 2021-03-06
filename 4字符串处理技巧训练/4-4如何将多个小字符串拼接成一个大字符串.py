#案例引入
#在设计某网络程序时，我们自定义了一个基于UDP的网络协议。按照固定次序向服务器传递一系列参数：
#...
# 在程序中我们将多个参数按次序收集到列表中：
#["<0112>","<32>","<1024*768>","<60>","<1>","<100.0>","<500.0>"]
#最终我们要把各个参数拼接成一个数据进行发送：
#"<0112><32><1024*768><60><1><100.0><500.0>"





#解决方案
#方法一：迭代列表，连续使用“+”操作依次拼接每一个字符串
#方法二：使用str.join()方法，更加快速的拼接列表中的所有字符串（推荐）




#方法一：（列表长的时候，开销巨大，造成浪费，不建议）
pl = ["<0112>","<32>","<1024*768>","<60>","<1>","<100.0>","<500.0>"]
s = ''

for p in pl:
    s+=p

#print(s)



#方法二：
c = ''.join(["<0112>","<32>","<1024*768>","<60>","<1>","<100.0>","<500.0>"])
print(c)



#在列表元素类型不一时候，可以使用生成器表达式对列表元素进行遍历转换格式
l = ['abc', 123, 45, 'xyz']

a = ''.join((str(x) for x in l)) #列表解析式用小括号括起来就变成了生成器解析式，这样做能在长列表的时候节省开销
print(a)