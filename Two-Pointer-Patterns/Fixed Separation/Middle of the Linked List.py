## 876. Middle of the Linked List

'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''
from typing import Optional
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[Node]) -> Optional[Node]:
        '''
        1. Two Pointer - Fixed Separation
             - We initialize two pointers, one fast ptr and slow ptr. we move our slow ptr by one and fast ptr by two. when the fast ptr reaches the end of the linked list, our slow ptr will be at the middle node. 
             - Time Complexity: O(n) where n is the length since our fast ptr will be traversing through the length of the linked list.
             - Space Complexity: O(1) since we are only using a few ptr variables that don't increase in size depending on the size of our linked list
        '''
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val

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
print(solution.middleNode(head=head))



