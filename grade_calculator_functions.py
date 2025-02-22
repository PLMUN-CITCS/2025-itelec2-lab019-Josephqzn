def get_student_score():

    score = input("Enter the student's score: ")
    if score.replace('.', '', 1).isdigit():
        score = float(score)
        if 0 <= score <= 100:
            return score
    print("Invalid input. Please enter a valid score between 0 and 100.")
    return get_student_score()

def calculate_grade(score):

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():

    score = get_student_score()
    grade = calculate_grade(score)
    print(f"The student's grade is: {grade}")

if __name__ == "__main__":
    main()