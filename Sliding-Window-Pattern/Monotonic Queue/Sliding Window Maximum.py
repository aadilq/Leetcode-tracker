## 239. Sliding Window Maximum
'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]
'''
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k:int) -> list[int]:
        '''
        1. Monotonic queue for max
            - in order to achieve a linear solution, we can rely on the use a queue where the front of the queue holds the maximum element that we have seen so far. we go through each number in nums, if the number is bigger than the last number in our queue, we pop from our queue and append the number. This way we make sure that front of the queue holds the maximum number in the current sliding window of k. If the first number in our queue is is out of bounds from the current sliding window, we pop it from the front of our queue. 
            
            - Time Complexity: O(n) where n is length of nums, this is because we are iterating until the very last number in nums. 
            - Space Complexity: O(n) because we are using deque to hold the maximum numbers that we have witnessed so far. worst case scenario is that we have decreasing numbers which means that our queue will hold ever single number.
        '''
        res = []

        q = deque()

        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)

            if q[0] == i - k:
                q.popleft()
            
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
solution = Solution()
print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], k = 3))
            
