## 905. Sort Array By Parity

'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
'''

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list:
        '''
        1. Two Pointer + Array Modification
            - we can use a two ptr approach where our right ptr scans through the array and whenever we come across an even number with our right ptr, we place it at our left ptr which is at the beginning of our array and shift our left ptr by one. 
            - Time Complexity: O(n) where n is the length of our input array. This is because our outer loop will run approximately n times
            - Space Complexity: O(1) since we are using a few ptrs to modify our input array in place
        '''

        L = R = 0
        while R < len(nums):
            if nums[R] % 2 == 0:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
            R += 1
        return nums
solution = Solution()
print(solution.sortArrayByParity([3,1,2,4]))

        