## 124. Binary Tree Maximum Path Sum

'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
'''

class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        1. Recursive Preorder Traversal
            - we can use a recursive preorder traversal where we first the left subtree and right subtree for every root of main subtree. for every root, we calculate the current maximum path sum if we do split at this root and we keep it in a class variable which we can call self.maxpathsum. however, we want to return the max path if we don't split which means taking the max from our left or right subtrees and adding it to our current root's value. 
            - Time Complexity: O(n) where n is the number of nodes in the binary tree. this is because we recursively visit each node at most once. 
            - Space Complexity: O(h) where h is the height of binary tree is the tree is balanced. else O(n) if the tree is skewed like a linked list.
        '''

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(left, 0)
            right = max(right, 0)

            maxPathSumWithSplit = root.val + left + right
            self.maxPath = max(self.maxPath, maxPathSumWithSplit)
            return root.val + max(left, right)
        self.maxPath = float('-inf')
        dfs(root)
        return self.maxPath

root = TreeNode(-10)
second, third = TreeNode(9), TreeNode(20)
fourth, fifth = TreeNode(15), TreeNode(7)

root.left, root.right = second, third
third.left, third.right = fourth, fifth
solution = Solution()
print(solution.maxPathSum(root=root))
        

