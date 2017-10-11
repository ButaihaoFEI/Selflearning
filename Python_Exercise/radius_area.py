import math
def circle_area(r):
	return math.pi*r*r
r = float(input("Input the radius of the circle : "))
area = circle_area(r)
print("Area of " + str(r) + " is: " + str(round(area,2)))