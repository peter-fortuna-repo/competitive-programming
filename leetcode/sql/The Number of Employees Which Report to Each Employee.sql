-- Link to problem: https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee

/* Write your T-SQL query statement below */
select e1.reports_to employee_id, max(e2.name) name, count(*) reports_count, round(avg(e1.age * 1.0), 0) average_age
from Employees e1
left join Employees e2 on e1.reports_to = e2.employee_id 
where e1.reports_to is not null
group by e1.reports_to