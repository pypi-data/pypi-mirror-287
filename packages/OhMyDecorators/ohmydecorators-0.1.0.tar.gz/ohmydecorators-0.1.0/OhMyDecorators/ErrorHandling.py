def ErrorCheck(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"ERROR: {func} {e}\n")
            return None
    return wrapper


