product = input()
is_fruit = False
is_vegetable = False

if product == 'banana' or \
        product == 'apple' or \
        product == 'kiwi' or \
        product == 'cherry' or \
        product == 'lemon' or \
        product == 'grapes':
    is_fruit = True
elif product == 'tomato' or \
        product == 'cucumber' or \
        product == 'pepper' or \
        product == 'carrot':
    is_vegetable = True

if is_fruit:
    print('fruit')
elif is_vegetable:
    print('vegetable')
else:
    print('unknown')
