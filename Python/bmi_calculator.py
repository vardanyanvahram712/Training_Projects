print ("hello world!")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
    
bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.1f}")

# ● BMI < 18.5: "Underweight"
# ● 18.5 <= BMI < 25: "Normal weight"
# ● 25 <= BMI < 30: "Overweight"
# ● BMI >= 30: "Obese"
if bmi <18.5:
    print("Underweight")
elif 18.5 <= bmi <25:
    print("Normal weight")
elif 25 <= bmi <30:
    print("Overweight")
else:
    print("Obese")
      