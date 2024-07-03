degrees = float(input())

if degrees < 5 or degrees > 35:
    print('unknown')
elif degrees <= 11.9:
    print('Cold')
elif degrees <= 14.9:
    print('Cool')
elif degrees <= 20.00:
    print('Mild')
elif degrees <= 25.9:
    print('Warm')
elif degrees <= 35.00:
    print('Hot')