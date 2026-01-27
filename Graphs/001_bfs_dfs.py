"""
Problem: Graph Traversal (BFS & DFS)
Level: Medium
Link: https://leetcode.com/problems/number-of-islands/
Category: Graphs

Description:
    Implement Breadth-First Search and Depth-First Search for graphs.

Example:
    Graph: A -- B
           |    |
           C -- D -- E
    
    BFS from A: [A, B, C, D, E]
    DFS from A: [A, B, D, C, E] (order may vary)

Hint:
    BFS uses a queue, DFS uses a stack (or recursion).

Expected Complexity:
    Time: O(V + E)
    Space: O(V)
"""
from collections import deque


def bfs(graph: dict, start: str) -> list[str]:
    """
    Breadth-First Search traversal.
    
    Args:
        graph: Adjacency list {node: [neighbors]}
        start: Starting node
        
    Returns:
        List of nodes in BFS order
    """
    # TODO: Implement BFS using a queue
    pass


def dfs(graph: dict, start: str) -> list[str]:
    """
    Depth-First Search traversal.
    
    Args:
        graph: Adjacency list {node: [neighbors]}
        start: Starting node
        
    Returns:
        List of nodes in DFS order
    """
    # TODO: Implement DFS using stack or recursion
    pass


# --- Test Cases ---
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D']
    }
    
    bfs_result = bfs(graph, 'A')
    assert 'A' == bfs_result[0], "BFS should start with A"
    assert len(bfs_result) == 5, "BFS should visit all 5 nodes"
    print(f"✅ BFS: {bfs_result}")
    
    dfs_result = dfs(graph, 'A')
    assert 'A' == dfs_result[0], "DFS should start with A"
    assert len(dfs_result) == 5, "DFS should visit all 5 nodes"
    print(f"✅ DFS: {dfs_result}")
    
    print("\n🎉 All tests passed!")
