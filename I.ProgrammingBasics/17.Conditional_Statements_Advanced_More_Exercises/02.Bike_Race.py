junior_cyclist = int(input())
senior_cyclist = int(input())
track_type = input()

juniors_total_tax = 0
seniors_total_tax = 0
discount = 0
expenses_percentage = 0.05

if track_type == 'trail':
    juniors_total_tax = junior_cyclist * 5.50
    seniors_total_tax = senior_cyclist * 7
elif track_type == 'cross-country':
    juniors_total_tax = junior_cyclist * 8
    seniors_total_tax = senior_cyclist * 9.5
    if (junior_cyclist + senior_cyclist) >= 50:
        discount = 0.25
elif track_type == 'downhill':
    juniors_total_tax = junior_cyclist * 12.25
    seniors_total_tax = senior_cyclist * 13.75
elif track_type == 'road':
    juniors_total_tax = junior_cyclist * 20
    seniors_total_tax = senior_cyclist * 21.50

total_tax = (juniors_total_tax + seniors_total_tax)

if discount > 0:
    total_tax *= (1 - discount)

final_sum_raised = total_tax * (1 - expenses_percentage)

print(f'{final_sum_raised:.2f}')