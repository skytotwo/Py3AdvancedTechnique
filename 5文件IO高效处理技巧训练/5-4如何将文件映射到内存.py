#案例引入：
#1、在访问某些二进制文件时，希望能把文件映射到内存中，可以实现随机访问。（framebuffer设备文件）
#2、某些嵌入式设备，寄存器被编址到内存地址空间，我们可以映射/dev/mem某范围，去访问这些寄存器。
#3、如果多个进程映射同一个文件，还能实现进程通信的目的。
#



#解决方法：
#使用标准库中mmap模块中的mmap()函数，它需要一个打开的文件描述符作为参数


#Windows: mmap(fileno, length[, tagname[, access[, offset]]])              
                                                                                                               
#Unix: mmap(fileno, length[, flags[, prot[, access[, offset]]]])           
                                                                           

#文件描述符获取方法

import os
os.open()
f=open("test.txt",20) 
f.fileno  #==>获得文件描述符

# 使用dd 创建大小为1M的文件

# dd if=/dev/zero of=test.bin bs=1024 count=1024
# od -x test.bin 
# 0000000 0000 0000 0000 0000 0000 0000 0000 0000
# *
# 4000000

import os 
import mmap
f=open("test.bin","r+b")
m=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_WRITE)
m[0]='\x88'  #赋值
m[4:8]='\xad'*4  #切片赋值

m2=mmap.mmap(f.fileno(),mmap.PAGESIZE * 8,access=mmap.ACCESS_WRITE,offset=mmap.PAGESIZE * 4)
m2[:0x1000]='\xaa'* 0x1000



#########################################################

# od -x test.bin
# 0000000 0088 0000 adad adad 0000 0000 0000 0000
# 0000020 0000 0000 0000 0000 0000 0000 0000 0000
# *
# 0040000 aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa
# *
# 0050000 0000 0000 0000 0000 0000 0000 0000 0000
# *
# 4000000