"""
The provided code stub will read in a dictionary containing key/value 
pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, 
showing 2 places after the decimal.

Example
"""


n = 2 
students_and_scores = ["Harsh 25 26.5 28", "Anurag 26 28 30"]
query_name = "Harsh"


student_marks = {}
for item in students_and_scores:
        name, *line = item.split()
        scores = list(map(float, line))
        student_marks[name] = scores

query_scores = student_marks[query_name]
average = sum(query_scores)/3  
print(f'{average:.2f}')