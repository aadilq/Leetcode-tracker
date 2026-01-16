## 501. Find Mode in Binary Search Tree

'''
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
Input: root = [1,null,2,2]
Output: [2]

Example 2:
Input: root = [0]
Output: [0]
'''

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

from typing import Optional
class Solution:
    def findModeInBst(self, root: Optional[TreeNode]) -> list[int]:
        '''
        1. iterative inorder traversal - stack & hashmap
        - we perform an iterative inorder traversal of the bst using a stack and for each element, we count its frequency using a hashmap. after we are done iterating through the whole bst and getting the frequency for each node, we see what the highest frequency is in our hashmap. we loop through our hashmap and see which nodes frequency matches the highest frequency. 
        - Time Complexity: O(n) where n is the number of nodes in the bst. this is because we add each node to our stack and to our hashmap as well. we also iterate through our hashmap, getting the nodes whose frequency match the highest frequency. 
        - Space Complexity: O(n) because we are using a hashmap to accumulate the frequency of all of the nodes in our hashmap and our hashmap can be as big as the bst. 
        '''

        stack = []
        count = {}
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            if node.val in count:
                count[node.val] += 1
            else:
                count[node.val] = 1
            if node.right:
                curr = node.right
        
        max_frequency = max(count.values())

        res = [x for x, y in count.items() if y == max_frequency]
        return res

root = TreeNode(12)
second, third = TreeNode(10), TreeNode(20)
fourth, fifth = TreeNode(9), TreeNode(11)
sixth = TreeNode(12)
seventh, eighth = TreeNode(10), TreeNode(12)

root.left, root.right = second, third
second.left, second.right = fourth, fifth
third.left = sixth
fifth.keft = seventh
sixth.right = eighth

solution = Solution()
print(solution.findModeInBst(root=root))
