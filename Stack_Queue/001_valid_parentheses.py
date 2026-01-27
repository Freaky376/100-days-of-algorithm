"""
Problem: Valid Parentheses
Level: Easy
Link: https://leetcode.com/problems/valid-parentheses/
Category: Stack

Description:
    Check if string has valid matching brackets: (), {}, []

Example:
    "()" -> True
    "()[]{}" -> True
    "(]" -> False
    "([)]" -> False

Hint:
    Use a stack. Push opening brackets, pop and match closing ones.

Expected Complexity:
    Time: O(n)
    Space: O(n)
"""


def is_valid(s: str) -> bool:
    """Check if parentheses are valid."""
    # TODO: Implement using a stack
    pass


# --- Test Cases ---
if __name__ == "__main__":
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("{[]}") == True
    print("✅ Valid parentheses passed!")
