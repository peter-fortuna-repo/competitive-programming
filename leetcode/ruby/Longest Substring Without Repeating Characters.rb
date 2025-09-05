# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
   max, set, i = 0, {}, 0
   
   while i < s.length
    current = s[i]
    if !set.has_key?(current)
        set[current] = i
        max = [max, set.keys.length].max
    else
        i = set[current]
        set = {}
    end
     i += 1
   end
    max    
end