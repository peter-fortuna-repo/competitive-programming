# Link to problem: https://leetcode.com/problems/determine-if-two-strings-are-close

# Solution: After the frequency of each letter is counted and we confirm that
# the two words share the same letters, we sort the frequencies for word1 and
# word2 and check that they are equal. The length of each frequency arry is 26,
# so this results in constant storage and constant time to sort. The O(n) 
# runtime comes from looping through the chars in each word.

# Time complexity: O(n) 
# Space complexity: O(1)

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count_1 = [0] * 26
        count_2 = [0] * 26

        for c in word1:
            count_1[ord(c) - 97] += 1
        
        for c in word2:
            count_2[ord(c) - 97] += 1
        
        for i in range(26):
            if bool(count_1[i]) != bool(count_2[i]):
                return False 

        count_1.sort()
        count_2.sort()
        return count_1 == count_2