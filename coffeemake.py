import time

def coffeemaker(coffee_type):
    print("-"*50)
    print("Coffee maker is started...")
    print(f"Making a {coffee_type} coffee...")
    time.sleep(2)
    print("Water is boiling...")
    time.sleep(3)
    print(f"Your {coffee_type} is ready.")
    print("Enjoy!")
    print("-"*50)


coffeemaker("Latte")
coffeemaker("Cappuccino")
coffeemaker("Americano")