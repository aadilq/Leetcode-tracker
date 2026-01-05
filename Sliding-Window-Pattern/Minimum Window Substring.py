## 76. Minimum Window Substring

'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''

class Solution:
    def minimumSubstring(self, s: str, t: str) -> str:
        '''
        1. Variable sliding window
            - we want the shortest substring of s that includes all of the character of t, even duplicates. to do, we're going to rely on the use of hashmaps. for string t, we are going to initialize a hashmap and count the occurrences of each character in string t. this will tell how many each times each character occurs, effectively checking for duplicates. then similarly, we are going to initialize a hashmap for string s and iterate until the two hashmaps are the same. if the current window length is smaller than the window length stored then, then we replace our minimum window subtring length and minimum substring itself. 
            - Time Complexity: O(n) for iterating and populating our hashmap for string t. O(n) for iterating and populating our hashmap for string s. 
            - Space Complexity: O(n) because we are using hashmaps to store the occurences of each character and worst case if each character is unique, then our hashmap is the same size as our input string. 
        '''

        if len(t) > len(s): return ""

        countT = {}

        for char in t:
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1
        
        countS = {}
        L = 0 
        reslen = float('inf')
        res = ""
        have, need = len(countT), 0

        for R in range(len(s)):
            charR = s[R]
            countS[charR] = countS.get(charR, 0) + 1

            if charR in countT and countT[charR] == countS[charR]:
                need += 1
            
            while have == need:
                if (R - L + 1) < reslen:
                    reslen = (R - L + 1)
                    res = s[L:R+1]
                charL = s[L]
                countS[charL] -= 1
                if charL in countT and countS[charL] < countT[charL]:
                    need -= 1
                L += 1
        return res

solution = Solution()
print(solution.minimumSubstring("ADOBECODEBANC", "ABC"))

        