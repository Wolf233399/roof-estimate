# Tests for estimate_logic.py - Sprint 2
# Each test calls one small function and checks the answer.
# Run them with: py -m pytest


from estimate_logic import calculate_area, calculate_squares, calculate_total   # IMPORT - brings in the math functions to test
from estimate_logic import is_valid_name, is_valid_measurement, make_estimate    # IMPORT - brings in the checking and record functions to test


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


def test_zero_measurement_is_not_valid():         # FUNCTION - tests the zero-measurement rule
    assert is_valid_measurement(0) == False       # assert - checks that 0 is not valid


def test_negative_measurement_is_not_valid():     # FUNCTION - tests the negative-measurement rule
    assert is_valid_measurement(-5) == False      # assert - checks that -5 is not valid


def test_positive_measurement_is_valid():         # FUNCTION - tests the good-measurement rule
    assert is_valid_measurement(40) == True       # assert - checks that 40 is valid


def test_make_estimate():                         # FUNCTION - tests the record builder
    result = make_estimate("Test", 20, 8500)     # VARIABLE = DICTIONARY - builds one estimate to check
    assert result["name"] == "Test"               # assert - checks the name part of the record
    assert result["squares"] == 20               # assert - checks the squares part of the record
    assert result["total"] == 8500               # assert - checks the total part of the record
