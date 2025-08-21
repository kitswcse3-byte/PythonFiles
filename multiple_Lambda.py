import math

def circle_operations():
    circumference = lambda r: 2 * math.pi * r
    area = lambda r: math.pi * r**2
    
    radius = float(input("Enter the radius of the circle: "))
    
    print(f"Circumference: {circumference(radius):.2f}")
    print(f"Area: {area(radius):.2f}")
    
circle_operations()
