## 226. Invert Binary Tree

'''
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        1. preorder traversal
        - we're going to follow a preorder traversal where we swap the left and right subtrees from our main root and then we recursively call our function on our left subtree to swap all of the inner subtree within our main left subtree and then on our right subtree. 
        - Time Complexity: O(n) where n is the number of nodes in our binary tree. we visit each node recursively to swap its left and right subtrees.
        - Space Complexity: Average case is O(h) where h is the height of our binary tree due to the recursive call stack. if the tree is balanced, our recursive call stack is going to be as big as the height of the tree. 
        '''
        if not root:
            return None
        tmp = root.right
        root.right = root.left
        root.left = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

