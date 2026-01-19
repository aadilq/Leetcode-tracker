## 366. Find Leaves of Binary Tree

'''
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.

Example 1:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.

Example 2:
Input: root = [1]
Output: [[1]]
'''

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

from typing import Optional
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> list[int]:
        '''
        1. Recursive Postorder traversal
            - we initialize an empty list where each index of the list corresponds to that specific height on the binary tree. for example, index 0 represents height 1, which are all of the root leaves. we perform a recursive postorder traversal of our tree and append the nodes according to their specific height while adjusting our current height.
            - Time Complexity: O(n) where n is the number of nodes in the binary tree. this is because we visit each node and place in its corresponding place on the list. 
            - Space Complexity: O(h) where h is the height of the tree if the tree is balanced. Else O(n).
        '''

        self.list = []

        def dfs(root):
            if not root:
                return -1
            
            currentHeight = 0

            left = dfs(root.left)
            right = dfs(root.right)

            currentHeight = 1 + max(left, right)

            if currentHeight == len(self.list):
                self.list.append([])

            self.list[currentHeight].append(root.val)
            return currentHeight
        dfs(root)
        return self.list

root = TreeNode(1)
second, third = TreeNode(2), TreeNode(3)
fourth, fifth = TreeNode(4), TreeNode(5)

root.left, root.right = second, third
second.left, second.right = fourth, fifth


solution = Solution()
print(solution.findLeaves(root=root))        