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
            - We want to find the shortest subarray with sum ≥ K. If we use prefix sums, then the sum of any subarray from index i to j is prefix[j] - prefix[i-1]. So we're looking for the smallest j - i where prefix[j] - prefix[i] >= K.
            The deque helps us maintain potential starting points for our subarray in a smart way. Here's the key insight:
            As we iterate through the array and build prefix sums, we maintain a deque that stores indices in a specific order. The deque serves two purposes:

            Finding valid subarrays: For each position j, we check if prefix[j] - prefix[deque.front()] >= K. If yes, we found a valid subarray and can update our answer.
            Removing useless candidates: We remove indices from the deque that will never be useful:

            From the front: Once we use an index to form a valid subarray, we remove it (since we want the shortest subarray, we won't need it again)
            From the back: If the current prefix sum is ≤ a previous one, that previous index is useless (why start from an earlier position with a larger prefix sum?)

            We remove an index from the back of the deque when the current prefix sum is less than or equal to a previous prefix sum. Here's why that previous index becomes useless:
            Key Insight: If prefix[i] <= prefix[j] where i < j, then index j is strictly better than index i as a potential starting point.
            Why? Because:

            Starting from j gives you a subarray that begins later (so it's shorter)
            Starting from j gives you a smaller or equal prefix to subtract (so the resulting sum is larger or equal) 

            By maintaining increasing prefix sums in the deque, we ensure that earlier indices have smaller prefix sums, making them more likely to produce larger subarray sums when subtracted from future positions.
                  
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

        


