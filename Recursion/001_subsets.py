"""
Problem: Subsets (Power Set)
Level: Medium
Link: https://leetcode.com/problems/subsets/
Category: Recursion/Backtracking

Description:
    Given an array of unique integers, return all possible subsets.

Example:
    Input: [1, 2, 3]
    Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

Hint:
    Use backtracking. For each element, choose to include or exclude it.

Expected Complexity:
    Time: O(n * 2^n)
    Space: O(n)
"""


def subsets(nums: list) -> list[list]:
    """Generate all subsets using backtracking."""
    # TODO: Implement backtracking solution
    pass


# --- Test Cases ---
if __name__ == "__main__":
    result = subsets([1, 2, 3])
    assert len(result) == 8, f"Expected 8 subsets, got {len(result)}"
    assert [] in result
    assert [1, 2, 3] in result
    print(f"✅ Subsets: {result}")
