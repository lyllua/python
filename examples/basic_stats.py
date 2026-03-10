nums = [float(input("Enter number: ")) for _ in range(5)]

mean = sum(nums) / len(nums)
variance = sum((x - mean) ** 2 for x in nums) / len(nums)
std_dev = variance ** 0.5

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)