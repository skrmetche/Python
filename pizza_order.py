
def pizza_order():
    print("""
    Welcome to Python Pizza Deliveries
    small pizza - 15$ 
    medium pizza - 20$ 
    large pizza - 25$ 
    pepporoni (small) - 2$ 
    pepporoni (medium, large) - 3$ 
    extra cheese - 1$
    """)

    size = input("What is the size of the pizza? S,M or L: ").lower()
    if size == "s":
        pizza_price = 15
    elif size == "m":
        pizza_price = 20
    elif size == "l":
        pizza_price = 25
    else:
        print("Invalid size. Please choose S, M, or L.")
        return  # Exit the function if the size is invalid
    

    pepperoni = input("Do you want pepperoni on your pizza? y or n: ").lower()
    if size == "s" and pepperoni == "y":
        pepperoni = 2
    elif (size == "m" or "l") and pepperoni == "y":
        pepperoni = 3
    elif pepperoni == "n":
        pepperoni = 0
    
    extra_cheese = input("Do you want extra cheese? y or n: ").lower()
    if extra_cheese == "y":
        extra_cheese = 1
    elif extra_cheese == "n":
        extra_cheese = 0


    total_bill = pizza_price + pepperoni + extra_cheese
    return print(f"Your total bill is {total_bill}$")


pizza_order()

    



    

    
