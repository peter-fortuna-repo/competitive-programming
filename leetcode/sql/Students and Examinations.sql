-- Link to problem: https://leetcode.com/problems/students-and-examinations

/* Write your T-SQL query statement below */
select a.student_id, 
    a.student_name, 
    a.subject_name, 
    case
        when b.attended_exams is null then 0
        else b.attended_exams 
    end as attended_exams
from (select * 
        from Students cross join Subjects) a
left join (select student_id, subject_name, count(*) as attended_exams
        from Examinations 
        group by student_id, subject_name) b
on a.student_id = b.student_id and a.subject_name = b.subject_name
order by a.student_id, a.subject_name