#字符串驻留机制
#定义2个相同的字符串，它们的内存地址都是一样的
a="python"
b="python"
print(a,id(a))  #python 4342023088
print(b,id(b))  #python 4342023088

#-5-256之间的整数数字也是可以驻留的
a=-5
b=-5
print(a,id(a))  #-5 4310433840
print(b,id(b))  #-5 4310433840

a=-6
b=-6
print(a,id(a))  #-6 4306942832
print(b,id(b))  #-6 4306942832

#字符串常用操作
s="hello,hello"
#查找lo第一次出现的位置
print(s.index("lo"))    #3
print(s.find("lo"))     #3
#查找lo最后一次出现的位置
print(s.rindex("lo"))   #9
print(s.rfind("lo"))    #9
#没找到子串就返回-1
print(s.find("k"))      #-1
print(s.rfind("k"))     #-1

#字符串大小写转换操作
str="hello,python"
#将字符串中所有字母转成大写，并产生一个新的字符串对象
strUpper=str.upper()
print(strUpper)      #HELLO,PYTHON
#将字符串中所有字母转成小写，并产生一个新的字符串对象
strLower=strUpper.lower()
print(strLower)     #hello,python

str1="HelLo,PythOn"
#将字符串中大小写字母颠倒（大写转小写，小写转大写）
print(str1.swapcase())  #hELLO,pYTHON
#把每个单词的第一个字符转换为大写，剩余字符转换为小写
str2="hello,python"
print(str2.title()) #Hello,Python


#字符串内容对齐操作
#center()居中对齐，第一个参数指定宽度；第二个参数指定填充符，是可选的，默认是空格。如果设置宽度小于实际宽度则返回原字符串
s="hello,python"
#这里指定宽度是20，原字符串s的宽度是12，由于是居中对齐所以左右两边各填充4个*
print(s.center(20,"*")) #****hello,python****

#ljust()左对齐，第一个参数指定宽度；第二个参数指定填充符，是可选的，默认是空格。如果设置宽度小于实际宽度则返回原字符串
print(s.ljust(20,"*"))  #hello,python********

#rjust()右对齐，第一个参数指定宽度；第二个参数指定填充符，是可选的，默认是空格。如果设置宽度小于实际宽度则返回原字符串
print(s.rjust(20,"*"))  #********hello,python

#zfill()右对齐，左边用0填充，该方法只接收一个参数，用于指定字符串的宽度，如果指定的宽度小于字符串的长度，返回字符串本身
print(s.zfill(20))  #00000000hello,python

#字符串劈分
#split()
#从字符串左边开始皮粉，默认皮粉字符是空格字符串，返回值都是一个列表
#通过参数sep指定劈分字符串的劈分符
#通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分后，剩余的子串会单独作为一部分
str1="hello,world"
lst=str1.split(sep=",")
print(lst)          #['hello', 'world']
str2="hello,world,aaa"
lst1=str2.split(sep=",",maxsplit=1)
print(lst1)         #['hello', 'world,aaa']

#rsplit()
#从字符串右边开始劈分，默认的劈分字符串是空格，返回值是一个列表
#通过参数sep指定劈分字符串的劈分符
#通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分后，剩余的子串会单独作为一部分

str1="hello,world"
lst=str1.rsplit(sep=",")
print(lst)          #['hello', 'world']
str2="hello,world,aaa"
lst1=str2.rsplit(sep=",",maxsplit=1)
print(lst1)         #['hello,world', 'aaa']

#判断字符串操作的方法
# isidentifier(),判断指定的字符串是不是合法的标识符（合法的标识符指的是字母，数字，下划线_）
s="hello,python"
print(s.isidentifier())     #False

# isspace(),判断指定的字符串是否全部由空白字符组成（回车、换行、水平制表符）
print("\t".isspace())       #True

# isalpha(),判断指定字符串是否全部由字母组成
print(s.isalpha())          #False

# isdecimal(),判断指定字符串是否全部由数字组成
num="123"
print(num.isdecimal())      #True

# isalnum(),判断指定字符串是否全部由字母和数字组成
str1="abc123"
print(str1.isalnum())       #True


#字符串替换与合并
# replace()，第一个参数指定被替换的子串，第二个参数指定替换子串的字符串，该方法返回替换后得到的字符串，替换前的字符串不发生变化，调用该方法时可以通过第3个参数指定最大替换次数
s="hello,python,python"
print(s.replace("python","java"))   #hello,java,java
print(s.replace("python","java",1)) #hello,java,python

# join(),将列表或元祖中的字符串合并成一个字符串
lst=["hello","java","python"]
print("|".join(lst))                #hello|java|python
print("".join(lst))                 #hellojavapython

#字符串的切片操作
#字符串时不可变类型，切片不具备增删改等操作，切片操作将产生新的对象
s="hello,python"
#取出s的0-4下标值组成一个新的字符串
s1=s[0:5]
print(lst)      #hello
#从s的第6个下标开始取值，直到最后一个下标，组成一个新的字符串
s2=s[6:]
print(s2)       #python

#步长为负数时切片
#没有写开始和结束索引下标时，步长又是负数，则从最后一个元素开始，到第一个元素结束
print(s[::-1])  #nohtyp,olleh

#负数索引从字符串末尾开始数，字符串最后一位索引是-1
print(s[-6::1]) #python

#格式化字符串
#%占位符
name="张天由"
age=18
print("我叫%s,今年%d岁" % (name,age))    #我叫张天由,今年18岁
#10表示的是宽度
print("%10d" % 99)      #        99
#宽度10，保留3位小数
print("%10.3f" % 3.1415926)   #     3.142

#{}
print("我叫{0},今年{1}岁".format(name,age))  #我叫张天由,今年18岁
#.3表示一共3位数
print("{0:.3}".format(3.1415926))           #3.14
#3f表示3位小数
print("{0:.3f}".format(3.1415926))          #3.142
#3f表示3位小数，10表示宽度
print("{:10.3f}".format(3.1415926))          #     3.142

#f-string
print(f"我叫{name},今年{age}岁")     #我叫张天由,今年18岁

#字符串编码与解码
#编码
s="测试编码"
print(s.encode(encoding="GBK"))     #b'\xb2\xe2\xca\xd4\xb1\xe0\xc2\xeb',GBK中一个中文占2个字节
print(s.encode(encoding="UTF-8"))   #b'\xe6\xb5\x8b\xe8\xaf\x95\xe7\xbc\x96\xe7\xa0\x81'，UTF8中一个中文占3个字节

#解码
byte=s.encode(encoding="GBK")
print(byte.decode(encoding="GBK"))  #测试编码
