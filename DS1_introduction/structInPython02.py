"""
   python 内置的类型 性能分析  数据结构
    1、列表list
    生成：+ , append, insert(index,值)，列表生成式[i for i in range(10)]， 类
    删： pop()  del(0)
    2、字典 dict
    增：
"""
# a = [1]
# b = [2]
# print(a+b)

def test1():
   l = []
   for i in range(1000):
      l = l + [i]
def test2():
   l = []
   for i in range(1000):
      l.append(i)
def test3():
   l = [i for i in range(1000)]
def test4():
   l = list(range(1000))

from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("+ ",t1.timeit(number=1000), "seconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "seconds")
t3 = Timer("test3()", "from __main__ import test3")
print("列表生成式 ",t3.timeit(number=1000), "seconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "seconds")

# +  1.4200432 seconds
# append  0.10801499999999997 seconds
# 列表生成式  0.03768569999999993 seconds
# list range  0.014598800000000134 seconds

x = list(range(2000000))
pop_zero = Timer("x.pop(0)","from __main__ import x")
print("pop_zero ",pop_zero.timeit(number=1000), "seconds")
x = list(range(2000000))
pop_end = Timer("x.pop()","from __main__ import x")
print("pop_end ",pop_end.timeit(number=1000), "seconds")



#python扩展数据类型


from pythonds.basic.stack import Stack #栈
from pythonds.basic.queue import Queue
from pythonds.basic.deque import Deque

from pythonds.trees import Tree  #树
from pythonds.graphs import Graph #图

程序 = 数据结构 + 算法
总结：算法是为了解决实际问题而设计的，数据结构是算法需要处理的问题载体