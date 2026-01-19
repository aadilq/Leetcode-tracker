## 543. Diameter of Binary Tree

'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
'''

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

from typing import Optional
class Solution:
    def diameterOfTree(self, root: Optional[TreeNode]) -> int:
        '''
        1. Recursive Postorder Traversal
            - we perform a standard recursive postorder traversal of our binary tree while keeping track of the max diameter (which we can keep track using a class variable). for each node, we compute diameter by adding the left and the right together and seeing if this beats our current max diameter. for each recursive call, we return the current height of the tree. 
            - Time Complexity: O(n) where n is the number of nodes in the binary tree. this is because we visit each node exactly once, computing the current diameter of the tree and returning the current tree's height. 
            - Space Complexity: O(h) where h is the height of the binary tree if the tree is balanced. 
        '''

        self.diameter = 0

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.diameter
    
root = TreeNode(1)
second, third = TreeNode(2), TreeNode(3)
fourth, fifth = TreeNode(4), TreeNode(5)

root.left, root.right = second, third
second.left, second.right = fourth, fifth

solution = Solution()
print(solution.diameterOfTree(root=root))