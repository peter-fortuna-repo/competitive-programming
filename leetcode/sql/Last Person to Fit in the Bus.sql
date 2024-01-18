-- Link to problem: https://leetcode.com/problems/last-person-to-fit-in-the-bus

/* Write your T-SQL query statement below */
select top 1 person_name
from (
    select 
        person_name,
        sum(weight) over (order by turn) total_weight
    from Queue
) a
where total_weight <= 1000
order by total_weight desc