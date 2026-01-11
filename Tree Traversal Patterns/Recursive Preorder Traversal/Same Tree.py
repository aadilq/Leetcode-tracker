## 100. Same Tree

'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value
 

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        1. Preorder traversal
            - we can perform a preorder traversal of both tree simultaneously. in each recursive check, we check for multiple different criteria. If both nodes happen to be None, this means we can return True because we've eached the ends of the tree. However, if either of the nodes is None and the other has a value, we return false because the structure of the trees is different. we also return False if the values at the positions are different. we perform a preorder traversal of our tree meaning we are going to visit the root first then our left subtree and then the right subtree. 
            - Time Complexity: O(n) where n is the number of nodes in the the tree. this is because we simultaneously checking nodes of both trees. 
            - Space Complexity: O(h) where h is the height of the tree. O(n) for a skewed tree
        '''
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right))
    
p = TreeNode(1)
pleft = TreeNode(2)
pright = TreeNode(1)
p.left, p.right = pleft, pright

q = TreeNode(1)
qleft = TreeNode(1)
qright = TreeNode(2)
q.left, q.right = qleft, qright

solution = Solution()
print(solution.sameTree(p=p, q=q))

