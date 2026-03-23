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
def calculate_multiplication_of_all_numbers(number):
    result = 1
    for x in number:
        result *= x
        
        
    return result


result =calculate_multiplication_of_all_numbers([1,2,3,4,5])
print(result)



        
    
    