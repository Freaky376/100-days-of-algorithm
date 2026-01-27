"""
Problem: Valid Palindrome
Level: Easy
Link: https://leetcode.com/problems/valid-palindrome/
Category: Strings

Description:
    Check if string is palindrome (considering only alphanumeric, ignore case).

Example:
    Input: "A man, a plan, a canal: Panama"
    Output: True

Hint:
    Use two pointers from both ends, skip non-alphanumeric.

Expected Complexity:
    Time: O(n)
    Space: O(1)
"""


def is_palindrome(s: str) -> bool:
    """Check if string is a valid palindrome."""
    # TODO: Implement with two pointers
    pass


# --- Test Cases ---
if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome(" ") == True
    print("✅ Valid palindrome passed!")
