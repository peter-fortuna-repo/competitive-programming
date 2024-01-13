-- Link to problem: https://leetcode.com/problems/find-followers-count

/* Write your T-SQL query statement below */
select user_id, count(distinct follower_id) as followers_count
from Followers
group by user_id