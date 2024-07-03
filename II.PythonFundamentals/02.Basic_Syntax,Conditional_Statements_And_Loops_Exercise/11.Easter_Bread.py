budget = float(input())
kg_flour_price = float(input())
egg_pack_price = kg_flour_price * 0.75
liter_milk_price = kg_flour_price * 1.25
milk_need_for_one_bread = liter_milk_price / 4
loaf_price = egg_pack_price + kg_flour_price + milk_need_for_one_bread

colored_eggs = 0
loaves_made = 0
counter = 0
while budget > loaf_price:
    budget -= loaf_price
    loaves_made += 1
    colored_eggs += 3
    counter += 1

    if counter % 3 == 0:
        colored_eggs -= (loaves_made - 2)


print(f'You made {loaves_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')