## 287. Find the Duplicate Number

'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def flattenTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        1. preorder traversal
        - we want to "convert" our binary tree to a linked list by making it so that our right ptr points to the next node. this entails taking the left side of our linked list and transferring it over to the right side of the linked list. we're going to perform a preorder traversal of our binary tree where we go to our left subtree if this is the last left value exist. essentially we assign the right ptr of last left node to the right node of that subtree. we connect our root to our right subtree by assigning the left ptr to the right ptr. lastly, we say that our root.left ptr is Null. 
        - Time Complexity: O(n) where n is the number of nodes in our binary tree. we visit each node in our tree exactly once, seeing if it needs to be transferred over to our right subtree. 
        - Space Complexity: O(h) where h is the height of the tree. at most our recursive call stack will go as long as the height of the tree, since we first focusing on the left subtree of our main root, then the right subtree. 
        1
       / \
      2     5
     / \     \ 
    3   4     6
        '''

        def dfs(root):
            if not root:
                return None
            
            lefttail = dfs(root.left)
            righttail = dfs(root.right)

            if lefttail != None:
                lefttail.right = root.right
                root.right = root.left
                root.left = None
            last = righttail or lefttail or root
            return last

root = TreeNode(1)
second, third = TreeNode(2), TreeNode(5)
fourth, fifth = TreeNode(3), TreeNode(4)
sixth = TreeNode(6)

root.left, root.right = second, third
second.left, second.right = fourth, fifth
third.right = sixth
solution = Solution()
print(solution.flattenTree(root=root))