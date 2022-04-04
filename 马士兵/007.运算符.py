# 作者: 张天由

#算数运算符

#加减乘除运算
print(1+1)
print(2-1)
print(3*4)
print(12/3)
#整除运算，结果只取整数部分，小数不做四舍五入
print(11//2)
#取余运算
print(11%2)
#幂运算，表示是2的3次方
print(2**3)

#一正一负整除时向下取整
print(9//-4)    #-3
print(-9//4)    #3


#赋值运算符
#链式赋值
a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))

a = 10
a+=10
print(a) #20

a=30
a-=5
print(a) #25

a=10
a*=2
print(a) #20

a=10
a//=2
print(a) #5


#解包赋值
a,b,c=10,20,30
print(a,id(a))
print(b,id(b))
print(c,id(c))

#交换2个变量的值
a,b=10,20
a,b=b,a
print(a,id(a))
print(b,id(b))


#比较运算符
a,b=10,20
# ==比较的是2个变量的值，而不是内存地址
print(a==b) #False
#比较2个变量的内存地址
print(a is b)   #False
print(a is not b)   #True


#布尔运算符
a,b=1,2
#and,相当于java中的&&
print(a==1 and b==2) #True

#or，相当于java中的||
print(a!=1 or b==2) #True

#not取反
b1 = True
print(not b1) #False

#in
str='helloworld'
#断言字符w是否在helloworld字符串中
print('w' in str)
#断言字符k不在helloworld字符串中
print('k' not in str)