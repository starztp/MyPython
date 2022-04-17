#面向对象的3大特征，封装、继承、多态
#封装
class Student:
    def __init__(self,name,age):
        self.name=name
        #age属性不希望在类的外部被直接使用，所以加了2个_,等同于java中的private
        self.__age=age

    #通过方法可以获取类中的private属性
    def getAge(self):
            return self.__age



stu=Student("天由",18)
print(stu.name)         #天由
#private属性只能通过类中的方法去访问
print(stu.getAge())     #18
#打印stu实例中的属性和方法
#['_Student__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'getAge', 'name']
print(dir(stu))
#在类的外部可以通过_类名__属性名的形式来访问private属性
print(stu._Student__age)    #18


#继承
#如果一个类没有继承任何类，则默认继承Object
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)
    def ovInfo(self):
        print("这是父类的输出")

#定义子类继承Person
class Student(Person):
    def __init__(self,name,age,stuNo):
        #调用父类构造方法
        super().__init__(name,age)
        self.stuNo=stuNo
    #子类重写父类的方法
    def ovInfo(self):
        print(self.stuNo)

#可定义多个子类继承父类
class Teacher(Person):
    def __init__(self,name,age,gender):
        #调用父类构造方法
        super().__init__(name,age)
        self.gender=gender

    # 子类重写父类的方法
    def ovInfo(self):
        #调用父类的ovInfo执行逻辑
        super(Teacher, self).ovInfo()
        print(self.gender)

stu=Student("天由",18,123)
teacher=Teacher("曹老师",20,"男")

#子类的实例调用父类的方法
stu.info()          #天由 18
teacher.info()      #曹老师 20
#调用重写父类的方法
stu.ovInfo()        #123
teacher.ovInfo()    #这是父类的输出 男


#多态
class Car:
    def getCar(self):
        print("这是车")

class BaoMa(Car):
    def getCar(self):
        print("这是宝马")

class BenChi(Car):
    def getCar(self):
        print("这是奔驰")

def fun(car):
    car.getCar()
#调用不同子类中的getCar方法
fun(Car())      #这是车
fun(BaoMa())    #这是宝马
fun(BenChi())   #这是奔驰