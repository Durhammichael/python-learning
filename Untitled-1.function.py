# Mini project phase 1
# bad_grade_tracker() responsibilities:data collection, info output
# Student Grade Tracker
# CS 1300 — Lecture 5 Mini-Project
# A modular, well-tested program that collects exam scores,
# calculates a letter grade and academic standing, and
# displays a formatted report.
# Functions:
    # get_student_name - collects student name for report
    # get_scores - collects student scores for report
    # calculate_average - calculates average of scores for report
    # determine_results - calculates end results for report
    # print_report - prints all results for report
def main():
    name = get_student_name()
    scores = get_scores(3)
    average = calculate_average(scores)
    standing, grade = determine_results(average)
    print_report(name, scores, average, grade, standing)

def get_student_name():
    return input("student name: ")

def is_valid_score(score):
    return 0 <= score <= 100
def get_scores(num_exams):
    scores = []
    for i in range(num_exams):
        while True:
            try:
                score = int(input(f"exam {i + 1} score: "))
                if is_valid_score(score):
                    scores.append(score)
                    break
                else:
                    print("invalid! score must be inbetween 0 and 100")
            except ValueError:
                print("invalid! please enter a whole number")
    return scores
def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0

def determine_results(average):
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    if average >= 90:
        standing = "Dean's List"
    elif average >= 70:
        standing = "Good Standing"
    elif average >= 60:
        standing = "Academic Probation"
    else:
        standing = "Academic Warning"
    return grade, standing

def print_report(name, scores, average, grade, standing):
    print("=" * 30)
    print("student grade report")
    print("=" * 30)

    print(f"student: {name}")
    for i, score in enumerate(scores, start=1):
        print(f"exam {i}: {score}") 
    
    print("=" * 30)
    print(f"average: {average:.2f}")
    print(f"grade: {grade}") 
    print(f"standing: {standing}")
    print("=" * 30)

def calculate_average(grades_list):
    return sum(grades_list) / len(grades_list) if grades_list else 0
def print_border(char="=", length=20):
    print(char + length)
def display_report(grades_list):
    print_border("=")
    print(f"scores: {grades_list}")
    print(f"Average: {calculate_average(grades_list):.2f}")
    print_border("=")

def get_validated_input(prompt):
    while True:
        try:
            val = float(input(prompt))
            if 0 <= val <= 100:
                return val
            print("please enter a number between 0 and 100.")
        except ValueError:
            print("invalid input")


if __name__ == "__main__":
    main()
    







