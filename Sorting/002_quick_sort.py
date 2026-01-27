"""
Problem: Quick Sort
Level: Medium
Link: https://leetcode.com/problems/sort-an-array/
Category: Sorting

Description:
    Implement quick sort - pick pivot, partition, sort subarrays.

Example:
    Input: [64, 34, 25, 12, 22, 11, 90]
    Output: [11, 12, 22, 25, 34, 64, 90]

Hint:
    1. Pick a pivot element
    2. Partition: elements < pivot go left, > pivot go right
    3. Recursively sort left and right

Expected Complexity:
    Time: O(n log n) average, O(n²) worst
    Space: O(log n)
"""


def quick_sort(arr: list) -> list:
    """Sort array using quick sort."""
    # TODO: Implement quick sort
    pass


# --- Test Cases ---
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert quick_sort(arr) == [11, 12, 22, 25, 34, 64, 90]
    print("✅ Quick sort passed!")
