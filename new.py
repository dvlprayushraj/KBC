def verify_integer_or_not(prompt):
   try:
       Value = int(input(prompt))
       
       return Value
   
   except ValueError:
       print("invalid integer ,inputa a valid integer ")
       
       
       
n = verify_integer_or_not("input an integer :")

print("input value :",n)
       
        