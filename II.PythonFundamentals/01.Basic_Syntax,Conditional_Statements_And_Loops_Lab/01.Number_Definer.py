number = float(input())

if number == 0:
    print('zero')
elif number > 0:
    if number < 1:
        print('small positive')
    elif number > 1_000_000:
        print('large positive')
    else:
        print('positive')
else:
    if abs(number) < 1:
        print('small negative')
    elif abs(number) > 1_000_000:
        print('large negative')
    else:
        print('negative')


# if number > 1_000_000:
#     print('large positive')
# elif number >= 1:
#     print('positive')
# elif 0 < number < 1:
#     print('small positive')
# elif number == 0:
#     print('zero')
# elif 0 > number > -1:
#     print('small negative')
# elif number < -1_000_000:
#     print('large negative')
# elif number <= -1:
#     print('negative')
