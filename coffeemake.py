import time

def coffeemaker(coffee_type, milk=False, sugar=False):
    print("-"*50)
    print("Coffee maker is started...")
    print(f"Making a {coffee_type} coffee...")
    time.sleep(2)
    print("Water is boiling...")
    time.sleep(3)

    if milk:
        print("Add milk...")
        time.sleep(1)
    
    if sugar:
        print("Add sugar...")
        time.sleep(1)

    print(f"Your {coffee_type} is ready.")
    print("Enjoy!")
    print("-"*50)


coffeemaker("Latte")
coffeemaker("Cappuccino", milk=True)
coffeemaker("Americano", sugar=True)
coffeemaker("Espresso", sugar=True, milk=True)