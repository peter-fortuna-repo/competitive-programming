-- Link to problem: https://leetcode.com/problems/average-time-of-process-per-machine

/* Write your T-SQL query statement below */
select machine_id, round(sum(time)/count(*), 3) processing_time
from (select a1.machine_id, a1.timestamp - a2.timestamp time
        from Activity a1 left join Activity a2 
            on a1.machine_id = a2.machine_id
            and a1.process_id = a2.process_id
        where a1.activity_type = 'end' and a2.activity_type = 'start') a
group by machine_id