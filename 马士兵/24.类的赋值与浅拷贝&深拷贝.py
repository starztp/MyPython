class Cpu:
    pass

class Disk:
    pass

class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

#变量的赋值
cpu1=Cpu()
cpu2=cpu1
#cpu1和cpu2的内存地址一样，同一个对象存储在2个变量里
print(cpu1)     #<__main__.Cpu object at 0x102d3fee0>
print(cpu2)     #<__main__.Cpu object at 0x102d3fee0>

#类的浅拷贝
import copy
disk=Disk()
computer=Computer(cpu1,disk)
computer2=copy.copy(computer)
#computer和computer2的是不同的对象，但是它们的子对象cpu和disk却是相同的
print(computer,computer.cpu,computer.disk)      #<__main__.Computer object at 0x1050b3e80> <__main__.Cpu object at 0x1050b3fd0> <__main__.Disk object at 0x1050b3eb0>
print(computer2,computer2.cpu,computer2.disk)   #<__main__.Computer object at 0x101147b20> <__main__.Cpu object at 0x101147fd0> <__main__.Disk object at 0x101147eb0>

#深拷贝
computer3=copy.deepcopy(computer)
#computer和computer3的是不同的对象，它们的子对象cpu和disk也是不相同的
print(computer,computer.cpu,computer.disk)      #<__main__.Computer object at 0x1045ebe80> <__main__.Cpu object at 0x1045ebfd0> <__main__.Disk object at 0x1045ebeb0>
print(computer3,computer3.cpu,computer3.disk)   #<__main__.Computer object at 0x104615ae0> <__main__.Cpu object at 0x1046159c0> <__main__.Disk object at 0x104615960>
