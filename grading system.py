# Grading System in Python

print("===== Student Grading System =====")

# Input marks
marks = float(input("Enter student marks (0-100): "))

# Check for valid input
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
else:
    # Assign grade
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    elif marks >= 35:
        grade = "E"
    else:
        grade = "F"

    # Display result
    print("\n===== RESULT =====")
    print("Marks :", marks)
    print("Grade :", grade)

    if marks >= 35:
        print("Result: PASS")
    else:
        print("Result: FAIL")
