
def bmi_cal():
    """
    Calculate BMI given weight and height.

    Parameters:
    weight (float): Weight in kilograms.
    height (float): Height in meters.

    Returns:
    float: The calculated BMI.
    """
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print("You are under weight")
    elif bmi < 25.0:
        print("Congratulations you have a healthy weight")
    elif bmi < 30.0:
        print("You are over weight.")
    elif bmi < 40.0:
        print("You are obese.")
    elif bmi >= 40.0:
        print("You are Severly Obese.")
    return bmi



print(bmi_cal())