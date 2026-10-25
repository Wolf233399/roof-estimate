# Roof Estimate - Sprint 1                      <- title comment
# US-01: Create an estimate / US-02: Calculate area, squares, total

print("Roof Estimate")                          # print() FUNCTION - shows text on screen
print("Create a new estimate")                  # print() FUNCTION - shows text on screen

customer_name = input("Customer name: ")        # VARIABLE = input() FUNCTION - waits for typing, saves it in customer_name

length = float(input("Roof length in feet: "))  # VARIABLE = float() FUNCTION changes typing to a decimal number, input() asks for it
width = float(input("Roof width in feet: "))    # VARIABLE = float() + input() FUNCTIONS - same as above

material_cost = float(input("Material cost: $"))  # VARIABLE = float() + input() FUNCTIONS
labor_cost = float(input("Labor cost: $"))        # VARIABLE = float() + input() FUNCTIONS
other_cost = float(input("Other cost: $"))        # VARIABLE = float() + input() FUNCTIONS

area = length * width                           # VARIABLE = CALCULATION - length times width
squares = area / 100                            # VARIABLE = CALCULATION - 1 square = 100 sq ft, so divide by 100
total = material_cost + labor_cost + other_cost # VARIABLE = CALCULATION - adds the 3 costs

print()                                         # print() FUNCTION - blank line for spacing
print("Estimate for:", customer_name)           # print() FUNCTION - shows text + the VARIABLE customer_name
print("Roof area:", area, "sq ft")              # print() FUNCTION - shows the area VARIABLE
print("Roofing squares:", squares)              # print() FUNCTION - shows the squares VARIABLE
print("Total price: $", total)                  # print() FUNCTION - shows the total VARIABLE
