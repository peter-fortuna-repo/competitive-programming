-- Link to problem: https://leetcode.com/problems/group-sold-products-by-the-date

/* Write your T-SQL query statement below */
select sell_date, count(*) num_sold, string_agg(product, ',') products
from (select distinct * from Activities) t
group by sell_date