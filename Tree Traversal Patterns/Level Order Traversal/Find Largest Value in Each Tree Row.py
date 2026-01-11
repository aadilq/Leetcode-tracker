## 515. Find Largest Value in Each Tree Row

'''
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]
'''
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        '''
        1. level order traversal
            - we do a standard level order traversal but we keep track of each level we are currently at and current max at each level. for each level, we append the largest value to our resulting array. 
            - Time Complexity: O(n) where n is the number of nodes in our binary tree. we visit each node exactly once and process it at most two times using a queue. 
            - Space Complexity: O(n) because at most, our deque can hold up to n nodes, however, our resulting array is going roughly n / 2 nodes. 
             1 
            / \
            
        '''

        if not root:
            return []
        
        res = []
        q = deque()
        q.append(root)

        while q:
            qlen = len(q)
            currMax = float('-inf')
            for _ in range(qlen):
                node = q.popleft()
                if node.val > currMax:
                    currMax = node.val
    
                if node.left != None: q.append(node.left)
                if node.right != None: q.append(node.right)
            res.append(currMax)
        return res
    
root = TreeNode(1)
second = TreeNode(2)
third = TreeNode(3)
fourth = TreeNode(4)
fifth = TreeNode(5)

root.left, root.right = second, third
second.right = fifth
third.right = fourth

solution = Solution()
print(solution.largestValues(root=root))

        


