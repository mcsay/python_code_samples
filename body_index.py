height = input("Enter your height in m : ")
weight = input("Enter your weight in kg :")

BMI = int(weight) / float(height) ** 2

print(type(BMI))
BMI_AS_INT = int(BMI)
print(type(BMI_AS_INT))
print("Your BMI :",BMI)
