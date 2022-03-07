

student_heights = input("Input a list of student heights ").split()

for x in range(0, len(student_heights)):
    student_heights[x] = int(student_heights[x])
#print(student_heights)

total_height = 0

for height in student_heights:
    total_height += height
#print(total_height)


number_of_students = 0

for student in student_heights:
    number_of_students += 1
#print(number_of_students)

average_height = round(total_height / number_of_students)

print(f"Average height is {average_height}cm")

"""
---Simple way---
total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)
"""