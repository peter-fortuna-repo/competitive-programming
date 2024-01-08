-- Link to problem: https://leetcode.com/problems/find-users-with-valid-e-mails

/* Write your T-SQL query statement below */
SELECT user_id, name, mail FROM Users
WHERE mail like '[A-Za-z]%@leetcode.com' and mail not like '[A-Za-z]%[^A-Za-z0-9_.-]%@leetcode.com'