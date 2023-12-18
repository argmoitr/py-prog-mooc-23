# Write your solution here

def print_stars(x: int, grades: list) -> None:
    count = 0
    for grade in grades:
        if x == grade:
            count += 1
    return "*" * count

def get_grades(exam_points: list, exercise_points: list) -> list:
    des_list = []
    for i in range(len(exam_points)):
        if exam_points[i] < 10:
            grade = 0
        elif exam_points[i] + exercise_points[i] < 15:
            grade = 0
        elif exam_points[i] + exercise_points[i] < 18:
            grade = 1
        elif exam_points[i] + exercise_points[i] < 21:
            grade = 2
        elif exam_points[i] + exercise_points[i] < 24:
            grade = 3
        elif exam_points[i] + exercise_points[i] < 28:
            grade = 4
        elif exam_points[i] + exercise_points[i] <= 30:
            grade = 5
        des_list.append(grade)
    return des_list
    
def pass_percentage(exam_points: list, exercise_points: list) -> float:
    passed = 0
    for i in range(len(exam_points)):
        if exam_points[i] >= 10 and exam_points[i] + exercise_points[i] >= 15:
            passed += 1
    return (passed/len(exam_points)) * 100

def points_average(exam_points: list, exercise_points: list) -> float:
    des_list = []
    for i in range(len(exam_points)):
        des_list.append(exam_points[i]+exercise_points[i])
    return sum(des_list) / len(des_list)

def convert_to_points(exercises_completed: list) -> list:
    des_list = []
    for exercises in exercises_completed:
        des_list.append(int((exercises/100)*10))
    return des_list
    
def main():
    exam_points = []
    exercises_completed = []
    exercise_points = []
    
    while True:
        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            break
        parts = user_input.split(" ")
        exam_points.append(int(parts[0]))
        exercises_completed.append(int(parts[1]))

    exercise_points = convert_to_points(exercises_completed)

    print(f"Statistics: ")
    print(f"Points average: {points_average(exam_points, exercise_points):.1f}")
    print(f"Pass percentage: {pass_percentage(exam_points, exercise_points):.1f}")

    grades = get_grades(exam_points, exercise_points)

    print("Grade distribution: ")
    i = 5
    while i >= 0:
        print(f"{i}: {print_stars(i, grades)}")
        i -= 1

main()
