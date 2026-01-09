## 643. Maximum Average Subarray I

'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
'''

class Solution:
    def maximumAverageSubarray(self, nums: list[int], k: int) -> float:
        '''
        1. Fixed Sliding window Approach
            - we keep a fixed sliding window of size k using left and right pointers. we keep track of two variables total and max_avg which will hold the maximum average that we have seen so far and this is what we will return at the end. 
            - Time Complexity: O(n) where n is the size of the sliding window because our right pointer is going to go through the entire list which is of size n.
            - Space Complexity: O(1) since we are only using a few pointers to keep track of our positions in the nums array and some variables to keep track of the information that we have seen so far. 
        '''
        total, max_avg = 0, float('-inf')

        L = 0 

        for R in range(len(nums)):
            total += nums[R]
            while (R - L + 1) == k:
                max_avg = max(max_avg, (total / k))
                total -= nums[L]
                L += 1
        return max_avg
solution = Solution()
print(solution.maximumAverageSubarray([1,12,-5,-6,50,3], k = 4))
print(solution.maximumAverageSubarray([-1], k = 1))

