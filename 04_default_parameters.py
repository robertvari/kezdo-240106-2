# default parameter: parameter_name=None
def say_hello(name, email=None, address=None):
    print("-"*50)
    print(f"Hello {name}")
    if email:
        print(f"Your email is {email}")
    
    if address:
        print(f"Your address is {address}")

say_hello("Csaba")
say_hello("Kriszta", "kriszta@gmail.com")
say_hello("Tamás", "tamas@gmail.com", "Pécs")