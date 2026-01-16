## 104. Maximum Depth of Binary Tree

'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
'''

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        1. Recursive postorder traversal
            - we can do a recursive postorder traversal of our binary tree which for every root, we visit its left subtree and then right subtree before going back to the root. for every root which includes our leaf nodes, we calculate the depth of current subtree by adding 1 to the max of our left and right subtree. when we get to the main root of our binary tree, we simple add 1 to the max of the left subtree and right subtree to get the total maximum depth of the binary tree. 
            - Time Complexity: O(n) where n is the number of nodes in the binary tree. this is because our recursive postorder traversal visits each nodes to calculate the current maximum depth. 
            - Space Complexity: O(h) where h is the height of the tree due to the recursive call stack. this is because we have to completely finish the main recursive call stack of left subtree before calling the recursive call stack for the right subtree. 
        '''
        
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            return 1 + max(left, right)
        return dfs(root)

root = TreeNode(3)
second, third = TreeNode(9), TreeNode(20)
fourth, fifth = TreeNode(15), TreeNode(7)

root.left, root.right = second, third
third.left, third.right = fourth, fifth

solution = Solution()
print(solution.maxDepth(root=root))