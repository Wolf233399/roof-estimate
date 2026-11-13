# Estimate Logic - Sprint 2
# This file holds the math and the checking rules for an estimate.
# It does not talk to the user and it does not touch any file.


def calculate_area(length, width):    # FUNCTION - works out the roof area
    area = length * width    # VARIABLE = CALCULATION - length times width
    return area    # RETURN - hands the area back to the caller


def calculate_squares(area):    # FUNCTION - works out the roofing squares
    squares = area / 100    # VARIABLE = CALCULATION - 1 square = 100 sq ft, so divide by 100
    return squares    # RETURN - hands the squares back to the caller


def calculate_total(material_cost, labor_cost, other_cost):    # FUNCTION - works out the total price
    total = material_cost + labor_cost + other_cost    # VARIABLE = CALCULATION - adds the 3 costs together
    return total    # RETURN - hands the total back to the caller


def is_valid_name(customer_name):    # FUNCTION - checks the customer name rule
    if customer_name == "":    # IF - checks if the name is empty
        return False    # RETURN - an empty name is not valid
    return True    # RETURN - a typed name is valid


def is_valid_address(address):    # FUNCTION - checks the address rule
    if address == "":    # IF - checks if the address is empty
        return False    # RETURN - an empty address is not valid
    return True    # RETURN - a typed address is valid


def is_valid_phone(phone):    # FUNCTION - checks the phone rule
    if phone == "":    # IF - checks if the phone is empty
        return False    # RETURN - an empty phone is not valid
    return True    # RETURN - a typed phone is valid


def is_valid_measurement(number):    # FUNCTION - checks a roof measurement rule
    if number <= 0:    # IF - checks if the number is 0 or less
        return False    # RETURN - 0 or less is not valid
    return True    # RETURN - more than 0 is valid


def make_estimate(customer_name, address, phone, squares, total):    # FUNCTION - builds one estimate record
    new_estimate = {"name": customer_name, "address": address, "phone": phone, "squares": squares, "total": total}    # VARIABLE = DICTIONARY - holds the customer's info and the results
    return new_estimate    # RETURN - hands the record back to the caller
