
class Student:
    #定义类属性
    prop="类属性"

    #定义初始化方法（类似java中的构造方法）
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #定义类的实例方法（在类中定义实例方法必须有self)
    def getName(self):
        print(self.name)

    #定义静态方法
    @staticmethod
    def staticMethod():
        print("这是静态方法")

    #定义类方法（定义类方法必须有cls)
    @classmethod
    def classMethod(cls):
        print("这是类方法")


#创建Student类的对象
stu=Student("天由",18)

#通过对象实例输出类中的对象属性值
print(stu.name)     #天由
print(stu.age)      #18
#几种方式通过实例对象调用类中的实例方法
stu.getName()    #天由
Student.getName(stu)    ##天由

#打印类属性的值
print(Student.prop)     #类属性
#修改类属性
Student.prop=123
print(Student.prop)     #123

#调用类方法
Student.classMethod()       #这是类方法

#调用类中的静态方法
Student.staticMethod()      #这是静态方法


#动态绑定实例属性
stu.gender="男"
print(stu.gender)   #男

#动态绑定实例方法
def show():
    print("这是要绑定的实例方法")
stu.show=show()
stu.show    #这是要绑定的实例方法
