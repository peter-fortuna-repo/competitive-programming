# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and 
# Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

# Solution 1: Top down
# The classic dynamic programming problem with a slight twist. Here's the top
# down solution (aka memoized). It's quick, but uses a bit extra memory.

# Time complexity: O(n) 
# Space complexity: O(n)

def tribonacci(n: int) -> int:
    sequence = [None]*(n+1)
    return self.tribonacciHelper(n, sequence)

def tribonacciHelper(n, sequence):
    if n == 0:
            return 0
    if n == 1 or n == 2:
            return 1
    if sequence[n] != None:
            return sequence[n]
    sequence[n] = (self.tribonacciHelper(n-1, sequence) + 
                        self.tribonacciHelper(n-2, sequence) + 
                        self.tribonacciHelper(n-3, sequence))
    return sequence[n]

# Solution 2: Bottom up
# The same solution as above, but implemented with a bottom up approach. Memory
# is constant since we use a three pointers to the previous values instead of
# storing all previous tribonacchi numbers.

# Time complexity: O(n)
# Space complexity: O(1)

def tribonacci(n: int) -> int:
        prev1 = 0
        prev2 = 1
        current = 1
        if n == 0:
              return prev1
        if n == 1 or n == 2:
              return prev2
        for i in range(3, n+1):
             temp = current
             current = current + prev1 + prev2
             prev1, prev2 = prev2, temp
        return current