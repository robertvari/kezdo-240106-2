def calculate_result(number):
    def add_numbers(a, b):
        return a + b

    def divide_numbers(a, b):
        return a / b

    def multiply_numbers(a, b):
        return a * b
    
    result_1 = add_numbers(number, 100)
    result_2 = divide_numbers(result_1, 32)
    result_3 = multiply_numbers(result_2, 100)
    return result_3


result = calculate_result(42)
print(result)