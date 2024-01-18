-- Link to problem: https://leetcode.com/problems/count-salary-categories

/* Write your T-SQL query statement below */
select category, count(*) - 1 as accounts_count
from (
    select 
        case
            when income < 20000 then 'Low Salary'
            when income <= 50000 then 'Average Salary'
            else 'High Salary'
        end category
    from Accounts

    union all

    select category from (values ('Low Salary'), ('Average Salary'), ('High Salary')) a (category)
) b
group by category