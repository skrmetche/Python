print("Welcome to the tip calculator!")
bill = int(input("What was the total bill? "))
tip = int(input("What is the tip you would like to give? 10,12 or 15: "))/100
people = int(input("How many number of people to split the bill? "))

pay_per_person = (bill*tip)/people

print(pay_per_person)
