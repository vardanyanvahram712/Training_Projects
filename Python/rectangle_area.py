print("Hello, world!")

# 1) Calculate the area of a rectangle
width = float(input(" width= "))
height =float (input(" height= "))
area = width * height
print("Rectangle area:", area)



# 2) use if , elif 
width = float(input(" width= "))
height =float (input(" height= "))
area = width * height
print("Rectangle area:", area)
if area > 100:
    print("Large rectangle")
elif area == 100:
    print("Normal rectangle")
elif area < 100:
     print("The area is too small")