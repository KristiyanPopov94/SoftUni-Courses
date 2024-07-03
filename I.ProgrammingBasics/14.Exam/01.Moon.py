import math

average_speed = float(input())
ltrs_needed_for_100km = float(input())
ltrs_for_1km = ltrs_needed_for_100km / 100
# 384_400 км

hours_needed = (384_400 / average_speed) * 2
ltrs_needed = (ltrs_for_1km * 384_400) * 2

total_time = hours_needed + 3

print(math.ceil(total_time))
print(int(ltrs_needed))
