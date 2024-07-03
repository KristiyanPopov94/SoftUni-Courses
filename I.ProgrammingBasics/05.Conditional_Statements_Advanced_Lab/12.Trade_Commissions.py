city = input()
sales_volume = float(input())

commission_percent = 0 / 100
wrong_city = False
negative_sales = False

if city == 'Sofia':
    if 0 <= sales_volume <= 500:
        commission_percent = 0.05
    elif 500 < sales_volume <= 1000:
        commission_percent = 0.07
    elif 1000 < sales_volume <= 10000:
        commission_percent = 0.08
    elif sales_volume > 10000:
        commission_percent = 0.12
    else:
        negative_sales = True
elif city == 'Varna':
    if 0 <= sales_volume <= 500:
        commission_percent = 0.045
    elif 500 < sales_volume <= 1000:
        commission_percent = 0.075
    elif 1000 < sales_volume <= 10000:
        commission_percent = 0.10
    elif sales_volume > 10000:
        commission_percent = 0.13
    else:
        negative_sales = True
elif city == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        commission_percent = 0.055
    elif 500 < sales_volume <= 1000:
        commission_percent = 0.08
    elif 1000 < sales_volume <= 10000:
        commission_percent = 0.12
    elif sales_volume > 10000:
        commission_percent = 0.145
    else:
        negative_sales = True
else:
    wrong_city = True

commission = sales_volume * commission_percent

if not (wrong_city or negative_sales):
    print(f'{commission:.2f}')
else:
    print('error')
