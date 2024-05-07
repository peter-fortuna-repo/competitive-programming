# Link to problem: https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/description/

# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def minimumOperationsToMakeKPeriodic(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        n = len(word)
        substrings = dict()
        max_number_of_repeats = 1
        for i in range(n/k):
            substring = word[k*i:k*(i+1)]
            if substring not in substrings:
                substrings[substring] = 0
            substring_count = substrings[substring]
            substring_count += 1
            substrings[substring] = substring_count
            if substring_count > max_number_of_repeats:
                max_number_of_repeats = substring_count

        return n/k - max_number_of_repeats