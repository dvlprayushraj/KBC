def calculate_error(x,y):
    try:
        result= x/y
        print("result :",result)
        
    except ZeroDivisionError:
        print("the divisior by zero")
        
        
numerator = 100
denominator = 0

calculate_error(numerator,denominator)