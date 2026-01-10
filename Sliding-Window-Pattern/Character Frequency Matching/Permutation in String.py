## 567. Permutation in String

'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        1. to find if s2 contains a permutation of s1, we want to first validate that we can check it. if s1 is bigger than s2, then we return false automatically because a permutation of s1 cannot exist in s2. then we initialize two hashmaps, one for counting the frequency of character in s1 and s2. we initialize a for loop and iterate through both strings of length s1. at the end of the for loop, if the hashmaps are equal, we return true otherwise, we use another for loop from len(s1) all the way to len(s2) to check the rest of s2 to see if a permuation exist. 
        - Time Complexity: O(n + m) where n is length of s1 and m is the length of s2. this is because we are iterating through both strings performing constant time operation such adding to a dictionary and removing from our dictionary but we are going through the both strings. 
        - Space Complexity: O(n) because the size of our hashmaps will only as big as len(s1).  
        '''
        if len(s2) < len(s1):
            return False
        
        S1count, S2count = {}, {}

        for i in range(len(s1)):
            S1count[s1[i]] = S1count.get(s1[i], 0) + 1
            S2count[s2[i]] = S2count.get(s2[i], 0) + 1
        if S1count == S2count:
            return True
        L = 0
        for R in range(len(s1), len(s2)):
            S2count[s2[R]] = S2count.get(s2[R], 0) + 1
            S2count[s2[L]] -= 1

            if S2count[s2[L]] == 0:
                del S2count[s2[L]]
            L += 1

            if S1count == S2count:
                return True
        return False
    