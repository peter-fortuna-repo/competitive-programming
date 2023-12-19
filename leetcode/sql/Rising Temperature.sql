-- Link to problem: https://leetcode.com/problems/rising-temperature

/* Write your T-SQL query statement below */
select id
from (select id, 
            temperature, 
            lag(temperature) over(order by recordDate) temperatureYesterday,
            recordDate,
            lag(recordDate) over (order by recordDate) dateYesterday
        from Weather) a
where temperature > temperatureYesterday and recordDate = dateadd(day, 1, dateYesterday)