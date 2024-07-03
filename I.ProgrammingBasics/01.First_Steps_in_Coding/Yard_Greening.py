squareMeters = float(input())
price = squareMeters * 7.61
discount = price * 0.18
finalPrice = price * 0.82

print(f'The final price is: {finalPrice:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')