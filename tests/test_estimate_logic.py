# Tests for estimate_logic.py - Sprint 2
# Each test calls one small function and checks the answer.
# Run them with: py -m pytest


from estimate_logic import calculate_area, calculate_squares, calculate_total   # IMPORT - brings in the math functions to test
from estimate_logic import is_valid_name, is_valid_address, is_valid_phone, is_valid_measurement, is_valid_status, make_estimate, set_status    # IMPORT - brings in the checking and record functions to test


def test_calculate_area():                        # FUNCTION - tests the area math
    assert calculate_area(40, 50) == 2000        # assert - checks that 40 times 50 is 2000


def test_calculate_squares():                     # FUNCTION - tests the squares math
    assert calculate_squares(2000) == 20         # assert - checks that 2000 divided by 100 is 20


def test_calculate_total():                       # FUNCTION - tests the total math
    assert calculate_total(5000, 3000, 500) == 8500   # assert - checks that 5000 + 3000 + 500 is 8500


def test_empty_name_is_not_valid():               # FUNCTION - tests the empty-name rule
    assert is_valid_name("") == False             # assert - checks that an empty name is not valid


def test_typed_name_is_valid():                   # FUNCTION - tests the typed-name rule
    assert is_valid_name("Test") == True          # assert - checks that a typed name is valid


def test_empty_address_is_not_valid():            # FUNCTION - tests the empty-address rule
    assert is_valid_address("") == False          # assert - checks that an empty address is not valid


def test_typed_address_is_valid():                # FUNCTION - tests the typed-address rule
    assert is_valid_address("123 Main St") == True   # assert - checks that a typed address is valid


def test_empty_phone_is_not_valid():              # FUNCTION - tests the empty-phone rule
    assert is_valid_phone("") == False            # assert - checks that an empty phone is not valid


def test_typed_phone_is_valid():                  # FUNCTION - tests the typed-phone rule
    assert is_valid_phone("555-1234") == True     # assert - checks that a typed phone is valid


def test_zero_measurement_is_not_valid():         # FUNCTION - tests the zero-measurement rule
    assert is_valid_measurement(0) == False       # assert - checks that 0 is not valid


def test_negative_measurement_is_not_valid():     # FUNCTION - tests the negative-measurement rule
    assert is_valid_measurement(-5) == False      # assert - checks that -5 is not valid


def test_positive_measurement_is_valid():         # FUNCTION - tests the good-measurement rule
    assert is_valid_measurement(40) == True       # assert - checks that 40 is valid


def test_good_status_is_valid():                  # FUNCTION - tests the good-status rule
    assert is_valid_status("Approved") == True    # assert - checks that Approved is a real stage


def test_bad_status_is_not_valid():               # FUNCTION - tests the bad-status rule
    assert is_valid_status("Banana") == False     # assert - checks that a made-up word is not a stage


def test_empty_status_is_not_valid():             # FUNCTION - tests the empty-status rule
    assert is_valid_status("") == False           # assert - checks that an empty status is not valid


def test_set_status_changes_it():                 # FUNCTION - tests changing a status
    estimate = make_estimate("Test", "123 Main St", "555-1234", 40, 50, 2000, 20, 5000, 3000, 500, 8500)   # VARIABLE = DICTIONARY - builds one estimate to change
    assert set_status(estimate, "Submitted") == True   # assert - checks the change was accepted
    assert estimate["status"] == "Submitted"      # assert - checks the record now holds the new status


def test_set_status_rejects_bad_word():           # FUNCTION - tests refusing a bad status word
    estimate = make_estimate("Test", "123 Main St", "555-1234", 40, 50, 2000, 20, 5000, 3000, 500, 8500)   # VARIABLE = DICTIONARY - builds one estimate to try to change
    assert set_status(estimate, "Banana") == False   # assert - checks the change was refused
    assert estimate["status"] == "Draft"          # assert - checks the status stayed Draft


def test_make_estimate():                         # FUNCTION - tests the record builder
    result = make_estimate("Test", "123 Main St", "555-1234", 40, 50, 2000, 20, 5000, 3000, 500, 8500)   # VARIABLE = DICTIONARY - builds one estimate to check
    assert result["name"] == "Test"               # assert - checks the name part of the record
    assert result["address"] == "123 Main St"     # assert - checks the address part of the record
    assert result["phone"] == "555-1234"          # assert - checks the phone part of the record
    assert result["length"] == 40                # assert - checks the length part of the record
    assert result["width"] == 50                 # assert - checks the width part of the record
    assert result["area"] == 2000                # assert - checks the area part of the record
    assert result["squares"] == 20               # assert - checks the squares part of the record
    assert result["material"] == 5000            # assert - checks the material cost part of the record
    assert result["labor"] == 3000               # assert - checks the labor cost part of the record
    assert result["other"] == 500                # assert - checks the other cost part of the record
    assert result["total"] == 8500               # assert - checks the total part of the record
    assert result["status"] == "Draft"            # assert - checks a new record starts as Draft
