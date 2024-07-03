limit_of_bad_grades = int(input())

total_grade_score = 0
bad_grades = 0
passed_exercises = 0
last_exercise = ''
passed_exam = False

while bad_grades < limit_of_bad_grades:
    exercise_name = input()

    if exercise_name == 'Enough':
        passed_exam = True
        break

    grade_for_exercise = int(input())

    if grade_for_exercise <= 4:
        bad_grades += 1

    total_grade_score += grade_for_exercise
    passed_exercises += 1
    last_exercise = exercise_name

if passed_exam:
    average_score = total_grade_score / passed_exercises
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {passed_exercises}')
    print(f'Last problem: {last_exercise}')
else:
    print(f'You need a break, {bad_grades} poor grades.')
