sites_open = int(input())
salary = int(input())

lost_salary = False

for i in range(sites_open):
    site = input()
    if site == 'Facebook':
        salary -= 150
    elif site == 'Instagram':
        salary -= 100
    elif site == 'Reddit':
        salary -= 50

    if salary <= 0:
        lost_salary = True
        print('You have lost your salary.')
        break

if not lost_salary:
    print(salary)
