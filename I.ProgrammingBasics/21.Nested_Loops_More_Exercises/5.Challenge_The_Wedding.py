man_count = int(input())
woman_count = int(input())
tables_count = int(input())
tables_taken = 0

for man in range(1, man_count + 1):
    for woman in range(1, woman_count + 1):
        if tables_taken == tables_count:
            break
        tables_taken += 1
        print(f'({man} <-> {woman})', end=' ')