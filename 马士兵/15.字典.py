# 作者: 张天由
#创建字典
#使用{}创建
map={"name":"天由","age":18}
print(type(map))                #<class 'dict'>
print(map)
#使用dict()创建
map1=dict(name="天由",age=18)
print(type(map1))                #<class 'dict'>
print(map1)

#字典元素的获取
#使用[]获取字典对应key的值
map={"name":"天由","age":18}
print(map["name"])      #天由
#使用get方法获取字典对应key的值
print(map.get("name"))  #天由
# print(map["aaa"])       #报错 KeyError: 'aaa'
print(map.get("aaa"))   #None
#当key不存在时，输出默认值88
print(map.get("bbb",88))    #88

#判断字典中指定Key是否存在
map={"name":"天由","age":18}
print("gender" in map)          #False
print("name" in map)            #True


#删除字典中指定的key和其对应的值
map={"name":"天由","age":18}
del map["name"]
print(map)      #{'age': 18}

#字典中的新增操作
map={"name":"天由","age":18}
map["gender"]="男"
print(map)      #{'name': '天由', 'age': 18, 'gender': '男'}

#修改字典key的值
map={"name":"天由","age":18}
map["age"]=16
print(map)      #{'name': '天由', 'age': 16}


#获取字典所有的key
map={"name":"天由","age":18}
keys=map.keys()
print(keys)     #dict_keys(['name', 'age'])
print(type(keys))   #<class 'dict_keys'>
print(list(keys))   #['name', 'age']

#获取字典所有的value
map={"name":"天由","age":18}
values=map.values();
print(values)           #dict_values(['天由', 18])
print(type(values))     #<class 'dict_values'>
print(list(values))     #['天由', 18]

#获取字典所有的键值对
map={"name":"天由","age":18}
items=map.items()
print(items)            #dict_items([('name', '天由'), ('age', 18)])
print(type(items))      #<class 'dict_items'>
print(list(items))      #[('name', '天由'), ('age', 18)]


#字典元素遍历
#循环输出字典中的key和value
map={"name":"天由","age":18}
for key in map:
    print(key,map.get(key))

#字典生成表达式
names=["天由","天由1","天由2","天由3"]
ages=[16,17,18]
#将2个列表合并为一个字典
newmap={name:age for name,age in zip(names,ages)}
print(newmap)   #{'天由': 16, '天由1': 17, '天由2': 18}