"""
Binary Search Template
======================
A reusable binary search template for various search problems.

Complexity:
    Time: O(log n)
    Space: O(1)
"""


def binary_search_basic(arr: list, target: int) -> int:
    """
    Basic binary search - find exact target.
    
    Returns:
        Index of target if found, -1 otherwise.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_left_bound(arr: list, target: int) -> int:
    """
    Find the leftmost (first) occurrence of target.
    
    Returns:
        Index of first occurrence, or insertion point if not found.
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left


def binary_search_right_bound(arr: list, target: int) -> int:
    """
    Find the rightmost (last) occurrence of target.
    
    Returns:
        Index after last occurrence, or insertion point if not found.
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left


def binary_search_condition(arr: list, condition) -> int:
    """
    Binary search with a custom condition function.
    Use for problems like "find minimum that satisfies condition".
    
    Args:
        condition: A function that returns True/False
        
    Returns:
        Index of first element satisfying the condition.
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if condition(arr[mid]):
            right = mid
        else:
            left = mid + 1
    
    return left


# --- Test Cases ---
if __name__ == "__main__":
    # Test basic binary search
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search_basic(arr, 7) == 3
    assert binary_search_basic(arr, 10) == -1
    print("✅ Basic binary search tests passed!")
    
    # Test left bound
    arr_dup = [1, 2, 2, 2, 3, 4]
    assert binary_search_left_bound(arr_dup, 2) == 1
    print("✅ Left bound tests passed!")
    
    # Test right bound
    assert binary_search_right_bound(arr_dup, 2) == 4
    print("✅ Right bound tests passed!")
    
    # Test condition-based search
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = binary_search_condition(arr, lambda x: x >= 5)
    assert result == 4  # First element >= 5 is at index 4
    print("✅ Condition-based search tests passed!")
    
    print("\n🎉 All binary search tests passed!")
