"""
    O(n²)
    Polynomial Time Notation

    By default is used the multiplication for nested loops, in this 
    algorithm below are done O(n) multiplied by O(n) that is O(n²).

    Algorithm that have polynomial time increase the number of operations
    significantly when more inputs are passed.

    Polynomial functions looks like n², n³ so on.
"""

items: list[str] = [
    'Andrew Ng', 'François Chollet', 'Josh Stamer', 
    'Kent Beck', 'Erick Evans', 'Soumith Chintala'
]

def find_all_pairs(items: list[str]):
    for item_a in items: # O(n)
        for item_b in items: # O(n)
            print(f"{item_a} - {item_b}")

if __name__ == "__main__":
    find_all_pairs(items)