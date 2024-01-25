-- Link to problem: https://leetcode.com/problems/investments-in-2016

 /* Write your T-SQL query statement below */
select round(sum(tiv_2016), 2) tiv_2016
from Insurance
where pid in (
    select max(pid)
    from Insurance
    group by lat, lon
    having count(*) = 1
)
and pid not in (
    select max(pid)
    from Insurance
    group by tiv_2015
    having count(*) = 1
)