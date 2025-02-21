# create a tuple called dimensions
# print each dimension in the tuple

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# use a for loop to print each dimension in the tuple

for dimension in dimensions:
    print(dimension)

# print the original tuple
# reasign the variable with new values and print the modified dimensions

print(f"Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print(f"The modified dimensions are:")
for dimension in dimensions:
    print(dimension)