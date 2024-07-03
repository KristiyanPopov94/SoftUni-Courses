strawberries_price = float(input())
bananas_kilograms = float(input())
oranges_kilograms = float(input())
raspberries_kilograms = float(input())
strawberries_kilograms = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2

total_sum_needed = strawberries_price * strawberries_kilograms \
                    + bananas_price * bananas_kilograms \
                    + oranges_price * oranges_kilograms \
                    + raspberries_price * raspberries_kilograms

print(f'{total_sum_needed:.2f}')