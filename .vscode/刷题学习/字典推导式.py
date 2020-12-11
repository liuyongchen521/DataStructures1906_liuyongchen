# 可能你见过列表推导时,却没有见过字典推导式,在2.7中才加入的:
iterable = "1,2,3,4,5,6,7"
b = {key:1 for key in iterable}
print(b)

name = ["张三", "李四", "王五", "李六"]  # 保存名字列表
sign = ["白羊座", "双鱼座", "狮子座", "处女座"]  #保存星座列表
dict1 = {i : j for i, j in zip(name, sign)}    # 字典推导式
print(dict1)