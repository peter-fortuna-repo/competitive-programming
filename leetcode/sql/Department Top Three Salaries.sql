-- Link to problem: https://leetcode.com/problems/department-top-three-salaries

/* Write your T-SQL query statement below */
select 
    D.name Department, 
    E.name Employee, 
    E.salary Salary
from Employee E
left join Department D
on E.departmentId = D.id
left join 
        (select 
            salary,
            departmentId,
            rank() over (partition by departmentId order by a.salary desc) r
        from
            (select 
                distinct salary,
                departmentId
            from Employee
        ) a
    ) b
on E.salary = b.salary and E.departmentId = b.departmentId
where r < 4