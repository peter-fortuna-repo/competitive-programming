-- Link to problem: https://leetcode.com/problems/immediate-food-delivery-ii

/* Write your T-SQL query statement below */
select round(100.0 * sum(immediate)/count(*), 2)immediate_percentage
from (select case 
                when order_date = customer_pref_delivery_date then 1
                else 0
            end immediate,
            rank() over (partition by customer_id order by order_date) r
        from Delivery
        ) a
where r = 1