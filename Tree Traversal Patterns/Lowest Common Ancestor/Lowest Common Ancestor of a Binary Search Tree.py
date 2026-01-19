## 235. Lowest Common Ancestor of a Binary Search Tree

'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
'''

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        1. Lowest Common Ancestor + Iterative traversal
            - we are trying to find the lowest common ancestor of both p and q in the binary tree where the ancestor has both p and q as descendants. p and q could also be descendants of themselves. we know that we are dealing with a bst which means that all of the values in the left subtree are less than the root node and all of the values in our right subtree are greater than the root. if both the values of p and q are greater than root's value, then we know that we can search the right subtree since the values will not exist in the left subtree. 
            - if p and q occur in separate trees, we return the current root
            - if p or q are one of the descendants, then we return p or q.

            - Time Complexity: O(h), where h is the height of the tree (O(log n) for balanced, O(n) for unbalanced).
            - Space Complexity: O(1) The algorithm uses a constant amount of extra space, as it only maintains a few pointers (curr).
        '''

        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr.val

root = TreeNode(6)
second, third = TreeNode(2), TreeNode(8)
fourth, fifth = TreeNode(0), TreeNode(4)
sixth, seventh = TreeNode(3), TreeNode(5)
eigth, ninth = TreeNode(8), TreeNode(7)
tenth = TreeNode(9)
p, q = TreeNode(2), TreeNode(8)

root.left, root.right = second, third
second.left, second.right = fourth, fifth
fifth.left, fifth.right = sixth, seventh
eigth.left, eigth.right = ninth, tenth

solution = Solution()
print(solution.lowestCommonAncestor(root=root, p=p, q=q))
