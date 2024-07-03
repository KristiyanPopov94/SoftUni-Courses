months = int(input())

electricity_bills = 0
water_bills_monthly = 20
internet_bills_monthly = 15
others = 0

for _ in range(0, months):
    electricity_bills_monthly = float(input())
    electricity_bills += electricity_bills_monthly
    others += (electricity_bills_monthly + water_bills_monthly + internet_bills_monthly) * 1.20

average_bills = water_bills_monthly + internet_bills_monthly + ((electricity_bills + others) / months)

print(f'Electricity: {electricity_bills:.2f} lv')
print(f'Water: {(water_bills_monthly * months):.2f} lv')
print(f'Internet: {(internet_bills_monthly * months):.2f} lv')
print(f'Other: {others:.2f} lv')
print(f'Average: {average_bills:.2f} lv')