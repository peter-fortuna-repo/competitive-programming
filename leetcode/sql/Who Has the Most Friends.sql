-- Link to problem: https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends

/* Write your T-SQL query statement below */
select top 1 a.id, count(*) num
from ((select requester_id id from RequestAccepted)
        union all
        (select accepter_id id from RequestAccepted)) a
group by a.id
order by num desc