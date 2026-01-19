## 98. Validate Binary Search Tree

'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def validateBST(self, root: Optional[TreeNode]) -> bool:
        '''
        1. inorder traversal
        - perform an inorder traversal of the BST and append the value of each node to an output list. after we finish traversing the tree, we go through each value in our output list and checking if the values are sorted in increasing order. 
        - Time Complexity: O(n) where n is the number of nodes in the binary search tree.
        - Space Complexity: O(n) because our output list will store all of the nodes values. 
        '''
        self.arr = []

        def inorderTraversal(root):
            if not root:
                return
            inorderTraversal(root.left)
            self.arr.append(root.val)
            inorderTraversal(root.right)
        
        def isValid(arr):
            for i in range(len(arr)):
                if arr[i] >= arr[i + 1]:
                    return False
            return True
        return isValid(self.arr)

root = TreeNode(1)
second, third = TreeNode(2), TreeNode(3)


solution = Solution()
print(solution.validateBST(root=root))
        

