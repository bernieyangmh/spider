'''
给实例创建一个与函数名同名的属性，将函数得到的结果赋值给这个属性
'''
class LazyProperty(object):
    def __init__(self, func):
        print 1
        self.func = func

    def __get__(self, instance, owner):
        print 2
        print 'owner is %s'% owner
        print 'instance is %s'% instance
        if instance is None:
            print 3
            return self
        else:
            print 4
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


import math


class Circle(object):
    def __init__(self, radius):
        print 5
        self.radius = radius

    @LazyProperty
    def area(self):
        print 'Computing area'
        return math.pi * self.radius ** 2

    @LazyProperty
    def perimeter(self):
        print 'Computing perimeter'
        return 2 * math.pi * self.radius

    def diameter(self,obj):
        print 'Computing diameter'
        return 2 * obj.radius

if __name__ == '__main__':
    print 7
    c = Circle(2)
    print 8
    print c.area
    print c.area
    print c.perimeter
    print c.perimeter
    print c.diameter(c)
    print c.diameter(c)


# result
# Computing area
# 12.5663706144
# 12.5663706144
# Computing perimeter
# 12.5663706144
# 12.5663706144
# Computing diameter
# 4
# Computing diameter
# 4