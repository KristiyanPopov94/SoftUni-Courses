lengthInCM = int(input()) / 10
widthInCM = int(input()) / 10
heightInCM = int(input()) / 10
percent = float(input()) / 100

area = (lengthInCM * widthInCM * heightInCM)

liters = area - (area * percent)

print(liters)