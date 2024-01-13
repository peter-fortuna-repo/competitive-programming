-- Link to problem: https://leetcode.com/problems/product-sales-analysis-iii

/* Write your T-SQL query statement below */
select product_id, year first_year, quantity, price
from (select product_id, year, quantity, price, rank() over(partition by product_id order by product_id, year) rank
        from Sales) a
where rank = 1