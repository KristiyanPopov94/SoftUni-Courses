cargo_count = int(input())

bus_total = 0
truck_total = 0
train_total = 0

for _ in range(0, cargo_count):
    cargo_weight = int(input())

    if cargo_weight <= 3:
        bus_total += cargo_weight
    elif cargo_weight <= 11:
        truck_total += cargo_weight
    elif cargo_weight >= 12:
        train_total += cargo_weight

bus_price = bus_total * 200
truck_price = truck_total * 175
train_price = train_total * 120

total_weight = bus_total + truck_total + train_total
average_cargo_price = (bus_price + truck_price + train_price) / total_weight

bus_percent = bus_total / total_weight * 100
truck_percent = truck_total / total_weight * 100
train_percent = train_total / total_weight * 100

print(f'{average_cargo_price:.2f}')
print(f'{bus_percent:.2f}%')
print(f'{truck_percent:.2f}%')
print(f'{train_percent:.2f}%')
