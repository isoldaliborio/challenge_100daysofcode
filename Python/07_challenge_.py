# Question:
# DNA is made of a sequence of 4 letters A, T, C and G. 
# When the letter can not be determined we will get the X letter instead.
# We have the sequence of the whole human genome in one flat file.
# We would like to calculate the number and proportion of the DNA letters in this file.
# We are assuming that we can fit the whole file in memory.
# Write a python script to calculate this.
    # Input:

    # ATCGATCGAAATCGATCGXX

    # Output: 

    # A - count: 6, ratio: 0.3
    # C - count: 4, ratio: 0.2
    # T - count: 4, ratio: 0.2
    # G - count: 4, ratio: 0.2
    # X - count: 2, ratio: 0.1



DNA = "TCGATCGAAATCGATCGXX"


count = {"A":0,
"T":0,
"C":0,
"G":0,
"X":0
}


for letter in DNA:
    if letter in count.keys():
        count[letter] = count[letter] + 1
    else:
        print(f"The letter {letter} is not part of DNA" )

size = len(DNA)
for letter in count:
    value = count[letter]
    ratio = round(value/size, 1)
    print(f"{letter} - count: {value}, ratio: {ratio}")



