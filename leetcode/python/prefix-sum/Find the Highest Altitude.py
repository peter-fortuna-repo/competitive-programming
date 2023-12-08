# There is a biker going on a road trip. The road trip consists of n + 1 
# points at different altitudes. The biker starts his trip on point 0 with 
# altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain
# in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the
# highest altitude of a point.


# Solution
# This very simple problem can be solved in one pass.

# Time complexity: O(n)
# Space complexity: O(1)

def largestAltitude(self, gain: List[int]) -> int:
    alt = 0
    max_alt = 0
    for g in gain:
        alt += g
        max_alt = max(max_alt, alt)
    return max_alt