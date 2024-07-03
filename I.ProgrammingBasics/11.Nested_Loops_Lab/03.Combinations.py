index = int(input())

counter = 0

for x in range(index + 1):
    for y in range(index + 1):
        for z in range(index + 1):
            if x + y + z == index:
                counter += 1
print(counter)
