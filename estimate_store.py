# Estimate Store - Sprint 2
# This file only reads and writes the saved estimates file.
# It does no math and it does not talk to the user.


import json                                       # IMPORT - brings in tools to save and load a list from a file


class EstimateStore:                              # CLASS - a kind of object that looks after one saved file

    def __init__(self, file_name):                # FUNCTION - runs when a store object is made
        self.file_name = file_name                # VARIABLE - remembers which file this store looks after

    def load(self):                               # FUNCTION - reads the saved estimates from the file
        try:                                      # TRY - try to open the saved file
            saved_file = open(self.file_name, "r")      # VARIABLE = open() FUNCTION - opens the file to read it
            estimates = json.load(saved_file)           # VARIABLE = json.load() FUNCTION - reads the saved list from the file
            saved_file.close()                          # close() FUNCTION - closes the file
            return estimates                            # RETURN - hands the saved list back to the caller
        except FileNotFoundError:                       # EXCEPT - runs only if the file is not found yet
            return []                                   # RETURN - no saved file yet, so an empty list

    def save(self, estimates):                    # FUNCTION - writes the estimates list into the file
        saved_file = open(self.file_name, "w")    # VARIABLE = open() FUNCTION - opens the file to write it
        json.dump(estimates, saved_file)          # json.dump() FUNCTION - writes the list into the file
        saved_file.close()                        # close() FUNCTION - closes the file
