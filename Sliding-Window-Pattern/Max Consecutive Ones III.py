## 1004. Max Consecutive Ones III

'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''

class Solution:
    def maxConsecOnes(self, nums: list[int], k: int) -> int:
        '''
        1. Variable Sliding window
            - we want to know the longest subarray that we can create after flipping k zeroes. what we can do is initialize a variable that count the current number of zeroes that we have seen so far. when the the number of zeroes exceeds k, we substract from our window until the number of zeroes is less than k. else, we keep on increasing the length of our longest subarray and updating our res variable. 
            - Time Complexity: O(n) where n is the length of the nums array. this is because we iterate all the way towards the end of the array
            - Space Complexity: O(1) because we are not using any additional data structures that will increase with the size of our input, only a variable to keep track of the amount of zeroes that we have seen so far.
        '''

        L = res = cntZeroes = 0

        for R in range(len(nums)):
            if nums[R] == 0:
                cntZeroes += 1
            
            while cntZeroes > k:
                if nums[L] == 0:
                    cntZeroes -= 1
                L += 1
            
            res = max(res, R - L + 1)
        return res

solution = Solution()
print(solution.maxConsecOnes([1,1,1,0,0,0,1,1,1,1,0], k = 2))