## 230. Kth Smallest Element in a BST

'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

from typing import Optional
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        1. Iterative inorder traversal
            - we want the kth smallest element in the binary so we can use to perform an iterative inorder traversal of our bst. we iterate using a stack to the farthest left element of the bst because that will be our smallest element. we keep going left until we have no more nodes. we essentially want to start from the most left subtree in our main left subtree because those will be our smallest elements. starting from that subtree, we perform an inorder traversal of every subtree, getting our value in order. we pop from our stack and decrement k by 1. when k is zero, we return the value of our popped node
            - Time Complexity: O(n) in the worst case that k is equal to the length of the bst, we would have iterate through all of the elements. 
            - Space Complexity: O(h) considering that the size of our stack is going to be roughly the height of the bst.
        '''

        stack = []

        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            if node.right:
                curr = node.right

root = TreeNode(3)
second, third = TreeNode(1), TreeNode(4)
fourth = TreeNode(2)

root.left, root.right = second, third
second.right = fourth

solution = Solution()
print(solution.kthSmallest(root=root,k=1))