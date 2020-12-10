'''
    栈：（堆叠栈）
        特点： 先进后出
        栈顶：增加和删除的操作都是在栈顶完成的，
        栈底：
    抽象的数据结构（ADT)
    Stack():空栈
    push(item): 添加元素，有参数，无返回值
    pop():删除栈顶的元素 ， 无参数，返回被删除的参数
    peek():返回栈顶的元素
    size():无参数，返回栈的长度（整数）
    isEmpty()：无参数，返回布尔值

'''
class Start():    #定义一个空栈
    def __init__(self):
        self.items = []
    def push(self,item):  #添加到栈顶
        return self.items.append(item)
    def pop(self):    #删除栈顶元素
        return self.items.pop()
    def peek(self):   #返回栈顶的元素
        return self.items(len(self.items)-1)
    def size(self):   # 返回栈的长度
        return len(self.items)
    def isEmpty(self):   #是否为空
        return self.items == []
