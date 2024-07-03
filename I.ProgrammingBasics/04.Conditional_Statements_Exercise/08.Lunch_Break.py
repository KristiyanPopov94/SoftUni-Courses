from math import ceil

tv_series_name = str(input())
episode_length = int(input())
break_length = int(input())

lunch_time = break_length * 0.125
chill_time = break_length * 0.25

time_left = break_length - (lunch_time + chill_time)

if time_left >= episode_length:
    print(f'You have enough time to watch {tv_series_name} and left with {ceil(time_left - episode_length)} minutes\
 free time.')
else:
    print(f'You don\'t have enough time to watch {tv_series_name}, you need {ceil(episode_length - time_left)} more\
 minutes.')
