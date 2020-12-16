作为python的模块是天然的单例模式,被引入使用就是创建的单例模式
# mysingleton.py

class My_Singleton(object):

    def foo(self):

        pass

 

my_singleton = My_Singleton()

 

# to use

from mysingleton import my_singleton

 

my_singleton.foo()

 