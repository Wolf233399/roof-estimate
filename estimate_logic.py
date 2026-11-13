# Estimate Logic - Sprint 2
# This file holds the math and the checking rules for an estimate.
# It does not talk to the user and it does not touch any file.


STATUSES = ["Draft", "Submitted", "Approved", "Completed"]    # VARIABLE = LIST - the only stages an estimate can be in; one list, one place to change


def calculate_area(length, width):    # FUNCTION - works out the roof area
    area = length * width    # VARIABLE = CALCULATION - length times width
    return area    # RETURN - hands the area back to the caller


def calculate_squares(area):    # FUNCTION - works out how many squares the roof is
    squares = area / 100    # VARIABLE = CALCULATION - 100 sq ft = 1 square
    return squares    # RETURN - hands the squares back to the caller


def calculate_total(material_cost, labor_cost, other_cost):    # FUNCTION - adds the three costs
    total = material_cost + labor_cost + other_cost    # VARIABLE = CALCULATION - adds all three costs
    return total    # RETURN - hands the total price back to the caller


def is_valid_name(customer_name):    # FUNCTION - checks the customer name
    if customer_name == "":    # IF - an empty name is not allowed
        return False    # RETURN - False means not valid
    return True    # RETURN - True means valid


def is_valid_address(address):    # FUNCTION - checks the customer address
    if address == "":    # IF - an empty address is not allowed
        return False    # RETURN - False means not valid
    return True    # RETURN - True means valid


def is_valid_phone(phone):    # FUNCTION - checks the customer phone number
    if phone == "":    # IF - an empty phone number is not allowed
        return False    # RETURN - False means not valid
    return True    # RETURN - True means valid


def is_valid_measurement(number):    # FUNCTION - checks a roof measurement
    if number <= 0:    # IF - zero or negative is not allowed
        return False    # RETURN - False means not valid
    return True    # RETURN - True means valid


def is_valid_status(status):    # FUNCTION - checks a status word
    if status in STATUSES:    # IF - the word is one of the stages in the STATUSES list
        return True    # RETURN - True means valid
    return False    # RETURN - False means not valid


def set_status(estimate, new_status):    # FUNCTION - changes the status saved in one estimate
    if is_valid_status(new_status) == False:    # IF - the new status word is not a real stage
        return False    # RETURN - False means nothing was changed
    estimate["status"] = new_status    # VARIABLE - writes the new status into the estimate record
    return True    # RETURN - True means the status was changed


def make_estimate(customer_name, address, phone, squares, total):    # FUNCTION - builds one estimate record
    new_estimate = {"name": customer_name, "address": address, "phone": phone, "squares": squares, "total": total, "status": "Draft"}    # VARIABLE = DICTIONARY - one estimate, and every new one starts as Draft
    return new_estimate    # RETURN - hands the new estimate back to the caller
