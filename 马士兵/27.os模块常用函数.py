#os模块是python内置的与操作系统和文件系统相关的模块
import os
#system入参是系统指令
# os.system()
#直接调用可执行文件，参数是文件路径
# os.startfile()
#打印当前的工作目录
print(os.getcwd())
#列出目录下的所有文件
print(os.listdir("../马士兵"))

#创建目录
os.mkdir("测试目录")
#创建多级目录
os.makedirs("测试目录1/aaa")
#删除目录
os.rmdir("测试目录")
#删除多级目录
os.removedirs("测试目录1/aaa")
#更换工作目录
os.chdir("/Users/tianyou")
print(os.getcwd())
os.chdir("/Users/tianyou/Developer/Myjobs/python/MyPython/马士兵")


#os.path模块常用方法
#获取文件的绝对路径
print(os.path.abspath("27.os模块常用函数.py"))    #/Users/tianyou/Developer/Myjobs/python/MyPython/马士兵/27.os模块常用函数.py
#判断文件是否存在
print(os.path.exists("27.os模块常用函数.py"))     #True
#将目录和文件拼接
print(os.path.join("../马士兵","abc"))         #../马士兵/abc
#将目录和文件分开
print(os.path.split("../马士兵/27.os模块常用函数.py"))   #('../马士兵', '27.os模块常用函数.py')
#将文件和后缀名分开
print(os.path.splitext("27.os模块常用函数.py"))         #('27.os模块常用函数', '.py')
#从一个目录中提取文件名
print(os.path.basename("../马士兵/27.os模块常用函数.py"))    #27.os模块常用函数.py
#从一个路径中提取文件路径，不包含文件名
print(os.path.dirname("../马士兵/27.os模块常用函数.py"))     #../马士兵
#判断是否为目录
print(os.path.isdir("../马士兵/27.os模块常用函数.py"))       #False