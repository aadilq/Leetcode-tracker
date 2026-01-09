## 3318. Find X-Sum of All K-Long Subarrays I

'''
You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

Count the occurrences of all elements in the array.
Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].

 

Example 1:
Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

Output: [6,10,12]

Explanation:

For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.

Example 2:
Input: nums = [3,8,7,8,7,5], k = 2, x = 2

Output: [11,15,15,15,12]

Explanation:

Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].
'''
from heapq import heappush, heappop
class Solution:
    def find(self, count: dict, x: int) -> int:
        heap = []
        for val, cnt in count.items():
            heappush(heap, (-cnt, -val))
        total = 0
        while x > 0 and heap:
            cnt, val = heappop(heap)
            cnt, val = -cnt, -val
            total += val * cnt
            x -= 1
        return total
    def findXSum(self, nums: list[int], k: int, x:int) -> list[int]:
        '''
        1. Fixed Sliding Window 
            - we want to count the occurences of each character in every subarray of size k and we can do so with a hashmap. we use left and right pointers to make sure that we don't go beyond our window of size k. we keep the occurences of each character in the subarray of size k and then we define another method to find the xsum of the top x most frequent elements. in this method we simulate a maxheap so that we can take the top x frequent elements and add them up. 
            - Time Complexity: our find function processes each element in the count dictionary by pushing each value into a heap which takes   ( U log U ) where U is the number of unique elements in the window and then we're going to have pop x times from the heap, which is going to be (X log U).  The findXSum function iterates over the entire nums list once, which is O(N), where N is the length of nums. For each window of size k, it calls find, which is O(U log U + x log U). Since U can be at most k (the size of the window), the total complexity is approximately O(N * (k log k + x log k)).
            - Space Complexity: The count dictionary stores at most k elements, so O(k). The heap in find can hold up to U elements, so O(k). Overall, the space complexity is dominated by the count and heap, which is O(k).
        '''

        res = []

        L = 0 
        count = {}

        for R in range(len(nums)):
            if nums[R] in count:
                count[nums[R]] += 1
            else:
                count[nums[R]] = 1
        
        if (R - L + 1) > k:
            if nums[L] in count:
                count[nums[L]] -= 1
                if count[nums[L]] == 0:
                    del count[nums[L]]
                L += 1
        
        if (R - L + 1) == k:
            res.append(self.find(count, x))
        return res

solution = Solution()
print(solution.findXSum([1,1,2,2,3,4,2,3], k = 6, x = 2))
        