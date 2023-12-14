-- Link to problem: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier

/* Write your T-SQL query statement below */
select unique_id, name
from Employees a left join EmployeeUNI b on a.id = b.id