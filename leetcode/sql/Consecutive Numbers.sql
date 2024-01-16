-- Link to problem: https://leetcode.com/problems/consecutive-numbers

/* Write your T-SQL query statement below */
select distinct first(num) ConsecutiveNums
from (
    select 
        num, 
        sum(flag) over(order by id) consecutive_id
    from (
        select 
            id,
            num, 
            case
                when num = lag(num) over(order by id) then 0
                else 1
            end flag
        from Logs) a ) b
group by consecutive_id
having count(*) >= 3