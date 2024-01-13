-- Link to problem: https://leetcode.com/problems/biggest-single-number

/* Write your T-SQL query statement below */
select max(num) num
from (select num, count(num) cnt from MyNumbers group by num) a
where cnt = 1