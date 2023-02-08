

# Python code
# To reverse words in a given string

    # Question: Given an input string s, reverse the order of the words.
    # A word is defined as a sequence of non-space characters.
    # The words in s will be separated by at least one space.
    # Return a string of the words in reverse order concatenated by a single space.
    # Note that s may contain leading or trailing spaces or multiple spaces between two words. 
    # The returned string should only have a single space separating the words. 
    # Do not include any extra spaces.
        # ---  [:] list slice (initial position, final position, step). In te final position is the previou number
 
# input string
string = "azul da cor do mar"
# reversing words in a given string
s = string.split()[::-1]
l = []
for itens in s:
    # apending reversed words to l
    l.append(itens)
# printing reverse words ----- .join --- transform a list into a string
print(" ".join(l))