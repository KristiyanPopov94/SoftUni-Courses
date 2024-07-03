yearlyTax = int(input())

sneakersPrice = yearlyTax * 0.60
outfitPrice = sneakersPrice * 0.80
ballPrice = outfitPrice * 0.25
accessoriesPrice = ballPrice * 0.20

totalPrice = yearlyTax + sneakersPrice + outfitPrice + ballPrice + accessoriesPrice

print(totalPrice)