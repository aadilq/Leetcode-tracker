## 19. Remove Nth Node From End of List

'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:


Example 2:
Input: head = [1], n = 1
Output: []
Example 3:

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''
from typing import Optional
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def removeNthNodeFromEnd(self, head: Optional[Node], n: int) -> Optional[Node]:
        '''
        1. Fixed Separation
            - we use two pointers that are separated by n. when fast reaches null, our slow pointer will be pointing towards the node that we want to remove. We use a DummyNode to bypass the testcases in which we only have one or two nodes. 
               - Time Complexity: 
               - Space Complexity: 
        '''

        dummyNode = Node(0)
        dummyNode.next = head

        slow, fast = dummyNode, head
        
        for _ in range(n):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummyNode.next
'''
head = [1,2,3,4,5], n = 2
'''

head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

solution = Solution()
print(solution.removeNthNodeFromEnd(head=head,n=2))

