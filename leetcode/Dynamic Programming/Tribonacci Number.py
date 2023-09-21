# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and 
# Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

# Solution 1: 
# The classic dynamic programming problem with a slight twist. It could use a
# bit less memory if I kept variables for Tn-1, Tn-2, and Tn-3 instead of 
# keeping all previous numbers.

# Time complexity: O(n) 
# Space complexity: O(n)

def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        sequence = [0,1,1]
        return self.tribonacciHelper(n, sequence)
    
def tribonacciHelper(self, n, sequence):
    if len(sequence) == n + 1:
        return sequence[-1]
    sequence.append(sequence[-3] + sequence[-2] + sequence[-1])
    return self.tribonacciHelper(n, sequence)