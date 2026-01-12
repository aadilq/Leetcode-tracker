## 101. Symmetric Tree

'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isSymmetricTree(self, root: Optional[TreeNode]) -> bool:
        '''
         1 
        / \
       2    2
      / \   / \ 
    3   4   4  3
        1. Preorder traversal
            - we want to see if our tree is symmetrical down the center, essentially mirroring itself. we know that the nodes at the second level of our tree should be equal but now we check their children. at this point, we want to check if the left.child of root.left is equal to right.child or root.right and if right.child of root root.left is equal to the left.child of root.right and so on. 
            - Time Complexity: O(n) where n is the number of the nodes in the binary tree and this is because we visit each nodes exactly once in our preorder traversal of the tree. 
            - Space Complexity: O(h) where h is the height of the tree because of the recursive call stack. The system stack stores the function calls that are currently active.. Average case If the tree is balanced, then its O(log n) and worst case if the tree is skewed(like a linked list), then O(n).
        '''
        def symmetric(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return (left.val == right.val and symmetric(left.left, right.right) and symmetric(left.right, right.left))
        return symmetric(root.left, root.right)
    
root = TreeNode(1)
second, third = TreeNode(2), TreeNode(2)
fourth, fifth, sixth, seventh = TreeNode(3), TreeNode(4), TreeNode(4), TreeNode(3)

root.left, root.right = second, third
second.left, second.right = fourth, fifth
third.left, third.right = sixth, seventh

solution = Solution()
print(solution.isSymmetricTree(root=root))
        

