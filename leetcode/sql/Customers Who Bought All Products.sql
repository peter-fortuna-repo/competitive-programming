-- Link to problem: https://leetcode.com/problems/custoemrs-who-bought-all-products

/* Write your T-SQL query statement below */
select customer_id
from Customer
group by customer_id
having count(distinct product_key) = (select count(distinct product_key) from Product)