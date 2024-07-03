students_tickets = 0
standard_tickets = 0
kids_tickets = 0

command = input()
while command != 'Finish':
    movie = command
    seats_available = int(input())
    tickets_sold = 0

    while tickets_sold < seats_available:
        ticket_type = input()

        if ticket_type == 'End':
            break
        elif ticket_type == 'student':
            students_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kids_tickets += 1

        tickets_sold += 1

    percent_projection_full = (tickets_sold / seats_available) * 100
    print(f'{movie} - {percent_projection_full:.2f}% full.')

    command = input()

total_tickets_sold = students_tickets + standard_tickets + kids_tickets

percent_students_tickets = (students_tickets / total_tickets_sold) * 100
standard_tickets = (standard_tickets / total_tickets_sold) * 100
kids_tickets = (kids_tickets / total_tickets_sold) * 100

print(f'Total tickets: {total_tickets_sold}')
print(f'{percent_students_tickets:.2f}% student tickets.')
print(f'{standard_tickets:.2f}% standard tickets.')
print(f'{kids_tickets:.2f}% kids tickets.')
