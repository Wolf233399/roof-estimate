# Roof Estimate

Roofing Estimate Manager - an app for roofing contractors to create and manage estimates for residential roofing jobs.

## Sprint 1 Goal

Allow a roofing contractor to create a new estimate, see the roof area, squares, and total price calculated automatically, save the estimate, and view it in a list.

## Sprint 2 Goal

A roofer can save a full estimate with the customer's address and phone number, mark what stage the job is in (Draft, Submitted, Approved, Completed), and open any saved estimate to see all of its details in one place.

## What the Program Does

- Create an estimate with the customer's name, address, and phone number
- Enter the roof length and width, and the material, labor, and other costs
- The program calculates the roof area, the squares, and the total price
- Estimates are saved to a file and shown in a numbered list with their status
- Change the status of a saved estimate
- View all the details of one saved estimate

## Files

- `roof_estimate.py` - the main program; it talks to the user
- `estimate_logic.py` - the math and the checking rules
- `estimate_store.py` - saves and loads the estimates file
- `tests/` - the automated tests

## Technologies

- Python 3
- pytest (for the tests)

## How to Run

Open a terminal in the project folder and run: py roof_estimate.py

## How to Run the Tests

Open a terminal in the project folder and run: py -m pytest

All 23 tests should pass.

## Known Limitations

Creating, calculating, saving, listing, changing status, and viewing details are included. Dashboard, search, edit, and delete will come in later sprints.
