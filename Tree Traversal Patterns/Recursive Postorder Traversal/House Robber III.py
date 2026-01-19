## 337. House Robber III

'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def houseRobberThree(self, root: Optional[TreeNode]) -> int:
        '''
        1. Recursive postorder traversal
            - we perform a recursive postorder traversal where for each node, we calculate the amount of money we can steal including this house and other eligible houses (houses not directly linked to this house) and not including this house. since we are doing a recursive postorder traversal, we will return the max of both our left and right subtrees before going to the root.
            - Time Complexity: O(n) where n is the number of node in the binary tree. we visit each node exactly once getting the current maximum with that node included and not including that node
            - Space Complexity: O(h) where h is the height of the binary tree if the binary tree is balanced. 
        '''

        def dfs(root):
            if not root:
                return [0, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            withRoot = root.val + left[1] + right[1]
            withOutRoot = max(left) + max(right)

            return [withRoot, withOutRoot]
        return max(dfs(root))

root = TreeNode(3)
second, third = TreeNode(4), TreeNode(5)
fourth, fifth = TreeNode(1), TreeNode(3)
sixth = TreeNode(1)

root.left, root.right = second, third
second.left, second.right = fourth, fifth
third.right = sixth



solution = Solution()
print(solution.houseRobberThree(root=root))
