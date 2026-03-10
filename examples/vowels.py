text = (input("Enter a phrase: "))
vowels = ["a", "e", "i", "o", "u"]

count = 0

for letter in text.lower():
    if letter in vowels:
        count += 1

print(f"The phrase contains {count} vowels")