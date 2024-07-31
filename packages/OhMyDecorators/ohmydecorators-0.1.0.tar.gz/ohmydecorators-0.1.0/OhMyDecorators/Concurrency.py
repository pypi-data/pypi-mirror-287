import threading
import tensorflow  as tf


def RunFunctionInThread(func, ThreadTimeout: float):
    def wrapper(*args, **kwargs):
        result = None
        def RunFunc():
            nonlocal result
            result = func(*args, **kwargs)
        
        FunctionThread = threading.Thread(target=RunFunc)
        FunctionThread.start()
        FunctionThread.join(ThreadTimeout)

        return result
    
    return wrapper



def RunFunctionOnGpu(func):
    def wrapper(*args, **kwargs):
        with tf.device('/device:GPU:0'):  # Use the first GPU
            value = func(*args, **kwargs)
        return value
    return wrapper

