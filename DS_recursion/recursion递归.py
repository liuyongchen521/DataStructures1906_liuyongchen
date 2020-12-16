'''
    哪些问题适合用递归解决
    怎么用递归的方式写程序
    ***** 递归的三大法则
    递归也是一种迭代
    什么是递归？
    一、递归的定义
        递归是一种解决问题的方法，它把一个问题分解为越来越小的子问题,直到问题的规模
        小到可以被很简单直接解决。
        通常为了达到分解问题的效果，递归过程中要引入一个***调用自身的函数***

        [1,2] [3,3] [6,4]
        ---->迭代的相加
计算[1,2,3,4,5,6,7]的和

1、跌代求和
'''
# import time

# def list_sum(my_list):
#     the_sum = 0
#     for sum in my_list:
#         the_sum = the_sum + sum 
#     return the_sum
# start_time = time.time()
# for i in range(100000):
#     list_sum([1,2,3,4,5,6,7])
# end_time = time.time()
# print(end_time -start_time)


#--------使用递归 ，不使用循环计算
#(1+(2+(3+(4))))

#列表中的第一个元素和剩余所有的元素的和之和
# listSum(list) = first(numlist) + listSum(reset[numlist])
#转换成python
#num_list[0]  + num_list[1:]
#递归函数recursion
# def list_sum(num_list):
#     #函数结束运行的必要条件，否则就是一个死循环
#     if len(num_list) == 1:
#         return num_list[0]
#     else:
#         return num_list[0] + list_sum(num_list[1:])
        #1+[2,3,4,5,6,7]
        #1+(2+[3,4,5,6,7])
        #1+(2+(3+[4,5,6,7]))
        #1+(2+(3+(4+[5,6,7])))
        #1+(2+(3+(4+(5+[6,7]))))
        #1+(2+(3+(4+(5+(6+[7])))))
# s_time = time.time()
# for i in range(100000):
#     list_sum([1,2,3,4,5,6,7])
# e_time = time.time()
# print(e_time - s_time)

#二、递归的三大定律
    1、递归算法必须有个基本结束条件（长度为1的列表）
    2、递归算法必须改变自己的状态并向基本结束条件演进
    3、递归算法必须递归的调用自身

#练习
#1、用list_sum 计算数列[2,4,6,8,10] 要进行多少次递归调用？
        2+sum(4,6,8,10)
        4+sum(6,8,10)
        6+sum(8,10)
        8+sum(10)
#2、计算某个数的阶乘的递归算法，（最合适的基本结束条件）,假设0！= 1 
        5！= 5*4*3*2*1
        n == 1
def fact(n):
    if n == 1 or n ==0:
        return 1
    else:
        return n*fact(n-1)