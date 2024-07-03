student = input()

grade = 1
total_sum_of_evaluation = 0
class_failed = 0

while grade <= 12:
    evaluation = float(input())

    if evaluation >= 4.00:
        grade += 1
        total_sum_of_evaluation += evaluation
    elif evaluation < 4.00:
        class_failed += 1

    if class_failed > 1:
        print(f'{student} has been excluded at {grade} grade')
        break

else:
    average_evaluation = total_sum_of_evaluation / 12
    print(f'{student} graduated. Average grade: {average_evaluation:.2f}')
