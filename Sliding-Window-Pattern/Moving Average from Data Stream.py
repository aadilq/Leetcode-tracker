## 346. Moving Average from Data Stream
'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
Implement the MovingAverage class:

- MovingAverage(int size) Initializes the object with the size of the window size.
- double next(int val) Returns the moving average of the last size values of the stream.

Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.01

Explanation

Moving Average movingAverage new Moving Average(3);
movingAverage.next(1); // return 1.0 1/1
movingAverage.next(10); // return 5.5 (1+10)/2
movingAverage.next(3); // return 4.66667 = (1+10+3)/3
movingAverage.next(5); // return 6.0 (10+3+5)/3
'''
    
from collections import deque
class Solution:
    '''
    1. Fixed Sliding Window
        - since we want to calculate the moving average of all integers in the sliding window upto size k, we can using a fixed sliding window. in order to get a fixed sliding window upto size k, we can use a queue where we can keep adding numbers to the queue and if the length of our queue ever exceeds size k, we can remove the leftmost element of our queue. 
        - Time Complexity: O(1) to append to the queue and popleft from the queue. 
        - Space Complexity: The space used by the queue is proportional to the window size `size`, so O(size). Additional variables (`runningSum`, etc.) use constant space.
    '''

    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.runningSum = 0
    
    def next(self, val) -> float:
        self.queue.append(val)
        self.runningSum += val
        if len(self.queue) > self.size:
            self.runningSum -= self.queue.popleft
        return self.runningSum / len(self.queue)
