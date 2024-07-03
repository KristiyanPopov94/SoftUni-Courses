count_of_groups = int(input())

musala = 0
monblan = 0
kalimanjaro = 0
k2 = 0
everest = 0

for _ in range(count_of_groups):
    people_count = int(input())

    if people_count <= 5:
        musala += people_count
    elif people_count <= 12:
        monblan += people_count
    elif people_count <= 25:
        kalimanjaro += people_count
    elif people_count <= 40:
        k2 += people_count
    elif people_count >= 41:
        everest += people_count

total_peoples_count = musala + monblan + kalimanjaro + k2 + everest

print(f'{(musala / total_peoples_count * 100):.2f}%')
print(f'{(monblan / total_peoples_count * 100):.2f}%')
print(f'{(kalimanjaro / total_peoples_count * 100):.2f}%')
print(f'{(k2 / total_peoples_count * 100):.2f}%')
print(f'{(everest / total_peoples_count * 100):.2f}%')
