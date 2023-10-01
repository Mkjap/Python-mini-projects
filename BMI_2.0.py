print("To Calculate Body Mass Index from a user's weight and height")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = round (weight / height ** 2 )
#bmi = int(weight) / float(height) ** 2
#BMI = float(bmi)
if BMI < 18.5:
    print(f"The user BMI is {BMI}, and the user is underweight.")
elif BMI < 25:
    print(f"The user BMI is {BMI},and the user is normal.")
elif BMI < 30:
    print(f"The user BMI is {BMI},and the user is overweight.")
elif BMI < 35:
    print(f"The user BMI is {BMI},and the user is obese.")
else:
    print(f"The user BMI is {BMI},and the user is clinically obese.")