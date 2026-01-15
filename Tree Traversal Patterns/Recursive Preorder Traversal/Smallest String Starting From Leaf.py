## 988. Smallest String Starting From Leaf

'''
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

 

Example 1:
Input: root = [0,1,2,3,4,3,4]
Output: "dba"

Example 2:
Input: root = [25,1,3,1,3,0,2]
Output: "adz"

Example 3:
Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"
'''

class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def smallestString(self, root: Optional[TreeNode]) -> str:
        '''
        1. preorder traversal
        - we perform a preorder traversal going down the main left and right subtrees of our main root. we return the min lexigraphical of either the left subtree and right subtree and return the string. we go down the left subtree first, performing the same recursive function, return our smallest lexigraphical string until we get to our leaf nodes. 
        - Time Complexity: O(n) where n is the number of nodes in the binary tree. 
        - Space Complexity: O(h) if the tree is balanced else O(n) if it is skewed like a linked list
        '''
        def dfs(root, curr):
            if not root:
                return
            
            curr = chr(ord('a') + root.val) + curr
            if root.left and root.right:
                return min(dfs(root.left, curr), dfs(root.right, curr))
            if root.left:
                return dfs(root.left, curr)
            if root.right:
                return dfs(root.right, curr)
            return curr
        return dfs(root, "")

root = TreeNode(0)
second, third = TreeNode(1), TreeNode(2)
fourth, fifth = TreeNode(3), TreeNode(4)
sixth, seventh = TreeNode(3), TreeNode(4)

root.left, root.right = second, third
second.left, second.right = fourth, fifth
third.left, third.right = sixth, seventh

solution = Solution()
print(solution.smallestString(root=root))
    
