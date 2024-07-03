actor_name = input()
academy_points = float(input())
judges_count = int(input())

total_points = academy_points
got_nominee = False

for _ in range(judges_count):
    judge_name = input()
    points_from_judge = float(input())
    total_points += len(judge_name) * points_from_judge / 2

    if total_points > 1250.50:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        got_nominee = True
        break

if total_points <= 1250.50 or not got_nominee:
    points_needed = 1250.50 - total_points
    print(f'Sorry, {actor_name} you need {points_needed:.1f} more!')
