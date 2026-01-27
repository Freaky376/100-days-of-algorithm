"""
Problem: Reverse Linked List
Level: Easy
Link: https://leetcode.com/problems/reverse-linked-list/
Category: Linked Lists

Description:
    Given the head of a singly linked list, reverse the list, 
    and return the reversed list.

Example:
    Input: 1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1

Hint:
    Use three pointers: prev, curr, next. Update links as you traverse.

Expected Complexity:
    Time: O(n)
    Space: O(1) iterative, O(n) recursive
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    """
    Reverse the linked list.
    
    Args:
        head: Head of the linked list
        
    Returns:
        New head of the reversed list
    """
    # TODO: Implement your solution here
    pass


# --- Helper Functions ---
def create_list(values: list) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def list_to_array(head: ListNode) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# --- Test Cases ---
if __name__ == "__main__":
    head = create_list([1, 2, 3, 4, 5])
    result = list_to_array(reverse_list(head))
    assert result == [5, 4, 3, 2, 1], "Test 1 Failed"
    print("✅ Test 1 passed")
    
    head = create_list([1, 2])
    result = list_to_array(reverse_list(head))
    assert result == [2, 1], "Test 2 Failed"
    print("✅ Test 2 passed")
    
    print("\n🎉 All tests passed!")
