plasticPackage = int(input())
paintLiters = int(input())
razreditel = int(input())
hoursNeeded = int(input())

plasticSum = (plasticPackage + 2) * 1.5
paintSum = (paintLiters * 14.5) * 1.10
razreditelSum = razreditel * 5
totalЕxpenses = plasticSum + paintSum + razreditelSum + 0.40
workersPaimentAnHour = totalЕxpenses * 0.30
finalSum = totalЕxpenses + (workersPaimentAnHour * hoursNeeded)

print(finalSum)