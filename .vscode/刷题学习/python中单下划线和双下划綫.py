>>> class MyClass():
...     def __init__(self):
...             self.__superprivate = "Hello"
...             self._semiprivate = ", world!"
...
>>> mc = MyClass()
>>> print(mc.__superprivate)
Traceback (most recent call last):
  File "", line 1, in
AttributeError: myClass instance has no attribute '__superprivate'
>>> print(mc._semiprivate)
, world!
>>> print(mc.__dict__)
{'_MyClass__superprivate': 'Hello', '_semiprivate': ', world!'}

#__foo__:一种约定,Python内部的名字,用来区别其他用户自定义的命名,以防冲突，
# 就是例如__init__(),__del__(),__call__()这些特殊方法

#_foo:一种约定,用来指定变量私有.程序员用来指定私有变量的一种方式.不能用from module import * 导入，其他方面和公有一样访问；

#__foo:这个有真正的意义:解析器用_classname__foo来代替这个名字,以区别和其他类相同的命名,
# 它无法直接像公有成员一样随便访问
# ,通过对象名._类名__xxx这样的方式可以访问.