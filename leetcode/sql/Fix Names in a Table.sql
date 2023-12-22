-- Link to problem: https://leetcode.com/problems/fix-names-in-a-table

/* Write your T-SQL query statement below */
select user_id, upper(substring(name, 1, 1)) + lower(substring(name, 2, 65535)) as name
from Users
order by user_id