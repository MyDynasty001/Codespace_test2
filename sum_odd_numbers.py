#!/usr/bin/env python3
"""
Script to sum the first 10 odd numbers.
"""

def sum_first_n_odd_numbers(n):
    """
    Calculate the sum of the first n odd numbers.
    
    Args:
        n: The count of odd numbers to sum
        
    Returns:
        The sum of the first n odd numbers
    """
    total = 0
    for i in range(n):
        odd_number = 2 * i + 1
        total += odd_number
    return total


if __name__ == "__main__":
    n = 10
    result = sum_first_n_odd_numbers(n)
    print(f"The sum of the first {n} odd numbers is: {result}")
