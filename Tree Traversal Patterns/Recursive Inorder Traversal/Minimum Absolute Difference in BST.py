## 530. Minimum Absolute Difference in BST

'''
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
'''

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

from typing import Optional
class Solution:
    def minAbsDiffBst(self, root: Optional[TreeNode]) -> int:
        '''
        1. recursive inorder traversal
            - we perform a recursive inorder traversal and append our nodes values to an list so that they are in sorted order. we go through each of the list items using a loop, comparing the absolute difference and if the absolute difference is 1, we break from our loop because 1 is the most minimum difference that exists. 
            - Time Complexity: O(n) where n is the number of nodes in the bst. this is because our recursive in order traversal goes through all of the nodes and adds them to a list. we also iterate through all of the nodes values using a for loop which could also be in the worst case O(n). 
            - Space Complexity: O(n) since we are using a list to acccumulate all of the nodes so our list will be as big as our bst. 
        '''

        arr = []

        def dfs(root):
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        print(arr)
        min_difference = float('inf')

        for i in range(1, len(arr)):
            curr_difference = abs(arr[i] - arr[i - 1])
            if curr_difference == 1:
                return 1
                break
            min_difference = min(min_difference, curr_difference)
        return min_difference


root = TreeNode(1)
second, third = TreeNode(0), TreeNode(48)
fourth, fifth = TreeNode(12), TreeNode(49)

root.left, root.right = second, third
third.left, third.right = fourth, fifth
solution = Solution()
print(solution.minAbsDiffBst(root=root))

