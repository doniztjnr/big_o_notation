"""
    COMPUTATIONAL COST O(n²)
    
        The number of operations increase significantly when more inputs 
        are passed.
        Polynomial functions looks like n², n³ so on.
"""

def O(n: int):
    for i in range(n): # O(n)
        for j in range(n): # O(n)
            print(n, end=' ')
        print('')
    
def main() -> None:
    O(5)

if __name__ == "__main__":
    main()