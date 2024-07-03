season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())

price_for_a_night = 0
sport_to_practice = ''
discount = 0

if season == 'Winter':
    if group_type == 'boys' or group_type == 'girls':
        price_for_a_night = 9.60
        if group_type == 'girls':
            sport_to_practice = 'Gymnastics'
        elif group_type == 'boys':
            sport_to_practice = 'Judo'
    elif group_type == 'mixed':
        price_for_a_night = 10
        sport_to_practice = 'Ski'
elif season == 'Spring':
    if group_type == 'boys' or group_type == 'girls':
        price_for_a_night = 7.20
        if group_type == 'girls':
            sport_to_practice = 'Athletics'
        elif group_type == 'boys':
            sport_to_practice = 'Tennis'
    elif group_type == 'mixed':
        price_for_a_night = 9.50
        sport_to_practice = 'Cycling'
elif season == 'Summer':
    if group_type == 'boys' or group_type == 'girls':
        price_for_a_night = 15
        if group_type == 'girls':
            sport_to_practice = 'Volleyball'
        elif group_type == 'boys':
            sport_to_practice = 'Football'
    elif group_type == 'mixed':
        price_for_a_night = 20
        sport_to_practice = 'Swimming'

if students_count >= 50:
    discount = 0.50
elif students_count >= 20:
    discount = 0.15
elif students_count >= 10:
    discount = 0.05

final_price = price_for_a_night * students_count * nights_count

if discount > 0:
    final_price *= (1 - discount)

print(f'{sport_to_practice} {final_price:.2f} lv.')