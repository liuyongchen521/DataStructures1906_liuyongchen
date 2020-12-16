新式类很早在2.2就出现了,所以旧式类完全是兼容的问题,Python3里的类全部都是新式类.
这里有一个MRO问题可以了解下
(新式类是广度优先,旧式类是深度优先),
<Python核心编程>里讲的也很多.

一个旧式类的深度优先的例子

class A():
    def foo1(self):
        print "A"
class B(A):
    def foo2(self):
        pass
class C(A):
    def foo1(self):
        print "C"
class D(B, C):
    pass

d = D()
d.foo1()
# A

按照经典类的查找顺序从左到右深度优先的规则，
在访问d.foo1()的时候,D这个类是没有的..那么往上查找,
先找到B,里面没有,深度优先,访问A,
找到了foo1(),所以这时候调用的是A的foo1()，从而导致C重写的foo1()被绕过

#新式类
class A(object):
   def __init__(self):
      self.n = "A"
      #   pass
class A1(object):
    def __init__(self):
        self.n="A1"
class B(A1):
   def __init__(self):
       super(B, self).__init__()
       self.n1 = "B"
class C(A):
    def __init__(self):
        super(C, self).__init__()
        self.n = "C"
class D(B,C):
    def __init__(self):
        super(D, self).__init__()
        # self.n = "D"
d = D()
print(d.n)

#执行顺序，调用d.n的时候，发现没有，然后会去B里面找，发现B里面也没有，
# 然后找与B同级的被继承类里寻找C，发现C里面有，则会用C里面的,如果没有同级的就会往上找
#B和C都没有会去A里面找

#同级指的是，B和C都是A的子类，