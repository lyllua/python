print("Enter a four digit integer:")
number = int(input())

a = number // 1000
b = (number // 100) % 10
c = (number // 10) % 10
d = number % 10

print("Thousands: ", a)
print("Hundreds: ", b)
print("Tens: ", c)
print("Units: ", d)
