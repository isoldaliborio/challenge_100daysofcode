
"""RackerRanck problem
    Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  12 hour format

Returns

string: the time in  24 hour format

Input format:
07:05:45PM

Output sample:
19:05:45


"""

def timeConversion(s):
    period = s[-2:]  # Correct extraction of AM/PM
    hour, minute, second = s[:-2].split(':')  # Correct slicing for time components

    hour = int(hour)
    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
            
    return f"{hour:02}:{minute}:{second}"


    # Other Nice Solution that I found in the discussions:
    # def timeConversion(s):
    # if s[-2:] == "PM":
    #     if s[:2] == "12":
    #         return s[:-2]
    #     else:
    #         return str(int(s[:2])+12) + s[2:-2]
    # else:   #AM
    #     if s[:2] == "12":
    #         return "00" + s[2:-2]
    #     else:
    #         return s[:-2]
      