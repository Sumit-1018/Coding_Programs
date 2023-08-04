import math

def circle_area(circle_radius):
    return ((circle_radius ** 2) * math.pi)

circle_radius=int(input("Enter the radius:"))
area = circle_area(circle_radius)
print (area)

def cube_area(side):
    return(side**3)

side=int(input("Enter the side length:"))
area=cube_area(side)
print(area)

def cuboid_area(length,breadth,height):
    return(length*breadth*height)
length=int(input("l:"))
breadth=int(input("b:"))
height=int(input("h:"))
area=cuboid_area(length,breadth,height)
print(area)