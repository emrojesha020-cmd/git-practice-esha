from utils import add, subtract, multiplication

print('Esha')
print('1/04/2026')

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiplication(a, b))

except ValueError:
    print("Error: enter valid numbers")