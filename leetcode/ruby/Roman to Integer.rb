# @param {String} s
# @return {Integer}
def roman_to_int(s)
    order = {"I" => 1, "V" => 5, "X" => 10, "L" => 50, "C" => 100, "D" => 500, "M" => 1000}
    sum = 0
    max = 0
    s.reverse.each_char do |char|
        if order[char] >= max
            sum += order[char]
            max = order[char]
        else
            sum -= order[char]
        end
    end
    sum
end
