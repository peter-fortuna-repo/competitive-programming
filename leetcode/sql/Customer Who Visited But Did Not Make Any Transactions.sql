-- Link to problem: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

/* Write your T-SQL query statement below */
select customer_id, count(*) as count_no_trans
from Visits V left join (select * from Transactions where amount is not null) T on T.visit_id = V.visit_id
where amount is null
group by customer_id