## 199. Binary Tree Right Side View

'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Explanation:



Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
Explanation:



Example 3:
Input: root = [1,null,3]
Output: [1,3]

Example 4:
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
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        '''
        1. Level Order Traversal
            - to get the right node val for each row if a left node val does exist, otherwise the left node. we can use a level order traversal where we initialize a variable called rightSide. everytime we pop a node from our queue, we assign rightSide to that node, essentially allowing the most right node to be assigned to rightSide
            - Time Complexity: O(n) where n is the number of nodes in our binary. We process each node at most twice, once when adding it the queue and removing it from the queue. 
            - Space Complexity: O(n) In the worst case (a complete binary tree), the maximum number of nodes stored at any level is roughly N/2.
        '''
        if not root:
            return []
        
        res = []

        q = deque()
        q.append(root)

        while q:
            qlen = len(q)
            rightSide = None
            for _ in range(qlen):
                node = q.popleft()
                rightSide = node.val

                if node.left != None: q.append(node.left)
                if node.right != None: q.append(node.right)
            if rightSide != None:
                res.append(rightSide)
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
print(solution.rightSideView(root=root))

