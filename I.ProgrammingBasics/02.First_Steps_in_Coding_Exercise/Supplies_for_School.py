pen = int(input())
markers = int(input())
detergentLiters = int(input())
discountPercentage = int(input()) / 100

sumBeforeDiscount = (pen * 5.8) + (markers * 7.2) + (detergentLiters * 1.2)
totalSum = sumBeforeDiscount - (sumBeforeDiscount * discountPercentage)

print(totalSum)