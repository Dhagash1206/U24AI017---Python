"""Write a program to make the length of each element 15 of a given Numpy array and the
string centred, left-justified, right-justified with paddings of _ (underscore)."""

import numpy as np

def format_strings(arr):
    centered = np.array([s.center(15, '_') for s in arr])
    left_justified = np.array([s.ljust(15, '_') for s in arr])
    right_justified = np.array([s.rjust(15, '_') for s in arr])
    print("Original Car Brands:\n", arr)
    print("\nCentered:\n", centered)
    print("\nLeft-Justified:\n", left_justified)
    print("\nRight-Justified:\n", right_justified)
    


# Car brand array
arr = np.array(["Toyota", "BMW", "Mercedes", "Audi", "Honda", "Ford", "Hyundai", "Kia", "Nissan", "Chevrolet"])

format_strings(arr)
