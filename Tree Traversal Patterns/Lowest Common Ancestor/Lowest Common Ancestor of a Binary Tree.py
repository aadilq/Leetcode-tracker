## 236. Lowest Common Ancestor of a Binary Tree

'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
'''

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        1. Lowest Common Ancestor + recursive dfs
            - we perform a dfs search through our tree, checking for different cases such as:
                - if there is no root, return None
                - if root's value equals p's value or q's value, return the root's value
            we go both our left and right subtrees. if both left and right are nonnull, it means that p and q exist in two different trees so we return the current root. if either left or right are nonnull, it means that p or q exist at one of those nodes and thats what we return
            -
        '''
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root.val
        return left or right

'''[3,5,1,6,2,0,8,null,null,7,4]'''
root = TreeNode(3)
second, third = TreeNode(5), TreeNode(1)
fourth, fifth = TreeNode(6), TreeNode(2)
sixth, seventh = TreeNode(0), TreeNode(8)
eigth, ninth = TreeNode(7), TreeNode(4)

root.right, root.left = second, third
second.left, second.right = fourth, fifth
third.left, third.right = sixth, seventh
fifth.left, fifth.right = eigth, ninth

solution = Solution()
print(solution.lowestCommonAncestor(root=root, p=TreeNode(5), q=TreeNode(1)))