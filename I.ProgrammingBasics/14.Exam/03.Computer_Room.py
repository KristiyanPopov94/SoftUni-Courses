month = input()
hours_spent = int(input())
people_count_in_group = int(input())
time_of_the_day = input()

regular_sum = 0
discount = 0
extra_discount = 0

if month == 'march' or month == 'april' or month == 'may':
    if time_of_the_day == 'day':
        regular_sum = 10.50
    else:
        regular_sum = 8.40
elif month == 'june' or month == 'july' or month == 'august':
    if time_of_the_day == 'day':
        regular_sum = 12.60
    else:
        regular_sum = 10.20

if people_count_in_group >= 4:
    discount += 0.10

if hours_spent >= 5:
    extra_discount += 0.50

price_for_hour_person = (regular_sum * (1 - discount)) * (1 - extra_discount)
total_sum = price_for_hour_person * people_count_in_group * hours_spent

print(f'Price per person for one hour: {price_for_hour_person:.2f}')
print(f'Total cost of the visit: {total_sum:.2f}')
