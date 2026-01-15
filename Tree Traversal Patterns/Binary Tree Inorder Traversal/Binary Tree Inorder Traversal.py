## 94. Binary Tree Inorder Traversal

'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]
'''

class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

from typing import Optional
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        '''
        1. Inorder traversal
        - we are going to perform an inorder traversal of the binary tree which means that for every subtree, we visit the left subtree, root, and then the right subtree. in that order, we will output our values to the a list which we will return after visiting the last node
        - Time Complexity: O(n) where n is the number of nodes in the binary tree. this is because we visit each node exactly once. 
        - Space Complexity: O(h) where h is the height of the tree. this is because we focus on our main left subtree and then our main right subtree and so our recursive call stack does not go above the height of the subtree.
        '''
        self.arr = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.arr.append(root.val)
            dfs(root.right)
        dfs(root)
        return self.arr
root = TreeNode(1)
second, third = TreeNode(2), TreeNode(3)

root.right = second
second.left = third

solution = Solution()
print(solution.inorderTraversal(root=root))
