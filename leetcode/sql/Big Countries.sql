-- Link to problem: https://leetcode.com/problems/big-countries

/* Write your T-SQL query statement below */

-- Solution 1:

select name, population, area
from World
where area >= 3000000

union

select name, population, area
from World
where population >= 25000000


-- Solution 2: This solution runs slightly faster than solution 1 on the given
-- test cases. However, for larger queries the 'or' operator can be slower than
-- the 'union' operator.

select name, population, area
from World
where area >= 3000000 or population >= 25000000