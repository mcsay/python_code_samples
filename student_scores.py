

student_scores = input("Input a list of student scores ").split()
for x in range(0, len(student_scores)):
    student_scores[x] = int(student_scores[x])
print(student_scores)

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is :{highest_score}")


"""
---Simple way---
max_value = max(student_scores)

print(f"The highest score in the class is :{max_value}")
"""