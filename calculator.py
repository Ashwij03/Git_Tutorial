a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Sum =", a + b + c)
print("Sub =", a - b - c)
print("Mul =", a * b * c)

if b != 0:
    print("Div =", a / b)
else:
    print("Division by zero is not allowed.")