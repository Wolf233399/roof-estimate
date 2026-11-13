# Roof Estimate - Sprint 2
# US-01: Create an estimate / US-02: Calculate area, squares, total
# US-03: Save an estimate and view the saved list
# Sprint 2 split: the math lives in estimate_logic.py, the file work lives in estimate_store.py,
# and this file only talks to the user (Single Responsibility).


from estimate_logic import calculate_area, calculate_squares, calculate_total   # IMPORT - brings in the math functions
from estimate_logic import is_valid_name, is_valid_address, is_valid_phone, is_valid_measurement, is_valid_status, make_estimate, set_status    # IMPORT - brings in the checking and record functions
from estimate_store import EstimateStore          # IMPORT - brings in the store class


def main(store):                                  # FUNCTION - runs the program; the store is handed in, not made here (Dependency Inversion)

    estimates = store.load()                      # VARIABLE = LIST - the saved estimates, read by the store

    print("Roof Estimate")                        # print() FUNCTION - shows text on screen
    print("Create a new estimate")                # print() FUNCTION - shows text on screen

    customer_name = input("Customer name: ")      # VARIABLE = input() FUNCTION - waits for typing, saves it in customer_name

    if is_valid_name(customer_name) == False:     # IF - checks if the name is empty, using the logic function
        print("Error: Customer name cannot be empty.")   # print() FUNCTION - shows the error message
        exit()                                    # exit() FUNCTION - stops the program

    address = input("Customer address: ")         # VARIABLE = input() FUNCTION - waits for typing, saves it in address

    if is_valid_address(address) == False:        # IF - checks if the address is empty, using the logic function
        print("Error: Customer address cannot be empty.")   # print() FUNCTION - shows the error message
        exit()                                    # exit() FUNCTION - stops the program

    phone = input("Customer phone: ")             # VARIABLE = input() FUNCTION - waits for typing, saves it in phone

    if is_valid_phone(phone) == False:            # IF - checks if the phone is empty, using the logic function
        print("Error: Customer phone cannot be empty.")   # print() FUNCTION - shows the error message
        exit()                                    # exit() FUNCTION - stops the program

    try:                                          # TRY - try to read the length as a number
        length = float(input("Roof length in feet: "))   # VARIABLE = float() FUNCTION changes typing to a decimal number, input() asks for it
    except ValueError:                            # EXCEPT - runs only if the typing was not a number
        print("Error: Roof length must be a number only, like 40.")   # print() FUNCTION - shows the error message
        exit()                                    # exit() FUNCTION - stops the program

    if is_valid_measurement(length) == False:     # IF - checks if length is 0 or less, using the logic function
        print("Error: Roof length must be more than 0.")   # print() FUNCTION - shows the error message
        exit()                                    # exit() FUNCTION - stops the program

    try:                                          # TRY - try to read the width as a number
        width = float(input("Roof width in feet: "))   # VARIABLE = float() + input() FUNCTIONS - same as length
    except ValueError:                            # EXCEPT - runs only if the typing was not a number
        print("Error: Roof width must be a number only, like 50.")   # print() FUNCTION - shows the error message
        exit()                                    # exit() FUNCTION - stops the program

    if is_valid_measurement(width) == False:      # IF - checks if width is 0 or less, using the logic function
        print("Error: Roof width must be more than 0.")   # print() FUNCTION - shows the error message
        exit()                                    # exit() FUNCTION - stops the program

    try:                                          # TRY - try to read the material cost as a number
        material_cost = float(input("Material cost: $"))   # VARIABLE = float() + input() FUNCTIONS
    except ValueError:                            # EXCEPT - runs only if the typing was not a number
        print("Error: Material cost must be a number only, like 5000.")   # print() FUNCTION - shows the error message
        exit()                                    # exit() FUNCTION - stops the program

    try:                                          # TRY - try to read the labor cost as a number
        labor_cost = float(input("Labor cost: $"))   # VARIABLE = float() + input() FUNCTIONS
    except ValueError:                            # EXCEPT - runs only if the typing was not a number
        print("Error: Labor cost must be a number only, like 3000.")   # print() FUNCTION - shows the error message
        exit()                                    # exit() FUNCTION - stops the program

    try:                                          # TRY - try to read the other cost as a number
        other_cost = float(input("Other cost: $"))   # VARIABLE = float() + input() FUNCTIONS
    except ValueError:                            # EXCEPT - runs only if the typing was not a number
        print("Error: Other cost must be a number only, like 500.")   # print() FUNCTION - shows the error message
        exit()                                    # exit() FUNCTION - stops the program

    area = calculate_area(length, width)          # VARIABLE = CALCULATION - the logic function times length by width
    squares = calculate_squares(area)             # VARIABLE = CALCULATION - the logic function divides area by 100
    total = calculate_total(material_cost, labor_cost, other_cost)   # VARIABLE = CALCULATION - the logic function adds the 3 costs

    print()                                       # print() FUNCTION - blank line for spacing
    print("Estimate for:", customer_name)         # print() FUNCTION - shows text + the VARIABLE customer_name
    print("Roof area:", area, "sq ft")            # print() FUNCTION - shows the area VARIABLE
    print("Roofing squares:", squares)            # print() FUNCTION - shows the squares VARIABLE
    print("Total price: $", total)                # print() FUNCTION - shows the total VARIABLE

    new_estimate = make_estimate(customer_name, address, phone, squares, total)   # VARIABLE = DICTIONARY - the logic function builds one estimate record
    estimates.append(new_estimate)                # append() FUNCTION - adds the new estimate to the list

    store.save(estimates)                         # FUNCTION CALL - the store writes the list into the file

    print()                                       # print() FUNCTION - blank line for spacing
    print("Saved estimates:")                     # print() FUNCTION - shows the list title

    number = 1                                    # VARIABLE - counts the estimates as the list prints

    for estimate in estimates:                    # LOOP - goes through each saved estimate, one at a time
        print(number, "Name:", estimate["name"], "- Squares:", estimate["squares"], "- Total: $", estimate["total"], "- Status:", estimate.get("status", "Draft"))   # print() FUNCTION - shows number, name, squares, total, status from the DICTIONARY; get() shows Draft for old estimates that have no status saved
        number = number + 1                       # VARIABLE = CALCULATION - moves the counter to the next number

    print()                                       # print() FUNCTION - blank line for spacing

    change = input("Do you want to change the status of an estimate? Type y or n: ")   # VARIABLE = input() FUNCTION - waits for typing, saves it in change

    if change == "y":                             # IF - only runs when the answer is y

        try:                                      # TRY - try to read the estimate number as a whole number
            pick = int(input("Type the number of the estimate: "))   # VARIABLE = int() FUNCTION changes typing to a whole number, input() asks for it
        except ValueError:                        # EXCEPT - runs only if the typing was not a number
            print("Error: Please type a number only.")   # print() FUNCTION - shows the error message
            exit()                                # exit() FUNCTION - stops the program

        if pick < 1 or pick > len(estimates):     # IF - the number is not on the list
            print("Error: That number is not on the list.")   # print() FUNCTION - shows the error message
            exit()                                # exit() FUNCTION - stops the program

        print("Stages: Draft, Submitted, Approved, Completed")   # print() FUNCTION - shows the 4 stages to pick from

        new_status = input("Type the new status: ")   # VARIABLE = input() FUNCTION - waits for typing, saves it in new_status

        if set_status(estimates[pick - 1], new_status) == False:   # IF - the logic function says the word is not a real stage; pick - 1 because the list starts counting at 0
            print("Error: Status must be Draft, Submitted, Approved, or Completed.")   # print() FUNCTION - shows the error message
            exit()                                # exit() FUNCTION - stops the program

        store.save(estimates)                     # FUNCTION CALL - the store writes the list with the new status into the file

        print()                                   # print() FUNCTION - blank line for spacing
        print("Status changed. Saved estimates:")   # print() FUNCTION - shows the list title again

        number = 1                                # VARIABLE - starts the counting again at 1

        for estimate in estimates:                # LOOP - goes through each saved estimate, one at a time
            print(number, "Name:", estimate["name"], "- Squares:", estimate["squares"], "- Total: $", estimate["total"], "- Status:", estimate.get("status", "Draft"))   # print() FUNCTION - shows the list with the new status in it
            number = number + 1                   # VARIABLE = CALCULATION - moves the counter to the next number


store = EstimateStore("estimates.json")           # VARIABLE = OBJECT - the real store, made here and handed to main
main(store)                                       # FUNCTION CALL - runs the program with the real store handed in
