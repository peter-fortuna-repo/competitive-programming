-- Link to problem: https://leetcode.com/problems/queries-quality-and-percentage

/* Write your T-SQL query statement below */
select query_name, 
        round(sum(cast(rating as decimal)/position)/count(*), 2) as quality, 
        round(100*sum(case when rating < 3 then 1.0 else 0.0 end)/count(*), 2) as poor_query_percentage
from Queries
where query_name is not null
group by query_name