## 2095. Delete the Middle Node of a Linked List

'''
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

Example 1:

Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Example 2:

Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:

Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
'''
from typing import Optional
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddleNode(self, head: Optional[Node]) -> Optional[Node]:
        '''
        1. Two Pointer + fixed separation
            - We use three ptrs to keep track of the middle node of the linked list and previous node before the middle node so that we can efficiently delete it. We use our slow and fast ptrs to find where the middle of the linked list exist and prev pointer which lags behind our slow ptr so that once we find the middle of the linked list, we can use this prev pointer to get rid of the middle node.
            - Time Complexity: O(n) where n is the length of the linked list because our fast ptr will traverse through the end of the linked list
            - Space Complexity: O(1) since we are not using any additional data structures that would increase as the size of our linked list would increase, only a few ptrs. 
        '''
        if head.next is None:
            return None
        
        slow = fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = prev.next.next
        return head

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
print(solution.deleteMiddleNode(head=head))