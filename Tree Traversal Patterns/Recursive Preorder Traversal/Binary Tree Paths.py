## 257. Binary Tree Paths

'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]
'''
class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def treePaths(self, root: Optional[TreeNode]) -> list[str]:
        '''
        1. preorder traversal
        - to get all of the tree paths from root to the leaf nodes, we can use a preorder traversal where we can append the values to a string joined by "->". for each node, we can first check if it is a null node because if it is a null node, we just return to our previous function call. if the node is not null, we're going to convert it into a string and store it within an shared state array called curr that is going to keep track of our current path. if we come across a node that does not have a left or right child, we append the current values in curr to a result array in which the values are joined by "->". we do recursively for the left subtree and right subtree. we pop the current after exhausting all the possibilities of it. 
        - Time Complexity: O(n) where n is the total number of nodes in the binary tree. this is because we visit each node at most once to add it our current path. 
        - Space Complexity: Average case O(h) where h is the height of the tree. O(n) in the worst case that our tree is skewed like a linked list.
        '''
        curr, res = [], []

        def dfs(root):
            if not root:
                return
            curr.append(str(root.val))
            if not root.left and not root.right:
                res.append("->".join(curr))
            dfs(root.left)
            dfs(root.right)
            curr.pop()
        dfs(root)
        return res

root = TreeNode(1)
second, third = TreeNode(2), TreeNode(3)
fourth = TreeNode(5)

root.left, root.right = second, third
second.right = fourth
solution = Solution()
print(solution.treePaths(root=root))
        
        