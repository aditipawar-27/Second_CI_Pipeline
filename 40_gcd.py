
def find_gcd(num1, num2):
    """Find the Greatest Common Divisor of two numbers."""

    num1 = abs(num1)
    num2 = abs(num2)

    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder

    return num1


number1 = 48
number2 = 18

result = find_gcd(number1, number2)

print("First Number:", number1)
print("Second Number:", number2)
print("Greatest Common Divisor:", result)
