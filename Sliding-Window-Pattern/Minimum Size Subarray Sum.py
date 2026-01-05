##  209. Minimum Size Subarray Sum

'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''
class Solution:
    def minSubArrayLen(self, nums: list[int], target: int) -> int:
        '''
        1. Variable Sliding window
            - we're going to use a variable sliding window where we add the current number at pointer R to our variable total, which we initialize in the beginning, when our total goes over or equal to the target, we see if our length is less than the minimum length we have seen so far, then we subtract the number from our total and shift our left ptr. 
            - Time Complexity: O(n) where n is the length of nums, this is because our right pointer goes up until the last element of nums. 
            - Space Complexity: O(1) because we aren't using any additional data structures that would grow alongside the size of our input, only a few variables.
        '''

        L = total = 0
        reslen = float('inf')

        for R in range(len(nums)):
            total += nums[R]

            while total >= target:
                reslen = min(reslen, (R - L + 1))
                total -= nums[L]
                L += 1
        return reslen

solution = Solution()
print(solution.minSubArrayLen([2,3,1,2,4,3], target=7))