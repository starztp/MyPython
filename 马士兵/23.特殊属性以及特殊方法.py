class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age

a=A("天由",18)
#输出实例中的属性
print(a.__dict__)   #{'name': '天由', 'age': 18}
#输出类对象中的属性
print(A.__dict__)   #{'__module__': '__main__', '__init__': <function A.__init__ at 0x1028d3f40>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
#输出对象所属的类型
print(a.__class__)  #<class '__main__.A'>
#输出类的父类型元素
print(A.__bases__)  #(<class 'object'>,)
#输出类的层次结构，A继承了Object
print(A.__mro__)    #(<class '__main__.A'>, <class 'object'>)
#查看子类
print(A.__subclasses__())   #[]


class Person:
    def __init__(self,name):
        self.name=name
    #写了这个能实现2个对象相加
    def __add__(self,other):
        return self.name+other.name

per1=Person("天由")
per2=Person("天由1")
#等同于per1.__add__(per2)
print(per1+per2)    #天由天由1