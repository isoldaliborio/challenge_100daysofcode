"""

Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. 
Your result cannot contain duplicates.

"""

SELECT DISTINCT CITY
FROM STATION
WHERE CITY LIKE "%A"
    OR CITY LIKE "%E"
    OR CITY LIKE "%I"
    OR CITY LIKE "%O"
    OR CITY LIKE "%U"
    OR CITY LIKE "%a"
    OR CITY LIKE "%e"
    OR CITY LIKE "%i"
    OR CITY LIKE "%o"
    OR CITY LIKE "%u";


-- SELECT DISTINCT CITY
-- FROM STATION
-- OR RIGHT(CITY,1) 
-- IN ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u');