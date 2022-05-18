"""
    O(n)
    The term (n) represent the number of inputs.

    Making one unique iteration for each value in loop
    the OPERATIONS increase linearly.
    This algorithm have a linear time of execution. 
"""

import time

lot_of_items: list[str] = ["coffee"] * 10_000

def find_coffee(items: list[str]):
    start = time.time()

    for item in items: # O(n)
        if (item == "coffee"):
            print("Found Coffee")

    finish = time.time()

    print(f"The operation took {(finish - start)} ms")

if __name__ == "__main__":
    find_coffee(lot_of_items)