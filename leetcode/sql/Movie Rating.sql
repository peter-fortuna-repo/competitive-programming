-- Link to problem: https://leetcode.com/problems/movie-rating

/* Write your T-SQL query statement below */
select name as results
from ( select top 1 name
    from MovieRating
    left join Users
    on MovieRating.user_id = Users.user_id
    group by Users.name
    order by count(*) desc, name asc) most_active_user

union all

select title as results
from (select top 1 title 
    from MovieRating
    left join Movies 
    on MovieRating.movie_id = Movies.movie_id
    where created_at < '2020-03-01' and created_at >= '2020-02-01'
    group by title
    order by avg(rating * 1.0) desc, title asc) best_rated_movie