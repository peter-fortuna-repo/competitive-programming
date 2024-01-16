-- Link to problem: https://leetcode.com/problems/primary-department-for-each-employee

/* Write your T-SQL query statement below */
select employee_id, department_id
from Employee
where primary_flag = 'Y'

union

select max(employee_id), max(department_id)
from Employee
group by employee_id
having count(*) = 1