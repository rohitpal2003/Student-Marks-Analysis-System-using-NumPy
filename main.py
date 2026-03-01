import numpy as np

# -------------------------------
# STEP 1: Student Marks Data
# Rows = Students, Columns = Subjects
# Subjects: Math, Physics, Chemistry
# -------------------------------
marks = np.array([
    [78, 65, 70],
    [88, 92, 85],
    [55, 48, 60],
    [90, 85, 88],
    [35, 40, 45]
])

subjects = ["Math", "Physics", "Chemistry"]

print("Student Marks Matrix:\n", marks)
print("-" * 40)

# -------------------------------
# STEP 2: Average Marks per Student
# -------------------------------
student_avg = np.mean(marks, axis=1)
print("Average Marks Per Student:")
for i, avg in enumerate(student_avg):
    print(f"Student {i+1}: {avg:.2f}")
print("-" * 40)

# -------------------------------
# STEP 3: Subject-wise Average
# -------------------------------
subject_avg = np.mean(marks, axis=0)
print("Subject-wise Average Marks:")
for sub, avg in zip(subjects, subject_avg):
    print(f"{sub}: {avg:.2f}")
print("-" * 40)

# -------------------------------
# STEP 4: Subject-wise Highest & Lowest
# -------------------------------
subject_max = np.max(marks, axis=0)
subject_min = np.min(marks, axis=0)

print("Highest & Lowest Marks Per Subject:")
for i in range(len(subjects)):
    print(f"{subjects[i]} -> Highest: {subject_max[i]}, Lowest: {subject_min[i]}")
print("-" * 40)

# -------------------------------
# STEP 5: Class Topper
# -------------------------------
total_marks = np.sum(marks, axis=1)
topper_index = np.argmax(total_marks)

print(f"Class Topper: Student {topper_index + 1}")
print(f"Total Marks: {total_marks[topper_index]}")
print("-" * 40)

# -------------------------------
# STEP 6: Pass / Fail Analysis
# -------------------------------
pass_marks = 40
pass_fail = np.all(marks >= pass_marks, axis=1)

print("Pass / Fail Status:")
for i, status in enumerate(pass_fail):
    result = "Pass" if status else "Fail"
    print(f"Student {i+1}: {result}")
print("-" * 40)

# -------------------------------
# STEP 7: Count Passed & Failed Students
# -------------------------------
passed = np.sum(pass_fail)
failed = len(pass_fail) - passed

print(f"Total Passed Students: {passed}")
print(f"Total Failed Students: {failed}")
print("-" * 40)

# -------------------------------
# STEP 8: Grade Assignment
# -------------------------------
grades = []

for avg in student_avg:
    if avg >= 85:
        grades.append("A")
    elif avg >= 70:
        grades.append("B")
    elif avg >= 50:
        grades.append("C")
    else:
        grades.append("D")

print("Grades:")
for i, grade in enumerate(grades):
    print(f"Student {i+1}: Grade {grade}")
print("-" * 40)

print("Student Marks Analysis Completed Successfully ✅")



