skumriya_kg_price = float(input())
caca_kg_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = float(input())

palamud_kg_price = skumriya_kg_price * 1.60
safrid_kg_price = caca_kg_price * 1.80

midi_total_price = midi_kg * 7.50
palamud_total_price = palamud_kg_price * palamud_kg
safrid_total_price = safrid_kg_price * safrid_kg

total_price = midi_total_price + palamud_total_price + safrid_total_price

print(f'{total_price:.2f}')