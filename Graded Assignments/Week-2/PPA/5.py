#Write a program to realize the equation of a line given 2 points (x1,y1) and (x2,y2) in 2D space. The input is in 5 lines where, the first, second, third, and fourth lines represent x1,y1,x2 and y2  = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
if x1 == x2:
    print("Vertical Line")
else:
    slope = (y2 - y1) / (x2 - x1)
    y3 = y1 + slope * (x3 - x1)
    print(y3)
if slope > 0:
    print("Positive Slope")
elif slope < 0:
    print("Negative Slope")
else:
    print("Horizontal Line")
