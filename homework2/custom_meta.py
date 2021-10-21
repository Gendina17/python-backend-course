""" Creating a custom meta class """


class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        custom_attr = {}
        for key, value in dct.items():
            if not key.startswith('__'):
                custom_attr['custom_' + key] = value
            else:
                custom_attr[key] = value

        def __setattr__(self, key, value):
            self.__dict__['custom_' + key] = value

        custom_attr['__setattr__'] = __setattr__
        return type(cls).__new__(cls, name, bases, custom_attr)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def foo(self):
        self.val2 = 123
