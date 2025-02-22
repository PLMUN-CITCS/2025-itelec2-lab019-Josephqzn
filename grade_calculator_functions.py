def get_student_score():

    while True:
        score = input("Enter the student's score: ")
        if score.replace('.', '', 1).isdigit():
            score = float(score)
            if 0 <= score <= 100:
                return score
        print("Invalid input. Please enter a valid score between 0 and 100.")

def calculate_grade(score):

    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'

def main():
    """
    Main program flow that gets the student's score,
    calculates the grade, and displays it to the user.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"The student's grade is: {grade}")

if __name__ == "__main__":
    main()
