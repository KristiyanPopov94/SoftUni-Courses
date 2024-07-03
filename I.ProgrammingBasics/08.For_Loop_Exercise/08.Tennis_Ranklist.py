from math import floor
tourneys_count = int(input())
starting_points = int(input())

additional_points = 0
wins = 0

for _ in range(tourneys_count):
    tourney_status = input()

    if tourney_status == 'W':
        additional_points += 2000
        wins += 1
    elif tourney_status == 'F':
        additional_points += 1200
    else:
        additional_points += 720

average_points = additional_points / tourneys_count
final_points = starting_points + additional_points
percent_won = (wins / tourneys_count)

print(f'Final points: {final_points}')
print(f'Average points: {floor(average_points)}')
print(f'{percent_won:.2%}')
