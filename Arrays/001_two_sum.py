"""
Problem: Two Sum
Level: Easy
Link: https://leetcode.com/problems/two-sum/
Category: Arrays

Description:
    Given an array of integers nums and an integer target, return indices of 
    the two numbers such that they add up to target.
    
    You may assume that each input would have exactly one solution, and you 
    may not use the same element twice.

Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1] (because nums[0] + nums[1] == 9)

Hint:
    Consider using a hash map to store values you've seen.

Expected Complexity:
    Time: O(n)
    Space: O(n)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two indices whose values sum to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices [i, j] where nums[i] + nums[j] == target
    """
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
    return []


# --- Test Cases ---
if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1], "Test 1 Failed"
    print("✅ Test 1 passed")
    
    assert two_sum([3, 2, 4], 6) == [1, 2], "Test 2 Failed"
    print("✅ Test 2 passed")
    
    assert two_sum([3, 3], 6) == [0, 1], "Test 3 Failed"
    print("✅ Test 3 passed")
    
    print("\n🎉 All tests passed!")
