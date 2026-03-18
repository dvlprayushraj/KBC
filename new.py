import math
class determine_area_and_perimeter:

    def area():
        pass

    def perimeter():
        pass


# Initialize the Circle object with a given radius

class circle:
    
    def __init__(self, radius):
        self.radius = radius

    def area_of_circle(self):
        return math.pi*self.radius*self.radius
    
    
    def perimeter_of_circle(self):
        return math.pi*2*self.radius
    
    
class rectangle:
    
    
    def __init__(self,base,height):
        self.base = base
        self.height = height
        
    def calculate_are_of_rectangle(self):
        
        return (self.base *self.height)
    
    def calculate_perimrter_of_rectangle(self):
        
        return (2*(self.base+self.height))
    
    
r =7
circle = circle(r)
circle_area = circle.area_of_circle()
circle_perimeter= circle.perimeter_of_circle()


print("radius of circle is :",r)
print("area of circle is :", circle_area)
print("perimetr of circle is :", circle_perimeter)



# now time to call rectangle

print()
print()


base = 4
height = 5

rectangle = rectangle(base,height)
rectangle_area = rectangle.calculate_are_of_rectangle()
rectangle_perimeter = rectangle.calculate_perimrter_of_rectangle()


print("base of rectangle is :"+"height of rectangle is : ",base, height)
print("area of rectangle is :",rectangle_area)
print("perimeter of rectangle is :", rectangle_perimeter)

        
        