#type    type就是Python的内建元类

#-----------metaclass属性------------
#你可以在写一个类的时候为其添加metaclass属性。

# class Foo(object):
    # __metaclass__ = something…
# […]


# 如果你这么做了，Python就会用元类来创建类Foo。小心点，这里面有些技巧。你首先写下class Foo(object)，但是类对象Foo还没有在内存中创建。Python会在类的定义中寻找metaclass属性，如果找到了，
# Python就会用它来创建类Foo，如果没有找到，就会用内建的type来创建这个类

# class Foo(Bar):
    # pass

# Python做了如下的操作：
    # Foo中有metaclass这个属性吗？如果是，Python会在内存中通过metaclass创建一个名
    # 字为Foo的类对象（我说的是类对象，请紧跟我的思路）。如果Python没有找到metaclass，
    # 它会继续在Bar（父类）中寻找metaclass属性，并尝试做和前面同样的操作。
    # 如果Python在任何父类中都找不到metaclass，它就会在模块层次中去寻找metaclass，
    # 并尝试做同样的操作。如果还是找不到metaclass,
    # Python就会用内置的type来创建这个类对象。

# 现在的问题就是，你可以在metaclass中放置些什么代码呢？
    # 答案就是：可以创建一个类的东西。那么什么可以用来创建一个类呢？type，或者任何使用到type或者子类化type的东东都可以。

#------------ 到底什么是元类--------

# 元类就是用来创建类的“东西”。你创建类就是为了创建类的实例对象，不是吗？但是我们已经学习到了Python中的类也是对象。好吧，
# 元类就是用来创建这些类（对象）的，元类就是类的类，你可以这样理解 为：

# MyClass = MetaClass()
# MyObject = MyClass()

# 你已经看到了type可以让你像这样做：
# MyClass = type('MyClass', (), {})

# 这是因为函数type实际上是一个元类。
# type就是Python在背后用来创建所有类的元类。
# 现在你想知道那为什么type会全部采用小写形式而不是Type呢？
# 好吧，我猜这是为了和str保持一致性，str是用来创建字符串对象的类，
# 而int是用来创建整数对象的类。type就是创建类对象的类。
# 你可以通过检查class属性来看到这一点。Python中所有的东西，


# 注意，我是指所有的东西——都是对象。这包括整数、字符串、函数以及类。它们全部都是对象，而且它们都是从一个类创建而来。

# 因此，元类就是创建类这种对象的东西。如果你喜欢的话，可以把元类称为“类工厂”（不要和工厂类搞混了:D）
#  type就是Python的内建元类，当然了，你也可以创建自己的元类。

# ----------自定义元类-----

# 元类的主要目的就是为了当创建类时能够自动地改变类。
# 通常，你会为API做这样的事情，你希望可以创建符合当前上下文的类。
# 假想一个很傻的例子，你决定在你的模块里所有的类的属性都应该是大写形式。
# 有好几种方法可以办到，但其中一种就是通过在模块级别设定metaclass。
# 采用这种方法，这个模块中的所有类都会通过这个元类来创建，
# 我们只需要告诉元类把所有的属性都改成大写形式就万事大吉了。

# 幸运的是，metaclass实际上可以被任意调用，
# 它并不需要是一个正式的类（我知道，某些名字里带有‘class'的东西并不需
# 要是一个class，画画图理解下，这很有帮助）。所以，我们这里就先以一
# 个简单的函数作为例子开始。

# 元类会自动将你通常传给‘type'的参数作为自己的参数传入

# 元类会自动将你通常传给‘type'的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
 


  # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr  #  这会作用到这个模块中的所有类

class Foo(object):
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'

print(hasattr(Foo, 'bar'))
# 输出: False
print(hasattr(Foo, 'BAR'))
# 输出:True

# f = Foo()
# print(f.BAR)
# 输出:'bip'