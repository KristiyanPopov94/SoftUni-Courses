euro_to_lv = 1.94

vegetables_kg_price = float(input())
fruits_kg_price = float(input())
vegetables_total_kg = int(input())
fruits_total_kg = int(input())

total_sum_in_euro = ((vegetables_kg_price * vegetables_total_kg) + (fruits_kg_price * fruits_total_kg)) / 1.94

print(f'{total_sum_in_euro:.2f}')