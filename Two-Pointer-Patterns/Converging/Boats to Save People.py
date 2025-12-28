## 881. Boats to Save People

'''
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
'''

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        '''
        1. Two Pointer Approach (Converging)
        Sort the input array so that all the heaviest people are at the end of the array. We set up two pointers, one at the beginning and end of the array. We add the weights of the two individuals. If the weights of the two individuals are equal to or less than the limit, we increase our result by 1 and decrement both pointers, meaning that we can fit both people into one boat. If not, this means we can only hold the heaviest pointer and decrement only our right pointer while also increasing result by 1.
        '''

        people.sort()
        res = 0

        L, R = 0, len(people) - 1

        while L <= R:
            if people[L] + people[R] <= limit:
                res += 1
                L += 1
                R -= 1
            else:
                res += 1
                R -= 1
        return res

solution = Solution()
print(solution.numRescueBoats([3,2,2,1], 3))