单例模式是一种常用的设计模式，在它的核心结构中值包含一个被称为单例类的特殊类，通过单例模式
可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源。
如果希望在系统中某个类的对象只能存在一个，单例模式是最好的解决方案。

__new__()在__init__()之前被调用，用于生成实例对象。利用这个方法和类的属性的特点可以实现设计模式的单例模式。
单例模式是指创建唯一对象，单例模式设计的类只能实例

使用 __new__()方法
class Singleion(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            orig = super(Singleion,cls)
            cls._instance = orig.__new__(cls,*args,**kwargs)
        return cls._instance


# 实例化一个单例
class Singleton(object):
    __instance = None

    def __new__(cls, age, name):
        #如果类数字能够__instance没有或者没有赋值
        #那么就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时
        #能够知道之前已经创建过对象了，这样就保证了只有1个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

a = Singleton(18, "dongGe")
b = Singleton(8, "dongGe")

print(id(a))
print(id(b))

a.age = 19 #给a指向的对象添加一个属性
print(b.age)#获取b指向的对象的age属性
