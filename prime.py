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
    print(num, "is a Valid Prime Number")
else:
    print(num, "is Not a Prime Number")
    
