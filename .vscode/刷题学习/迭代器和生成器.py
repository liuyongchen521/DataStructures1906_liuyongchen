# 这里有个关于生成器的创建问题面试官有考：
# 问： 将列表生成式中[]改成() 之后数据结构是否改变？

# 答案：是，从列表变为生成器

# >>> L = [x*x for x in range(10)]

# >>> L

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# >>> g = (x*x for x in range(10))

# >>> g

#  at 0x0000028F8B774200>
#  通过列表生成式，可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的
#  。而且，创建一个包含百万元素的列表，不仅是占用很大的内存空间
# 如：我们只需要访问前面的几个元素，后面大部分元素所占的空间都是浪费的
# 。因此，没有必要创建完整的列表（节省大量内存空间）。
# 在Python中，我们可以采用生成器：边循环，边计算的机制—>generator


# Python中关键字yield有什么作用?
# def node._get_child_candidates(self, distance, min_dist, max_dist):
#     if self._leftchild and distance - max_dist < self._median:
#         yield self._leftchild
#     if self._rightchild and distance + max_dist >= self._median:
#         yield self._rightchild
# 下面是调用它:

# result, candidates = list(), [self]
# while candidates:
#     node = candidates.pop()
#     distance = node._get_dist(obj)
#     if distance <= max_dist and distance >= min_dist:
#         result.extend(node._values)
#     candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))
# return result
# 当_get_child_candidates方法被调用的时候发生了什么?是返回一个列表?还是一个元祖?它还能第二次调用吗?后面的调用什么时候结束?


# ------------理解generators(生成器)------理解iterables(迭代器)-----
# 为了理解yield有什么用,首先得理解generators,而理解generators前还要理解iterables

# iterables（可迭代的）
# 当你创建了一个列表,你可以一个一个的读取它的每一项,这叫做iteration（迭代）:

# >>> mylist = [1, 2, 3]
# >>> for i in mylist:
# ...    print(i)
# 1
# 2
# 3
# Mylist是可迭代的.当你用列表推导式的时候,你就创建了一个列表,而这个列表也是可迭代的:
# >>> mylist = [x*x for x in range(3)]
# >>> for i in mylist:
# ...    print(i)
# 0
# 1
# 4
# 所有你可以用在for...in...语句中的都是可迭代的:比如lists,strings,files...因为这些可迭代的对象你可以随意的读取所以非常方便易用,
# 但是你必须把它们的值放到内存里,当它们有很多值时就会消耗太多的内存.

# -----------Generators  生成器
# 生成器也是迭代器的一种,但是你只能迭代它们一次.
# 原因很简单,因为它们不是全部存在内存里,它们只在要调用的时候在内存里生成:
# >>> mygenerator = (x*x for x in range(3))
# >>> for i in mygenerator:
# ...    print(i)
# 0
# 1
# 4
# 生成器和迭代器的区别就是用()代替[]
# 还有你不能用for i in mygenerator第二次调用生成器:首先计算0,然后会在内存里丢掉0去计算1,直到计算完4.


# Yield
# Yield的用法和关键字return差不多,下面的函数将会返回一个生成器:
def createGenerator():
    mylist = range(3)
    for i in mylist:
        print("jinlai-%s"%i)
        yield i*i

mygenerator = createGenerator() # 创建生成器
# >>> print(mygenerator) # mygenerator is an object!
# <generator object createGenerator at 0xb7555c34>
for i in mygenerator:
    print(i)

# # 在这里这个例子好像没什么用,
# # 不过当你的函数要返回一个非常大的集合并且你希望只读一次的话,那么它就非常的方便了.

# # 要理解Yield你必须先理解当你调用函数的时候,
# # 函数里的代码并没有运行.函数仅仅返回生成器对象,这就是它最微妙的地方:-)

# # 然后呢,每当for语句迭代生成器的时候你的代码才会运转.

# # 现在,到了最难的部分:
# # 当for语句第一次调用函数里返回的生成器对象,数里的代码就开始运作,直到碰到yield,然后会返回本次循环的第一个返回值.
# # 所以下一次调用也将运行一次循环然后返回下一个值,直到没有值可以返回.

# # 一旦函数运行并且没有碰到yeild语句就认为生成器已经为空了.原因有可能是循环结束或者没有满足if/else之类的.

# # 控制迭代器的穷尽
class Bank(): #让我们建一个银行，生产很多的ATM
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield "$100"

hsbc = Bank()   #当一切就绪了你想要的多少ATM就给多少
corner_street_atm = hsbc.create_atm()
print(corner_street_atm.__next__())

print([corner_street_atm.__next__() for cash in range(5)])

# hsbc.crisis = True # cao,经济危机来了没有钱了!
print(corner_street_atm.__next__())


wall_street_atm = hsbc.create_atm() # 对于其他ATM,它还是True

>>> print(wall_street_atm.next())
<type 'exceptions.StopIteration'>
>>> hsbc.crisis = False # 麻烦的是,尽管危机过去了,ATM还是空的
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> brand_new_atm = hsbc.create_atm() # 只能重新新建一个bank了
>>> for cash in brand_new_atm:
...    print cash



# Itertools (迭代器),你的好基友
# itertools模块包含了一些特殊的函数可以操作可迭代对象.有没有想过复制一个生成器?链接两个生成器?把嵌套列表里的值组织成一个列表?Map/Zip还不用创建另一个列表?

# 来吧import itertools

# 来一个例子?让我们看看4匹马比赛有多少个排名结果:
import itertools     #迭代器
houses = [1,2,3,4]
races = itertools.permutations(houses) 
print(races)
print(list(races))
迭代是可迭代对象(对应__iter__()方法)和迭代器(对应__next__()方法)的一个过程.
可迭代对象就是任何你可以迭代的对象.
迭代器就是可以让你迭代可迭代对象的对象(有点绕口,意思就是这个意思)