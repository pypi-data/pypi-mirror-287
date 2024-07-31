import time


def Deprecated(func, Message):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} is deprecated: {Message}\n")
        result = func(*args, **kwargs)  # Call the original function
        return result
    return wrapper



# Decorator for measuring execution time
def MeasureExecutionTime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper



# Decorator for caching function results
def CacheFunctionResults(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"Using cached result for {func.__name__}({args})")
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper



# Decorator for retrying a function on exception
def RetryOnException(func, Attempts):
    def wrapper(*args, **kwargs):
        while Attempts > 0:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"An exception occurred: {e}. Retrying...")
                Atempts -= 1
        print("Max attempts reached. Aborting.")
    return wrapper



# Decorator for ensuring input arguments are of a specific type
def EnforceArgumentType(ArgumentType):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, ArgumentType):
                    raise TypeError(f"Argument {arg} is not of type {ArgumentType}")
            for arg in kwargs.values():
                if not isinstance(arg, ArgumentType):
                    raise TypeError(f"Argument {arg} is not of type {ArgumentType}")
            return func(*args, **kwargs)
        return wrapper
    return decorator



# Decorator for ensuring input arguments are within a specified range
def EnforceArgumentRange(MinValue, MaxValue):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not MinValue <= arg <= MaxValue:
                    raise ValueError(f"Argument {arg} is not within range [{MinValue}, {MaxValue}]")
            for arg in kwargs.values():
                if not MinValue <= arg <= MaxValue:
                    raise ValueError(f"Argument {arg} is not within range [{MinValue}, {MaxValue}]")
            return func(*args, **kwargs)
        return wrapper
    return decorator



