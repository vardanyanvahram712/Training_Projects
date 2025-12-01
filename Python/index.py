'''
print("Hello, world!")
# 1) Calculate the area of a rectangle
width = float(input(" width= "))
height =float (input(" height= "))
area = width * height
print("Rectangle area:", area)
'''

'''
# 2) use if , el if 
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
'''
# def rectangle_area(width, height):
#     return width * height

# def main():
#     width = float(input("Enter width: "))
#     height = float(input("Enter height: "))
    
#     area = rectangle_area(width, height)
#     print("Rectangle area:", area)

# if __name__ == "__main__":
#     main()




# income = float(input(" income= "))
# expenses = float(input(" expenses= "))
# total =expenses / income*100
# if  total >=20:
#     print("You are saving enough!")
# else:
#     print("You need to save more.")
# print(" percentage:", total)


# income = float(input(" income= "))
# expenses = float(input(" expenses= "))
# saving_rate = (income - expenses) / income * 100
# if saving_rate >= 20:
#     print("You are saving enough!")
# else:
#     print("You need to save more.")
# print("Saving rate:", saving_rate, "%")


# income = float(input(" income= "))
# expenses = float(input(" expenses= "))
# total =income + expenses
# remaining= income - expenses
# income_percent=income/total*100
# expenses_percent=expenses/total*100
# print ("income_percent:" , income_percent)
# print ("expenses_percent:" , expenses_percent)
# if remaining > 20:
#       print("You are saving money.") 
# elif remaining < 20:
#     print("You need to save more.") 
# else :
#     print("You are breaking even.")

# income = float(input(" income= "))
# expenses = float(input(" expenses= "))      
# total =income + expenses
# remaining= income - expenses
# income_percent=income/total*100
# expenses_percent=expenses/total*100
# print ("income_percent:" , income_percent)
# print ("expenses_percent:" , expenses_percent)
# if remaining > 20 and income_percent ==20:
#       print("You are saving money.")
# elif remaining < 20 and expenses_percent ==20:
#     print("You need to save more.")
# else :
#     print("You are breaking even.")



# user = input(" Enter username: ")
# password = input(" Enter password: ")

# if user == "admin" and password == "1234" or user == "vahram" and password == "1234":
#     print("Login successful")

# else:
#     print("Login failed")



# user=input("enter your name -" )
# age=int(input("enter your age-" ))
# surname=input("enter your surname-" )

# surname_lenght=12
# if len(surname) > surname_lenght:
#         print("you are not allowed")
# else:
#     print("you are allowed")
    

# if age > 18 and age < 30:
#         print("you have to be careful")
# elif age >=30 and age <60:
#         print("you are wellcome")        
# else:
#     print("login failed")

# max_length =7
# if len(user) > max_length:
#       print ("username is too long")
# else:
#       print("username is acceptable")
      




income = float(input("income = "))
expenses = float(input("expenses = "))


total = income + expenses
remaining = income - expenses
income_percent = income / total * 100
expenses_percent = expenses / total * 100

 
print("income_percent:", income_percent)
print("expenses_percent:", expenses_percent)


if remaining > 20:
    print("You are saving money.")
elif remaining < 20:
    print("You need to save more.")
else:
    print("You are breaking even.")
