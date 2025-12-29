## 27. Remove Element

'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        '''
        1. Two Pointer Approach + Array Modification
            - we use a pointer k that keeps track of the position that we replace. when we come across an element that is not equal to val, we place it on the kth position. k is going to tell use which position to place the unique element and how many elements are not equal to val.
            - Time Complexity: O(n) where n is the length of the array nums. This is because we have to traverse the whole array to make sure we haven't left out any values that are not val
            - Space Complexity: O(1) since we are not using any additional data structures beyond a few ptrs
        '''

        k = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
solution = Solution()
print(solution.removeElement([0,1,2,2,3,0,4,2], val = 2))