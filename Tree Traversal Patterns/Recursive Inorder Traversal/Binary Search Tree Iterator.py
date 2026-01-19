## 173. Binary Search Tree Iterator

'''
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

 

Example 1:
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
'''

class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

from typing import Optional
class BSTiterator:
    '''
    1. inorder traversal
    - we want to perform an inorder traversal of the tree while using O(h) memory which means that we want to only be focusing on the left side of the tree before going over to the right side of the tree. we can do this iteratively using a stack. given that our tree is a bst, we can use a stack to append our root node first and then the left subtree. we go as much left as possible to get the smallest value in the bst. every time the next function is called, we pop from the stack and we check if the right node of the tree exist, effectively going left ->  root ->  right and keeping the inorder traversal intact. for our last function, we just check if our stack is empty yet.
    - Time Complexity: O(n) because we are still going to be traversing each node iteratively and appending/popping it to our stack, which is O(1).
    - Space Complexity: O(h) where h is the height of the tree. we are using a stack to first explore our left subtree before going down the right subtree. 
    '''

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        curr = root

        while curr:
            self.stack.append(curr)
            curr = curr.left
    
    def next(self) -> int:
        node = self.stack.pop()
        curr = node.right
        while curr:
            self.stack.append(curr.right)
            curr = curr.left
        return node.val

    
    def hasNext(self) -> bool:
        return self.stack != []

root = TreeNode(7)
second, third = TreeNode(3), TreeNode(15)
fourth, fifth = TreeNode(9), TreeNode(20)

root.left, root.right = second, third
third.left, third.right = fourth, fifth

bSTIterator = BSTiterator(root=root)

bSTIterator.next();   
bSTIterator.next();   
bSTIterator.hasNext();
bSTIterator.next();  
bSTIterator.hasNext();
bSTIterator.next();   
bSTIterator.hasNext();
bSTIterator.next();   
bSTIterator.hasNext();
