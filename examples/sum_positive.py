total = 0
n = int(input("Enter a number: "))
while n >= 0:
    if n > 0:
        total += n
    n = int(input("Enter another number: "))

print("Sum of the positive numbers: ", total)