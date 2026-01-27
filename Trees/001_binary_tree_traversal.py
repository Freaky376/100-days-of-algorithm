"""
Problem: Binary Tree Traversals
Level: Easy
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
Category: Trees

Description:
    Implement tree traversals:
    - Inorder (Left, Root, Right)
    - Preorder (Root, Left, Right)  
    - Postorder (Left, Right, Root)

Example:
        1
       / \
      2   3
     / \
    4   5
    
    Inorder: [4, 2, 5, 1, 3]
    Preorder: [1, 2, 4, 5, 3]
    Postorder: [4, 5, 2, 3, 1]

Expected Complexity:
    Time: O(n)
    Space: O(h) where h = height
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: TreeNode) -> list[int]:
    # TODO: Left -> Root -> Right
    pass

def preorder(root: TreeNode) -> list[int]:
    # TODO: Root -> Left -> Right
    pass

def postorder(root: TreeNode) -> list[int]:
    # TODO: Left -> Right -> Root
    pass


# --- Helper ---
def build_tree(values: list) -> TreeNode:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# --- Test Cases ---
if __name__ == "__main__":
    root = build_tree([1, 2, 3, 4, 5])
    
    assert inorder(root) == [4, 2, 5, 1, 3], "Inorder failed"
    print("✅ Inorder passed")
    
    assert preorder(root) == [1, 2, 4, 5, 3], "Preorder failed"
    print("✅ Preorder passed")
    
    assert postorder(root) == [4, 5, 2, 3, 1], "Postorder failed"
    print("✅ Postorder passed")
    
    print("\n🎉 All tests passed!")
