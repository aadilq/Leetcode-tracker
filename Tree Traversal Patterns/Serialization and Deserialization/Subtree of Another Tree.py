## 572. Subtree of Another Tree

'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

'''

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def isSubtree(self, root: 'TreeNode', subRoot: 'TreeNode') -> bool:
        '''
        1. Serialization
            - to know if a subtree of root matches the tree of subRoot, we can serialize both trees into strings and check if the serialization string of subroot exists within the serialization string of root. 
            - Time Complexity: O(n + m) where n is the number of nodes in the root tree and m is the number of nodes in the subroot tree. this is because we are iterating through both trees and serializing them into strings. 
            - Space Complexity: O(n + m) where n is the number of nodes in the root tree and m is the number of nodes in the subroot tree. the size of serializations string is dependent on how many nodes exist in our binary trees. 
        '''

        preorder_root, preorder_subroot = [], []

        def dfs(root, res):
            if not root:
                res.append("N")
            res.append('(' + str(root.val) + ')')
            dfs(root.left, res)
            dfs(root.right, res)
        
        preorder_root = dfs(root=root, res=preorder_root)
        preorder_subroot = dfs(root=subRoot, res=preorder_subroot)

        preorder_root = ",".join(preorder_root)
        preorder_subroot = ",".join(preorder_subroot)

        return preorder_subroot in preorder_root
