print ("Hello, world!")

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
