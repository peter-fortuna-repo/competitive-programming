-- Link to problem: https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher

/* Write your T-SQL query statement below */
select teacher_id, count(distinct subject_id) cnt
from Teacher
group by teacher_id