"""
Find the difference between the total number of CITY entries 
in the table and the number of distinct CITY entries in the table.

"""

SELECT COUNT(s.CITY) - COUNT(DISTINCT s.CITY) 
FROM Station s;