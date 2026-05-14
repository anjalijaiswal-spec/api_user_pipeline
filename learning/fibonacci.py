
from typing import List

def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.

    Uses an iterative approach for O(n) time complexity and O(1) space complexity.
    
    Args:
        n: The position in the Fibonacci sequence (0-indexed).
           Must be a non-negative integer.
    
    Returns:
        The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    
    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(5)
        5
        >>> fibonacci(10)
        55
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


def fibonacci_sequence(n: int) -> List[int]:
    """
    Generate the first n Fibonacci numbers.
    
    Args:
        n: The count of Fibonacci numbers to generate.
           Must be a non-negative integer.
    
    Returns:
        A list of the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is negative.
    
    Examples:
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
        >>> fibonacci_sequence(8)
        [0, 1, 1, 2, 3, 5, 8, 13]
    """
    if n < 0:
        raise ValueError("ns must be a non-negative integer")
    
    sequence: List[int] = []
    for i in range(n):
        sequence.append(fibonacci(i))
    return sequence


if __name__ == "__main__":
    # Example usage
    print("First 10 Fibonacci numbers:")
    print(fibonacci_sequence(10))
    
    print("\nFibonacci number at position 15:")
    print(fibonacci(15))

