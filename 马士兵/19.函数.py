def calc(a,b):
    return a+b

print(calc(1,2))    #3

print(calc(b=1,a=2))    #3

#函数存在多个返回值时，返回对象是元祖
def mutiReturn(a,b):
    return a,b
print(mutiReturn(1,2))  #(1, 2)


#函数默认值参数
#给形参设置默认值参数，只有与默认值不符的时候才需要传递实参
def calc1(a,b=10):
    return a+b
print(calc1(1))     #11
print(calc1(1,3))   #4

#个数可变的位置形参
#当参数数量不确定时，可以使用*加上参数名，参数类型默认为元祖
def fun(*args):
    print(args)

fun(10)     #(10,)
fun(10,20)  #(10, 20)

#当关键字参数数量不确定时，可以使用**加上参数名，参数类型默认为字典
def fun1(**args):
    print(args)

fun1(a=10,b=20) #{'a': 10, 'b': 20}


#递归函数
#斐波那契数列
def digui(n):
    if(n==1):
        return 1
    else:
        return (n-2)+(n-1)

print(digui(5))     #7