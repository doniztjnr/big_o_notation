"""
    COMPUTATIONAL COST O(log n)
        
        The algorithm logarithmic reduce to half one list all
        time that is executed.
"""

items: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search(array: list[int], x: int):
    """Binary Search 
        
        Split to conquer.
        Search the number inside of array looking to his index instead
        to his data.

    Args:
        array (list[int]): A vector with int values in growing order.
        x (int): The number that we are search inside of array.
    """

    idx: int = (len(array) - 1) // 2
    
    while x != array[idx]:

        if x > array[idx]:
            array = array[idx + 1:]

        elif x < array[idx]:
            array = array[:idx + 1]

        idx = (len(array) - 1) // 2
    
    print(f"X = {x};")
    print(f"SEARCH = {array[idx]};")

def main() -> None:
    binary_search(items, 5)

if __name__ == "__main__":
    main()