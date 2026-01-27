"""
Problem: Fibonacci Number
Level: Easy
Link: https://leetcode.com/problems/fibonacci-number/
Category: Dynamic Programming

Description:
    Calculate the nth Fibonacci number.
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)

Example:
    F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 3, F(5) = 5

Challenge:
    Implement multiple approaches:
    1. Naive recursive
    2. Memoization (top-down)
    3. Tabulation (bottom-up)
    4. Space-optimized O(1)

Expected Complexity:
    Time: O(n) with DP
    Space: O(1) with optimization
"""


def fib_recursive(n: int) -> int:
    """Naive recursive - O(2^n) time"""
    # TODO: Implement
    pass


def fib_memo(n: int, memo: dict = None) -> int:
    """Memoization - O(n) time, O(n) space"""
    # TODO: Implement
    pass


def fib_tabulation(n: int) -> int:
    """Bottom-up DP - O(n) time, O(n) space"""
    # TODO: Implement
    pass


def fib_optimized(n: int) -> int:
    """Space optimized - O(n) time, O(1) space"""
    # TODO: Implement
    pass


# --- Test Cases ---
if __name__ == "__main__":
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    for i, exp in enumerate(expected):
        assert fib_optimized(i) == exp, f"fib({i}) failed"
    
    print("✅ All Fibonacci tests passed!")
