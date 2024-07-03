students_count = int(input())

failed_grades = 0
grades_between_3_and_4 = 0
grades_between_4_and_5 = 0
perfect_grades = 0
total_grade = 0

for _ in range(0, students_count):
    grade = float(input())
    total_grade += grade

    if grade < 3:
        failed_grades += 1
    elif grade < 4:
        grades_between_3_and_4 += 1
    elif grade < 5:
        grades_between_4_and_5 += 1
    else:
        perfect_grades += 1

average_grade = total_grade / students_count

failed_percent = failed_grades / students_count * 100
between_3_and_4_percent = grades_between_3_and_4 / students_count * 100
between_4_and_5_percent = grades_between_4_and_5 / students_count * 100
perfect_percent = perfect_grades / students_count * 100

print(f'Top students: {perfect_percent:.2f}%')
print(f'Between 4.00 and 4.99: {between_4_and_5_percent:.2f}%')
print(f'Between 3.00 and 3.99: {between_3_and_4_percent:.2f}%')
print(f'Fail: {failed_percent:.2f}%')
print(f'Average: {average_grade:.2f}')