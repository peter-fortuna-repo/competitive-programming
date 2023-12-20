-- Link to problem: https://leetcode.com/problems/average-selling-price

/* Write your T-SQL query statement below */
select p.product_id, 
        case
            when sum(units*price) is null then 0
            else round(cast(sum(units*price) as decimal)/sum(units), 2)
        end as average_price
from prices p
left outer join UnitsSold u on p.product_id = u.product_id 
                and purchase_date >= start_date 
                and purchase_date <= end_date
group by p.product_id