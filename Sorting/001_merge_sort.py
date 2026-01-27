"""
Problem: Merge Sort
Level: Medium
Link: https://leetcode.com/problems/sort-an-array/
Category: Sorting

Description:
    Implement merge sort - divide array in half, sort each, merge.

Example:
    Input: [38, 27, 43, 3, 9, 82, 10]
    Output: [3, 9, 10, 27, 38, 43, 82]

Hint:
    1. Divide array into halves until single elements
    2. Merge sorted halves back together

Expected Complexity:
    Time: O(n log n)
    Space: O(n)
"""


def merge_sort(arr: list) -> list:
    """Sort array using merge sort."""
    # TODO: Implement merge sort
    pass


def merge(left: list, right: list) -> list:
    """Merge two sorted arrays."""
    # TODO: Implement merge helper
    pass


# --- Test Cases ---
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    assert merge_sort(arr) == [3, 9, 10, 27, 38, 43, 82]
    print("✅ Merge sort passed!")
