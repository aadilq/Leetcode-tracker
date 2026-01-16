## 110. Balanced Binary Tree

'''
Given a binary tree, determine if it is height-balanced.

 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
'''

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def balancedTree(self, root: Optional[TreeNode]) -> bool:
        '''
        1. Recurive Postorder Traversal
            - we implement a recursive postorder traversal in which we first visit our left subtree and then our right subtree before visiting the root. when visiting the root, we determine that the tree upto this point is balanced as well get the current height of the tree so that we can check our other subtrees. If any our subtrees are not balanced, we return False otherwise we return True. 
            - Time Complexity: O(n) where n is the number of nodes in the binary tree. this is because our recursive postorder traversal goes through every single node in the tree
            - Space Complexity: O(h) where h is the height of the binary tree if the binary is balanced, otherwise O(n) if the binary tree is skewed like a linked list. 
        '''

        def dfs(root):
            if not root:
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1+max(left[1], right[1])]
        return dfs(root)[0]

root = TreeNode(3)
second, third = TreeNode(9), TreeNode(20)
fourth, fifth = TreeNode(15), TreeNode(7)

solution = Solution()
print(solution.balancedTree(root=root))
        