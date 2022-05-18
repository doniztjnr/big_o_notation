"""
    O(1)
    The TIME of execution and MEMORY used are CONSTANTS

    The operation is represented by one horizontal line 
    in term of scalability.
    This algorithm going to be executed in the same time forever.

"""

authors: list[str] = [
    'Andrew Ng', 'Josh Stamer', 'Kent Beck', 
    'Martin Fowler', 'Erick Evans', 'Erich Gamma'
]

def first_two_authors(authors: list[str]):
    print(authors[0]) # n(1)
    print(authors[1]) # n(1)

if __name__ == "__main__":
    first_two_authors(authors)