# 创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法.

class Borg(object):
    _state = {}
    def __new__(cls,*args,**kwargs):
        ob = super(Borg,cls).cls.__new__(cls,*args,**kwargs)
        ob.__dict__ = cls._state
        return ob

class Myclass2(Borg):
    a = 1


