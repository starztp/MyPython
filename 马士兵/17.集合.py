# 作者: 张天由

#集合中不允许有重复元素
#集合的创建
#使用{}创建
col = {1,2,3,4,5}
print(col)              #{1, 2, 3, 4, 5}
print(type(col))        #<class 'set'>

#使用set()内置函数
col1=set(range(6))
print(col1)             #{0, 1, 2, 3, 4, 5}
print(type(col1))       #<class 'set'>

col2={1,1,2,2,3,3}
print(col2)             #{1, 2, 3}
print(type(col2))       #<class 'set'>

#定义空集合
col3=set()

#判断元素是否在集合中存在
col4={1,2,3}
print(1 in col4)    #True
print(5 in col4)    #False

#向集合中添加元素
col5={100,50,200,300}
col5.add(80)
print(col5)         #{100, 200, 300, 80, 50}
#向集合中添加指定内容
#向集合中添加其它集合
col5.update({22,33,44})
print(col5)         #{33, 100, 200, 300, 44, 80, 50, 22}
#向集合中添加列表
col6={100,50,200,300}
col6.update([22,33,44]) #{33, 100, 200, 300, 44, 50, 22}
print(col6)

#向集合中添加元祖
col7={100,50,200,300}
col7.update((22,33,44)) #{33, 100, 200, 300, 44, 50, 22}

#集合的删除操作
col8={100,50,200,300}
col8.remove(100)
print(col8)         #{200, 50, 300}

#集合之间的关系
#判断2个集合是否相等
s1={1,2,3}
s2={3,1,2}
#集合的存储顺序不会根据输入的顺序变化，因此这2个集合是相等的
print(s1==s2)   #True

#判断一个集合是否是另一个集合的子集，超集，交集
s1={1,5,10}
s2={1,5}
#判断s2是不是s1的子集
print(s2.issubset(s1)) #True
#判断s1是不是s2的超集
print(s1.issuperset(s2)) #True
#判断s1和s2是不是没有交集
print(s1.isdisjoint(s2)) #False(有交集为False)


#集合的数学操作
s1={1,5,10}
s2={1,5}
#输出交集
#intersection方法和&都是等价的，都是交集操作
print(s1.intersection(s2))
print(s1 & s2)

#输出并集
print(s1.union(s2))
print(s1 | s2)

#输出差集
print(s1.difference(s2)) #10
print(s1-s2)             #10

#集合生成式
s={i*i for i in range(10)}
print(s)    #{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}