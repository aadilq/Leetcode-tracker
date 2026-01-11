## 287. Find the Duplicate Number

'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
'''
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
        1. Level order traversal 
            - we perform a standard level order traversal but we also keep track of the level of which we are at and cumulative sum of all the values in that level. for each level, we add all of the nodes values and check if that is bigger than our previous maximum sum, if it is, we replace our result with that level and with each time we move to a new row, we increase our level by 1.
            - Time Complexity: O(n) where n is the number of nodes in our binary tree. we visit each node exactly once. 
            - Space Complexity: O(n) because in the worst case, our queue can hold up at most up to n nodes.
        '''
        res = 0

        level = 1

        q = deque()
        q.append(root)
        maxsum = float('-inf')

        while q:
            qlen = len(q)
            currsum = 0
            for _ in range(qlen):
                node = q.popleft()
                currsum += node.val

                if node.left != None: q.append(node.left)
                if node.right != None: q.append(node.right)
            if currsum > maxsum:
                maxsum = currsum
                res = level
            level += 1
        return res
    
root = TreeNode(1)
second = TreeNode(7)
third = TreeNode(0)
fourth = TreeNode(7)
fifth = TreeNode(-8)

root.left, root.right = second, third
second.left, second.right = fourth, fifth

solution = Solution()
print(solution.maxLevelSum(root=root))
            


