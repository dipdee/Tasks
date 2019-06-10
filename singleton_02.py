#Singleton as decorator

def singleton(myClass):
    instances = {}
    def getInstance(*args,**kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]
    return getInstance

@singleton
class TestClass(object):
    pass

x = TestClass()
z = TestClass()
x.y = 20
x.r = 55
print(z.y)
z.y = 30
print(x.y)
print(z.r)
z.r = 66
print(x.r)


