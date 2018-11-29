
#BMI Calculator
print("Welcome to the BMI Calculator")
print("Please enter your weight in kilograms and your height in meters")
weight = float(input("Please enter your weight: "))
height = float(input("Please enter your height: "))
bmi = weight / (height * height)
bmi = round(bmi,1)
print ("Your BMI is:",bmi)

if(bmi<18.5):
  print ("Underweight")
elif((bmi>=18.5) and (bmi<25)):
   print ("Normal")
elif((bmi>=25) and (bmi<30)):
   print ("Overweight")
else:
    print ("Obese")
