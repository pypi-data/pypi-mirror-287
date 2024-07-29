import model
import inspect


def f(key):
    if '_' not in key:
        return key

for name, obj in inspect.getmembers(model):
    if '_' not in name and name != 'Optional':
        print(name)
        # dd = __import__(name)
        print(list(map(f, obj.__dict__.keys())))
