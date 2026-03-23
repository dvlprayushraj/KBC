import functools

def my_decorator(func):
    """Decorator that adds logging around a function call."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"product of two numbers is '{func.__name__}' runs")
        result = func(*args, **kwargs)
       
        return result
    return wrapper

@my_decorator
def calculate_multiplication(x,y):
    print("the product of two number is :")
    return x*y

print(calculate_multiplication(5,4))