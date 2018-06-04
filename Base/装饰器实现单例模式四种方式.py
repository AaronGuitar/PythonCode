# # 方法一：使用函数装饰器实现单例
# def Singleton(cls):
#     _instance = {}
#
#     def _singleton(*args, **kargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kargs)
#             print(cls(*args, **kargs))
#         return _instance[cls]
#
#     return _singleton
#
#
# # a = singleton(A)
# @Singleton
# class A(object):
#     a = 1
#
#     def __init__(self, x=0):
#         self.x = x
#
#
# a1 = A(2)
# a2 = A(3)
# print(a1.x)
# print(a2.x)
# print(id(a1))
# print(id(a2))


# #方法二： 使用类实现单例
# class MusicPlayer(object):
#
#     # 定义类属性记录单例对象引用
#     instance = None
#
#     def __new__(cls, *args, **kwargs):
#
#         # 1. 判断类属性是否已经被赋值
#         if cls.instance is None:
#             cls.instance = super().__new__(cls)
#
#         # 2. 返回类属性的单例引用
#         return cls.instance


# #方法三： 使用类装饰器实现单例模式
# class Singleton(object):
#     def __init__(self, cls):
#         self._cls = cls
#         self._instance = {}
#
#     def __call__(self, *args, **kwargs):
#         if self._cls not in self._instance:
#             self._instance[self._cls] = self._cls()
#         return self._instance[self._cls]
#
#
# @Singleton
# class Cls(object):
#     def __init__(self):
#         pass
#
#
# cls1 = Cls()
# cls2 = Cls()
# print(id(cls1) == id(cls2))


# 方法四：使用metaclass实现单例模式
class Singleton(type):
    _instance = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instance:
            self._instance[self] = super(Singleton, self).__call__(*args,**kwargs)
        return self._instance[self]


class Cls4(metaclass=Singleton):
    pass


cls1 = Cls4()
cls2 = Cls4()
print(id(cls1) == id(cls2))






