-- Link to problem: https://leetcode.com/problems/confirmation-rate

/* Write your T-SQL query statement below */
select user_id, 
        round(sum(case when action='confirmed' then 1.0 else 0.0 end)/count(*), 2) as confirmation_rate
from (select * from Confirmations
        union
        select user_id, time_stamp, 'signup' as action
        from Signups
        where user_id not in (select distinct user_id from Confirmations)) a
group by user_id