"""
Problem: Climbing Stairs
Level: Easy
Link: https://leetcode.com/problems/climbing-stairs/
Category: Dynamic Programming

Description:
    You are climbing a staircase with n steps.
    Each time you can climb 1 or 2 steps.
    How many distinct ways can you reach the top?

Example:
    n=2: 2 ways (1+1, 2)
    n=3: 3 ways (1+1+1, 1+2, 2+1)
    n=4: 5 ways

Hint:
    This is essentially the Fibonacci problem!
    ways(n) = ways(n-1) + ways(n-2)

Expected Complexity:
    Time: O(n)
    Space: O(1)
"""


def climb_stairs(n: int) -> int:
    """
    Count distinct ways to climb n stairs.
    
    Args:
        n: Number of stairs
        
    Returns:
        Number of distinct ways
    """
    # TODO: Implement your solution
    pass


# --- Test Cases ---
if __name__ == "__main__":
    assert climb_stairs(1) == 1, "Test 1 Failed"
    assert climb_stairs(2) == 2, "Test 2 Failed"
    assert climb_stairs(3) == 3, "Test 3 Failed"
    assert climb_stairs(4) == 5, "Test 4 Failed"
    assert climb_stairs(5) == 8, "Test 5 Failed"
    
    print("✅ All Climbing Stairs tests passed!")
