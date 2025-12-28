## 141. Linked List Cycle

'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
'''
from typing import Optional
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[Node]) -> bool:
        '''
        1. Fast & Slow pointer approach
            - set up two pointers, slow and fast, where the slow pointer moves by one each time and the fast pointer moves by two each time. if there is a cycle, the fast pointer will overlap and intersect where the slow pointer is. If there is not a cycle, our fast pointer will run to end of the linked list, return False
            
            - Time Complexity: O(n), where n is the number of nodes in the linked list. This is because in the worst case, the slow and fast pointers traverse the list once until they meet or reach the end. 
            - Space Complexity: O(1) because the algorithm uses only a fixed amount of extra space, specifically for the two pointers (slow and fast)
        '''

        if not head:
            return None
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False
    
# Input: head = [3,2,0,-4], pos = 1
    
Head = Node(3)
second = Node(2)
third = Node(0)
fourth = Node(-4)

Head.next = second
second.next = third
third.next = fourth
fourth.next = second

solution = Solution()
print(solution.hasCycle(head=Head))





