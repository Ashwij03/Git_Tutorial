num = int(input("Enter a number: "))

print("\nNumber Analysis")
print("----------------")

if num % 2 == 0:
    print(f"{num} is an Even Number")
else:
    print(f"{num} is an Odd Number")

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")