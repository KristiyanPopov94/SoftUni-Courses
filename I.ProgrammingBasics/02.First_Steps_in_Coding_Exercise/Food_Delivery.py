chickenMenu = int(input())
fishMenu = int(input())
veganMenu = int(input())

menuSum = (chickenMenu * 10.35) + (fishMenu * 12.4) + (veganMenu * 8.15)
desertPrice = menuSum * 0.2
totalSum = menuSum + desertPrice + 2.5

print(totalSum)