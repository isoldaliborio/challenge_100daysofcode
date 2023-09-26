inputs = ["Krishna 67 68 69", "Arjun 70 98 63", "Malika 52 56 60"]

n = 3

student_marks = {}

for i in range(n):
    name, *line = inputs[i].split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = "Malika"

print(student_marks)