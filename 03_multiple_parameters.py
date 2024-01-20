def say_hello(email, name, address):
    print(f"Hello {name}")
    print(f"Your email is {email}")
    print(f"Your address is {address}")

# keyword parameter: param_name=value
say_hello(address="Pécs", email="csaba@gmail.com", name="Csaba")

say_hello(address="Pécs", "csaba@gmail.com", "Csaba")

#          posittional                  keyword
say_hello("csaba@gmail.com", "Csaba", address="Pécs")