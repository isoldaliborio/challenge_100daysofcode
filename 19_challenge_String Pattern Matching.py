"""You are given two strings: pattern and source. 
    The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

Your task is to calculate the number of substrings of source that match pattern. 

We'll say that a substring source[l..r] matches pattern if the following three conditions are met:
- The pattern and substring are equal in length.
- Where there is a 0 in the pattern, there is a vowel in the substring. 
- Where there is a 1 in the pattern, there is a consonant in the substring. 

Vowels are 'a', 'e', 'i', 'o', 'u', and 'y'. All other letters are consonants. """

def check_for_pattern(pattern, source, start_index):
    vowels = ["a", "e", "i", "o", "u", "y"]
    for i in range(len(pattern)):
        if pattern[i] == "0":
            if source[start_index + i] not in vowels:
                return 0
        elif pattern[i] == "1":
            if source[start_index + i] in vowels:
                return 0
        elif pattern[i] != "1" and pattern[i] != "0":
            return "not valid source"
    return 1


def solution(pattern, source):
    aswer = 0
    for start_index in range(len(source) - len(pattern) +1):
        answer += check_for_pattern(pattern,source, start_index)
    return answer 


pattern = "010"
source = "amazing"

print(solution(pattern, source))





# def check_for_pattern(pattern, source, start_index):
#    for offset in range(len(pattern)):
#        if pattern[offset] == '0':
#            if source[start_index + offset] not in vowels:
#                return 0
#        else:
#            if source[start_index + offset] in vowels:
#                return 0
#    return 1
#   def solution(pattern, source):
#    answer = 0
#    for start_index in range(len(source) - len(pattern) + 1):
#        answer += check_for_pattern(pattern, source, start_index)
#    return answer