#用with语句不需要关闭file，跳出with语句时会自动释放资源，类似于java中的try
with open("a.txt","r") as file:
    print(file.read())