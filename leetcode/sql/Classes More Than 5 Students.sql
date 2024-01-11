-- Link to problem: https://leetcode.com/problems/classes-more-than-5-student

/* Write your T-SQL query statement below */
select class
from (select class, count(distinct student) cnt
        from Courses
        group by class) a
where cnt >= 5