num = int(input("Enter a number: "))

is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

print("\nPrime Number Check")
print("------------------")

if is_prime:
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is Not a Prime Number")

if num > 0:
    print("The entered number is Positive")
elif num < 0:
    print("The entered number is Negative")
else:
    print("The entered number is Zero")