-- Link to problem: https://leetcode.com/problems/exchange-seats

/* Write your T-SQL query statement below */
select
    case
        when id%2 = 0 then prev_id
        when next_id is null then id
        else next_id
    end id,
    student
from ( 
    select 
        id, 
        lead(id) over(order by id) next_id, 
        lag(id) over(order by id) prev_id,
        student
    from Seat) t1
order by id