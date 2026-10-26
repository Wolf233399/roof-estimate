# Roof Estimate - Sprint 1                      <- title comment
# US-01: Create an estimate / US-02: Calculate area, squares, total
# US-03: Save an estimate and view the saved list

import json                                       # IMPORT - brings in tools to save and load a list from a file

estimates = []                                    # VARIABLE = LIST - empty list, will hold the saved estimates

try:                                              # TRY - try to open the saved file
    saved_file = open("estimates.json", "r")      # VARIABLE = open() FUNCTION - opens the file to read it
    estimates = json.load(saved_file)             # VARIABLE = json.load() FUNCTION - reads the saved list from the file
    saved_file.close()                            # close() FUNCTION - closes the file
except FileNotFoundError:                         # EXCEPT - runs only if the file is not found yet
    estimates = []                                # VARIABLE = LIST - no saved file yet, so start with an empty list

print("Roof Estimate")                          # print() FUNCTION - shows text on screen
print("Create a new estimate")                  # print() FUNCTION - shows text on screen

customer_name = input("Customer name: ")        # VARIABLE = input() FUNCTION - waits for typing, saves it in customer_name

if customer_name == "":                         # IF - checks if the name is empty
    print("Error: Customer name cannot be empty.")  # print() FUNCTION - shows the error message
    exit()                                      # exit() FUNCTION - stops the program

length = float(input("Roof length in feet: "))  # VARIABLE = float() FUNCTION changes typing to a decimal number, input() asks for it

if length <= 0:                                 # IF - checks if length is 0 or less
    print("Error: Roof length must be more than 0.")  # print() FUNCTION - shows the error message
    exit()                                      # exit() FUNCTION - stops the program

width = float(input("Roof width in feet: "))    # VARIABLE = float() + input() FUNCTIONS - same as length

if width <= 0:                                  # IF - checks if width is 0 or less
    print("Error: Roof width must be more than 0.")  # print() FUNCTION - shows the error message
    exit()                                      # exit() FUNCTION - stops the program

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

new_estimate = {"name": customer_name, "squares": squares, "total": total}  # VARIABLE = DICTIONARY - one estimate, with named parts
estimates.append(new_estimate)                  # append() FUNCTION - adds the new estimate to the list

saved_file = open("estimates.json", "w")        # VARIABLE = open() FUNCTION - opens the file to write it
json.dump(estimates, saved_file)                # json.dump() FUNCTION - writes the list into the file
saved_file.close()                              # close() FUNCTION - closes the file

print()                                         # print() FUNCTION - blank line for spacing
print("Saved estimates:")                       # print() FUNCTION - shows the list title
for estimate in estimates:                      # LOOP - goes through each saved estimate, one at a time
    print("Name:", estimate["name"], "- Squares:", estimate["squares"], "- Total: $", estimate["total"])  # print() FUNCTION - shows name, squares, total from the DICTIONARY
