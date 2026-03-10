savings = 0

def deposit(amount):
    global savings
    savings += amount

def create_deposit_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = create_deposit_counter()

deposit(10)
deposit(5)
print(savings)     
print(counter())
print(counter())




