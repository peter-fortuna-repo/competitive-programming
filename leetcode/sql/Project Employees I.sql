-- Link to problem: https://leetcode.com/problems/project-employees-i

/* Write your T-SQL query statement below */
select project_id, round(avg(cast(experience_years as decimal)), 2) as average_years
from Project p left join Employee e on p.employee_id = e.employee_id
group by project_id