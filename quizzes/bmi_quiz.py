

height_inches = int(input('input your height in inches'))
weight_lbs = int(input('input your weight in lbs'))

bmi = (weight_lbs * 703) / (height_inches * height_inches)

rounded_bmi = round(bmi, 2)

if bmi < 16.0:
    print(f"Your BMI is {rounded_bmi} makes you Severely Underweight")
elif 16.0 < bmi < 18.4:
    print(f"Your BMI is {rounded_bmi} makes you Underweight")
elif 18.5 < bmi < 24.9:
    print(f"Your BMI is {rounded_bmi} makes you Normal")
elif 25.0 < bmi < 29.9:
    print(f"Your BMI is {rounded_bmi} makes you Overweight")
elif 30.0 < bmi < 34.9:
    print(f"Your BMI is {rounded_bmi} makes you Moderately Obese")
elif 35.0 < bmi < 39.0:
    print(f"Your BMI is {rounded_bmi} makes you Severely Obese")
else:
    print(f"Your BMI is {rounded_bmi} makes you Morbidly Obese")
