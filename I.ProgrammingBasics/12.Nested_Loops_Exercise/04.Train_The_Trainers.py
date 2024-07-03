judges_count = int(input())

total_evaluation = 0
total_evaluation_count = 0

command = input()
while command != 'Finish':
    presentation_name = command
    evaluation = 0
    counter = 0

    for _ in range(judges_count):
        evaluation += float(input())
        total_evaluation_count += 1
        counter += 1

    average_grade_presentation = evaluation / counter
    print(f'{presentation_name} - {average_grade_presentation:.2f}.')
    total_evaluation += evaluation
    evaluation = 0
    counter = 0
    command = input()

average_evaluation = total_evaluation / total_evaluation_count
print(f'Student\'s final assessment is {average_evaluation:.2f}.')
