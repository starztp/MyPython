# 作者: 张天由

#这些对象的布尔值都是False,其它对象的布尔值为True
print(bool(False)) #False
print(bool(0)) #False
print(bool(0.0)) #False
print(bool(None)) #False
print(bool('')) #False
print(bool("")) #False
print(bool([])) #False  空列表
print(bool(list())) #False  空列表
print(bool(())) #False 空元祖
print(bool(tuple())) #False 空元祖
print(bool({})) #False 空字典
print(bool(dict())) #False 空字典
print(bool(set()))  #False 空集合