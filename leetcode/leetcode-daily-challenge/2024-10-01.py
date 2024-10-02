# Solution 1
# Computational complexity: O(n^2)

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        new_arr = []
        for val in arr:
            new_arr.append(val%k)
        new_arr.sort()

        while new_arr:
            val = new_arr.pop()
            for i in range(len(new_arr)):
                if (new_arr[i] + val) % k == 0:
                    new_arr.pop(i)
                    break
                if i == len(new_arr)-1:
                    return False
        return True

# Solution 2
# Computational complexity: O(n)    
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod_counts = dict()
        for val in arr:
            if val%k not in mod_counts.keys():
                mod_counts[val%k] = 1
            else:
                mod_counts[val%k] += 1
        
        for key in mod_counts.keys():
            if key == k/2:
                if mod_counts[key]%2 == 1:
                    return False
            elif key == 0:
                if mod_counts[key%2] == 1:
                    return False
            elif k-key not in mod_counts.keys():
                return False
            elif mod_counts[key] != mod_counts[k-key]:
                return False
        return True