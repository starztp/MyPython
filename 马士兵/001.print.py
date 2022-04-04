# 作者: 张天由

#输出字符串
print("hello world")

#输出数字
print(123)
print(10.11)

#输出表达式结果
print(1+1)

#将内容输出到文件中
#第1个参数是文件名，第二个参数是写入模式，这里的a+表示文件不存在就创建，文件存在就在文件内容后面继续追加
temp=open("/Users/tianyou/Developer/Myjobs/python/text.txt","a+")
print('hello',file=temp)
temp.close

#不换行输出
print("hello","world","python")