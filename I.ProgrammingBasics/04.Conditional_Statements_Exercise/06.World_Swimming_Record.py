from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_per_meter = float(input())

# съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.
# Когато се изчислява колко пъти Иван ще се забави, в резултат на съпротивлението на водата,
# резултатът трябва да се закръгли надолу до най-близкото цяло число.

times_slowed_down = floor(distance_in_meters / 15)
ivan_swim_time = distance_in_meters * seconds_per_meter + times_slowed_down * 12.5

if ivan_swim_time < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {ivan_swim_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {(ivan_swim_time - record_in_seconds):.2f} seconds slower.')
