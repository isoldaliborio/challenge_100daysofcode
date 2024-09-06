"Check if a string is an panagram (contains all the letters of the alphabet)"

def pangrams(s):
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    s = set(s.lower())
    if alphabet_set.issubset(s):
        return "pangram"
    else:
        return "not pangram"



# def pangrams(s):
#     alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
#     len_s = len(s)
#     for letter in s:
#         letter = letter.lower()
#         if letter in alphabet_set:
#             alphabet_set.remove(letter)
    
#     if not alphabet_set:
#         return "pangram"
#     else:
#         return "not pangram"

# complexity O(n)