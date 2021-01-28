size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
print(square_feet)
square_meters = square_feet / 10.8
print(square_meters)
print(f"the size of your house in square feet {square_feet} in square meters is {square_meters:.2f}")