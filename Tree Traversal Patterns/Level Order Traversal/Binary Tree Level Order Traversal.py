## 102. Binary Tree Level Order Traversal

'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



 
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
'''
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def levelOrderTraversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        '''
        1. Level Order Traversal
            - since we want the nodes values by the level, we could use a level order traversal algorithm to go through row of the tree and group the nodes values. we can use a deque where for each node, we append its children to the deque while appending the node's value to a list if the node is not null. 
            - Time Complexity: O(n) is n is the number of nodes in the tree. This is because we visit each node at most twice, appending it to our deque O(1) and then popping it from the deque to see if we can append it to our current level's list. 
            - Space Complexity: O(n) because our answer list is proportional to the size of the nodes of the tree and our deque can hold upto O(n) for the largest row of nodes. 
        '''

        if not root:
            return []
        
        res = []

        q = deque()
        q.append(root)

        while q:
            qlen = len(q)
            level = []
            for _ in range(qlen):
                node = q.popleft()
                if node != None:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
    
root = TreeNode(3)
second = TreeNode(9)
third = TreeNode(20)
fourth = TreeNode(15)
fifth = TreeNode(7)
root.left, root.right = second, third
third.left, third.right = fourth, fifth

solution = Solution()
print(solution.levelOrderTraversal(root=root))
            
        


