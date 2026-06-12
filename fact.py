num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    print(f"Factorial of {num} is {fact}")
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")