#案例引入：
#某项目中，我们从传感器采集数据，每收集到1G数据后，做数据分析，最终只保存分析结果。
#这样很大的临时数据如果常驻内存，将消耗大量内存资源，我们可以使用临时文件存储这些
#临时数据（外部存储）
#
#临时文件不用命名，且关闭后会自动删除



#解决方法：
#使用标准库中tempfile下的TemporaryFile(不能在系统中找到)，NamedTemporaryFile(带名字，可以在系统中找到)
#临时文件关闭后会自动删除掉，如果不想关闭后删除，只需要指定参数delete=false即可，这样可以在多个进程下访问多个文件




from tempfile import TemporaryFile, NamedTemporaryFile

f = TemporaryFile()
f.write('abcdef' * 1000000)
f.seek(0)
f.reed(100)


ntf = NamedTemporaryFile()
print(ntf.name)


