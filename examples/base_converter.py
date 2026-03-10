n = int(input("Enter a decimal number: "))
print("Binary:", bin(n))
print("Hex:", hex(n))
print("Octal:", oct(n))

b = input("Enter a binary number: ")
print("Binary to decimal:", int(b, 2))

h = input("Enter a hexadecimal number: ")
print("Binary + Hex (in decimal):", int(b, 2) + int(h, 16))