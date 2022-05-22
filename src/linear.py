"""
    COMPUTATIONAL COST O(n)

        Making iteration for each value in loop the OPERATIONS increase 
        linearly. 
        TIME and MEMORY increase of according INPUTS size.
    
    EXAMPLE 
        n = 10 going to have Time and Memory different of n = 1_000_000.
"""

def O(n: int):
    
    for i in range(n): # O(n)
        print(i)
    
    print(f"Number: {i}")
    
def main() -> None:
    O(10_000)

if __name__ == "__main__":
    main()