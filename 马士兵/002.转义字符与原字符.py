# 作者: 张天由

# /表示转义
#注意：最后一个字符不能是反斜杠\，但可以是2个斜杠\\

# \n表示换行
print("hello\nworld")

#\t表示4个空格的位置
print("hello\tworld")

#\r表示回车，只输出最后一个\r后面的值
print("hello\rworld\r333")

#\b表示退一格
print("hello\bworld")

#输出结果包含双引号，单引号等特殊字符
print("老师说：\"大家好\"")

#原字符，不希望字符串中的转义字符起作用就使用原字符，使用方式就是在字符串前加r或R
print(r"hello\nworld")