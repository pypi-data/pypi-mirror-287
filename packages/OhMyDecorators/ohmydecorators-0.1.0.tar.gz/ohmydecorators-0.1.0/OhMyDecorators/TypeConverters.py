


# Decorator for converting function output to integers with error handling
def ConvertOutputToInt(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
            return int(result)
        except (ValueError, TypeError) as e:
            print(f"Error converting output to integer: {e}")
            return None
    return wrapper



# Decorator for converting function output to floats with error handling
def ConvertOutputToFloat(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
            return float(result)
        except (ValueError, TypeError) as e:
            print(f"Error converting output to float: {e}")
            return None
    return wrapper



# Decorator for converting function output to strings with error handling
def ConvertOutputToString(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
            return str(result)
        except (ValueError, TypeError) as e:
            print(f"Error converting output to string: {e}")
            return None
    return wrapper



# Decorator for converting function output to booleans with error handling
def ConvertOutputToBoolean(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
            return bool(result)
        except (ValueError, TypeError) as e:
            print(f"Error converting output to boolean: {e}")
            return None
    return wrapper



# Decorator for converting function output to lists with error handling
def ConvertOutputToList(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
            return list(result)
        except (ValueError, TypeError) as e:
            print(f"Error converting output to list: {e}")
            return None
    return wrapper

