goal_reached = True
steps_counter = 0

while steps_counter < 10000:
    command = input()

    if command == 'Going home':
        steps_counter += int(input())
        if steps_counter < 10000:
            goal_reached = False
        break

    steps_counter += int(command)

if goal_reached:
    steps_over_the_goal = steps_counter - 10000
    print('Goal reached! Good job!')
    print(f'{steps_over_the_goal} steps over the goal!')
else:
    steps_needed = 10000 - steps_counter
    print(f'{steps_needed} more steps to reach goal.')
