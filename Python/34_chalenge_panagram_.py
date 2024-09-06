"Check if a string is an panagram (contains all the letters of the alphabet)"

def pangrams(s):
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    len_s = len(s)
    result = None

    for i in range(len_s):
        letter = letter.lower()

        for letter in alphabet_set:
            if letter in s:
                result = "pangram"
            else:
                result = "not pangram"
    
    return result

s = "the quick brown fox jumps over the lazy dog"
result = pangrams(s)
print(result)

# complexity o(n2)





# def pangrams(s):
#     alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
#     len_s = len(s)
#     for i in range(len_s):
#         for letter in s:
#             letter = letter.lower()
#             if letter in alphabet_set:
#                 alphabet_set.remove(letter)
    
#     if not alphabet_set:
#         return "pangram"
#     else:
#         return "not pangram"

# complexity O(n)