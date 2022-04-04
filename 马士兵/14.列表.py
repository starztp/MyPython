# 作者: 张天由

#创建列表的第一种方式，使用[]
list1=["aaa","bbb",10]
print(list1)
print(type(list1))

#创建列表的第一种方式，使用内置函数list()
list2=list(["aaa","bbb",20])
print(list2)
print(list2[0]) #aaa
#负数索引是从后向前的逆向顺序，-1指的是列表最后一位
print(list2[-1])    #20

#获取指定元素的索引
list3=["aaa","bbb","ccc"]
print(list3.index("ccc")) #2
#列表中存在相同元素时，只返回相同元素中第一个元素的索引
list4=["aaa","aaa","ccc"]
print(list4.index("aaa"))
#在指定的下标区间查找元素索引
print(list4.index("ccc",0,3)) #2


#列表的切片操作
lst = [1,2,3,4,5,6,7,8]
#从索引1取值到索引4的所有数据，步长为1
print(lst[1:5:1])   #[2, 3, 4, 5]
#从索引1取值到索引4的所有数据，步长为2
print(lst[1:5:2])   #[2, 4]
#步长为负数的情况下
print(lst[::-1])    #[8, 7, 6, 5, 4, 3, 2, 1]

#判断元素是否在列表中存在
print(5 in lst)         #True
print(100 in lst)       #False
print(100 not in lst)   #True

#遍历列表
for item in lst:
    print(item)


#向列表中添加元素
lst1=[1,2,3,4,5,6,7,8]
lst2=["aaa","bbb"]
lst1.append(10)
print(lst1) #[1, 2, 3, 4, 5, 6, 7, 8, 10]
#将lst2添加到lst1末尾
lst1.extend(lst2)
print(lst1)         #[1, 2, 3, 4, 5, 6, 7, 8, 10, 'aaa', 'bbb']
#在任意位置添加一个元素
lst3=[1,2,3,4,5,6,7,8]
#在索引1的位置添加元素20
lst3.insert(1,20)
print(lst3)         #[1, 20, 2, 3, 4, 5, 6, 7, 8]

#删除列表中的元素
lst1=[1,2,3,4,5,6,7,8,1]
#删除列表中的指定元素，只删除第一个匹配到的元素
lst1.remove(1)
print(lst1)         #[2, 3, 4, 5, 6, 7, 8, 1]
#删除指定索引位置上的元素
lst2=[1,2,3,4,5,6,7,8]
lst2.pop(2)
print(lst2) #[1, 2, 4, 5, 6, 7, 8]
#如果不指定参数，则删除列表中的最后一个元素
lst3=[1,2,3,4,5,6,7,8]
lst3.pop()
print(lst3)

#清除列表中的所有元素
lst1=[1,2,3,4,5,6,7,8,1]
lst1.clear()
print(lst1)     #[]
#删除列表
# del lst1
# print(lst1) #NameError: name 'lst1' is not defined.


#列表排序
lst=[20,88,30,55,20,40]
print("排序前的列表",lst)
#默认升序排列
lst.sort()
print("排序后的列表",lst) #[20, 20, 30, 40, 55, 88]
#降序排序
lst.sort(reverse=True)      #reverse=True表示降序排序
print("降序排序后的列表",lst)       #[88, 55, 40, 30, 20, 20]

#通过内置sorted函数进行排序，sorted会生成一个新列表，不影响原列表
lst1=[20,88,30,55,20,40]
newlst=sorted(lst1,reverse=True)
print(newlst)       #[88, 55, 40, 30, 20, 20]

#列表生成式
#生成一个包含1-9整数的列表
lst=[i for i in range(1,10)]
print(lst)  #[1, 2, 3, 4, 5, 6, 7, 8, 9]
#生成一个包含2，4，6，8，10的值的列表
lst1=[i*2 for i in range(1,6)]
print(lst1)     #[2, 4, 6, 8, 10]
