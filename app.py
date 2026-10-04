def calculate_basic(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    return addition, multiplication, subtraction

# Example usage:
add_result, mult_result, subtraction_result = calculate_basic(10, 5)

print(f"Addition result: {add_result}")       # Outputs: 15
print(f"Multiplication result: {mult_result}")    # Outputs: 5
print(f"Subtraction result: {subtraction_result}") # Outputs: 5

addition_result, multiplication_result, subtraction_result = calculate_basic(10, 5)

print(f"Addition result: {addition_result}")       # Outputs: 15
print(f"Multiplication result: {multiplication_result}")    # Outputs: 5
print(f"Subtraction result: {subtraction_result}") # Outputs: 5