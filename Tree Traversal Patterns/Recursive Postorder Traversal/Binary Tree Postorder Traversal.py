## 145. Binary Tree Postorder Traversal

'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]
Explanation:

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,6,7,5,2,9,8,3,1]
Explanation:

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]
'''

class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def postOrderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        '''
        1. Recursive Postorder traversal
            - In order to perform a postorder traversal of a binary tree, we follow the path of going from the left -> right -> root. this means that we before we visit the root, we visit the left and right subtrees and so on. 
            - Time Complexity: O(n) where n is the number of nodes in the binary tree. our postorder traversal visit each node exactly once, adding it to our result list.
            - Space Complexity: O(h) where h is the height of the tree if the tree is balanced. O(n) if the binary tree is skewed like a linked list. 
        '''
        self.arr = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            self.arr.append(root.val)
        dfs(root)
        return self.arr

root = TreeNode(1)
second, third = TreeNode(2), TreeNode(3)
root.right = second
second.left = third

solution = Solution()
print(solution.postOrderTraversal())
