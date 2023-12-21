-- Link to problem: https://leetcode.com/problems/percentage-of-users-attended-a-contest

/* Write your T-SQL query statement below */
declare @num_users decimal;
set @num_users = (select count(distinct user_id) from Users);

select contest_id, round(100*count(*)/@num_users, 2) as percentage
from Register
group by contest_id
order by percentage desc, contest_id