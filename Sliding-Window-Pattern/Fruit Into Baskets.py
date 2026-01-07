## 904. Fruit Into Baskets

'''
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
'''
from collections import defaultdict
class Solution:
    def fruitsInBasket(self, fruits: list[int]) -> int:
        '''
        1. Variable Sliding Window + hashmap
            - we can essentially use a sliding window and a hashmap approach where our the size of our hashmap determines which ptrs we can move. If the size of our hashmap ever exceeds two which means that we're holding a third fruit, we have to move our left ptr and decrement the count the hashmap until we have at most two fruits in our hashmap. 
            - Time Complexity: O(n) where n is the length of the input string and this is because we iterate through every fruit in fruits to see the maximum number of fruits that we can hold given the constraints.
            - Space Complexity: O(1) because the size our hashmap is never going to become bigger than the size of 2. 
        '''

        L = curr = res = 0

        count = defaultdict(int)

        for R in range(len(fruits)):
            count[fruits[R]] = count.get(fruits[R], 0) + 1
            curr += 1

            while len(count) > 2:
                count[fruits[L]] -= 1
                curr -= 1
                if count[fruits[L]] == 0:
                    del count[fruits[L]] 
                L += 1
            res = max(res, curr)
        return res
solution = Solution()
print(solution.fruitsInBasket([1,2,3,2,2]))
