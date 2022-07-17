my_grades = {
    "Chemistry": "A",
    "Math": "B",
    "Biology": "A",
    "Physics": "C"
}
grade_points = {
    "A": 100,
    "B": 80,
    "C": 40
}
total_points = 0
for subject_name, subject_grade in my_grades.items():
    print(
        f"My Grade In {subject_name} Is '{subject_grade}', Which Equals {grade_points[subject_grade]} Points")
    total_points += grade_points[subject_grade]
else:
    print(f"My Total Points Score Is: {total_points}")
