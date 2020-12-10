'''
    什么是队列：
        队列是一系列元素的集合，新元素的加入在队列一端，这一段叫做队尾（rear）
        已有元素 的移除发生在队列的另一端，叫做队首（front)
    特点：先进先出（FIFO）first-in-first-on
    ----------------------
    rear                    front
    ---------------------
    抽闲数据类型（ADT)
        Queue():创建一个空队列对象，无参数，返回空的队列
        enqueue(item):将数据添加到队尾，有参数，无返回值
        dequeue()  从队首移出到数据项，无需参数，返回值为队首数据项
        isEmpty() 测试队列是否为空，无需参数，返回值为布尔值
        size()  返回队列中的数据项的个数，无需参数
'''
# class Queue():
#     def __init__(self):
#         self.items = []
#     def enqueue(self,item):
#         self.items.insert(0,item)

#     def dequeue(self):
#         return self.items.pop()
#     def isEmpty(self):
#         return self.items == []
#     def size(self):
#         return len(self.items)

# q = Queue()

# q.enqueue("a")
# q.enqueue("b")
# q.enqueue("c")

# print(q.size())
# print(q.dequeue())

# print(q.size())



'''
    马铃薯游戏（击鼓传花）选地一个作为开始的人，数到num个人，将此人淘汰

'''
from pythonds.basic.queue import Queue

name_list = ["1","2","3","4","5","6","7","8","9","10","11"]
num = 7

def send_flowers(name_list,num):
    simqueue = Queue()
    for name in name_list:
        simqueue.enqueue(name)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        print(simqueue.dequeue())
    return simqueue.dequeue()
print(send_flowers(name_list,num))