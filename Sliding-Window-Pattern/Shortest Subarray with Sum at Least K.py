## 862. Shortest Subarray with Sum at Least K

'''
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
'''
from collections import deque
class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        '''
        1. Monotonic increasing queue
            - in order to return a non-empty subarray with sum of atleast k, we need to calculate the prefix sum for each element because the prefix sum is going help us track the current sum upto that specific index. we use a deque where the front of the deque represent the smallest valid current sum. we iterate through each sum in prefixsum array and compare with the smallest valid current sum at the front of queue, if this equal to or bigger than k, we update the length accordingly. 
            - Time Complexity: O(n) because we are iterating through each nums in nums and calculating the prefix sum. we then iterate through our prefix sum array to find the length of shortest subarray that is equal to or greater than k. 
            - Space Complexity: O(n) because we are using a prefix sum array that is approximately equal to the length of nums. we're also using a deque where in the worst case scenario where each prefix sum is increasing, the length of our deque could be of size n. 
        '''
        prefixSum = [0] * (len(nums) + 1)
        for i in range(len(nums) + 1):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        
        res = float('inf')
        q = deque()

        for i in range(len(nums) + 1):
            while q and prefixSum[i] - prefixSum[q[0]] >= k:
                res = min(res, i - q.popleft())
            
            while q and prefixSum[i] <= prefixSum[q[-1]]:
                q.pop()
            q.append(i)
        return res

        


