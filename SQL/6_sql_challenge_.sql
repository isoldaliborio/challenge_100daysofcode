"""
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION.
 Your result cannot contain duplicates.

"""

SELECT CITY FROM STATION
WHERE CITY LIKE 'a%'
    OR CITY LIKE 'e%' 
    OR CITY LIKE 'i%' 
    OR CITY LIKE 'o%' 
    OR CITY LIKE 'u%'
    OR CITY LIKE 'A%' 
    OR CITY LIKE 'E%' 
    OR CITY LIKE 'I%' 
    OR CITY LIKE 'O%'
    OR CITY LIKE 'U%';