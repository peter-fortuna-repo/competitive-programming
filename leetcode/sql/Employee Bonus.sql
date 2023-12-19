-- Link to problem: https://leetcode.com/problems/article-views-i

/* Write your T-SQL query statement below */
select name, bonus
from Employee e left join Bonus b on e.empId = b.empId
where bonus is null or bonus < 1000