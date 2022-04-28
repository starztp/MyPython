#读取文件内容并关闭资源
#r参数调用open只能读，不能写
file=open("a.txt","r")
print(file.readlines())
file.close()

#创建a.txt文件并写入内容abc,w参数调open只能写，不能读
file1=open("a.txt","w")
file1.write("abc")
file1.close()
#文件已存在时替换原文件的内容
file2=open("a.txt","w")
file2.write("bbb")
file2.close()

#a.txt已存在时使用a参数调用open则在原文件中追加
file3=open("a.txt","a")
file3.write("123")
file3.close()

#复制文件
src_file=open("a.txt","rb")
target_file=open("copy.txt","wb")
#读取原文件全部内容并写入target_file
target_file.write(src_file.read())
target_file.close()
src_file.close()


#常用方法
file4=open("b.txt","r",encoding="utf-8")
#read读取文件全部内容
print("读取文件全部内容：\n"+file4.read())
file4.close()
file4=open("b.txt","r",encoding="utf-8")
print("读取文件指定最大可读取字符：\n"+file4.read(2))
file4.close()
file4=open("b.txt","r",encoding="utf-8")
print("readline:"+file4.readline())
file4.close()
file4=open("b.txt","r",encoding="utf-8")
print("readlines:",file4.readlines())