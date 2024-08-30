# 2. Sort a list
# Create a function in Porderthon that accepts two parameters. 
# The first will be a list of numbers. 
# The second parameter will be a string that can be one of the following values: asc, desc, and none.

# If the second parameter is "asc," 
# then the function should return a list with the numbers in ascending order. 
# If it's "desc," then the list should be in descending order, 
# and if it's "none," it should return the original list unaltered.

# in a list, the sort() method changes the original list "in-place". so orderou don't
# need to assign it to a new variable

def sort_list(list_input,order):
    if order == "asc":
        list_input.sort()
    elif order == "desc":
        list_input.sort(reverse=True)
    elif order == "none":
        list_input = list_input
    else:
        list_input = None
    return list_input

num = [10,3,9,4,7]
order = "asc"

sorted_list = sort_list(num, order)

if sorted_list is None:
    print("Invalid order")
else:
    print(sorted_list)
