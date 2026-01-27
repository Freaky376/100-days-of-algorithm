"""
Problem: Linked List Cycle (Floyd's Cycle Detection)
Level: Easy
Link: https://leetcode.com/problems/linked-list-cycle/
Category: Linked Lists

Description:
    Given head, the head of a linked list, determine if the linked list 
    has a cycle in it. Return True if there is a cycle, False otherwise.

Example:
    Input: 3 -> 2 -> 0 -> -4 -> (back to 2)
    Output: True

Hint:
    Use slow/fast pointers. If they meet, there's a cycle.

Expected Complexity:
    Time: O(n)
    Space: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode) -> bool:
    """
    Detect if linked list has a cycle.
    
    Args:
        head: Head of the linked list
        
    Returns:
        True if cycle exists, False otherwise
    """
    # TODO: Implement Floyd's Tortoise and Hare algorithm
    pass


# --- Helper ---
def create_cycle_list(values: list, pos: int) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    cycle_node = head if pos == 0 else None
    for i, val in enumerate(values[1:], 1):
        curr.next = ListNode(val)
        curr = curr.next
        if i == pos:
            cycle_node = curr
    if pos >= 0:
        curr.next = cycle_node
    return head


# --- Test Cases ---
if __name__ == "__main__":
    head = create_cycle_list([3, 2, 0, -4], 1)
    assert has_cycle(head) == True, "Test 1 Failed"
    print("✅ Test 1 passed: cycle exists")
    
    head = create_cycle_list([1], -1)
    assert has_cycle(head) == False, "Test 2 Failed"
    print("✅ Test 2 passed: no cycle")
    
    print("\n🎉 All tests passed!")
