## 105. Construct Binary Tree from Preorder and Inorder Traversal

'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        '''
        ## Insight #1
        - the first element of the preorder array is always the root of the Tree. 

        ## Insight #2 
        - findind the index of the root in the inorder allows us to know what goes in our left subtree and what goes in our right subtree. everything to the left of the root in inorder is apart of the left subtree and everything to the right is apart of the right subtree. 

        1. preorder traversal
        - using the first insight that the first element of the preorder array is the root of our tree, we're going to pop it from the preorder array and store it within a variable called rootVal. then, we create the root Node of our tree using the TreeNode class. we find the index of where the rootVal occurs in the inorder array because everything to the left of rootVal in the inorder array belongs in the left subarray and everything to the right belong in the right subarray.
        we recurisvely build our left subtree first and then our right subtree, following the preorder traversal guide. 
        - Time Complexity: O(n^2) where n is the number of nodes in the tree and this is because for each node, we search for its index in the inorder array, which could be at most n search. 
        - Space Complexity: O(n) where h is the height of the tree. 
        '''
        if not preorder or not inorder:
            return None
        rootval = preorder.pop(0)

        root = TreeNode(rootval)
        mididx = inorder.index(rootval)

        root.left = self.buildTree(preorder=preorder, inorder=inorder[:mididx])
        root.right = self.buildTree(preorder=preorder, inorder=inorder[mididx + 1:])
        return root

solution = Solution()
print(solution.buildTree(preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]))