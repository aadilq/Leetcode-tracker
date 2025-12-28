## 287. Find the Duplicate Number

'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
'''

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        '''
        1. fast & slow pointer approach 
            - Treating the array as a linked list where nums[i] points to the index nums[i] and since there is a duplicate value, multiple indices will be pointing to the same value. This creates a cycle in our linked list. 
            1. Phase 1: Detecting if a cycle exists
            2. Phase 2: Finding the cycle entrance (entrance is where the duplicate number exists)
            - Time Complexity: O(n) where n is the length of the array as each element is visited at most 2-3 times
            - Space Complexity: O(1) since we are only using a few pointers that don't rely on the size of the array
                0 1 2 3 4 
        nums = [1,3,4,2,2]

       0 -> 1 -> 3 -> 2 -> 4
                      | 
                 ^ - - 

        '''
        slow = fast = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow            
        