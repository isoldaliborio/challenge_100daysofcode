"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands
where each command will be of the  types listed above.
Iterate through each command in order and perform the corresponding operation on your list.
"""

# Initialize an empty list
my_list = []

# Number of commands
N = int(input())

# Iterate through each command
for _ in range(N):
    command = input().split()

    if command[0] == "insert":
        # Insert element at specified position
        i, e = int(command[1]), int(command[2])
        my_list.insert(i, e)
    elif command[0] == "print":
        # Print the list
        print(my_list)
    elif command[0] == "remove":
        # Remove the first occurrence of an element
        e = int(command[1])
        my_list.remove(e)
    elif command[0] == "append":
        # Append an element to the end of the list
        e = int(command[1])
        my_list.append(e)
    elif command[0] == "sort":
        # Sort the list
        my_list.sort()
    elif command[0] == "pop":
        # Pop the last element from the list
        my_list.pop()
    elif command[0] == "reverse":
        # Reverse the list
        my_list.reverse()
