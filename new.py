import functools

def my_decorator(func):
    """Decorator that adds logging around a function call."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Something before the function '{func.__name__}' runs")
        result = func(*args, **kwargs)
        print(f"Something after the function '{func.__name__}' runs")
        return result
    return wrapper


@my_decorator
def multiply_numbers(x,y):
    return x*y


result = multiply_numbers(10,20)
print(result)
