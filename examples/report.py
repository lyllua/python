def report(title, *items, **details):
    print("==", title, "==")
    print("Items:")
    for item in items:
        print("-", item)
    print("Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

report("Expenses", "Bread", "Milk", total=12, currency="EUR")
