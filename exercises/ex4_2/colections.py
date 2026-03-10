# 2.3
numbers = list(range(5, 21))
print(numbers)

total = 0
for n in numbers:
    total += n

print("Sum:", total)


# 2.4
list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 5, 7]

for n in list2:
    if n not in list1:
        print(n, "is not in list1")
    else:
        print(n, "is in list1")


# 2.4 - find position
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    a, b = b, a

numbers = list(range(a, b + 1))
print(numbers)

x = int(input("Enter a number inside the range: "))

if x in numbers:
    pos = numbers.index(x) + 1
    print("It is element", pos, "of the list")
else:
    print("The number is not in the list")


# 2.5
numbers = [1, 2, 3, 2, 4, 1, 5]
print("Original:", numbers)

clean = []
for n in numbers:
    if n not in clean:
        clean.append(n)

print("Without duplicates:", clean)

# 2.6
temps = [[h / 2 for h in range(24)] for d in range(31)]
min_afternoon = temps[0][12]
sum_3pm = 0

for day in range(31):
    afternoon = temps[day][12:24]
    if min(afternoon) < min_afternoon:
        min_afternoon = min(afternoon)
    sum_3pm += temps[day][15]

print("Min afternoon temperature:", min_afternoon)
print("Average at 3pm:", sum_3pm / 31)

# 2.7
numbers = [i**3 for i in range(7)]
print("Original:", numbers)

length = len(numbers)
for i in range(length // 2):
    numbers[i], numbers[length - i - 1] = numbers[length - i - 1], numbers[i]

print("Reversed:", numbers)

# 2.8
phonebook = {
    "lydia": 444444444,
    "victor": 666666666,
    "sergio": 888888888
}

for name in sorted(phonebook):
    print(name, ":", phonebook[name])

