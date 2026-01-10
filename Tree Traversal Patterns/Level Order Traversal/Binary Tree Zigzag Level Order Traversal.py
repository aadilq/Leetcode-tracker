## 103. Binary Tree Zigzag Level Order Traversal

'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

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
    def zigZagTraversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        '''
        1. level order traversal
            - in order to group the nodes by their respective level, we can use a standard bfs algorithm. in order to return the zigzag levels (left to right, right to left), we can use a variable called levelOrder. initially our levelOrder variable is going to be 1 to represent the first level with the root node, which appears as normal. each time we go to a new level in our tree, we increment levelOrder by 1. when levelOrder % 2 == 0, this means we're at a level where we have to reverse the order of nodes. 
            - Time Complexity: O(n) where n is the number of nodes in our tree. this is because each node is processed at most twice, once for enqueuing the node and second for dequeing the node (both operation O(1)) and reversing the list is also O(n)
            - Space Complexity: O(n) where n is the number of nodes in our tree because our output array is prorportional to the amount of nodes and atmost our deque can hold upto n nodes for the largest row in our tree. 
        '''
        if not root:
            return []
        
        res = []
        q = deque()
        q.append(root)

        levelOrder = 1

        while q:
            qlen = len(q)
            level = []
            for _ in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                if levelOrder % 2 == 0:
                    res.append(level[::-1])
                else:
                    res.append(level)
            levelOrder += 1
        return res
root = TreeNode(3)
second = TreeNode(9)
third = TreeNode(20)
fourth = TreeNode(15)
fifth = TreeNode(7)
root.left, root.right = second, third
third.left, third.right = fourth, fifth
solution = Solution()
print(solution.zigZagTraversal(root=root))