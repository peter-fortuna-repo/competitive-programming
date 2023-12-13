-- Link to problem: https://leetcode.com/problems/find-customer-referee

/* Write your T-SQL query statement below */
select name 
from Customer
where referee_id != 2
union all
select name 
from Customer
where referee_id is null