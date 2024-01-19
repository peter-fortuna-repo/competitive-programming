-- Link to problem: https://leetcode.com/problems/restaurant-growth

/* Write your T-SQL query statement below */
select 
    visited_on, 
    sum(amount) over(order by visited_on rows between 6 preceding and current row) amount, 
    round(sum(amount) over(order by visited_on rows between 6 preceding and current row)/7.0, 2) average_amount
from (
    select 
        visited_on,
        sum(amount) amount
    from Customer
    group by visited_on) a
order by visited_on
offset 6 rows