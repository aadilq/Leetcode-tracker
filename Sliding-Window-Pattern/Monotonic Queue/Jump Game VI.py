## 1696. Jump Game VI

'''
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

 

Example 1:
Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.

Example 2:
Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.

Example 3:
Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0
'''
from collections import deque
class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        '''
        1. Montonic Queue + DP solution
            - we can use a monotonic queue to keep track of our maximum jump so far in front of the queue. Essentially, we loop through nums and for each number, we check if it is beyond our window of size k so far. if it is, we pop it left from our queue. now we take the number of the first index in our queue and add with the current number in nums. if this number is bigger than the number of the last index of our queue, we pop from our queue and insert the current index. 
            - Time Complexity: O(n) since we are iterating through list of nums. Adding/popping from the queue is O(1) operation. 
            - Space Complexity: O(n) since we are using a deque to keep track of the indices that we have encountered so far. 
        '''

        dq = deque()

        for i in range(len(nums)):
            while dq and i - dq[0] > k:
                dq.popleft()
            
            if dq:
                nums[i] += nums[dq[0]]
            
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
        return nums[-1]
        

