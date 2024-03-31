from time import perf_counter

def timer(fn):
    """
    Decorator for count function execution time
    """
    def func(*args, **kwargs):
        start = perf_counter()
        to_execute = fn(*args, **kwargs)
        end = perf_counter()
        print("{0} function took {1} time to execute".format(fn.__name__, (end-start)))
    return func

@timer
def printi(a,b,**kwargs):
    for i in range(1000000):
        print(i)

printi(1,2, name='ttu')