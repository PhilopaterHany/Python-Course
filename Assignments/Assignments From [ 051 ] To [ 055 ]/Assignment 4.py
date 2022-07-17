students = {
    "Philopater": {
        "Math": "B",
        "Chemistry": "A",
        "Biology": "A",
        "Physics": "C",
        "Problem Solving": "B"
    },
    "Osama": {
        "Math": "A",
        "Chemistry": "D",
        "Biology": "C",
        "Physics": "B",
        "Problem Solving": "A"
    },
    "Mohamed": {
        "Math": "A",
        "Chemistry": "B",
        "Biology": "C",
        "Physics": "C",
        "Problem Solving": "D"
    }
}
grades_points = {
    "A": 100,
    "B": 80,
    "C": 40,
    "D": 20
}
# Solution 1
# for student in students:
#     print("".center(40, "="))
#     print(f" Student Name: {student} ".center(40, "="))
#     print("".center(40, "="))
#     total_points = 0
#     for subject in students[student]:
#         print(
#             f"- {subject} => {students[student][subject]} => {grades_points[students[student][subject]]} Points.")
#         total_points += grades_points[students[student][subject]]
#     print(f"{student}\'s Total Points Score Is {total_points}.")

# Solution 2 (With .items())
for student, subjects in students.items():
    print("".center(40, "="))
    print(f" Student Name: {student} ".center(40, "="))
    print("".center(40, "="))
    total_points = 0
    for subject, grade in subjects.items():
        print(
            f"- {subject} => {grade} => {grades_points[grade]} Points.")
        total_points += grades_points[grade]
    print(f"{student}\'s Total Points Score Is {total_points}.")
