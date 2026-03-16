def triangle_finder(a, b, c):
    if (a==b==c):
        return "Equilateral"
    elif (a==b or b==c or a==c):
        return "Isosceles"
    else:
        return "Scalene"


print(triangle_finder(1, 1, 1))
print(triangle_finder(1, 1, 2))
print(triangle_finder(1, 2, 3))