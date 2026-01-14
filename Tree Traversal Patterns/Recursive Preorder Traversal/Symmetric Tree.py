## 101. Symmetric Tree

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
    def symmetricTree(self, root: Optional[TreeNode]) -> bool:
        '''
        1. Pre-order level traversal
        - we want to see if the left and right subtrees of our binary are mirrored, meaning that they are symmetric around the center of the tree. if our tree has more than our two levels, then the outer nodes should match with each other and the inner nodes should match with each other. Perform a preorder traversal where we check the outer nodes of our two subtrees and the inner nodes of the binary tree, these values should match each other. 
        - Time Complexity: O(n) since we are visiting every node in the binary tree exactly once.
        - Space Complexity: Average case, it should be O(h) where h is the height of the binary due to our recursive call stack. our recursive should only run up until our leaf nodes. O(n) if our binary tree is skewed like a linked list

        1 
       / \
      2     2
     / \   / \
     3  4  4  3
        '''

        def symmetric(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and symmetric(left.left, right.right) and symmetric(left.right, right.left))
        return symmetric(root.left, root.right)

root = TreeNode(1)
second = TreeNode(2)
third = TreeNode(2)
fourth = TreeNode(3)
fifth = TreeNode(4)
sixth = TreeNode(4)
seventh = TreeNode(3)
root.left, root.right = second, third
second.left, second.right = fourth, fifth
third.left, third.right = sixth, seventh

solution = Solution()
print(solution.symmetricTree(root=root))

