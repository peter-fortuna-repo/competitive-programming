-- Link to problem: https://leetcode.com/problems/game-play-analysis-iv

/* Write your T-SQL query statement below */
select round(count(*)*1.0/(select count(distinct player_id) from Activity), 2) fraction
from 
(select 
    event_date,
    lead(event_date) over(partition by player_id order by event_date) as next_login,
    row_number() over(partition by player_id order by event_date) as login_num
    from Activity) a
where login_num = 1 and datediff(day,event_date, coalesce(next_login, '9999-12-31'))=1