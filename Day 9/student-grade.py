student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
    result = student_scores[student]
    if result > 90:
        student_grades[student] = "Outstanding"
    elif result > 80:
        student_grades[student] = "Exceeds Expectations"
    elif result > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
    
print(student_grades)