from my_functions import math_functions as mf  # import math_functions from my_functions and give it a shotr name
from my_functions import simple_prints as sp # import simple_prints from my_functions and give it a shotr name
from my_functions import my_globals as globals # import my_globals from my_functions
from my_functions.my_globals import *  # import all variables from my_finctions.my_globals
from my_functions.settings import * # import all variables from my_finctions.settings
from my_functions.math_functions import add_numbers, multiply_numbers  # import two functions from math_functions
from os import listdir, path
from time import sleep

print(MY_NAME)
print(ADDRESS)
print(AGE)
print(SERVER_ADDRESS)
print(SERVER_PASSWORD)

add_result = add_numbers(10, 20)
print(add_result)
sleep(10)