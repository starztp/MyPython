try:
    a=int(input("请输入第一个整数"))
    b=int(input("请输入第二个整数"))
    result=a/b
    print("result:",result)
except ZeroDivisionError:
    print("除数不可为0")
except ValueError:
    print("除数或被除数必须是数字")

print("程序结束")

#捕获所有可能出现的异常
try:
    a=int(input("请输入第一个整数"))
    b=int(input("请输入第二个整数"))
    result=a/b
    print("result:",result)
except BaseException as e:
    print(e)

print("程序结束")

#无论程序是否有异常，都会执行finally中的代码
try:
    a=int(input("请输入第一个整数"))
    b=int(input("请输入第二个整数"))
    result=a/b
    print("result:",result)
except BaseException as e:
    print(e)
finally:
    print("程序结束")


#使用traceback打印异常信息
import traceback
try:
    1/0
except:
    traceback.print_exc()