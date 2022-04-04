# 作者: 张天由
#元祖内的对象是不可变的
#元祖的创建
#使用()创建元祖
yuanzu1=("tianyou","tianyou1","tianyou2")
print(yuanzu1)
print(type(yuanzu1))    #<class 'tuple'>

#使用内置函数tuple创建元祖
yuanzu2=tuple(("tianyou","tianyou1","tianyou2"))
print(yuanzu2)
print(type(yuanzu2))    #<class 'tuple'>
#定义只包含一个元素的元祖时需要加逗号
yuanzu3=("tianyou",)
print(yuanzu3)
print(type(yuanzu3))    #<class 'tuple'>

#空元祖的创建方式
yuanzu4=()
yuanzu5=tuple()

#遍历元祖
yuanzu6=tuple(("tianyou","tianyou1","tianyou2","tianyou3"))
for item in yuanzu6:
    print(item)