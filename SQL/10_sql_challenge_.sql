"""
Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

Table: Station
Fields: ID, CITY, STATE, LAT_N, LONG_N

"""
-- SELECT DISTINCT CITY FROM STATION
-- WHERE CITY NOT LIKE "^[aeiouAEIOU]%"
-- OR CITY NOT LIKE "%[aeiouAEIOU]$";
--      like does not support regex

SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(CITY,1) 
NOT IN ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u') 
OR RIGHT(CITY,1) 
NOT IN ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u');