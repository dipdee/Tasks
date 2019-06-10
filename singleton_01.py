#Singleton as class

class Singleton(object):
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance = super(Singleton, self).__new__(self)
        return self._instance


x = Singleton();
z = Singleton()
x.y = 20
x.r = 55
print(z.y)
z.y = 30
print(x.y)
print(z.r)
z.r = 66
print(x.r)


