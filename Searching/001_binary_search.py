"""
Problem: Binary Search
Level: Easy
Link: https://leetcode.com/problems/binary-search/
Category: Searching

Description:
    Given a sorted array and target, return index of target or -1.

Example:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4

Hint:
    Compare target with middle element, eliminate half each time.

Expected Complexity:
    Time: O(log n)
    Space: O(1)
"""


def binary_search(arr: list, target: int) -> int:
    """Find target in sorted array, return index or -1."""
    # TODO: Implement binary search
    pass


# --- Test Cases ---
if __name__ == "__main__":
    arr = [-1, 0, 3, 5, 9, 12]
    assert binary_search(arr, 9) == 4
    assert binary_search(arr, 2) == -1
    print("✅ Binary search passed!")
