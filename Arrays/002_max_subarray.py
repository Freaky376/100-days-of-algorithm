"""
Problem: Maximum Subarray (Kadane's Algorithm)
Level: Medium
Link: https://leetcode.com/problems/maximum-subarray/
Category: Arrays

Description:
    Given an integer array nums, find the subarray with the largest sum,
    and return its sum.

Example:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6 (subarray [4,-1,2,1] has the largest sum)

Hint:
    Track current sum and max sum. Reset current if it goes negative.

Expected Complexity:
    Time: O(n)
    Space: O(1)
"""


def max_subarray(nums: list[int]) -> int:
    """
    Find the maximum sum of any contiguous subarray.
    
    Args:
        nums: List of integers (can be negative)
        
    Returns:
        Maximum subarray sum
    """
    # TODO: Implement Kadane's algorithm here
    pass


# --- Test Cases ---
if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "Test 1 Failed"
    print("✅ Test 1 passed")
    
    assert max_subarray([1]) == 1, "Test 2 Failed"
    print("✅ Test 2 passed")
    
    assert max_subarray([5, 4, -1, 7, 8]) == 23, "Test 3 Failed"
    print("✅ Test 3 passed")
    
    assert max_subarray([-3, -2, -5, -1]) == -1, "Test 4 Failed"
    print("✅ Test 4 passed")
    
    print("\n🎉 All tests passed!")
