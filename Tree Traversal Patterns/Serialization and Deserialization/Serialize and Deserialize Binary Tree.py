## 297. Serialize and Deserialize Binary Tree

'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []
'''

class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def serialize(self, root):
        '''
        1. Serialize
            - we want to serialize our binary tree into a single string in a way to deserialize our binary tree with ease. in order to do so, we can use a list and perform a preorder traversal of our binary Tree. Since, each Node has an integer value, we convert that value into a string and append it to our list and continue to do so for our left and right subtrees. If we come across a Null Node, we append an "N".
            - Time Complexity: O(n) where n is the number of nodes in the binary tree. this is because our preorder traversal goes through each node exactly once, converting into a string and appending it to a list.
            - Space Complexity: O(n) where n is the number of nodes in the binary tree. this is because we are converting our tree into a single string and our string could be as big as the binary tree depending on how many nodes there are. 
        '''

        res = []

        def dfs(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)


    
    def deserialize(self, data):
        '''
        1. deserialize
            - we want to deserialize our binary tree using the string that is passed in from our function. since our string is going to be in an array format, we can track which current point we are at in the tree using a class variable of i. essentially we follow the preorder format of our list and use that to construct our binary tree. 
            - Time Complexity: O(n) where n is the number of nodes that were in the binary tree.
            - Space Complexity: O(n) because the size of the binary tree is dependent on the number of nodes 
        '''

        vals = data.split(",")

        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


